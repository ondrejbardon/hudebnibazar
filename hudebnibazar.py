import os
import requests
import boto3
from bs4 import BeautifulSoup
from spontit import SpontitResource

BASE_URL = "https://hudebnibazar.cz"
URL = "https://hudebnibazar.cz/kytarove-efekty/110500/"
KEYWORDS = ["montreal assembly", "drolo", "chase", "walrus", "earthquaker", "neunaber", "strymon", "empress",
        "jhs", "pladask", "keeley", "red panda", "meris", "obne", "old blood noise", "eqd", "digitakt", "zvex"]
SPONTIT_USERNAME = "USER"
SPONTIT_SECRET_KEY = "SECRET"

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
                
# def create_table(dynamodb=None, table_name):
#     if not dynamodb:
#         dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

#     table = dynamodb.create_table(
#         TableName=table_name,
#         KeySchema=[
#             {
#                 'AttributeName': 'link',
#                 'KeyType': 'HASH'  # Partition key
#             },
#             {
#                 'AttributeName': 'date',
#                 'KeyType': 'RANGE'  # Sort key
#             }
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': 'link',
#                 'AttributeType': 'S'
#             },
#             {
#                 'AttributeName': 'date',
#                 'AttributeType': 'S'
#             },

#         ],
#         ProvisionedThroughput={
#             'ReadCapacityUnits': 10,
#             'WriteCapacityUnits': 10
#         }
#     )
#     return table

def send_push_notification(notification):
    resource = SpontitResource(SPONTIT_USERNAME, SPONTIT_SECRET_KEY)
    response = resource.push(notification)

if __name__ == "__main__":
    links = get_links(URL, KEYWORDS)
    check_file_and_notify(links)
