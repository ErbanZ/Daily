import requests
from bs4 import BeautifulSoup

# ----1
# # URL of Toplist category
# url = "https://wallhaven.cc/toplist"

# # Send GET request to Toplist URL
# response = requests.get(url)

# # Parse HTML content with BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Select the first 10 links to wallpaper images
# links = soup.select('ul > li > figure > a[href*="/wallpaper/"]')[:10]

# # Extract the image URL from each link
# image_urls = [link['href'] for link in links]

# # Print the list of image URLs
# print(image_urls)

# -----2
# url = 'https://wallhaven.cc/toplist'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# image_divs = soup.find_all('div', class_='thumb-listing-page')
# images = []

# for div in image_divs:
#     for a_tag in div.find_all('a', class_='preview'):
#         img_url = a_tag['href']
#         images.append(img_url)

# top_10_images = images[:10]
# print(top_10_images)

# -----3
import requests
from bs4 import BeautifulSoup

url = 'https://wallhaven.cc/toplist?page=1'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('figure', class_='thumb')

for result in results[:10]:
    image_url = result.find('img').get('data-src')
    print(image_url)
