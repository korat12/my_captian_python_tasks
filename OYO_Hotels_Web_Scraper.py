# Project 2: Web scraper using BeautifulSoup4 and requests

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX = 3

scraped_info_list = []

# Loop through pages
for page_num in range(1, page_num_MAX):
    req = requests.get(oyo_url + str(page_num))
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict = {}

        # Basic info
        hotel_dict["name"] = hotel.find(
            "h3", {"class": "listingHotelDescription__hotelName"}
        ).text.strip()

        hotel_dict["address"] = hotel.find(
            "span", {"itemprop": "streetAddress"}
        ).text.strip()

        hotel_dict["price"] = hotel.find(
            "span", {"class": "listingPrice__finalPrice"}
        ).text.strip()

        # Rating (optional)
        try:
            hotel_dict["rating"] = hotel.find(
                "span", {"class": "hotelRating__ratingSummary"}
            ).text.strip()
        except AttributeError:
            hotel_dict["rating"] = None

        # Amenities
        parent_amenities_element = hotel.find(
            "div", {"class": "amenityWrapper"}
        )

        amenities_list = []
        if parent_amenities_element:
            for amenity in parent_amenities_element.find_all(
                "div", {"class": "amenityWrapper__amenity"}
            ):
                amenities_list.append(
                    amenity.find("span", {"class": "d-body-sm"}).text.strip()
                )

        hotel_dict["amenities"] = ", ".join(amenities_list[-1:])

        scraped_info_list.append(hotel_dict)

# Create DataFrame
dataFrame = pd.DataFrame(scraped_info_list)

# Save to CSV
dataFrame.to_csv("oyo.csv", index=False)

print("✅ Scraping completed. Data saved to oyo.csv")
