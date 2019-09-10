# requests
# lxml
# beautifulsoup4
# html5lib

from bs4 import BeautifulSoup
import requests
import csv
import re
from apps.base.models import Categories, Books


def scraping():
    Books.objects.all().delete()
    Categories.objects.all().delete()
    html = 'http://books.toscrape.com/index.html'
    source = requests.get(html).text

    soup = BeautifulSoup(source, 'lxml')
    categories = soup.select('a[href^="catalogue/category/books/"]')
    # print(soup.prettify())
    for i, categoria in enumerate(categories,1):
        # print('id: ' + str(i+1))
        name = categoria.get_text().strip()
        # print(categoria.attrs['href'])
        Categories.objects.get_or_create(id=i+1,name=name)

    next = soup.find('li',class_="next")
    # print(next.a.attrs['href'])

    # Algoritmo
    while (next is not None):
        for book in soup.find_all('article'):
            print('href: ' + book.h3.a['href'].strip())
            if 'catalogue/' in book.h3.a['href'].strip():
                html = ('http://books.toscrape.com/' + book.h3.a['href'].strip())
            else:
                html = ('http://books.toscrape.com/catalogue/' + book.h3.a['href'].strip())
            article_source = requests.get(html).text
            article_soup = BeautifulSoup(article_source, 'lxml')
            article = article_soup.find('article',class_='product_page')
            #category
            category = article_soup.find('ul',class_='breadcrumb')
            # print(category)
            category_id = re.findall("\d+", category.find_all('li')[-2].a['href'])[0]
            # product_description
            if article.find('p',class_="") is not None:
                product_description = article.find('p',class_="").get_text()
            else:
                product_description = ''
            # upc
            table = article_soup.find('table',class_='table table-striped')
            rows  = table.find_all('tr')
            for row in rows:
                if row.th.get_text() == 'UPC':
                    upc = row.td.text
            # title
            title = book.h3.a['title'].strip()
            # thumbnail_url
            if '../' in book.div.a.img['src']:
                thumbnail_url = 'http://books.toscrape.com/' + book.div.a.img['src'][3:]
            else:
                thumbnail_url = 'http://books.toscrape.com/' + book.div.a.img['src']
            # price
            price = book.find('p',class_='price_color').get_text()[2:]
            # stock
            if 'In stock' in book.find('p',class_='instock availability').get_text().strip():
                stock = True
            else:
                stock = False
            cat = Categories.objects.get(id=category_id)
            Books.objects.get_or_create(category_id=cat,title=title,thumbnail_url=thumbnail_url,price=price,stock=stock,product_description=product_description,upc=upc)

        next = soup.find('li',class_="next")
        if next is not None:
            if 'catalogue/' in next.a.attrs['href']:
                html = 'http://books.toscrape.com/' + next.a.attrs['href']
            else:
                html = 'http://books.toscrape.com/catalogue/' + next.a.attrs['href']
        else:
            break
        # print(next.a.attrs['href'])
        source = requests.get(html).text
        soup = BeautifulSoup(source, 'lxml')

    return 'Proceso Exitoso!'
