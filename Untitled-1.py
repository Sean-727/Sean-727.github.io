from urllib.parse import urlparse, parse_qs

url = input("Enter URL: ")
item_id = parse_qs(urlparse(url).query)["id"][0]
print(f"https://jpfans.com/product?id={item_id}&platform=mercari")