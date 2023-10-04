import requests
import json
import os


def scan(url: str):

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + os.environ['token'],
    }

    myobj = json.dumps(
        {
            'url': url,
            'properties': {
                'webhooks': {
                    'newResult': 'https://enlal2w5n5nz.x.pipedream.net', 
                    'status': 'https://enlal2w5n5nz.x.pipedream.net/{STATUS}/my-custom-id'
                },
            }
        })

    response = requests.put('https://api.copyleaks.com/v3/scans/submit/url/my-custom-id', headers=headers, data=myobj)


def login(email: str, key: str) -> None:
    headers = {
        'Content-type': 'application/json'
    }

    myobj = json.dumps({'email': email, 'key': key})

    response = requests.post('https://id.copyleaks.com/v3/account/login/api', headers=headers, data=myobj)
    os.environ['token'] = response.json()['access_token']


def main():
    if 'token' not in os.environ:
        email = input("Enter your email: ")
        key = input("Enter your API key: ")
        login(email, key)
    
    print("token", os.environ['token'])
    url = input("Enter the URL to scan: ")
    if url.startswith("http://") or url.startswith("https://"):
        scan(url)
    else:
        print("Invalid URL")


if __name__ == '__main__':
    main()
