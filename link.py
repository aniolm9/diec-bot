import urllib.parse
import urllib.request
import tls

def generate_url(word):
    word = urllib.parse.quote_plus(word.lower(), encoding="Windows-1252")
    url = "https://dlc.iec.cat/results.asp?txtEntrada=" + word + "&operEntrada=0"

    return url

def open_web(url):
    tls.fix_tls()  # Fix the cert error for DIEC website.

    u = urllib.request.urlopen(url)
    web = u.read().decode("Latin1")
    u.close()

    return web