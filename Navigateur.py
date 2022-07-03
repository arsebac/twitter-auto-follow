from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import time

from selenium.webdriver.common.by import By


class Navigateur:
    """Crée une fenetre Chrome avec Selenium, pour pouvoir intéragir avec elle grace à du code."""

    def __init__(self):
        pass

    def demarrer(self):
        """demare une instance de Chrome"""
        chrome_options = Options()

        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/97.0.4692.71 Safari/537.36")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=2")
        chrome_options.add_argument('--no-default-browser-check')
        chrome_options.add_argument('--no-first-run')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-default-apps')
        self.browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)
        self.browser.get("https://www.twitter.com/?lang=fr")
        self.browser.maximize_window()

    def connection_twitter(self, compte):
        pseudo = compte.get('pseudo')
        mdp = compte.get('mdp')
        if pseudo is None:
            print("Erreur de configuration du compte: 'pseudo' n'est pas défini dans ", compte.get('fichier'))
            return False
        if mdp is None:
            print("Erreur de configuration du compte: 'mdp' n'est pas défini dans ", compte.get('fichier'))
            return False
        self.browser.get("https://www.twitter.com/login")
        time.sleep(3)
        # On rentre le pseudo et on appuie sur entrée
        self.browser.find_element(By.NAME, "text").send_keys(pseudo + '\n')
        time.sleep(3)
        # On rentre le mdp
        self.browser.find_element(By.NAME, "password").send_keys(mdp + '\n')
        time.sleep(3)

        # on regarde si il faut rentrer le mail ou le numéro de téléphone
        try:
            element = self.browser.find_element(By.NAME, "text")
            element.send_keys(compte.get('telOuEmail', '') + '\n')
        except:
            print("Pas besoin de l'email, on est connecté")

        return True

    def follow(self, compte):
        # Etape 1 : on ouvre la page du compte Twitter a follow
        self.browser.get("https://twitter.com/" + compte)
        time.sleep(3)

        # Etape 2 : on vérifie si le compte existe
        try:
            bouton_follow = self.browser.find_element(By.CSS_SELECTOR, 'div[data-testid="placementTracking"] > div:nth-child(1) > div:nth-child(1)')
        except:
            print("Il y a un probleme pour accéder au compte Twitter '" + compte + "'. Est-ce que le compte existe ?")
            return False

        # Etape 3 : on vérifie si on ne follow pas déja ce compte en vérifiant si le bouton est "Follow" au lieu de "Unfollow"
        attribut_html = bouton_follow.get_attribute("aria-label")
        if attribut_html.startswith("Suivre @") or attribut_html.startswith("Follow @"):
            # C'est un bouton Follow, on clic dessus
            bouton_follow.send_keys(Keys.ENTER)
            time.sleep(2)
            return True

        # On follow déja le compte, on ne fait rien
        return False