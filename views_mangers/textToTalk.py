import pyttsx3
import threading




class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

        self.text = ''
        self.wordsList = []
        self.lock = threading.Lock()


    def speechText(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        with self.lock:
            self.wordsList.append(text)

    def speechFullText(self):
        thread = threading.Thread(target=self._speechFullTextThread)
        thread.start()

    def _speechFullTextThread(self):
        full_word = " "
        with self.lock:
            word_list = self.wordsList.copy()
        for word in word_list:
            full_word += word + " "
        self.engine.say(full_word)
        self.engine.runAndWait()

    def clearList(self):
        with self.lock:
            self.wordsList = []


# # Example usage
# text1 = "Hello, how are you?"
# text2 = "I hope you're doing well."
#
#
# textToSpeech = TextToSpeech()
#
# textToSpeech.speechText(text1)
# textToSpeech.speechText(text2)
#
# textToSpeech.speechFullText()
#
# textToSpeech.clearList()
#
# print("List cleared")
#
# textToSpeech.speechFullText()