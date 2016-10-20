from lxml import html
import requests

url = 'http://land-book.com';

page = requests.get(url)
tree = html.fromstring(page.content)

#This will create a list of buyers:
xpath = '//figure[@class="website"]//a[starts-with(@href, "/websites/")]/@href'
paths = tree.xpath(xpath)

print paths

path = paths[0];

print path