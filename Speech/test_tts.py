from Speech.text_to_speech import TextToSpeech

tts = TextToSpeech()

print("\nAvailable Voices\n")

voices = tts.list_voices()

for voice in voices:

    print(

        voice["index"],

        voice["name"]

    )

tts.set_rate(170)

tts.set_volume(1)

tts.speak(

    "Hello Krishna. Welcome to your AI Interview."

)