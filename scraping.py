from bs4 import BeautifulSoup as bs
from pathlib import Path
import requests
import re
import math

URL = "http://books.toscrape.com/"


def catch_parser(url: str) -> bs:
	"""Envoie de la requête à l'url et retourne de le contenu de la page html"""

	print('Etape 3 : book_request')
	response = requests.get(url)
	content_book_url = bs(response.content, 'html.parser')
	return content_book_url


def catch_all_page_catalogue(url: str) -> list:
    """ Récupération des 50 pages présente sur la page d'accueil du site pour récupérer les images"""

    page = 1
    pages_url = []

    while True:
        page_url = (url +'catalogue/' + f"page-{page}.html")
        page += 1
        response = requests.get(page_url)
        if response.status_code == 200:
            pages_url.append(page_url)
        else:
            break
    return pages_url


def catch_all_category_urls(url: str) -> list:
    """ Récupération des urls de chaque catégorie présente sur le site"""

    print("Etape 2 : Extraction")
    all_category = []
    soup = catch_parser(url)
    all_ul = soup.find('div', class_="side_categories").find('ul').find_all('li')[1:]
    for category_url in all_ul:
        href = category_url.find("a")["href"]
        url = URL+("/")+href
        all_category.append(url)
    print(all_category)
    return all_category


def catch_pages_url(category_url: str) -> int:
	""" Récupération des urls des pages à partir des urls de chaque catégorie"""

	print('Etape 4 : catch_categories_url')
	pages_urls = []
	number_of_pages = catch_number_of_pages_from_category(category_url)
	if number_of_pages == 1:
		pages_urls.append(category_url)
	else:
		for i in range(number_of_pages):
			page_url = category_url.replace("index.", f"page-{i + 1}.")
			print('Extraction de la page : ', page_url)
			pages_urls.append(page_url)
	return pages_urls


def catch_books_urls(pages_urls: list) -> list:
	""" Récupération des urls de tous les livres présents dans chaque catégorie"""

	books_url = []
	print('Etape 4 catch_book_urls')
	for page_url in pages_urls:
		content = catch_parser(page_url)
		titles = content.find_all("h3")
		for title in titles:
			href = title.find('a')["href"]
			if "../../.." in href:
				url = href.replace(
					"../../../", "http://books.toscrape.com/catalogue/")
			else:
				url = "http://books.toscrape.com/" + href

			books_url.append(url)
	print(books_url)
	return books_url


def catch_number_of_pages_from_category(categories_url: str) -> int:
	""" 
		Vérification du nombre de pages présentes dans la catégorie
		On récupère le nombre total de livres présents dans la catégorie
		Sachant qu'il y a 20 livres par pages on divise le résultat par 20 
		et on arrondit au nombre supérieur pour récupérer le nombre de pages

	"""

	content = catch_parser(categories_url)
	number_element_page = content.select("strong")[1].text
	page_in_int = int(number_element_page)
	division_pages = page_in_int / 20
	number_of_page = math.ceil(division_pages)
	print('Nombre de page présente ', number_of_page)
	return number_of_page


def catch_book_data(url: str) -> dict:
	"""Récupération des données des livres"""

	url = catch_parser(url)
	print('Etape 5 catch_book_data')
	main = url.find(class_='product_main')
	book_data = {}

	book_data['title'] = main.find('h1').get_text(strip=True)
	book_data['category'] = url.find('ul', class_='breadcrumb').find_all('a')[2].get_text(strip=True)
	book_data['price'] = main.find(class_='price_color').get_text(strip=True).replace('Â', '')
	book_data['review_rating'] = ' '.join(main.find(class_='star-rating') \
	                                      .get('class')).replace('star-rating', '').strip()
	book_data['image_url'] = url.find(class_='thumbnail').find('img').get('src').replace('../../',
	                                                                                     'https://books.toscrape.com/')
	desc = url.find(id='product_description')

	if desc:
		book_data['description'] = desc.find_next_sibling('p') \
			.get_text(strip=True)
	book_product_table = url.find(text='Product Information').find_next('table')
	for row in book_product_table.find_all('tr'):
		header = row.find('th').get_text(strip=True)
		header = re.sub('[^a-zA-Z]+', '_', header)
		value = row.find('td').get_text(strip=True).replace('Â', '')
		book_data[header] = value

	return book_data


def catch_all_category_urls(url: str) -> list:
    """ Récupération des urls de chaque catégorie présente sur le site"""

    print("Etape 2 : Extraction")
    all_category = []
    soup = catch_parser(url)
    all_ul = soup.find('div', class_="side_categories").find('ul').find_all('li')[1:]
    for category_url in all_ul:
        href = category_url.find("a")["href"]
        url = URL+("/")+href
        all_category.append(url)
    print(all_category)
    return all_category


def catch_images(url: str):
    """ 
        Récupération des images à partir de liens récupérés dans la fonction catch_all_page_catalogue
        Le stockage des images se fait dans dossier "images".
    """

    page_url = catch_all_page_catalogue(url)
    folder = Path("data/images/")
    folder.mkdir(parents=True, exist_ok=True)
    for links in page_url:
        print('Extraction de la page : ', links)
        result = requests.get(links)
        content = result.text
        content_page = bs(content, 'lxml')
        images = content_page.find_all('img')
        

        for image in images:
            name = image['alt']
            url =(URL + image['src'])
            print(name)
            name = re.sub(r"['\"[\]{}()?\-\+*&é;:./!,$=#]*","",name)
            print('nouveau nom',name)
            with open((f"data\images\{name}.jpg"), 'wb') as f:
                f.write(requests.get(url).content)

