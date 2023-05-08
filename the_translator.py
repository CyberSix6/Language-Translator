"""This module contains functions for translating text using Watson Language Translator APIs."""
import re
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Setup service & API access
URL_LT = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/40324722-7654-4cf0-9f2c-d80386993c61'
APIKEY_LT ='u-T7aWU9qQ-x_Xq2BSuhvNaVUujsQ3V3JYkreIxzJStL'
VERSION_LT ='2023-05-01'

def remove_whitespace(text):
    """Remove all the whitespaces and newlines from the text using the regex."""
    return re.sub(r'\s+', '', text)



# Create language translator object
authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(URL_LT)


def translate_english_to_french(english_text):
    """Translate English text to French."""
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation = translation_response.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def translate_english_to_german(english_text):
    """Translate English text to German."""
    translation_response = language_translator.translate(text=english_text, model_id='en-de')
    translation = translation_response.get_result()
    german_text = translation['translations'][0]['translation']
    return german_text
