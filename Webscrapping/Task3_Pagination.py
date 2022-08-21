#Task 3: Add pagination or scrape all data for a single category.
################################### For Shampoo Category ##############################################
#Important Libraries
import requests
import pandas as pd
import re
import urllib.parse
from bs4 import BeautifulSoup

#Method 2 (Final)
product_name = []
product_orig_price = []
product_discounted_price = []
relative_url=[]


for x in range(1,4):

    #Get the HTML (Pagination)
    url="https://bagallery.com/collections/shampoo?page="
    url_final=url+str(x)
    request_session=requests.session()
    response=request_session.get(url=url_final)
    print(response.status_code)

    # Parse the HTML
    soup = BeautifulSoup(
    markup=response.content,
    features="html.parser")

    results = soup.find_all('div',class_="product-details")
    #Put everything together inside a For-Loop to get list of prod_details
    for result in results:
        # name
        try:
            product_name.append(result.find('a', {'class':'product-title'}).get_text()) 
        except:
            product_name.append('n/a')
        
        # orig price
        try:
            product_orig_price.append(result.find('span', {'class':'money'}).get_text())
        except:
            product_orig_price.append('n/a')
        # discounted price
        try:
            product_discounted_price.append(result.find('span', {'class':'special-price'}).get_text())
        except:
            product_discounted_price.append(result.find('span', {'class':'money'}).get_text())
        # relative URL
        try:
            relative_url.append(result.find('a', {'class':'product-title'}).get('href'))
        except:
                relative_url.append('n/a')

    url_combined = []
    root_url="https://bagallery.com/"
    for link in relative_url:
        url_combined.append(urllib.parse.urljoin(root_url, link))


#Create Pandas Dataframe
product_details= pd.DataFrame({'Name': product_name, 'Original_Price':product_orig_price,'Discounted_Price':product_discounted_price,
                                'Link': url_combined})

#Saved Output in CSV/EXCEL
#product_details.to_csv('product_details_shampoo_2022_08_12.csv')
product_details.to_excel('product_details_shampoo_2022_08_12.xlsx')

# Task 4 Chron job to Human Readable 

from cron_descriptor import get_description,ExpressionDescriptor
print(get_description("0 17 * * 0-5"))
print(get_description("11 5 * * 5,6"))
