import os
import requests
from bs4 import BeautifulSoup
from spontit import SpontitResource

# Configuration
BASE_URL = "https://hudebnibazar.cz"
URL = "https://hudebnibazar.cz/kytarove-efekty/110500/"
KEYWORDS = [
    "chase", 
    "walrus", 
    "earthquaker", 
    "neunaber", 
    "strymon", 
    "empress", 
    "jhs", 
    "pladask", 
    "keeley", 
    "red panda", 
    "meris", 
    "obne", 
    "old blood noise", 
    "eqd"
    ]
SPONTIT_USERNAME = "USER"
SPONTIT_SECRET_KEY = "SECRET"

# Functions
def get_links(url, keywords) -> list:

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = []

    for link in soup.find_all('a'):
        for keyword in KEYWORDS:
            if keyword in link.get('href'):
                links.append(link.get('href'))

    return(links)

def check_file_and_notify(links) -> list:
    with open("links_seen.txt", "r+") as file:
        file_content = file.read()  # cursor at the end
        new_links = []
        for link in links:
            if link not in file_content:
                send_push_notification(BASE_URL + link)
                file.write(link + "\n")
                new_links.append(link)
    return(new_links)
                

def send_push_notification(notification):
    resource = SpontitResource(SPONTIT_USERNAME, SPONTIT_SECRET_KEY)
    response = resource.push(notification)

# Main body
if __name__ == "__main__":
    links = get_links(URL, KEYWORDS)
    check_file_and_notify(links)
