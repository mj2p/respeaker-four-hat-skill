from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler


class RespeakerFourHat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hat.four.respeaker.intent')
    def handle_hat_four_respeaker(self, message):
        self.speak_dialog('hat.four.respeaker')


def create_skill():
    return RespeakerFourHat()

