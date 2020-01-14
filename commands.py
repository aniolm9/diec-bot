import paraules
import link
from time import sleep

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Gràcies per iniciar-me! Si no saps com funciono pots utilitzar l'ordre /ajuda")

def ajuda(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Només cal que escriguis @diec_bot en qualsevol xat seguit de la paraula que vols cercar.")

def inlinequery(update, context):
    # Handle the inline query.
    query = update.inline_query.query

    if (query == ""):
        sleep(0.7)
    elif (query.isalpha()):
        url = link.generate_url(query)
        meanings = paraules.get_meanings(url)
        id_list = paraules.get_ids(url, meanings)
        defs_urls = paraules.get_defs_urls(id_list)
        results = paraules.generate_results(meanings, defs_urls)

    try:
        update.inline_query.answer(results)
    except:
        pass
