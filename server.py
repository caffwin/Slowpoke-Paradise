from pymongo import MongoClient
from random import randint
from datetime import datetime
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
import base64
import os

client = MongoClient(os.environ["MONGO_CONNECTION_STRING"])
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)


db = client.paradise

#Step 2: Create sample data
# names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
# company_type = ['LLC','Inc','Company','Corporation']
# company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
# for x in range(1, 501):
#     business = {
#         'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
#         'rating' : randint(1, 5),
#         'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
#     }
#     #Step 3: Insert business object directly into MongoDB via isnert_one
#     result=db.reviews.insert_one(business)
#     #Step 4: Print to the console the ObjectID of the new document
#     print('Created {0} of 100 as {1}'.format(x,result.inserted_id))
#Step 5: Tell us that you are done
# print('finished creating 100 business reviews')

fivestar = db.reviews.find_one({'rating': 5})
pprint(fivestar)

pprint("******")
fivestar_find = db.reviews.find({'rating': 5})

for item in fivestar_find:
    pprint(item)

class CollectionItem():

    # def __init__(self, tags = [], title, artist=null , ):
    # img = 
    img_title = "" 
    img_desc = ""
    region = ""
    date = datetime.today()
    category = ""

yadon_db = client["mydatabase"]
yadon_collection = yadon_db["All Items"]

#use property of this pic and convert to base64

encoded_string = ""

with open("smolimg.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

print(encoded_string)

zukan_figure = { "img": encoded_string, "img_title": "zukan.jpg", "img_desc": "1:40 scale high quality figurine", "region": "Japan", "category": "Figure" }


# zukan_figure = CollectionItem(img_title="zukan.jpg", img_desc="1:40 scale high quality figurine", region="Japan", date = datetime.utcnow(), category="Figure")
# tomy_figure = CollectionItem(img_title="tomys.jpg", img_desc="Tomy Figurines", region="Japan", date = datetime.utcnow(), category="Figure")
# taffeta_plush = CollectionItem(img_title="taffetaplush.jpg", img_desc="Soft plush", region="Japan", date = datetime.utcnow(), category="Plush")

# db.images.insert_one(zukan_figure)
# db.images.insert_one(tomy_figure)
# db.images.insert_one(taffeta_plush)

# x = yadon_collection.insert_one(zukan_figure)
print("Hello World")
# img
# img_title
# img_desc
# region
# date
# category/type (plush/figures/misc/flats/)
# img_size (option)






# yadon_item = {"img_title": "zukan.jpg", }

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }


# zukan_figure = { "img_title": "zukan.jpg", "img_desc": "1:40 scale high quality figurine", "region": "Japan", "category": "Figure" }

# x = mycol.insert_one(mydict)




print("End")
