from googletrans import Translator

def translate_word(word, dest='pt'):
  translator = Translator()
  translated_word = translator.translate(word, dest=dest)
  return translated_word.text
