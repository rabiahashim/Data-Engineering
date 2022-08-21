######## Pak wheels Car Details data########
import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib

url="https://www.pakwheels.com/new-cars/"
session_request=requests.session()
response=session_request.get(url=url)
response.status_code
#Parse The HTML
soup = BeautifulSoup(
markup=response.text,
features="html.parser")
#complete data
product_css=soup.find_all('div',class_="cards")

##Lists to store information
car_name=[]
car_price=[]
launch_date=[]
car_reviews=[]
relative_url=[]
website_name=[]

# loop through product_css
for all_data in product_css:
     # car title
      try:
        car_name.append(all_data.find('a',class_="show").get_text().strip())
      except:
        car_name.append('n/a')
      # car price
      try:
        car_price.append(all_data.find('div',class_="generic-green truncate fs14").get_text().strip())
      except:
        car_price.append('n/a')
       # car launching date
      try:
        launch_date.append(all_data.find('div',class_="mt10 mb10 generic-gray").get_text().strip())
      except:
        launch_date.append('Not Disclosed')
       # car reviews
      try:
        car_reviews.append(all_data.find('span',class_="fs14 generic-gray ml5 dib").get_text().strip())
      except:
        car_reviews.append('0 Reviews')
     # car url
      try:
        relative_url.append(all_data.find('a',class_="show").get('href'))
      except:
        relative_url.append('n/a')
     #Website Name
      website_name.append('PakWheels')


url_combined = []
root_url="https://www.pakwheels.com/new-cars/"
for link in relative_url:
    url_combined.append(urllib.parse.urljoin(root_url, link))

#Create Pandas Dataframe
product_details= pd.DataFrame({'Name': car_name, 'Price':car_price,'Launching_Date':launch_date,'Reviews':car_reviews,
                               'Link': url_combined,'website_name':website_name})
#Saved Output in CSV
product_details.to_csv('pakwheels_Details_Data.csv',index=False)


######## CarFirst  Details data########
import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.parse

##Lists to store information
car_name=[]
car_price=[]
launch_date=[]
car_reviews=[]
relative_url=[]
website_name=[]


for i in range (1,4):
    
    # website in variable
    url = 'https://buy.carfirst.com/?page=' + str(i)
    
    # request
    request_session=requests.session()
    response=request_session.get(url=url)
    
    # soup object
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # all_data
    product_css=soup.find_all('div',class_="grid-5-col")
    
    # loop through product_css
    for all_data in product_css:
          # car title
      try:
        car_name.append(all_data.find('h4').get_text().strip())
      except:
        car_name.append('n/a')
      # car price
      try:
        car_price.append(all_data.find('h5',class_="price").get_text().strip())
      except:
        car_price.append('n/a')
           # car launching date
      try:
        launch_date.append(all_data.find('p',class_="text-muted text-small").get_text().strip()[:4])
      except:
        launch_date.append('Not Disclosed')
      # car reviews are not provided

      car_reviews.append('Reviews are not disclosed')
      # car url
      try:
        relative_url.append(all_data.find('a').get('href'))
      except:
        relative_url.append('n/a')
      #Website Name
      website_name.append('CarFirst')


url_combined = []
root_url="https://buy.carfirst.com/"
for link in relative_url:
    url_combined.append(urllib.parse.urljoin(root_url, link))


#Create Pandas Dataframe
product_details= pd.DataFrame({'Name': car_name, 'Price':car_price,'Launching_Date':launch_date,'Reviews':car_reviews,
                               'Link': url_combined,'website_name':website_name})
#Saved Output in CSV
product_details.to_csv('CarFirst_Details_data.csv',index=False)
#product_details.to_excel('Car_Details.xlsx')