''' Python Project for AI & Application Development Final Project '''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def translate_text(original_text="", translation_model=""):
    ''' Translate text using IBM Cloud Language Translator. '''

    if original_text == "" or translation_model == "":
        return ""
    translation = language_translator.translate(
        text=original_text,
        model_id=translation_model).get_result()
    return translation['translations'][0]['translation']

def english_to_french(english_text=""):
    '''Translate English to French using translate_text function.'''

    french_text = translate_text(english_text, 'en-fr')
    return french_text

def french_to_english(french_text=""):
    '''Translate French to English using translate_text function.'''

    english_text = translate_text(french_text, 'fr-en')
    return english_text
