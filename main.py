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

# url = 'https://reservations.ontarioparks.com/api/availability/map?mapId=-2147483553&bookingCategoryId=5&equipmentCategoryId=null&subEquipmentCategoryId=null&cartUid=e4a5d5ee-11a7-4fe8-8a15-bf1fdd628878&cartTransactionUid=4b3943ba-54f1-4372-9dc0-a24a1a5cdd61&bookingUid=45fb3b00-018e-4902-9458-01d0d1390382&startDate=2023-05-13&endDate=2023-05-26&getDailyAvailability=true&isReserving=true&filterData=%5B%5D&boatLength=null&boatDraft=null&boatWidth=null&partySize=1&numEquipment=1&seed=2023-05-11T02:36:07.683Z'
# data = requests.get(url, headers=HEADERS)
# print(data)
# # data = json.load(data)
# availabilities = data.json()['resourceAvailabilities']
a = {'-2147479764': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479758': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479743': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479732': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479724': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479723': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479714': [{'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479694': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479641': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}], '-2147479634': [{'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 0, 'remainingQuota': None}, {'availability': 1, 'remainingQuota': None}]}
a = str(a)

replace_list = [{"{'availability': 0, 'remainingQuota': None}":"NO"},
                {"{'availability': 1, 'remainingQuota': None}":"YES"}]

a = a.replace("{'availability': 1, 'remainingQuota': None}","1")
a = a.replace("{'availability': 0, 'remainingQuota': None}","0")
a = a.replace("'",'"')

a = json.loads(a)
df = pd.DataFrame(a)
print(df)
exit()
print(availabilities)

# create dataframe from json
df = pd.DataFrame(availabilities)
print(df)

exit()



payload = {}
for param in request.split('?')[1].split('&'):
    key, value = param.split('=')
    payload[key] = value
print(payload)



exit()