# OpenClassrooms_projet_2_Loic
# Version béta d'un programme de scraping.

La version bêta de ce programme permet d'automatiser la récupération des données liées aux livres, depuis le site http://books.toscrape.com/ . 

Le programme récupère puis exporte les informations suivantes au format csv : 

1. Le titre (title)

2. Le prix (price)

3. La note (review_rating)

4. L'url de l'image (image_url)

5. La description (description)

6. Le numéro UPC (UPC)

7. Le type de produit (Product_Type)

8. Le prix HT (Price_excl_tax_)

9. Le prix TTC (Price_incl_tax_)

10. Le montant de la Taxe (Tax)

11. La quantité de livre disponible (number_available)

12. Number_of_reviews

## Pré-requis 

* Python 3 installé ([Télécharger Python](https://www.python.org/downloads/))
* Git ([Télécharger Git](https://github.com/))

## Installation

Pour la suite des instructions je conseille aux utilisateurs de Windows d'utiliser ([gitbash](https://git-scm.com/downloads))

1. **Téléchargement du projet.**


    Depuis votre terminal, placez-vous à l'endroit souhaité:
    
    ```cd [chemin d'accès]```  
    
    Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    Copier le programme source:
    
    ```git clone https://github.com/Lockco/Open-Classrooms-Projet-2```
    
     Vous devez voir (depuis votre explorateur) les fichiers suivants:
        * __main__.py
        * __init__.py
        * save_data.py
        * scraping.py
        * README.md
        * requirements.txt
    
    ![](gif/telecharger_projet.gif)


2. **Creer un environnement virtuel.**

    Depuis windows/mac/linux: ```python3 -m venv env``` ou ```py -m venv env```
    
3. **Activer l'environnement.**
    
    Depuis windows: ``` source env\Scripts\activate.bat``` si cette commande ne fonctionne pas essayer la commande suivante : ```source env\Scripts\activate```
    
    Depuis mac/linux: ```source env/bin/activate```

4. **Installer les paquets.**

    Attention : pour éviter de rencontrer des problème avec ```pip``` veillez à vérifier que PYTHONPATH soit correctement configurées : 
    ([PYTHONPATH](https://datatofish.com/add-python-to-windows-path/))

    ```pip install -r requirements.txt```

    En éxecutant la commande: ```pip freeze```, vous devez voir apparaitre cette liste: 

        beautifulsoup4==4.11.1
        certifi==2022.5.18.1
        charset-normalizer==2.0.12
        idna==3.3
        numpy==1.22.4
        pandas==1.4.2
        python-dateutil==2.8.2
        pytz==2022.1
        requests==2.27.1
        six==1.16.0
        soupsieve==2.3.2.post1
        urllib3==1.26.9
        parse==1.19.0

    ![](gif/creation_env.gif)

5. **Lancement du programme**

    Pour le démarrage du programme dans votre terminal verifier que vous êtes dans le dossier 
    où le projet a été cloné avec la commande suivante

    Sous linux : ```ls``` 
    Sous windows : ```dir```
    
    
    puis lancer le script à l'aide de la commande suivante :

    ```py __main__.py```

    Lors du démarrage vous aurez le choix entre 3 options :

        1. Extraire les informations des livres : 

            L'option 1 lancera le script et va récupérer les informations de chaque livre par catégorie.
            Cela créera un dossier nommé "data" puis l'extraction de chaque catégorie créera un dossier dans lequel vous trouverez le fichier .csv contenant les données récupérées.

        2. Extraire les couvertures des livres :

            L'option 2 lancera le script et récupéra toutes les images depuis la page d'accueil.
            Cela entrainera la création d'un dossier data (s'il n'existe pas encore) puis d'un dossier images dans lequel vous trouverez toutes les couvertures des livres au format .jpg.

        3. Quitter l'application :

            L'option 3 vous permet de quitter l'application

    ![](gif/lancer_programme.gif)
            
## Logiciel utilisé
[Visual Studio Code] (https://code.visualstudio.com/download)
[gitbash] (https://git-scm.com/downloads)

## Remerciements

Merci à **Julien**, **Thibault**, pour leur patience et leur aide précieuse. 





