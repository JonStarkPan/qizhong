import requests
import lxml
import csv
import pymysql
from lxml import etree


def get_page():
    result = []
    for a in range(0, 10):
        url = 'https://movie.douban.com/top250?start=%s&filter=' % a*25
        res = requests.get(url)
        tree = etree.HTML(res.text)
        top250 = tree.xpath('//span[@class="title"][1]/text()')
        result += top250
    return result
res = get_page()
print(res)

db = pymysql.connect("localhost", "root", "123456", "test")
cursor = db.cursor()
print(res)
sql = "INSERT INTO testmodel_test(movie_name) VALUES(%s)"
for a in res:
    cursor.execute(sql, (a))
    db.commit()
db.close()
