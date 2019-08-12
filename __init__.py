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

    # Définition de l'intent directionnel, concrètement
    # permettre au curseur de monter quand on dit "monte"
    # @intent_handler(IntentBuilder("keyRemoteIntent").optionally("Query").require('Go').require("Direction"))
    @intent_file_handler('direction.press.intent')
    def handle_key_remote_intent(self, message):
       try:
            key_input = message.data['up']
            key_input = "KEY_"+key_input.upper()
            response_code = self.sendRequest("remote", key_input)
            
            self.speak_dialog('Confirm')

       except Exception as e:
            self.speak_dialog('connection.error')
            
    # @intent_file_handler('direction.press.intent')
    # def handle_direction_press_f(self, message):
    #     self.handle_direction_press(message)   

    # # Handle: direction pressed
    # def handle_direction_press(self, message):

    #     try:
    #         r = requests.post(domainServer, data = 'my_key_input')
    #         self.speak_dialog('Confirm')

    #     except Exception as e:
    #         self.speak_dialog('connection.error')    


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

    # @intent_file_handler('button.press.intent')
    # def handle_button_press_f(self, message):
    #     self.handle_button_press(message)   

    # # Handle: button pressed
    # def handle_button_press(self, message):

    #     try:
    #         r = requests.post(domainServer, data = 'my_key_input')
    #         self.speak_dialog('Confirm')

    #     except Exception as e:
    #         self.speak_dialog('connection.error') 

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

