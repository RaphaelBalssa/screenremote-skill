import json

from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.messagebus.message import Message
from mycroft.util.format import nice_time
from mycroft.util.log import LOG
from mycroft.util.parse import extract_datetime
from mycroft.util.format import nice_number
from adapt.intent import IntentBuilder
from mycroft.util.log import getLogger
import mycroft.audio
import random

import requests

# cette ligne permet d'obtenir les log du Skill
LOGGER = getLogger(__name__)

# j'ai noté ici l'adresse à laquelle on fait la requête
# mais c'était seulement pour le phase de test, le nom de domaine doit 
# être paramétré dans un fichier JSON

class Screenremote(MycroftSkill):

    # initialisation du Skill, concrètement on ne fait qu'initialiser son
    # nom ici
    def __init__(self):
        super().__init__("Screenremote")

    def init_dict(self, lang):
        if(lang == "fr"):
            fr_dict = {"haut": "up", "bas": "bas",
            "gauche": "left", "droite": "right",
            "redémarre": "reboot", "menu": "menu"}
            return fr_dict
        else:
             return None


    @intent_file_handler('test.intent')
    def handle_test_intent(self, message):
        self.speak_dialog('Confirm')


    # Définition de l'intent directionnel, concrètement
    # permettre au curseur de monter quand on dit "monte" ou autre
    #@intent_handler(IntentBuilder("keyRemoteIntent").optionally("Query").require('Go').require("Direction"))
    @intent_file_handler('direction.press.intent')
    def handle_direction_intent(self, message):
       try:
            key_input = message.data['direction']
            language = str(self.settings.get("language"))
            
            if(language != 'en'):
                key_input= self.__translate(key_input, language)
            key_input = "KEY_"+key_input.upper()
            response_code = self.sendRequest("remote", key_input)
            
            self.speak_dialog('Confirm')

       except Exception as e:
            self.speak_dialog('connection.error')

    @intent_file_handler('volume.up.intent')
    def handle_volume_up_intent(self, message):
        try:
            response_code = self.sendRequest("order", "VOLUMEUP")
            self.speak_dialog('Confirm')
        
        except Exception as e:
            self.speak_dialog('connection.error')


    @intent_file_handler('volume.down.intent')
    def handle_volume_down_intent(self, message):
        try:
            response_code = self.sendRequest("order", "VOLUMEDOWN")
            self.speak_dialog('Confirm')
        
        except Exception as e:
            self.speak_dialog('connection.error')


    # @intent_file_handler('direction.press.intent')
    # def handle_direction_press_f(self, message):
    #     self.handle_direction_press(message)   

    # # Handle: direction pressed
    # def handle_direction_press(self, message):


    # Définition de l'intent des boutons, concrètement
    # appuie sur le bouton vert ou encore le bouton 1 
    # si on lui dit de le faire
    # @intent_handler(IntentBuilder("orderRemoteIntent").optionally("Query").require('Press').require("Order"))
    @intent_file_handler('button.press.intent')
    def handle_order_remote_intent(self, message):
        try:
            key_input = message.data['reboot'].upper()
            response_code = self.sendRequest("order", key_input)
            self.speak_dialog('Confirm')
        
        except Exception as e:
            self.speak_dialog('connection.error')

    def __translate(self, word, lang):
        my_dict = self.init_dict(lang)
        for i in my_dict:
            if(i==word):
                return my_dict[word]
        return None


    def sendRequest(self, typeR, value):
        IPaddress = str(self.settings.get("TerminalIPaddress"))
        port = str(self.settings.get("port"))
        domainName = str(self.settings.get("domainName"))
        myrand=str(random.random())
        URL = "http://"+domainName+"/wget.php?type="+typeR+"&value="+value+"&server="+IPaddress+":"+port+"&nocache="+myrand+"&end"
        r = requests.get(URL)
        return r.status_code

    

def create_skill():
    return Screenremote()

