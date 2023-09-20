from google.cloud import translate_v2 as translate

credentials_path = 'path/to/your/credentials.json'
translate_client = translate.Client.from_service_account_json(credentials_path)

def translate_english_to_hindi(text):
    target_language = 'hi'
    translation = translate_client.translate(text, target_language=target_language)

    return translation['input'], translation['translatedText']

if __name__ == '__main__':
    input_text = input('Enter English text to translate to Hindi: ')
    input_text, hindi_translation = translate_english_to_hindi(input_text)
    print(f'Input: {input_text}')
    print(f'Translation: {hindi_translation}')
