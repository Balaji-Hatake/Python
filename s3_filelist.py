import boto3

s3 = boto3.client('s3')


def s3_fileList():

    bucket = input("Please enter the name of the s3 Bucket: ")

    print()

    files = s3.list_objects_v2(Bucket=bucket)

    file_names = [item['Key'] for item in files['Contents']]

    for file_name in file_names:

        print(f"The files in the s3 Buckets are : {file_name}")
        print()

    print(len(file_names))


s3_fileList()
