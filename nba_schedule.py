import pandas as pd
from text import sms_all



def main():
    scraper = pd.read_html('https://www.cbssports.com/nba/schedule/')
    
    row = pd.concat(scraper)
    df = pd.DataFrame(row, columns= ['Away', 'Home', 'Time / TV'])
    print(df)
    sms_all(df)
    

main()