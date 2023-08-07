import pychrome

# Fonction pour vérifier les certificats SSL/TLS
def check_ssl_certificates():
    url = "https://example.com"  # Remplacez par l'URL de votre site

    # Créer une instance du navigateur Chrome
    browser = pychrome.Browser(url="http://127.0.0.1:9222")

    # Créer un nouvel onglet
    tab = browser.new_tab(url)

    # Attendre que la page soit chargée
    tab.start()

    # Exécuter un script JavaScript pour vérifier le certificat SSL/TLS
    result = tab.Runtime.evaluate(expression='location.protocol', returnByValue=True)
    protocol = result['result']['value']

    if protocol == 'https:':
        print(f"Le certificat SSL/TLS pour {url} est valide.")
    else:
        print(f"Le certificat SSL/TLS pour {url} n'est pas valide.")

    # Fermer l'onglet
    tab.stop()

# Vérifier les certificats SSL/TLS
check_ssl_certificates()
