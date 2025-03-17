import requests

proxy = {
    "http": "http://137.59.63.198:80",
}

try:
    response = requests.get("https://www.youtube.com", proxies=proxy, timeout=5)
    if response.status_code == 200:
        print("Proxy is working!")
    else:
        print("Proxy failed!")
except Exception as e:
    print(f"Error: {e}")
