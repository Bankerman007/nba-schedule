import pandas as pd
from text import sms_all
from datetime import time


def main():
    scraper = pd.read_html('https://www.cbssports.com/nba/schedule/')
   
    sms_all(scraper)

main()