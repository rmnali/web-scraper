# install packages using command line
 # pip/pip3 install beautifulsoup4
 # pip/pip3 install requests

# import packages
import requests
from bs4 import BeautifulSoup
import csv

# before using header, site content wouldn't load and access denied error would appear inside HTML tags user agent is
# used to simulated a user browsing the site

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# sends GET request to reach URL
linkURL = 'https://www.noon.com/egypt-en/electronics-and-mobiles/mobiles-and-accessories/'
pageAddress = requests.get(linkURL, headers=HEADERS)

# uses content function to load page content(HTML)
pageContent = pageAddress.content

# use BeautifulSoup to parse HTML, "html.parser" is chosen as a HTML parser because no package installation required
soup = BeautifulSoup(pageContent, "html.parser")

# find elements that has the intended content like product name & price
productNames = soup.find_all("div", {"class": "kDpjlW"})
productPrices = soup.find_all("strong")

# create CSV file, create rows for product price and name, write data into file
fileName = "products.csv"
f = open(fileName, "w")

colTitle = "Product Name, Product Price\n"
f.write(colTitle)

# using while loop to iterate on product names and prices and extract product info then make a list
i = 0
while i < len(productNames):
    product_name = productNames[i].div["title"]         # extract name from title HTML attribute
    product_price = productPrices[i].text               # extract price from span HTML element
    i += 1                                              # iterate to next item in list
    print(product_name)
    print(product_price)
    f.write(product_name.replace("\n", " ") + "," + product_price + "\n")   # write extracted data to CSV file

# close file
f.close()
