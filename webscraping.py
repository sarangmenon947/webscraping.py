import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

def scrape_google():
    url = "https://www.google.com"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    # Scrape desired details. This is just an example.
    details = {
        "title": soup.title.string,
        "link": url,
        # Add other details as needed
    }
    return details

def export_data(data, file_type):
    if file_type == "CSV":
        df = pd.DataFrame(data)
        df.to_csv("output.csv", index=False)
        print("Data exported as CSV.")
        
    elif file_type == "JSON":
        with open("output.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Data exported as JSON.")
        
    elif file_type == "XML":
        df = pd.DataFrame(data)
        df.to_xml("output.xml", index=False)
        print("Data exported as XML.")
        
    elif file_type == "XLSX":
        df = pd.DataFrame(data)
        df.to_excel("output.xlsx", index=False)
        print("Data exported as XLSX.")
        
    else:
        print("Invalid file type.")

def main():
    email = "example@example.com"
    phone = "+91 1234567890"
    
    while True:
        print("\nFetching details from Google...")
        scraped_data = scrape_google()
        
        if scraped_data is None:
            print("Exiting program due to an error.")
            break
        
        print("Scraped data:", scraped_data)
        
        # Ask user for export options
        user_input = input("Which file type do you want for exporting your file? Options: CSV, JSON, XML, XLSX: ").strip().upper()
        
        if user_input in ["CSV", "JSON", "XML", "XLSX"]:
            export_data(scraped_data, user_input)
        else:
            print("Invalid file type selected.")
        
        another = input("Do you want to scrape another file? (yes/no): ").strip().lower()
        if another != "yes":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
