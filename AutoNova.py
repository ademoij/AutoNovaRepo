from ia_web import IAWeb
from ia_analyse import IAAnalyse

# Initialisation des modules IA
nova.web = IAWeb()
nova.analyse = IAAnalyse(language_module=None)  # Remplace None par ton GPT local si disponible

# Liste des sites à analyser
sites = [
    "https://raw.githubusercontent.com/ademoij/AutoNovaRepo/main/new_features.py",
    "https://example.com"
]

# Boucle d’auto-apprentissage
def auto_learning_loop(nova, sites):
    import time
    while True:
        for url in sites:
            html = nova.web.fetch_page(url)
            if html:
                text = nova.web.extract_text(html)
                new_code = nova.analyse.learn_from_text(text)
                nova.modify_self(new_code)
        time.sleep(3600)  # toutes les heures

# Lancer la boucle
auto_learning_loop(nova, sites)
