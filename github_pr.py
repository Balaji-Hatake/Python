import requests

response = requests.get(
    "https://api.github.com/repos/kubernetes/kubernetes/pulls")

details = response.json()


def git_pr_details():

    for user in range(len(details)):
        print(
            f"IDs and UserName of the PRs are : {details[user]["id"]} , {details[user]["user"]["login"]}")


git_pr_details()
