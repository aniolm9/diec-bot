# diec-bot
Bot de Telegram que permet fer consultes inline al DIEC.

# Instal·lació

## Paquets
```
sudo apt install python3 python3-pip python3-setuptools python3-venv build-essential libgnutls-openssl27 libgnutls30 libcurl3-gnutls
```

## Entorn virtual
````
BOT="" # Directori del bot.
python3 -m venv $BOT
source $BOT/bin/activate
pip3 install python-telegram-bot --upgrade
pip3 install markdownify --upgrade
````

## Clonar repositori
```
cd $BOT && git clone https://github.com/xaldiks/diec-bot.git
```

## Canviar Token
Cal crear un fitxer __TOKEN__ amb una sola línia que sigui el Token.

## Executar
```
cd diec-bot && python3 main.py
```

**Nota:** Cal activar el mode *inline* al BotFather.
