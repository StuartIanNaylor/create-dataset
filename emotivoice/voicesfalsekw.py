TTS_Text = open('falsekw.txt', 'r')
TTS = open('tts-text.txt', 'w')
Count = 0
EmotCount = 0
while True:
  Males = open('Voices-Male.csv', 'r')
  Females = open('Voices-Female.csv', 'r')
  Emot=['|Fear|','|Happy|','|Sad|','|Angry|']
  while True:
    TextLine = TTS_Text.readline()
    if not TextLine:
      print(Count)
      TTS.close()
      quit()
    MaleVoice = Males.readline()
    FemaleVoice = Females.readline()
    if not MaleVoice:
      break
    if not FemaleVoice:
      break
    Count += 1
    EmotCount += 1
    if EmotCount > 3:
      EmotCount = 0     
    Line = MaleVoice.split(",")[0] + Emot[EmotCount] + TextLine.strip() + '|Hey Jarvis\n'
    print(Line)
    TTS.write(Line)
    Line = FemaleVoice.split(",")[0] + Emot[EmotCount] + TextLine.strip() + '|Hey Jarvis\n'
    print(Line)
    TTS.write(Line)
