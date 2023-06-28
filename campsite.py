import json
from datetime import datetime, timedelta
import requests
import pandas as pd

class Campsite:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }

    def __init__(self, park_name):
        with open('./mapping/sites.json', 'r') as file:
            self.park_sites = json.load(file)
    
        self.park_name = park_name
        self.park_id = self.get_park_id(park_name)

    # get the park's mapId from the sites.json file
    def get_park_id(self, park_name):
        if self.park_sites['park'] == park_name:
            return self.park_sites['mapId']
        
    # returns a dataframe of the park's availability for the next 14 days
    def get_park_availability(self, start_date):
        end_date = datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=13)
        url = f'https://reservations.ontarioparks.com/api/availability/map?mapId={self.park_id}&bookingCategoryId=4&equipmentCategoryId=null&subEquipmentCategoryId=null&cartUid=7bafe8a4-c90e-45d1-9664-1c4575f9d916&cartTransactionUid=831caed3-48f1-44f7-acc8-7be851714ce5&bookingUid=2995b3e2-64a2-40e4-8c99-d5bbf8417507&startDate={start_date}&endDate={end_date}&getDailyAvailability=true&isReserving=true&filterData=%5B%5D&boatLength=null&boatDraft=null&boatWidth=null&partySize=1&numEquipment=1&seed=2023-06-14T02:51:41.385Z'
        # url = 'https://reservations.ontarioparks.com/api/availability/map?mapId=-2147483553&bookingCategoryId=4&equipmentCategoryId=null&subEquipmentCategoryId=null&cartUid=6bafe8a4-c90e-45d1-9664-1c4575f9d916&cartTransactionUid=831caed3-48f1-44f7-acc8-7be851714ce5&bookingUid=2995b3e2-64a2-40e4-8c99-d5bbf8417507&startDate=2023-09-02&endDate=2023-09-15&getDailyAvailability=true&isReserving=true&filterData=%5B%5D&boatLength=null&boatDraft=null&boatWidth=null&partySize=1&numEquipment=1&seed=2023-06-15T02:35:58.015Z'
        data = requests.get(url, headers=self.HEADERS)

        availabilities = data.json()['resourceAvailabilities']
        
        availabilities = str(availabilities)
        availabilities = availabilities.replace("{'availability': 1, 'remainingQuota': None}","1")
        availabilities = availabilities.replace("{'availability': 0, 'remainingQuota': None}","0")
        availabilities = availabilities.replace("'",'"')

        availabilities = json.loads(availabilities)
        df = pd.DataFrame(availabilities)
        df = df.transpose()

        replace_dict = {site["siteId"]: site["siteName"] for site in self.park_sites["sites"]}
        df.rename(index=replace_dict, inplace=True)

        end_date = datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=13)
        end_date = end_date.strftime('%Y-%m-%d')
        date_range = pd.date_range(start=start_date, end=end_date, periods=14).strftime('%b-%d')
        df.columns = date_range

    def get_park_availability_test(self, start_date):
        availabilities = {'-2147479764': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479758': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479743': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479732': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479724': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479723': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479714': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479694': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479641': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479634': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}]}
        availabilities = str(availabilities)
        availabilities = availabilities.replace("{'availability': 1, 'remainingQuota': None}","1")
        availabilities = availabilities.replace("{'availability': 0, 'remainingQuota': None}","0")
        availabilities = availabilities.replace("'",'"')

        availabilities = json.loads(availabilities)
        df = pd.DataFrame(availabilities)
        df = df.transpose()

        replace_dict = {site["siteId"]: site["siteName"] for site in self.park_sites["sites"]}
        df.rename(index=replace_dict, inplace=True)
        
        end_date = datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=13)
        date_range = pd.date_range(start=start_date, end=end_date, periods=14).strftime('%b-%d')
        df.columns = date_range
        return df

