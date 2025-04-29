import boto3
from botocore.exceptions import ClientError
import datetime

# Initialize the boto3 client for EC2
ec2_client = boto3.client('ec2')

def list_unattached_volumes():
    """
    List all unattached EBS volumes.
    """
    try:
        volumes = ec2_client.describe_volumes(
            Filters=[
                {'Name': 'status', 'Values': ['available']}
            ]
        )
        unattached_volumes = volumes['Volumes']
        print(f"Found {len(unattached_volumes)} unattached volumes.")
        return unattached_volumes
    except ClientError as e:
        print(f"An error occurred: {e}")
        return []

def delete_volume(volume_id):
    """
    Delete an EBS volume by its volume ID.
    """
    try:
        ec2_client.delete_volume(VolumeId=volume_id)
        print(f"Deleted volume: {volume_id}")
    except ClientError as e:
        print(f"Could not delete volume {volume_id}: {e}")

def main():
    unattached_volumes = list_unattached_volumes()
    for volume in unattached_volumes:
        volume_id = volume['VolumeId']
        # Optional: Check if the volume is older than 7 days before deleting
        create_time = volume['CreateTime']
        age_in_days = (datetime.datetime.now(datetime.timezone.utc) - create_time).days
        if age_in_days >= 7:
            print(f"Deleting volume {volume_id} (age: {age_in_days} days)")
            delete_volume(volume_id)
        else:
            print(f"Skipping volume {volume_id} (only {age_in_days} days old)")

if __name__ == "__main__":
    main()