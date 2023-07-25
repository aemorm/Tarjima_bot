from googletrans import Translator


translator = Translator()
async def translate_user_text(text, lang):
    result = translator.translate(text=text, dest=lang)

    return result.text








