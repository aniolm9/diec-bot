# diec-bot
Bot de Telegram que permet fer consultes inline al DIEC.

# Instal·lació

## Paquets
```
$ sudo apt install python3 python3-pip python3-setuptools build-essential python3-venv
```

## Entorn virtual
````
$ BOT="" # Directori del bot.
$ python3 -m venv $BOT
$ source $BOT/bin/activate
$ pip3 install python-telegram-bot
````

## Clonar repositori
```
$ cd $BOT && git clone https://github.com/xaldiks/diec-bot.git
```

## Canviar Token
El token es troba al fitxer **main.py**.

## Executar
```
$ cd diec-bot && python3 main.py
```