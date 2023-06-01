import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Prompt the user to enter the URL of the web page to crawl
url = input("Enter the URL of the web page to crawl: ")

# Send an HTTP GET request to retrieve the web page content
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print the text content of all the links on the web page
links = soup.find_all("a")
for link in links:
    print(link.text)

# Extract and print the text content of all the headings on the web page
headings = soup.find_all(["h1", "h2", "h3"])
for heading in headings:
    print(heading.text)

# Follow links in the navigation menu and extract information from each linked page
nav_links = soup.find_all("a", class_="nav-link")
for nav_link in nav_links:
    # Construct the absolute URL by joining the base URL and the relative URL of the link
    absolute_url = urljoin(url, nav_link.get("href"))
    # Send an HTTP GET request to the linked page
    linked_response = requests.get(absolute_url)
    # Create a new BeautifulSoup object to parse the linked page
    linked_page_soup = BeautifulSoup(linked_response.text, "html.parser")
    # Extract and print information from the linked page
    # ...

# Handle pagination (assuming there is a "Next" link on each page)
next_link = soup.find("a", strings="Next")
while next_link:
    absolute_next_url = urljoin(url, next_link.get("href"))
    next_response = requests.get(absolute_next_url)
    next_page_soup = BeautifulSoup(next_response.text, "html.parser")
    # Extract and print information from the next page
    # ...

    next_link = next_page_soup.find("a", text="Next")
