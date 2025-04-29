import boto3

aws_ec2 = boto3.client('ec2')


def ec2_create():
    response = aws_ec2.run_instances(
        ImageId="ami-0c1ac8a41498c1a9c",
        InstanceType="t3.micro",
        MaxCount=1,
        MinCount=1,
        Monitoring={
            'Enabled': False
        },
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Python_Test'
                    }
                ]


            }
        ]
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance ID : {instance_id}")


ec2_create()
