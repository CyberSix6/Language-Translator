"""Use Watson APIs to create functions.
Create a function that translates English to French.
Create a function that translates English to German.
Run coding standards check against the functions above.
Write unit tests to test the above functions.
Run unit tests and interpret the results.
Package the above functions and tests as a standard python package."""

# Importing the libraries
import json_normalize from pandas
import Language Translator V3 from ibm_watson 


# Setup service & API access

url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/40324722-7654-4cf0-9f2c-d80386993c61'
apikey_lt='u-T7aWU9qQ-x_Xq2BSuhvNaVUujsQ3V3JYkreIxzJStL' # Enter the apikey
version_lt='2023-05-01'

# create language translator object


from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('apikey_lt')
language_translator = Language Translator V3(
    version='version_lt',
    authenticator=authenticator
)

language_translator.set_service_url('url_lt')

language_translator.set_disable_ssl_verification(False)

json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")


# following functions translate english to french and german

def english_to_french(english_text):
    """Translates English to French"""
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    translation_response = language_translator.translate(text=english_text,model_id='en-fr')
    translation=translation_response.get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def english_to_german(english_text):
    """Translates English to German"""
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    translation_response = language_translator.translate(text=english_text,model_id='en-de')
    translation=translation_response.get_result()
    german_text=translation['translations'][0]['translation']
    return german_text








