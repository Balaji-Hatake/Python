import boto3

s3 = boto3.client('s3')


def s3_fileOps():
    s3_bucketname = input("Enter the name of the s3 Bucket : ").strip()
    s3_filepath = input("Enter the path of the file : ").strip()
    s3_key = input("Enter the key to be modified : ").strip()
    s3_value = input("Enter the value to be updated : ").strip()

    download = s3.get_object(Bucket=s3_bucketname, Key=s3_filepath)
    content = download['Body'].read().decode('utf-8')
    lines = content.splitlines()
    updated_lines = []
    for line in lines:
        if '=' in line:
            key, val = line.split('=', 1)
            if key.strip() == s3_key:
                updated_lines.append(f"{s3_key}={s3_value}")
                continue
        updated_lines.append(line)

    updated_content = "\n".join(updated_lines) + "\n"

    s3.put_object(Bucket=s3_bucketname, Key=s3_filepath,
                  Body=updated_content.encode('utf-8'))

    print("File Updated Successfully in s3!")


s3_fileOps()
