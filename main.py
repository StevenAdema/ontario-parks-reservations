import json
import pandas as pd
import requests

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

# Open the file in read mode
with open('./mapping/sites.json', 'r') as file:
    # Load the JSON data from the file
    sites_dic = json.load(file)

# url = 'https://reservations.ontarioparks.com/api/availability/map?mapId=-2147483553&bookingCategoryId=4&equipmentCategoryId=null&subEquipmentCategoryId=null&cartUid=4314e624-f8e1-4c7a-87ff-2992378289a0&cartTransactionUid=4b573d4a-04be-4a59-8b7c-66dbcbc6132a&bookingUid=422092c5-5fa0-4e2f-8fdb-2f24eb949aba&startDate=2023-08-26&endDate=2023-09-08&getDailyAvailability=true&isReserving=true&filterData=%5B%5D&boatLength=null&boatDraft=null&boatWidth=null&partySize=1&numEquipment=1&seed=2023-06-14T02:51:41.385Z'
# data = requests.get(url, headers=HEADERS)
# print(data)
# exit()
# data = json.load(data)
# availabilities = data.json()['resourceAvailabilities']
a = {'-2147479764': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479758': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479743': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479732': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479724': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479723': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479714': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479694': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479641': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479634': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}]}
a = str(a)

a = a.replace("{'availability': 1, 'remainingQuota': None}","1")
a = a.replace("{'availability': 0, 'remainingQuota': None}","0")
a = a.replace("'",'"')

a = json.loads(a)
df = pd.DataFrame(a)
df = df.transpose()

# Create a replacement dictionary from siteId to siteName
replace_dict = {site["siteId"]: site["siteName"] for site in sites_dic["sites"]}
# Replace the index names
df.rename(index=replace_dict, inplace=True)

date_range = pd.date_range(start='08-23-2023', end='09-08-2023', periods=14).strftime('%b-%d')
df.columns = date_range

print(df)

exit()
payload = {}
for param in request.split('?')[1].split('&'):
    key, value = param.split('=')
    payload[key] = value
print(payload)
