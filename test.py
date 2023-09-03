from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep

import os
from dotenv import load_dotenv
load_dotenv()
HANDLE = os.getenv('CF_HANDLE')
PASSWORD = os.getenv('CF_PASSWORD')

CFLIST_BASE_URL='https://codeforces.com/list/'
CF_LOGIN='https://codeforces.com/enter'
print(HANDLE)