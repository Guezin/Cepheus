from googletrans import Translator

def translate_word(word, dest='pt'):
  translator = Translator()
  translated_word = translator.translate(word, dest=dest)
  return translated_word.text

def translate_word_if_exists(word):
  translated_word = word is not None and translate_word(word) or None 
  return translated_word