import save_data


URL = "http://books.toscrape.com/"


def display():
    
    print("""
            ----------------------------------------
            Bienvenue dans l'outil d'extraction de données

            choisissez une option :

            1 : Extraire les informations des livres
            2 : Extraire les couvertures des livres
            3 : Quitter l'application
            ----------------------------------------
            """
            )
            
    choix = input("Votre choix -> ")
    choix_menu = ["1","2","3"]

    
    if choix not in choix_menu:

        print(" Saisi invalide ")
        return display()

    else:

        if choix  == "1":
            save_data.main(URL)
            print("Extractions des informations terminées. ")

        elif choix == "2":
            save_data.save_images(URL)
            print("Les couvertures ont bien été extraitent et sauvegardées. ")

        elif choix == "3":
            print("Au revoir")
            exit()

display()