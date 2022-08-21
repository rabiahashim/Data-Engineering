import pymysql
import pandas as pd
import pandas.io.sql as sql

# Connect to the database
def create_connection():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='ERMDB')
    return(connection)

# create new table using execute command
# table query
query1 = '''CREATE TABLE `car_details` (
   `car_name` varchar(900) NOT NULL ,
   `car_price`  varchar(900) NOT NULL ,
   `launch_date`  VARCHAR(900) NOT NULL,
   `car_reviews` varchar(900) NOT NULL,
   `relative_url` varchar(900) NOT NULL,
   `website_name` varchar(900) NOT NULL
) ;'''

#Loading scrapped data in dataframes
CarFirst_Details_data=pd.read_csv('CarFirst_Details_data.csv')
CarFirst_Details_data.columns=['car_name','car_price','launch_date','car_reviews','relative_url','website_name']
PakWheels_Details_data=pd.read_csv('pakwheels_Details_Data.csv')
PakWheels_Details_data.columns=['car_name','car_price','launch_date','car_reviews','relative_url','website_name']
print(CarFirst_Details_data.head(3))
print(PakWheels_Details_data.head(3))


# creating column list for insertion
cols = "`,`".join([str(i) for i in CarFirst_Details_data.columns.tolist()])
cols

connection=create_connection()
with connection:
       with connection.cursor() as cursor:
           cursor.execute(query1)
           connection.commit()
       # connection is not autocommit by default. So you must commit to save
       # your changes.
       with connection.cursor() as cursor:
        # Insert DataFrame of CarFirst recrds one by one.
            for i,row in CarFirst_Details_data.iterrows():
                sql = "INSERT INTO `car_details` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
                cursor.execute(sql, tuple(row))
                connection.commit()  # the connection is not autocommitted by default, so we must commit to save our changes 
        # Insert DataFrame of PakWheels recrds one by one.
       with connection.cursor() as cursor:
            for i,row in PakWheels_Details_data.iterrows():
                sql = "INSERT INTO `car_details` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
                cursor.execute(sql, tuple(row))
                connection.commit()