import link
from markdownify import markdownify as md
from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

# Searches for javascript:getAccepcio and substracts 1.
def get_meanings(url):
    web = link.open_web(url)
    meanings = web.count('onclick="GetDefinition(')
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
        definition = "https://dlc.iec.cat/Results/PrintAccepcio?id=" + id
        defs_urls.append(definition)

    return defs_urls

def get_definition(defi_url):
    definition_title = []

    # Open the web and convert the HTML to MakDown.
    web = link.open_web(defi_url).encode("latin-1").decode("utf-8") # Something weird happens with the encoding.
    content = md(web, strip=["a"])

    # Cut the start and end of the definition
    content = content[content.find("LOGO_IEC.png")+19:content.rfind("Institut d'Estudis Catalans")]

    # There's too much space between the word and the definition. I delete one \n.
    content_list = content.split('\n')
    del content_list[2]
    definition = "\n".join(content_list)

    return definition

def generate_results(meanings, defs_urls):
    results = []
    if meanings <= 0:
        results.append(InlineQueryResultArticle(
            id=0,
            title="DIEC",
            description="Enllaç a la web del DIEC.",
            thumb_url="https://imatges.vilaweb.cat/catalunyanord/wp-content/uploads/2015/09/logo-iec-300x270.jpg",
            input_message_content=InputTextMessageContent('<a href="https://dlc.iec.cat">Accedeix al DIEC</a>', parse_mode='HTML')))
    else:
        cont = 1
        for defi_url in defs_urls:
            output = get_definition(defi_url)
            inici_def = output.find("----")
            results.append(InlineQueryResultArticle(
                id=cont,
                title=output[:inici_def],
                description=output[inici_def+8:],
                thumb_url="https://imatges.vilaweb.cat/catalunyanord/wp-content/uploads/2015/09/logo-iec-300x270.jpg",
                input_message_content=InputTextMessageContent(output, parse_mode=ParseMode.MARKDOWN)))
            cont += cont

    return results
