english_to_hindi = {
    "hello": "नमस्ते",
    "world": "दुनिया",
    "translate": "अनुवाद करें",

}

def translate_to_hindi(english_text):

    words = english_text.split()
    translated_words = []

    for word in words:
        translated_word = english_to_hindi.get(word.lower(), word)
        translated_words.append(translated_word)

    # Join the translated words to form the translated sentence
    translated_sentence = " ".join(translated_words)

    return translated_sentence


# Input text in English
english_text = "Hello world, translate this!"

# Translate the input text to Hindi
translated_text = translate_to_hindi(english_text)

# Print the translated text
print("English: ", english_text)
print("Hindi: ", translated_text)
