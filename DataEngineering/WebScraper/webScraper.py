import requests
from bs4 import BeautifulSoup

url = 'https://www.drom.ru/pdd/themes/traffic_signs/'

headers = {
	'Accept': '*/*',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36'
}

def get_data():
	s = requests.Session()
	response = s.get(url=url, headers=headers)
	soup = BeautifulSoup(response.text, 'lxml')
	tags = soup.find_all('img', class_="b-image b-image__image")

	for i in range(len(tags)):
		link = tags[i].attrs["src"]
		req = s.get(url=link, headers=headers)

		with open(f'DataEngineering/WebScraper/imgs/{i+1}.jpg', 'wb') as f:
			f.write(req.content)
			print(f'Downloaded {i+1} of {len(tags)}')

if __name__ == '__main__':
	get_data()	