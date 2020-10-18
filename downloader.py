from tqdm import tqdm
import requests
url = input('Enter Your Url: ')
chunk_size = 256
with open("sample.pdf", "wb") as file:
    r = requests.get(url, stream = True)
    total = int(r.headers['Content-Length']) / chunk_size
    for chunk in tqdm(r.iter_content(chunk_size), total = total):
        file.write(chunk)
