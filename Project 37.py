import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language = 'en'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')

    if language == 'en':
        engine.setProperty('voice', voices[0].id)
    else:
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text(language = 'en'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now...")
        audio = recognizer.listen(source)

    try:
        print(" 🔍 Recognizing speech...")
        text = recognizer.recognize_google(audio, language = language)
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")

    return ""

def translate_text(text, source_language = 'en', target_language = 'de'):
    translator = Translator()
    translation = translator.translate(text, src = source_language, dest = target_language)
    print(f"🌐 Translated text: {translation.text}")
    return translation.text

def display_language_options():
    print("\n🌐 Available translation languages: ")
    print("1. English (en)")
    print("2. French (fr)")
    print("3. Spanish (es)")
    print("4. German (de)")
    print("5. Italian (it)")
    print("6. Portuguese (pt)")
    print("7. Tamil (ta)")
    print("8. Telugu (te)")
    print("9. Hindi (hi)")

    language_dict = {
        "1": "en",
        "2": "fr",
        "3": "es",
        "4": "de",
        "5": "it",
        "6": "pt",
        "7": "ta",
        "8": "te",
        "9": "hi"
    }

    speak("\nPlease select your source speaking language number (1-9): ")
    source_choice = input("\nPlease select your source speaking language number (1-9): ")
    source_language = language_dict.get(source_choice.strip(), "en")

    speak("\nPlease select your target translation language number (1-9): ")
    target_choice = input("\nPlease select your target translation language number (1-9): ")
    target_language = language_dict.get(target_choice.strip(), "de")

    return source_language, target_language

def continue_or_exit():
    choice = input("\n Do you want to continue inputing and translating text? (y/n): ")

    if choice == "y" or choice == "Y" or choice == "yes" or choice == "Yes":
        main()
    else:
        print("❌ Exiting the program. Goodbye!")
        speak("Exiting the program. Goodbye!")

def starting_screen():
    print("="*50)
    print(" 🌐 Welcome to the Speech-to-Text Translator!")
    speak("Welcome to the Speech-to-Text Translator!")
    print(" This program allows for various language inputs and English or other languages output.")
    speak(" This program allows for various language inputs and English or other languages output.")
    print(" 🥂 Break a leg!")
    speak("Break a leg!")
    print("="*50)

def main():
    starting_screen()
    source_language, target_language = display_language_options()
    
    print(f"\n[Config] Source: {source_language} ➔  Target: {target_language}\n")
    
    original_text = speech_to_text(language = source_language)

    if original_text:
        translated_text = translate_text(original_text, source_language, target_language)
        speak(translated_text, language = target_language)

        speak("Translation spoken out!")
        print("✅ Translation spoken out!")

    continue_or_exit()

if __name__ == "__main__":
    main()