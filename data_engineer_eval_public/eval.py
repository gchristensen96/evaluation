import requests
import pandas as pd
import sqlite3
from eval_sql import merge_dummy, create_cities_table, create_csv_export, drop_temp


connection = sqlite3.connect("data.db")
cursor = connection.cursor()


# Objective 1
#Get data from url
url = "https://dummyjson.com/products"
response = requests.get(url)

products_data = response.json()["products"]
# Convert the data to a pandas DataFrame
df = pd.DataFrame(products_data)
# extract needed columns, copy into product_df
product_columns = [
    "id",
    "title",
    "description",
    "price",
    "discountPercentage",
    "rating",
    "stock",
    "brand",
    "category",
    "thumbnail",
]
product_df = df[product_columns].copy()
#Re-name to match existing table
#If I were to do this again, I would pull tables as a dataframe first and check differences instead of this one off approach.
product_df.rename(columns={"discountPercentage": "discount_percentage"}, inplace=True)
#Write to temp table
product_df.to_sql("product_temp", connection, if_exists="replace", index=False)
#Merge temp table with existing table
cursor.execute(merge_dummy("product"))
#Drop temp table
cursor.execute(drop_temp("product_temp"))
connection.commit()

#this was the hardest one for me for sure, I pretty much hacked it. I would do this to a similar standard as I did the others if I had the time.
#get specific image columns for easier use
image_columns = ["id", "images"]
image_df = df[image_columns].copy()
#rename to match existing table
image_df.rename(columns={"id": "product_id"}, inplace=True)
image_df.rename(columns={"images": "url"}, inplace=True)
#XPLODE the table to get individual rows for each URL
image_df = image_df.explode("url")

#this is weird, but it works. I did the merge in pandas instead of SQL, I couldn't figure it out in SQL.
sql_query = """select * from product_image"""
product_image_df = pd.read_sql_query(sql_query, connection)

merged_df = pd.merge(product_image_df, image_df, on="url", how="left")

merged_df.to_sql("product_image_temp", connection, if_exists="replace", index=False)

#Merge temp table with existing table
#Drop temp table
cursor.execute(drop_temp("product_image_temp"))
connection.commit()


#Objective 2
#Create cities_table to write to, declare primary key
cursor.execute(create_cities_table())
#Read csv into dataframe
df = pd.read_csv("cities.csv")
#Add id column
df["id"] = range(1, len(df) + 1)
#Write to temp table
df.to_sql("cities_temp", connection, if_exists="replace", index=False)
#Merge temp table with existing table
cursor.execute(merge_dummy("cities"))
#Drop temp table
cursor.execute(drop_temp("cities_temp"))
connection.commit()

# Objective 3
# Using sql join, get necessary columns and count. JOIN is in eval_sql.py
cursor.execute(create_csv_export())
result = cursor.fetchall()
for row in result:
    # write to csv from dataframe
    df = pd.read_sql_query(create_csv_export(), connection)
    df.to_csv("export.csv", index=False)
    connection.commit()

connection.close()
