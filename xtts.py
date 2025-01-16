from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

languages = tts.languages
speakers = tts.speakers
for speaker in speakers:
    for lang in languages:
    # generate speech by cloning a voice using default settings
        if lang != "hi" and lang != "ko":
            tts.tts_to_file(text="Hey Jarvis",
                            file_path=speaker + "2-" + lang + ".wav",
                            speaker=speaker,
                            language=lang,
                            split_sentences=False
                            )                           
            tts.tts_to_file(text="hey jarvis",
                            file_path=speaker + "3-" + lang + ".wav",
                            speaker=speaker,
                            language=lang,
                            split_sentences=False
                            )  
