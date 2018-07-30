from mycroft import MycroftSkill
from .alexa_pattern import AlexaLedPattern


class RespeakerFourHat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.alexa_pattern = AlexaLedPattern()

    def initialize(self):
        self.add_event('recognizer_loop:wakeword', self.handle_wakeword)
        self.add_event('recognizer_loop:record_begin', self.handle_record_begin)
        self.add_event('speak', self.handle_speak)

    def handle_wakeword(self, message):
        self.alexa_pattern.wakeup()

    def handle_record_begin(self, message):
        self.alexa_pattern.listen()

    def handle_speak(self, message):
        self.alexa_pattern.speak()


def create_skill():
    return RespeakerFourHat()

