import network   #import des fonction lier au wifi
import urequests  #import des fonction lier au requetes http
import utime      #import des fonction lier au temps
import ujson      #import des fonction lier aà la convertion en Json
from machine import Pin, PWM
from random import randint  #import de la fonction randint pour générer un nombre aléatoire


# initialisation des broches de la Raspberry Pi pour les LED RGB
ledRouge = PWM(Pin(5, mode=Pin.OUT))
ledRouge.freq(1_000) # la frequence est de 1000 (défaut)
ledRouge.duty_u16(0) # la led est éteinte par défaut

ledVert = PWM(Pin(6, mode=Pin.OUT))
ledVert.freq(1_000) 
ledVert.duty_u16(0)

ledBleu = PWM(Pin(7, mode=Pin.OUT))
ledBleu.freq(1_000) 
ledBleu.duty_u16(0) 


# un dictionnaire des types de Pokémon avec leur correspondance aux valeurs RGB
Type_Liste = {
    "Acier": [8800, 18800, 22400],
    "Combat": [51000, 10600, 0],
    "Dragon": [8000, 9600, 65000],
    "Eau": [4100, 12800, 23900],
    "Électrik": [40200, 40000, 0],
    "Fée": [50900, 0, 50900],
    "Feu": [46000, 0, 0],
    "Glace": [0, 50600, 50500],
    "Insecte": [28500, 32100, 5000],
    "Normal": [15900, 16100, 15900],
    "Plante": [0, 46000, 0],
    "Poison": [28500, 13000, 40300],
    "Psy": [46900, 13000, 24100],
    "Roche": [45500, 42900, 25900],
    "Sol": [56500, 20100, 0],
    "Spectre": [55200, 5000, 55200],
    "Ténèbres": [8000, 6500, 6300],
    "Vol": [24900, 36500, 46900]
}


wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'IIM_Private'
password = 'Creatvive_Lab_2023'
wlan.connect(ssid, password) # connecte la raspi au réseau
# définit l'URL de base 
base_url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/"


# Tant que la Raspberry Pi n'est pas connectée, affiche sur la console "pas co"
while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

# Boucle principale pour exécuter le programme indéfiniment.
while True:
    try:
        num = randint(1, 1010)  # génère un nombre aléatoire entre 1 et 1010 inclusivement
        url = base_url + str(num)  # assemble l'URL de base avec le nombre aléatoire généré
        r = urequests.get(url) # lance une requete sur l'url
        Type = r.json()["types"][0]["name"] # cette variable est associé au type du pokemon
        print("ID: ", r.json()["pokedexId"])# affiche sur la console l'Id du pokemon
        print("Nom: ", r.json()["name"]["fr"])# affiche sur la console le nom du pokemon
        print("Type: ", Type) # affiche sur la console le premier type du pokemon
        # Lie les led RGB à la valeur dans le Type_liste correspondant au type du pokemon défini
        ledRouge.duty_u16(Type_Liste[Type][0])
        ledVert.duty_u16(Type_Liste[Type][1])
        ledBleu.duty_u16(Type_Liste[Type][2])
        r.close() # ferme la demande
        utime.sleep(1)
    except Exception as e:
        print(e)