from mycroft import MycroftSkill, intent_file_handler
import requests

class Screenremote(MycroftSkill):
    def __init__(self):
        super().__init__("Screenremote")

    @intent_handler(IntentBuilder("").require("Direction").optionally("Query"
        ).build())
    def handle_direction_remote(self, message):
        
        self.speak_dialog('Confirm')

    @intent_handler(IntentBuilder("").require("Key").optionally("Query"
        ).build())
    def handle_key_remote(self, message):
        
        self.speak_dialog('Confirm')

def create_skill():
    return Screenremote()

