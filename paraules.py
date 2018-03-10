import link
from telegram import InlineQueryResultArticle, InputTextMessageContent


# Searches for javascript:getAccepcio and substracts 1.
def get_meanings(url):
    web = link.open_web(url)
    meanings = web.count("javascript:getAccepcio") - 1

    return meanings

def get_ids(url, meanings):
    web = link.open_web(url)
    pos = 0
    id_list = []

    while (meanings > 0):
        pos_id = web.find('id="0', pos)
        inici_id = pos_id + 4
        fi_id = web.find('"', inici_id)
        id = web[inici_id:fi_id]
        id_list.append(id)
        meanings -= 1
        pos = fi_id

    return id_list

def get_defs_urls(id_list, word):
    defs_urls = []
    for id in id_list:
        definition = "https://dlc.iec.cat/accepcio.asp?Word=" + id + "&Id=" + id
        defs_urls.append(definition)

    return defs_urls

def get_definition(defi_url):
    definition_title = []
    web = link.open_web(defi_url)

    definition_title.append(title)
    definition_title.append(definition)

    return definition_title

def generate_results(word, meanings, defs_urls):
    results = []
    if meanings <= 0:
        results.append(InlineQueryResultArticle(
            id=0,
            title="No s'han trobat resultats.",
            input_message_content=InputTextMessageContent("No s'han trobat resultats.")))
    else:
        cont = 1
        for defi_url in defs_urls:
            output = get_definition(defi_url)
            results.append(InlineQueryResultArticle(
                id=cont,
                title=output[0],
                input_message_content=InputTextMessageContent(output[1])))
            cont += cont

    return results