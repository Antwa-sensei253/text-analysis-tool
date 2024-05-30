from googletrans import Translator

def translate_to_arabic(text):
    """
    Translate text to Arabic using Google Translate API.

    Args:
        text: The text to translate.

    Returns:
        The translated text in Arabic.
    """
    translator = Translator()
    translated = translator.translate(text, dest='ar')
    return translated.text

if __name__ == "__main__":
    text_to_translate = input("Enter the text to translate to Arabic: ")

    translated_text = translate_to_arabic(text_to_translate)

    print("Translated text (Arabic):", translated_text)
