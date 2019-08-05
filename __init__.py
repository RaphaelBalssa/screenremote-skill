import json

from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.messagebus.message import Message
from mycroft.util.format import nice_time
from mycroft.util.log import LOG
from mycroft.util.parse import extract_datetime
from mycroft.util.format import nice_number
from adapt.intent import IntentBuilder
import mycroft.audio

import requests

localhost = "http://localhost/testSkill.php"

class Screenremote(MycroftSkill):
    def __init__(self):
        super().__init__("Screenremote")

    @intent_handler(IntentBuilder("").require("Direction").optionally("Query"
        ).build())
    def handle_direction_remote(self, message):
        try:
            key_entry = message.data['Direction']
            r = requests.post(localhost, data = key_entry)
            self.speak_dialog('Confirm')

    @intent_handler(IntentBuilder("").require("Key").optionally("Query"
        ).build())
    def handle_key_remote(self, message):
        try:
            data = {"user": user, "key_entry": message.data['Key']}
            r = requests.post(localhost, data = key_entry)
        self.speak_dialog('Confirm')

    @intent_handler(IntentBuilder("").require("MenuQuery").optionally("TVButton"
        ).build())
    def handle_TV_menu(self, message):
    
    @intent_handler(IntentBuilder("").require("MenuQuery").optionally("RadioButton"
        ).build())
    def handle_radio_menu(self, message):

    @intent_handler(IntentBuilder("").require("MenuQuery").optionally("GameButton"
        ).build())
    def handle_game_menu(self, message):

    @intent_handler(IntentBuilder("").require("MenuQuery").optionally("Button"
        ).build())
    def handle_main_menu(self, message):

def create_skill():
    return Screenremote()

