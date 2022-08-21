#Important Libraries
import requests
import pandas as pd
import re
import urllib.parse
from bs4 import BeautifulSoup
product=str.upper(input('Please enter your product which you want to scrape data for:'))
if product=='CLEANSERS':
  ############################### For Product Cleansers #######################################

    #Get the HTML 
    url="https://bagallery.com/collections/cleansers"
    request_session=requests.session()
    response=request_session.get(url=url)
    print(response.status_code)

    # Parse the HTML
    soup = BeautifulSoup(
    markup=response.content,
    features="html.parser")

    #Method 2 (Final Cleansers)
    product_name = []
    product_orig_price = []
    product_discounted_price = []
    relative_url=[]
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
    #Saved Output in Excel
    product_details.to_csv('product_details_cleansers.csv')

elif product=='SHAMPOO':
 ############################### For Product Shampoo #######################################

    #Get the HTML 
    url="https://bagallery.com/search?type=product&filter=1&q=shampoo"
    request_session=requests.session()
    response=request_session.get(url=url)
    print(response.status_code)

    # Parse the HTML
    soup = BeautifulSoup(
    markup=response.content,
    features="html.parser")

        #Method 2 (Final Shampoo)
    product_name = []
    product_orig_price = []
    product_discounted_price = []
    relative_url=[]
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
    #Saved Output in CSV
    product_details.to_csv('product_details_shampoo.csv')
else:
    print('your desired product is not available for scrapping')