import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # 1. Log the incoming event for debugging
    print("Received event: " + json.dumps(event))
    
    try:
        # 2. Extract the Bucket Name from the AWS Config event
        # Note: EventBridge sends the 'detail' object which contains 'resourceId'
        bucket_name = event['detail']['resourceId']
        print(f"Detected Non-compliant bucket: {bucket_name}")
        
        # 3. Slam the door: Enable Block Public Access
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        
        print(f"Successfully remediated bucket: {bucket_name}")
        
    except Exception as e:
        print(f"Error: {e}")
        raise e
