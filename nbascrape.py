#NBA SCRAPE
import pandas as pd
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'http://www.basketball-reference.com/leagues/NBA_2017_games-march.html'
#my_url = 'http://www.basketball-reference.com/leagues/NBA_2017_games-april.html'


#opening connection, grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

#print(page_soup.h1)

table = page_soup.find("table",{"class":"suppress_glossary sortable stats_table now_sortable"})

page_soup.findAll('tr', limit=2)[0].findAll('th')

column_headers = [th.getText() for th in page_soup.findAll('tr', limit=2)[0].findAll('th')]
#print column_headers

data_rows = page_soup.findAll('tr')[1:]
#print type(data_rows)

team_data = [[td.getText() for td in data_rows[i].findAll('td')]
            for i in range(len(data_rows))]


df = pd.DataFrame(team_data, columns = column_headers[1:])

#print (df.columns)
#del df('Notes')
df = df.drop('Notes', 1)
#print df.head()

df.to_csv('text.csv')


#containers = page_soup.findAll("div",{"class":""})
