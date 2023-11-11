import json
import os
from datetime import datetime
 
import pypd
from hurry.filesize import size
 
from src.utils.api_utils import get_list_of_buckets_req
from src.utils.aws_utils import (
    get_boto3_client,
    get_file_path_from_object_key,
    get_files_in_bucket,
)
from src.utils.exceptions import ApiException
from src.utils.format_utils import convert_to_local_zone, format_response
from src.utils.route_utils import is_xtg_file
 
 
def search(event, context):
    print("Starting search...")
 
    region = os.environ["AWS_REGION"]
    s3_client = get_boto3_client(service_name="s3", region=region)
 
    response = get_list_of_buckets_req()
    if response.status_code == 200:
        bucket_response = response.json()
    else:
        raise ApiException
    if bucket_response:
        bucket_response_region_map = {
            "us-east-1": "eastBuckets",
            "us-west-2": "westBuckets",
        }
        list_of_lob_buckets = bucket_response[bucket_response_region_map[os.environ.get("AWS_REGION")]]
    else:
        print("Could not determine list of buckets")
        return
 
    current_datetime = datetime.now()
    list_of_stuck_files = []
 
    for bucket in list_of_lob_buckets:
        print(f"Bucket: {bucket}")
        list_of_files = get_files_in_bucket(s3_client, bucket=bucket, filter_latest=True)
        if not list_of_files:
            print(f"{bucket} has no files")
            pass
        else:
            for file in list_of_files:
                file_name = file["Key"]
                print(f"File: {file_name}")
                bytes_length = file["Size"]
                last_modified_datetime = file["LastModified"].replace(tzinfo=None)
                mins_diff = int((current_datetime - last_modified_datetime).total_seconds() / 60.0)

                key = file["Key"]
                Name = key.split("/")
                Directory = Name[0]
                dirs = Directory.split("/")

                partner_name = dirs[len(dirs) - 1]
                Filename = Name[1]

                if check_if_file_is_stuck(size=bytes_length, mins_passed=mins_diff) and not is_xtg_file(file):
                    print(file["ETag"])
                    file_path, file_name = get_file_path_from_object_key(file["Key"])
                    file_size = size(bytes_length)
                    last_modified_et = convert_to_local_zone(last_modified_datetime)
            stuck_file_entry = {
                        "bucket": bucket,
                        "etag": file["ETag"],
                        "version_id": file["VersionId"],
                        "file_path": file_path,
                        "file_name": file_name,
                        "file_size": file_size,
                        "file_creation_timestamp": str(last_modified_et),
                        "mins": mins_diff,
                    }
            list_of_stuck_files.append(stuck_file_entry)

    print("Finished search!")
    print(f"List of stuck files: {list_of_stuck_files}")
    response_str = format_response(response_dict=list_of_stuck_files)
 
    # PagerDuty notifications
    if (
        os.environ.get("ENVIRONMENT") not in ["dev", "local"]
        and os.environ.get("PD_ROUTING_KEY")
and len(list_of_stuck_files) > 0
    ):
        send_to_pagerduty(
            report_name="S3 Stuck File Report",
            response_data=response_str,
            routing_key=os.environ.get("PD_ROUTING_KEY"),
        )
 
    # Lambda return value for development purposes
    return {"statusCode": 200, "body": json.dumps(response_str)}
 
 
def check_if_file_is_stuck(size: int, mins_passed: int) -> bool:
    # excluding files that have been stuck longer than 24 hours
    mins_threshold = 1440
    if mins_passed >= mins_threshold:
        return False
    else:
        return (
            (size < 52428800 and mins_passed >= 30)  # 0 bytes - 50 megabytes check
            or (52428800 <= size < 1073741824 and mins_passed >= 45)  # 50 megabytes - 1 gigabyte check
            or (1073741824 <= size < 26843545600 and mins_passed >= 100)  # 1 gigabyte - 25 gigabyte check
            or (26843545600 <= size < 53687091200 and mins_passed >= 120)  # 25 gigabyte - 50 gigabyte check
            or (size >= 53687091200 and mins_passed >= 240)  # larger than 50 gigabyte check
        )
 
 
def send_to_pagerduty(report_name: str, response_data: str, routing_key: str):
    print("Sending to PagerDuty")
    pypd.EventV2.create(
        data={
            "routing_key": routing_key,
            "event_action": "trigger",
            "payload": {
                "summary": f"{report_name} - {os.environ.get('ENVRIONMENT')}",
                "timestamp": datetime.now().isoformat(),
                "source": "s3",
                "severity": "info",
                "custom_details": response_data,
            },
        }
    )