# Import libraries
import requests
from bs4 import BeautifulSoup
import csv

# Fetch webpage content
link = "https://en.antaranews.com/tag/education/"
response = requests.get(link)

# Check response status from website
if response.status_code == 200:
    soup = BeautifulSoup(response.content,'html.parser')

    # Extract tags
    news = soup.find_all('h2', class_='h5')

    # List to store the scraped data
    data = []

    for antaranews in news:
        a_tag = antaranews.find('a')
        if a_tag:
            title = a_tag.get_text()
            url = a_tag['href']

    # Open a CSV file to write the data
    with open('excercise.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['Title', "Link"])
        
        writer.writerows(data)

    print('Data has been written to antaranews.csv')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')