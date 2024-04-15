import speech_recognition as sr
import os


def ouvir_microfone():
    audio_input = sr.Recognizer()

    with sr.Microphone() as source:
        print("Hello, my name is Gabriel, pleased to help you.")
        print("Say (Google/Spotify): ")
        audio_input.adjust_for_ambient_noise(source)
        audio = audio_input.listen(source)
        try:
            frase = audio_input.recognize_google(audio, language="pt-BR")
            print("You said: " + frase)

            if "Google" in frase:
                os.system("xdg-open https://www.google.com")
                print("Google opened successfully!")
                return True

            if "Spotify" in frase:
                os.system("xdg-open spotify:")
                print("Spotify opened successfully!")
                return True

        except sr.UnknownValueError:
            print("Speech not recognized.")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {}".format(
                    e
                )
            )

    return False


# while not ouvir_microfone():
#    pass
