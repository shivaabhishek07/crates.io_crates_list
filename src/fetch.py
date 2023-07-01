import requests
import json

url = "https://crates.io/api/v1/crates"
crate_names = []
next_page = None

while True:
    resp = requests.request('GET', url=url)
    data = resp.json()
    for crate in data['crates']:
        crate_names.append(crate['id'])
    next_page = data['meta']['next_page']
    if not next_page:
        break
    url = f'https://crates.io/api/v1/crates{next_page}'
    with open('../urls.txt', 'a') as f:
        f.write(f'{url}\n')

with open('../crates.json','w') as f:
    json.dump(crate_names, f,indent=2)
