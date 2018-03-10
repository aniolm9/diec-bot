import paraules
import link

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Gràcies per iniciar-me! Si no saps com funciono pots utilitzar l'ordre /ajuda")

def ajuda(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Només cal que escriguis @diec_bot en qualsevol xat seguit de la paraula que vols cercar.")


def inlinequery(bot, update):
    # Handle the inline query.
    query = update.inline_query.query

    url = link.generate_url(query)
    meanings = paraules.get_meanings(url)
    id_list = paraules.get_ids(url, meanings)
    defs_urls = paraules.get_defs_urls(id_list, query)

    results = paraules.generate_results(query, meanings, defs_urls)

    #print (results[0])
    update.inline_query.answer(results)
