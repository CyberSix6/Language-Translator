url_lt=' https://api.us-south.language-translator.watson.cloud.ibm.com/instances/0cada5bf-37c8-4d2f-80a0-420f576cd4f8'
apikey_lt='FZgHrvUl8N8VO4BHM4zJ5Tojn_Q93iyYNtI6vEfY5k_K'
version_lt='2023-01-18'

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticatorurl_lt

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)


"""This function translate from english to french
"""
def english_to_french(text):
    translation_response = language_translator.translate(\
    text=text, model_id='en-fr')

    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']

    return french_translation