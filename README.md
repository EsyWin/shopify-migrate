# shopify-migrate

## prerequesites :

node.js and python3 + a shopify to extract data.
learn about extracting shopify data as .csv [here](https://help.shopify.com/en/manual/products/import-export/export-products)

only python dependency : wget

```python
pip3 install -r requirements.txt
```

Edit variables after import statements in "main.py" :

```python
# edit these variables :
githubUsername="EsyWin"
githubRepo="shopify-migrate"
shopifyCSV="shopify.csv"
```

The script assume you saved you CSV file under "CSV/shopify.csv"

## run the script :

```shell
python3 main.py
```

**copy and paste "build/shop.data.json" and "build/shop.data.jsx" in "redux/shop" of our ecommerce app.**

## upload images to your github cdn

This project assume the following cdn folder structure : "images/products"
This path is written to our CSV, shop.data.jsx and later inside firestore !
Laziness to play with python more easily around downloading, string formatting, etc..
You'll find images inside "images/products" after running the script.

```
my-cdn/
├─ readme.md
├─ images/
│  ├─ products/
│  │  ├─ image.jpeg
```

You can follow on [Section 16 : Advanced Redux + Firebase](https://www.udemy.com/course/complete-react-developer-zero-to-mastery/learn/lecture/15188186) when you're done!

P.S : csv/data.csv and build/data.json are junk files that will cost to learn asyc python waiting for node.js to finish : sorry!
