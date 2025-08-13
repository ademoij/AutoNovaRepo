import requests
from bs4 import BeautifulSoup

class IAWeb:
    def fetch_page(self, url):
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                return r.text
            return None
        except:
            return None

    def extract_text(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()
