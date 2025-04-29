import boto3

aws_ec2 = boto3.client('ec2')


def ec2_delete():
    response = aws_ec2.terminate_instances(
        InstanceIds=[
            'i-07ba829acbd0ab4b3',
        ],
    )
    print(response)


ec2_delete()
