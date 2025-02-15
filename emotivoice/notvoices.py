TTS = open('tts-text.txt', 'w')
Count = 0
EmotCount = 0
cycles = [0]
Emot=['|高兴|','|兴奋|','|悲伤|','|生气|']
Males = open('Voices-Male.csv', 'r')
Females = open('Voices-Female.csv', 'r')
for cycle in cycles:
  TTS_Text = open('notkw.txt', 'r')
  while True:
    TextLine = TTS_Text.readline()
    if not TextLine:
      print(Count)
      break
    MaleVoice = Males.readline()
    FemaleVoice = Females.readline()
    if not MaleVoice:
        Males = open('Voices-Male.csv', 'r')
        Females = open('Voices-Female.csv', 'r')
        MaleVoice = Males.readline()
        FemaleVoice = Females.readline()
    if not FemaleVoice:
        Males = open('Voices-Male.csv', 'r')
        Females = open('Voices-Female.csv', 'r')
        MaleVoice = Males.readline()
        FemaleVoice = Females.readline()
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
