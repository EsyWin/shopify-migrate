# shopify-migrate

## prerequesites :

node.js and python3 + a shopify to extract data.
learn about extracting shopify data as .csv [here](https://help.shopify.com/en/manual/products/import-export/export-products)

only python dependency : wget

```python
pip3 install -r requirements.txt
```

Edit values in "main.py" : githubUsername and githubRepo line 7 to 9 with your actual github username and repo :

```python
# edit these variables :
githubUsername="EsyWin"
githubRepo="shopify-migrate"
```

## run the script :

```shell
python3 main.py
```

The main output of this script are "build/shop.data.json" and "build/shop.data.jsx" which consume this json just as our previous SHOP_DATA to copy and paste inside "redux/shop" of our Ecommerce App.

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

You can follow on [Section 16 : Advanced Reduc + Firebase](https://www.udemy.com/course/complete-react-developer-zero-to-mastery/learn/lecture/15188186) when you're done!

P.S : csv/data.csv and build/data.json are junk files that will cost to learn asyc python waiting for node.js to finish : sorry!
