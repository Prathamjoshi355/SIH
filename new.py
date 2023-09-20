from googletrans import Translator

def translate_english_to_hindi(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

if __name__ == "__main__":
    input_text = input("Enter text in English: ")
    translated_text = translate_english_to_hindi(input_text)
    print(f"Translation in Hindi: {translated_text}")
