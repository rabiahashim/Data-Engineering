################################### For Shampoo Category ##############################################

#Important Libraries
import requests
import pandas as pd
import re
import urllib.parse
from bs4 import BeautifulSoup

#Get the HTML 
url="https://bagallery.com/search?type=product&filter=1&q=shampoo"
request_session=requests.session()
response=request_session.get(url=url)
print(response.status_code)

# Parse the HTML
soup = BeautifulSoup(
markup=response.content,
features="html.parser")

# Method 1 

# product_name="div.grid-item div.product-bottom a.product-title span"
# orig_product_price="div.grid-item div.product-bottom span.old-price span.money"
# disc_product_price="div.grid-item div.product-bottom span.special-price span.money"
# product_list_css=soup.select(selector=product_name)
# orig_product_price_ls=soup.select(selector=orig_product_price)
# disc_product_price_ls=soup.select(selector=disc_product_price)
# print(product_list_css)
# print(len(product_list_css))
# print(len(orig_product_price_ls))
# print(len(disc_product_price_ls))

# product_data = {
# "product_name":[],
# "original_price":[],
# "discounted_price":[],
# #"product_url":[]
# }

# for index in range(len(product_list_css)):
#     product_data.get('product_name').append(product_list_css[index].text.strip())  
#     for index1 in range(len(orig_product_price_ls)):
#         product_data.get('original_price').append(orig_product_price_ls[index1].text.strip())
#         product_data.get('discounted_price').append(disc_product_price_ls[index1].text.strip())
   
# product_data

#Method 2 (Final)
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
#product_details.to_csv('product_details_shampoo_2022_08_12.csv')
product_details.to_excel('product_details_shampoo_2022_08_12.xlsx')

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

#Method 2 (Final)
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
#product_details.to_csv('product_details_cleansers_2022_08_12.csv')
product_details.to_excel('product_details_cleansers_2022_08_12.xlsx')


