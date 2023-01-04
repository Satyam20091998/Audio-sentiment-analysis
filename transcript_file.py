import json
import boto3
import time
from urllib.request import urlopen

def lambda_handler(event, context):
    transcribe=boto3.client("transcribe")
    s3=boto3.client("s3")
    print(event)
    if event:
        file_obj= event['Records'][0]
        bucket_name=str(file_obj["s3"]["bucket"]["name"])
        file_name=str(file_obj["s3"]["object"]["key"])
        print(file_name)
        s3url=create_url(bucket_name,file_name)
        file_type=file_name.split(".")[1]
        job_name=context.aws_request_id
        
        
        response=transcribe.start_transcription_job(TranscriptionJobName=job_name,
                                            Media={"MediaFileUri":s3url},
                                            MediaFormat=file_type,
                                            OutputBucketName="trscripted-bucket",
                                            LanguageCode="en-US")

    return 0

def create_url(bucket_name,file_name):
    return "s3://"+bucket_name+"/"+file_name
