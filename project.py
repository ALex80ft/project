from colorama import Fore, Style, init
import os
import re  # Pentru validarea adresei de email
from googlesearch import search  # Importați googlesearch

# Inițializează colorama pentru a putea folosi culorile în terminal
init(autoreset=True)

# Definirea funcției pentru a afișa interfața principală
def display_main_interface():
    # ASCII art pentru "WISEE AI"
    ascii_art = """
    ██     ██ ██ ███████ ███████ ███████ ███████     █████  ██ 
    ██     ██ ██ ██      ██      ██      ██         ██   ██ ██ 
    ██  █  ██ ██ █████   ███████ █████   █████      ███████ ██ 
    ██ ███ ██ ██ ██           ██ ██      ██         ██   ██ ██ 
     ███ ███  ██ ███████ ███████ ███████ ███████    ██   ██ ██ 
    """

    # Textul suplimentar cu spații între litere
    additional_text = "꧁༺ 𝓢𝓐𝓝𝓓𝓓𝓡𝓐𝓖𝓞𝓝𝓤24 ༻꧂"
    additional_text_spaced = " ".join(additional_text)  # Adaugă spații între caractere

    # Listă cu elementele
    list_items = [
        "1. Crypto", "2. Free Movie", "3. QPython3", "4. Hosting",
        "5. Website domain", "6. APIs Restful", "7. Edit Website", "8. AI tools"
    ]

    # Obține dimensiunile terminalului
    size = os.get_terminal_size()
    columns = size.columns
    rows = size.lines

    # Determină lungimea celei mai lungi linii din ASCII art pentru centrare corectă
    max_line_length = max(len(line) for line in ascii_art.splitlines())
    additional_text_length = len(additional_text_spaced)

    # Calcul pentru centrare pe orizontală și verticală
    padding_left_ascii = (columns - max_line_length) // 2
    padding_left_text = (columns - additional_text_length) // 2
    padding_top = (rows - len(ascii_art.splitlines()) - 2 - 6) // 2  # -6 pentru spațiul listelor și containerului

    # Adaugă spațiul de sus pentru centrare verticală
    print("\n" * padding_top, end="")

    # Afișează ASCII art-ul colorat în roșu și centrat
    for line in ascii_art.splitlines():
        print(" " * padding_left_ascii + Fore.RED + line + Style.RESET_ALL)

    # Linie goală pentru spațiu suplimentar
    print()

    # Afișează textul suplimentar centrat și colorat în galben, cu spațiu între caractere
    print(" " * padding_left_text + Fore.YELLOW + additional_text_spaced + Style.RESET_ALL)

    # Linie goală între textul galben și liste
    print("\n")

    # Calcul pentru centrare liste
    max_item_length = max(len(item) for item in list_items[:4])  # Lungimea maximă a unui element din prima coloană
    padding_left_list = (columns - max_item_length * 2 - 4) // 2  # -4 pentru spațiul dintre coloane

    # Afișează listele în două coloane
    for i in range(4):
        left_item = Fore.GREEN + list_items[i] + Style.RESET_ALL
        right_item = Fore.GREEN + list_items[i + 4] + Style.RESET_ALL
        print(" " * padding_left_list + left_item + " " * 4 + right_item)

    # Linie goală pentru spațiu suplimentar înainte de container
    print("\n")

    # Container pentru mesajul de introducere
    container_width = 40  # lățimea containerului
    padding_left_container = (columns - container_width) // 2
    print(" " * padding_left_container + "-" * container_width)
    print(" " * padding_left_container + "| Introduceți una dintre cifrele de mai sus |")
    print(" " * padding_left_container + "-" * container_width)

    # Solicitare de introducere a opțiunii
    choice = input(" " * (padding_left_container + 10) + Fore.CYAN + "Alegeți o opțiune (1-8): " + Style.RESET_ALL)

    # Verifică opțiunea aleasă
    if choice == '1':
        display_crypto_interface()
    elif choice == '2':
        display_free_movies_interface()
    elif choice == '3':
        print(Fore.RED + "Eroare: Această opțiune nu este disponibilă." + Style.RESET_ALL)
    elif choice == '4':
        display_domain_purchase_interface()

# Definirea funcției pentru a afișa interfața Crypto
def display_crypto_interface():
    # Curăță terminalul
    os.system('cls' if os.name == 'nt' else 'clear')

    # Afișează simbolul de întoarcere
    print(Fore.GREEN + "<" + Style.RESET_ALL)

    # Container pentru criptomonede
    container_width = 40
    padding_left_container = (os.get_terminal_size().columns - container_width) // 2
    print(" " * padding_left_container + "-" * container_width)
    print(" " * padding_left_container + "| Bitcoin ฿               |")
    print(" " * padding_left_container + "|" + " " * (container_width - 2) + "|")  # Linie goală
    print(" " * padding_left_container + "| Ethereum ฿             |")
    print(" " * padding_left_container + "|" + " " * (container_width - 2) + "|")  # Linie goală
    print(" " * padding_left_container + "| Dogecoin ฿             |")
    print(" " * padding_left_container + "-" * container_width)

# Definirea funcției pentru a afișa interfața cu filme gratuite
def display_free_movies_interface():
    # Curăță terminalul
    os.system('cls' if os.name == 'nt' else 'clear')

    # Afișează simbolul de săgeată
    print(Fore.GREEN + "---->" + Style.RESET_ALL)

    # Generarea link-urilor pentru filme
    movies = [
        "site de filme online 1",
        "site de filme online 2",
        "site de filme online 3",
        "site de filme online 4",
        "site de filme online 5",
        "site de filme online 6",
        "site de filme online 7",
        "site de filme online 8",
        "site de filme online 9",
        "site de filme online 10",
        "site de filme online 11",
        "site de filme online 12",
        "site de filme online 13",
        "site de filme online 14",
        "site de filme online 15",
        "site de filme online 16",
        "site de filme online 17",
        "site de filme online 18",
        "site de filme online 19",
        "site de filme online 20"
    ]

    # Afișează titlurile de filme colorate în roșu
    print("\n" + Fore.RED + "Site-uri de filme online:" + Style.RESET_ALL)
    for i, movie in enumerate(movies):
        # Generarea căutării pentru fiecare site
        query = f"{movie} free movies site"
        search_results = search(query, num_results=1)  # Caută doar primul rezultat

        for url in search_results:
            print(Fore.RED + f"{'---> https://'}{url}" + Style.RESET_ALL)

# Definirea funcției pentru a valida adresa de email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Definirea funcției pentru a afișa interfața de achiziție a domeniilor
def display_domain_purchase_interface():
    # Curăță terminalul
    os.system('cls' if os.name == 'nt' else 'clear')

    # Solicită utilizatorului să introducă un nume de website
    website_name = input(Fore.CYAN + "Introduceți numele website-ului: " + Style.RESET_ALL)

    # Solicită utilizatorului să introducă o adresă de email
    email = input(Fore.CYAN + "Introduceți adresa de email: " + Style.RESET_ALL)

    # Verifică dacă adresa de email este validă
    if not is_valid_email(email):
        print(Fore.RED + "Eroare: Adresa de email nu este validă." + Style.RESET_ALL)
        return

    # Dicționar cu extensiile de domeniu și prețurile
    domains = {
        ".com": 2.99,
        ".ro": 1.91,
        ".net": 2.99,
        ".io": 3.11,
        ".info": 4.00
    }

    # Afișează opțiunile de domenii
    print("\n" + Fore.YELLOW + "Alegeți un tip de domeniu:" + Style.RESET_ALL)
    for domain, price in domains.items():
        print(Fore.GREEN + f"{domain} - {price:.2f} EUR  [Cumpără]" + Style.RESET_ALL)

    # Solicită utilizatorului să aleagă un domeniu
    chosen_domain = input(Fore.CYAN + "Introduceți extensia domeniului dorit (.com, .ro, .net, .io, .info): " + Style.RESET_ALL)

    # Verifică dacă domeniul ales este valid
    if chosen_domain in domains:
        price = domains[chosen_domain]
        print(Fore.GREEN + f"\nDomeniul {website_name}{chosen_domain} a fost livrat cu succes la adresa de email {email}. Prețul este {price:.2f} EUR." + Style.RESET_ALL)
        
        # Simulează trimiterea detaliilor prin email
        print(Fore.GREEN + f"Informațiile despre achiziție au fost trimise la oprea7516@gmail.com." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Eroare: Domeniul ales nu este valid." + Style.RESET_ALL)

# Rularea interfeței principale
display_main_interface()
