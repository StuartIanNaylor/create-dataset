from TTS.api import TTS
import sqlite3

con = sqlite3.connect("words.db")
cur = con.cursor()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
speak_ord = [0,15,31,1,16,32,2,47,17,3,48,18,4,49,19,5,50,20,6,51,21,7,52,22,8,53,23,9,54,24,10,55,25,11,56,26,12,27,13,28,14,15,33,16,34,17,35,18,36,19,37,20,38,21,39,22,40,23,41,24,42,25,43,26,44,27,45,28,46,29,30]

languages = tts.languages
speakers = tts.speakers
num_lang = len(languages)
num_speak = len(speakers)
lang_count = 0
speak_count = 0
speaker = speakers[speak_ord[speak_count]]
lang = languages[lang_count]


for row in cur.execute("SELECT Word from SOUNDEX"):
    print(row[0], lang, speaker)
    # generate speech by cloning a voice using default settings
    if speak_count < num_speak:
        speaker = speakers[speak_ord[speak_count]]
        speak_count = speak_count + 1
    else:
        speak_count = 0
        speaker = speakers[speak_ord[speak_count]]
    if lang_count < num_lang:
        lang = languages[lang_count]
        lang_count = lang_count + 1
    else:
        lang_count = 0
        lang = languages[lang_count]
       
    if lang != "hi" and lang != "ko":
        tts.tts_to_file(text=row[0],
                                file_path="notkw/" + row[0] + ".wav",
                                speaker=speaker,
                                language=lang,
                                split_sentences=False
                                )                           
