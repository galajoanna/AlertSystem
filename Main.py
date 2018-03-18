
# coding: utf-8

# In[35]:

import urllib.request
import html
import os
import pandas as pd
from bs4 import BeautifulSoup

def main():
    
# get alert list from AlertDB.csv
    alertdf = pd.read_csv('AlertDB.csv', sep=',')
    print(alertdf)
    
    return
 
# parse the last price from Netdania
def CheckLastPrice_Netdania(pair):    
    webpage = "http://www.netdania.com/currencies/" + pair
    websource = urllib.request.urlopen(webpage)
    soup = BeautifulSoup(websource.read(),'html.parser')
    resultset = soup.find_all(id="ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelLast")
    for span in resultset:
        last = span.contents[0]
    return last




# In[ ]:



