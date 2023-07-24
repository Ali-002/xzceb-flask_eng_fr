""""translator program """
from deep_translator import MyMemoryTranslator

def EnglishToFrench(english_text):
    """translate from English to French"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def FrenchToEnglish(french_text):
    """translate from French to English"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
