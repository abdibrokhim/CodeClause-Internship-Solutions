import argparse
import urllib.parse
import requests


def shorten(api_key: str, url: str) -> str:
    response = requests.get(f'http://cutt.ly/api/api.php?key={api_key}&short={url}')
    result = response.json()
    link = result['url']['shortLink']
    return link


def main() -> None:
    parser = argparse.ArgumentParser(description="Shorten URLs using the cutt.ly API")
    parser.add_argument('-k', '--api-key', required=True, help="API Key for cutt.ly. Get it from https://cutt.ly/")
    parser.add_argument('-u', '--url', required=True, help="URL to be shortened. Example: https://github.com/abdibrokhim")
    args = parser.parse_args()
    
    api_key = args.api_key
    url = urllib.parse.quote(args.url)
    
    print("Original URL:", args.url)
    shortened_url = shorten(api_key, url)
    print("Shortened URL:", shortened_url)


if __name__ == '__main__':
    main()
