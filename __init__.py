from mycroft import MycroftSkill
from .alexa_pattern import AlexaLedPattern
from pixels import pixels


class RespeakerFourHat(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.pixels = pixels
        self.pixels.pattern = AlexaLedPattern(show=pixels.show)

    def initialize(self):
        self.add_event('recognizer_loop:wakeword', self.handle_wakeword)
        self.add_event('recognizer_loop:record_begin', self.handle_record_begin)
        self.add_event('speak', self.handle_speak)

    def handle_wakeword(self, message):
        self.pixels.wakeup()

    def handle_record_begin(self, message):
        self.pixels.listen()

    def handle_speak(self, message):
        self.pixels.speak()


def create_skill():
    return RespeakerFourHat()

