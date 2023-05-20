import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    # Split the text into chunks (adjust the chunk size as needed)
    chunk_size = 100
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    for chunk in chunks:
        engine.say(chunk)
        engine.iterate()

    engine.runAndWait()


# Example usage
text1 = "Hello, how are you?"
text2 = "I hope you're doing well."

text_to_speech(text1)
text_to_speech(text2)