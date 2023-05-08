"""Use Watson APIs to create functions.
Create a function that translates English to French.
Create a function that translates English to German.
Run coding standards check against the functions above.
Write unit tests to test the above functions.
Run unit tests and interpret the results.
Package the above functions and tests as a standard python package."""

# Importing the libraries
from pandas import json_normalize
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 


# Setup service & API access

url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/40324722-7654-4cf0-9f2c-d80386993c61'
apikey_lt='u-T7aWU9qQ-x_Xq2BSuhvNaVUujsQ3V3JYkreIxzJStL'
version_lt='2023-05-01'

# create language translator object

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

# list the languages that can be identified by the service


json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")


# following functions translate english to french and german

def english_to_french(english_text):
    """Translates English to French"""
    translation_response = language_translator.translate(text=english_text,model_id='en-fr')
    translation=translation_response.get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def english_to_german(english_text):
    """Translates English to German"""
    translation_response = language_translator.translate(text=english_text,model_id='en-de')
    translation=translation_response.get_result()
    german_text=translation['translations'][0]['translation']
    return german_text








