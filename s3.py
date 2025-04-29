import boto3

aws_s3 = boto3.client('s3')


def create_s3():
    response = aws_s3.create_bucket(
        Bucket='pythontestbalaji001',
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-north-1',
        },
    )
    host_id = response['ResponseMetadata']['HostId']
    print(f"Host ID : {host_id}")


create_s3()
