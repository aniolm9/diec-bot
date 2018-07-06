import urllib.parse
import urllib.request

def generate_url(word):
    word = urllib.parse.quote_plus(word.lower(), encoding="Windows-1252")
    url = "http://mdlc.iec.cat/results.asp?txtEntrada=" + word + "&operEntrada=0"

    return url

def open_web(url):
    u = urllib.request.urlopen(url)
    web = u.read().decode("latin-1")
    u.close()

    return web