import pandas as pd
from text import sms_all

def main():

    teams = 'Chicago'

    for t in teams:
        
        try:
            scraper = pd.read_html('https://www.cbssports.com/nba/schedule/', match= t)

        except ValueError:
            continue

    
    
    sms_all(scraper)

main()