from bs4 import BeautifulSoup as bs
import scraping
import requests
import pandas as pd
import re
from pathlib import Path

URL = "http://books.toscrape.com/"


def save_images(url: str):
    """ 
        Récupération des images à partir de liens récupérés dans la fonction catch_all_page_catalogue
        Le stockage des images se fait dans dossier "images".
    """

    page_url = scraping.catch_all_page_catalogue(url)
    print("Création du dossier images")
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
            print('Enregistrement de la couverture : ',name)
            with open((f"data\images\{name}.jpg"), 'wb') as f:
                f.write(requests.get(url).content)


def save_book_data(category_url: str):
	"""Sauvegarde des informations récupérées pour chaque livre"""
	
	books_data = []
	pages_urls = scraping.catch_pages_url(category_url)
	books_url = scraping.catch_books_urls(pages_urls)

	for url in books_url:
		
		book = scraping.catch_book_data(url)
		books_data.append(book)

		file_name = books_data[0]["category"]
		folder = Path(f"data\{file_name}")
		folder.mkdir(parents=True, exist_ok=True)

	print('Sauvegarde de : ', file_name)
	pd.DataFrame(books_data).to_csv(f'data/{file_name}/{file_name}.csv', encoding='utf-8')

	return file_name, books_data


def main(url: str):
    """
        Fonction principale qui permet de sauvegarder toutes les données récupérées pour chaques urls
        présentes dans la liste que retourne la fonction catch_all_category_urls 
    """
    
    print('Extraction en cours : ')
    all_products = []
    list_url = scraping.catch_all_category_urls(url)
    print(url)
    for url in list_url:
        save_book_data(url)

