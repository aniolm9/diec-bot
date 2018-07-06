import link
from markdownify import markdownify as md
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

# Searches for javascript:getAccepcio and substracts 1.
def get_meanings(url):
    web = link.open_web(url)
    meanings = web.count("javascript:getAccepcio")
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

def get_defs_urls(id_list):
    defs_urls = []
    for id in id_list:
        definition = "http://mdlc.iec.cat/accepcio.asp?Word=" + id + "&Id=" + id
        defs_urls.append(definition)

    return defs_urls

def get_definition(defi_url):
    definition_title = []

    # Open the web and convert the HTML to MakDown.
    web = link.open_web(defi_url).encode("latin-1").decode("utf-8") # Something weird happens with the encoding.
    content = md(web, strip=["a"])

    # Get the word
    pos = content.find('"UTF-8"?') + 8
    content = content[pos:]
    content_list = content.split("\n")
    title = content_list[0]

    # There's too much space between the word and the definition. I delete one \n.
    del content_list[2]
    definition = "\n".join(content_list)

    # Add the word and the definition to a list.
    definition_title.append(title)
    definition_title.append(definition)

    return definition_title

def generate_results(meanings, defs_urls):
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
                input_message_content=InputTextMessageContent(output[1], parse_mode=ParseMode.MARKDOWN)))
            cont += cont

    return results