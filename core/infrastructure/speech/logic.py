import logging
import sys
import threading
import speech_recognition as SR
import pyttsx3 as TTS
from neuralintents import GenericAssistant
from dataclasses import dataclass
from djitellopy import Tello
from abc import ABC, abstractmethod
from typing import Optional

from core.infrastructure.modules.methods import log

drone = Tello()

commands = {
    "intents": [
        {
            "tag": "actions",
            "patterns": [
                'takeoff',
            ],
            'responses': [
                drone.takeoff()
            ]
        },
        {
            "tag": "actions",
            "patterns": [
                'land',
            ],
            'responses': [
                drone.land()
            ]
        }
    ]
}


class Executor(ABC):

    @abstractmethod
    def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> None:
        ...


@dataclass
class VoiceAssistant:

    def __post_init__(self):
        self.recognizer = SR.Recognizer()
        self.speaker = TTS.init()
        self.speaker.setProperty('rate', 150)
        self.assistant = GenericAssistant(commands, intent_methods={'file': self.create_file})
        threading.Thread(target=self.run_assistant).start()

    @staticmethod
    def create_file() -> None:
        with open('file.txt', 'w') as file:
            file.write('')

    def run_assistant(self) -> None:
        while True:
            try:
                with SR.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=.2)
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    if 'takeoff' in text:
                        drone.takeoff()
                        if text == 'stop':
                            drone.land()
                            self.speaker.stop()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
            except Exception as e:
                log(e, logging.ERROR)
                continue


@dataclass
class Actions(VoiceAssistant):

    takeoff: str
    land: str

    def takeoff(self) -> str:
        return self.takeoff

    def land(self) -> str:
        return self.land


@dataclass
class Drone(Executor):

    actions: Actions(**commands)

    def execute(self) -> None:
        if 'takeoff' in self.actions:
            self.actions.takeoff()



if __name__ == '__main__':
    VoiceAssistant()
