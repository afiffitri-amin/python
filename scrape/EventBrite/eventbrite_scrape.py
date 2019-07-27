import requests
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
import json

url = 'https://www.eventbrite.com/d/malaysia--kuala-lumpur/all-events/?page='

events_list = []

for num in tqdm(range(1,50)):
    pages = requests.get(f"{base_url}{num}", timeout=5)
    soup = BeautifulSoup(pages.text, "html.parser")

    events = soup.find_all(class_="eds-l-pad-all-6 eds-media-card-content eds-media-card-content--list eds-media-card-content--standard eds-media-card-content--fixed")

    for event in events:
        eventEntry= {
            "Event Title" : str(event.find(class_="eds-event-card__formatted-name--is-clamped").get_text()),
            "Event Time" : str(event.find(class_="eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1").get_text(strip=True)),
            "Event Venue" : str(event.find_all(class_="eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1")[1].get_text()),
            "Event Price" : str(event.find_all(class_="eds-text-bs--fixed eds-text-color--grey-600 eds-l-mar-top-1")[2].get_text(strip=True))
        }
        events_list.append(eventEntry)
        with open("EventsData.json", "w") as file:
            json.dump(events_list, file, indent=2)

    sleep(5)
