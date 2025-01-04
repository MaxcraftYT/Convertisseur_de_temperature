import time
import sys
from termcolor import colored
from tqdm import tqdm  # Ajout de la barre de progression

# Fonction pour afficher le message de bienvenue avec un affichage plus moderne
def afficher_bienvenue():
    print(colored("==============================================", "dark_grey"))
    time.sleep(0.5)  # Pause de 0,5 seconde
    print(colored("🚀 Bienvenue dans le convertisseur de température 🌡️", "white"))
    time.sleep(0.5)  # Pause de 0,5 seconde
    print(colored("==============================================", "dark_grey"))

# Fonction pour demander et valider la saisie de l'utilisateur
def demander_temperature():
    while True:
        try:
            celsius = float(input(colored("\n🌡️ Entrez votre température en Celsius :", "magenta")))
            return celsius
        except ValueError:
            print(colored("❌ Veuillez entrer un nombre valide pour la température en Celsius.", "red"))

# Fonction pour convertir la température selon l'unité choisie
def convertir_temperature(celsius, choix_unite):
    if choix_unite == 'F':
        return 1.8 * celsius + 32
    elif choix_unite == 'K':
        return celsius + 273.15
    else:
        return None  # Retourner None si l'unité est incorrecte

# Fonction pour afficher une barre de progression lors de la conversion
def afficher_animation():
    print(colored("\n🔄 Conversion en cours, veuillez patienter...", "yellow"))
    for _ in tqdm(range(100), desc="Conversion", ncols=100, ascii=True):
        time.sleep(0.02)  # Simulation d'une conversion avec une barre de progression

# Fonction pour afficher le résultat avec plus de modernité
def afficher_resultat(celsius, fahrenheit, kelvin):
    print("\n\033[1;35m✨ Résultats :\033[0m")
    print()
    if fahrenheit is not None:
        print(colored(f"🌡️ Température en Celsius : {celsius:.2f}°C", "white"))
        print(colored(f"🔥 Température en Fahrenheit : {fahrenheit:.2f}°F", "white"))
    if kelvin is not None:
        print(colored(f"❄️ Température en Kelvin : {kelvin:.2f}K", "white"))

# Fonction pour afficher le message de fin
def afficher_message_fin():
    print()
    time.sleep(0.5)  # Pause de 0,5 seconde
    print(colored("Merci d'avoir utilisé notre programme ! 🙏", "white"))
    print(colored("=======================================", "dark_grey"))

# Fonction pour afficher un menu de conversion avec choix d'unités
def afficher_menu_conversion():
    print(colored("\n🔧 Choisissez l'unité de conversion :", "cyan"))
    print(colored("1 - Convertir en Fahrenheit (°F)", "yellow"))
    print(colored("2 - Convertir en Kelvin (K)", "yellow"))
    choix = input(colored("\nEntrez votre choix (1 ou 2) : ", "cyan"))
    return choix

# Fonction principale avec gestion de la répétition
def main():
    afficher_bienvenue()  # Affiche le message de bienvenue
    while True:
        celsius = demander_temperature()  # Demande la température en Celsius
        choix = afficher_menu_conversion()  # Choix de l'unité de conversion
        
        if choix == '1':
            fahrenheit = convertir_temperature(celsius, 'F')
            kelvin = convertir_temperature(celsius, 'K')
        elif choix == '2':
            fahrenheit = convertir_temperature(celsius, 'F')
            kelvin = convertir_temperature(celsius, 'K')
        else:
            print(colored("❌ Choix invalide. Veuillez entrer 1 ou 2.", "red"))
            continue
        
        afficher_animation()  # Affiche l'animation de conversion
        afficher_resultat(celsius, fahrenheit, kelvin)  # Affiche le résultat
        
        # Demander à l'utilisateur s'il souhaite effectuer une nouvelle conversion
        refaire = input(colored("\nVoulez-vous faire une autre conversion ? (y/n) : ", "yellow")).lower()
        if refaire != 'y':
            afficher_message_fin()  # Affiche le message de fin
            break

# Lancer le programme
if __name__ == "__main__":
    main()