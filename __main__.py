from save_data import main, save_images



URL = "http://books.toscrape.com/"


def display():

    print("""
            ----------------------------------------
            Bienvenu dans l'outil d'extraction de donnée

            choisissez une option :

            1 : Extraire les informations des livres
            2 : Extraire les couvertures des livres
            3 : Quitter l'application
            ----------------------------------------
            """
            )
            
    choix = input("Votre choix -> ")
    choix_menu = ["1","2","3"]

    while choix in choix_menu:

        if choix  == "1":
            main(URL)

        elif choix == "2":
            save_images(URL)

        elif choix == "3":
            print("Au revoir")
            exit()

    print('Saisi invalide')
    return display()

display()