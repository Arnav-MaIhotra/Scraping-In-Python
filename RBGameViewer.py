import requests
from bs4 import BeautifulSoup
url = input("Enter the url for the game\n")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
info = soup.find('ul', class_='border-top border-bottom game-stats-container follow-button-enabled')
name = soup.find('h1', class_='game-name')
creator = soup.find('a', class_='text-name text-overflow')
desc = soup.find('pre', class_='text game-description linkify')
print("\n"*3)
print("Name: ", name.text)
print("Creator: ", creator.text)
print(desc.text)
print(info.text)