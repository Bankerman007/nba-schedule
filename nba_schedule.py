import pandas as pd
from email_service import send_email

def main():

    teams = 'Chicago'

    for t in teams:
        
        try:
            scraper = pd.read_html('https://www.cbssports.com/nba/schedule/', match= t)

        except ValueError:
            continue

    

    send_email(scraper)

main()