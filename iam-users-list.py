import boto3

iam_console = boto3.resource('iam')


def get_users():

    for each_user in iam_console.users.all():
        print(f"User Name : {each_user.name}")

    for each_role in iam_console.roles.all():
        print(f"Role Name : {each_role.name}")


get_users()
