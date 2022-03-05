# import statements, wget is the only dependency
import os
import csv
import wget
import json

# edit these variables :
githubUsername="EsyWin"
githubRepo="shopify-migrate"
shopifyCSV="shopify.csv"
# global variables
fieldnames = ['id', 'title', 'imageUrl', 'price', 'category']
categories = []
x=1

# carefully pre-clean from example run
junkJSON='build/data.json'
junkBeanie='images/products/kids-beanie.jpg'
junkJean='images/products/distressed-kids-jeans.jpg'
junkTShirt='images/products/green-t-shirt.jpg'

def cleanJunk(junkPath):
    if os.path.exists(junkPath):
        os.remove(junkPath)
cleanJunk(junkBeanie)
cleanJunk(junkJean)
cleanJunk(junkTShirt)
with open('csv/data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
# open shopify csv file
with open('csv/{}'.format(shopifyCSV), newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # extract values from rows in"shopify.csv"
        #  you might have to play around these values, uncomment next line to alls csv rows :
        print(row)
        title=row['Title']
        imageUrlShopify=row['Image Src']
        price=row['Variant Price']
        category=row['Custom Product Type']
        if imageUrlShopify:
            # remove "?v=xxx" after file extension
            imageUrlRaw=imageUrlShopify.split('?')
            imageUrl=imageUrlRaw[0]
            # enter path where images will be hosted, assuming "example.com/" to download images in "/images/products/"
            cdnPath=r"https://raw.githubusercontent.com/{}/{}/main/".format(githubUsername, githubRepo)

            # download images using wget, comment code block below to skip download :
            imagePath=r"images/products/{}".format(imageUrl.split("/")[-1])
            image_filename = wget.download(imageUrl, imagePath)
            print('Image Successfully Downloaded: ', image_filename)
            fullPath=cdnPath+imagePath
        
        # uncomment the line below to skip download
        # fullPath=cdnPath+'images/products/'+handle+'.jpg'

        # append rows to our csv
        with open('csv/data.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'id': x, 'title': title, 'imageUrl':fullPath, 'price': price, 'category': category}),
            x+=1

# convert our fresh data.csv into json
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'csv/data.csv'
jsonFilePath = r'build/data.json'
csv_to_json(csvFilePath, jsonFilePath)
os.popen('node index.js')