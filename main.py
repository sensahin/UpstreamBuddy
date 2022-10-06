import requests

upstream = 'https://api.github.com/repos/owner/repo/tags'
fork = 'https://api.github.com/repos/owner/repo/tags'

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer XXXXX',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def get_latest_tag_from_upstream(url):
    response = requests.get(url, headers=headers)
    return response.json()[0]['name']

def get_latest_tag_from_fork(url):
    response = requests.get(url, headers=headers)
    return response.json()[0]['name']

print("Fork tag: ", get_latest_tag_from_fork(fork))
print("Upstream tag: ", get_latest_tag_from_upstream(upstream))

def trigger_workflow():
    url = 'https://api.github.com/repos/owner/repo/actions/workflows/id/dispatches'
    data = {"ref": "master"}
    response = requests.post(url, headers=headers, json=data)
    print(response)


if get_latest_tag_from_fork(fork) != get_latest_tag_from_upstream(upstream):
    print("Fork is behind, updating")
    trigger_workflow()
else:
    print("Fork is up to date")
