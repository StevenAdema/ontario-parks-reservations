import json
import pandas as pd
import requests
from datetime import datetime, timedelta
from campsite import Campsite

camp = Campsite("Charleston Lake")
camp.get_park_availability('2023-08-23')