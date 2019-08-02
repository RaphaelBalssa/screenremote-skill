from mycroft import MycroftSkill, intent_file_handler


class Screenremote(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('screenremote.intent')
    def handle_screenremote(self, message):
        self.speak_dialog('screenremote')


def create_skill():
    return Screenremote()

