from TTS.api import TTS
import sqlite3

con = sqlite3.connect("words.db")
cur = con.cursor()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
languages = tts.languages
print(languages)
speakers = tts.speakers
num_lang = len(languages)
num_speak = len(speakers)
lang_count = 0
speak_count = 0
speaker = speakers[speak_count]
lang = languages[lang_count]
speak_ord = [0,15,31,1,16,32,2,47,17,3,48,18,4,49,19,5,50,20,6,51,21,7,52,22,8,53,23,9,54,24,10,55,25,11,56,26,12,27,13,28,14,15,33,16,34,17,35,18,36,19,37,20,38,21,39,22,40,23,41,24,42,25,43,26,44,27,45,28,46,29,30]
for speak_count in range(0, num_speak -1):
    print(speakers[speak_count], speak_count)
    tts.tts_to_file("Hello",
            file_path=str(speak_count) + speakers[speak_count] + ".wav",
            speaker=speakers[speak_count],
            language=lang,
            split_sentences=False
            )         
