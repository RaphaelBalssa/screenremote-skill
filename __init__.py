import json

from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.messagebus.message import Message
from mycroft.util.format import nice_time
from mycroft.util.log import LOG
from mycroft.util.parse import extract_datetime
from mycroft.util.format import nice_number
from adapt.intent import IntentBuilder
from mycroft.util.log import LOG
import mycroft.audio

import requests

# cette ligne permet d'obtenir les log du Skill
LOGGER = getLogger(__name__)

# j'ai noté ici l'adresse à laquelle on fait la requête
# mais c'était seulement pour le phase de test, le nom de domaine doit 
# être paramétré dans un fichier JSON
# domainServer = "http://www.mytestskill.com"

class Screenremote(MycroftSkill):

    # initialisation du Skill, concrètement on ne fait qu'initialiser son
    # nom ici
    def __init__(self):
        super().__init__("Screenremote")

    # Définition de l'intent directionnel, concrètement
    # permettre au curseur de monter quand on dit "monte"
    @intent_handler(IntentBuilder("DirectionRemoteIntent").require('Go').require("Direction").optionally("Query"
        ).build())
    def handle_direction_remote_intent(self, message):
        try:
            #key_input = message.data['Direction']
            #r = requests.post(domainServer, data = key_input)
            self.speak_dialog('Confirm')

        except Exception as e:
            self.speak_dialog('connection.error')
            
    # Définition de l'intent des boutons, concrètement
    # appuie sur le bouton vert ou encore le bouton 1 
    # si on lui dit de le faire
    @intent_handler(IntentBuilder("KeyRemoteIntent").require('Press').require("Key"
        ).optionally("Query").build())
    def handle_key_remote_intent(self, message):
        try:
            #data = {"user": user, "key_input": message.data['Key']}
            #r = requests.post(domainServer, data = key_input)
            self.speak_dialog('Confirm')
        
        except Exception as e:
            self.speak_dialog('connection.error')

    # @intent_handler(IntentBuilder("").require("MenuQuery").require("TVButton"
    #     ).build())
    # def handle_TV_menu(self, message):
    #     try:
    #         data = { "key_input": message.data['']}
    #         self.speak_dialog('Confirm')

    #     except Exception as e:
    #         self.speak_dialog('connection.error')


    # @intent_handler(IntentBuilder("").require("MenuQuery").require("RadioButton"
    #     ).build())
    # def handle_radio_menu(self, message):
    #     try:
    #         data = {key_input: message.data['MenuQuery']}
            
    #         self.speak_dialog('Confirm')

    # @intent_handler(IntentBuilder("").require("MenuQuery").require("GameButton"
    #     ).build())
    # def handle_game_menu(self, message):
    #     try:
            
    #         self.speak_dialog('Confirm')

    # @intent_handler(IntentBuilder("").require("MenuQuery").require("Button"
    #     ).build())
    # def handle_main_menu(self, message):
    #     try:
    #         self.speak_dialog('Confirm')

    # méthode permettant d'appuyer sur le bouton OK
    #def handle_press_input(self, message):
    #    try:
    #        data = {"data": message.data['Press']}
    #        requests.post(domainServer, data = data)


   # def sendRequest(url):
   #    return False

def create_skill():
    return Screenremote()

