Males = open('Voices-Male.csv', 'r')
Females = open('Voices-Female.csv', 'r')
TTS = open('tts-text.txt', 'w')
Emot=['|高兴|','|兴奋|','|悲伤|','|生气|']
Count = 0
cycles = [0, 1]
for cycle in cycles:
  Words1 = open('falseword1.txt', 'r')
  for Word1 in Words1:
    Words2 = open('falseword2.txt', 'r')
    for Word2 in Words2:
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
      
      Count += 12          
      print(MaleVoice.split(",")[0] + Emot[0] + '<sos/eos> ' + Word1.rstrip('\n') + 'sp1' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      print(FemaleVoice.split(",")[0] + Emot[0] + '<sos/eos> ' + Word1.rstrip('\n') + 'sp1' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(MaleVoice.split(",")[0] + Emot[0] + '<sos/eos> ' + Word1.rstrip('\n') + 'sp1' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(FemaleVoice.split(",")[0] + Emot[0] + '<sos/eos> ' + Word1.rstrip('\n') + 'sp1' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(MaleVoice.split(",")[0] + Emot[1] + '<sos/eos> ' + Word1.rstrip('\n') + 'sp2' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(FemaleVoice.split(",")[0] + Emot[1] + '<sos/eos> ' + Word1.rstrip('\n') + 'sp2' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')    
      TTS.write(MaleVoice.split(",")[0] + Emot[2] + '<sos/eos> ' + Word1.rstrip('\n') + 'engsp1' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(FemaleVoice.split(",")[0] + Emot[2] + '<sos/eos> ' + Word1.rstrip('\n') + 'engsp1' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')  
      TTS.write(MaleVoice.split(",")[0] + Emot[3] + '<sos/eos> ' + Word1.rstrip('\n') + 'engsp4' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(FemaleVoice.split(",")[0] + Emot[3] + '<sos/eos> ' + Word1.rstrip('\n') + 'engsp4' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(MaleVoice.split(",")[0] + Emot[0] + '<sos/eos> ' + Word1.rstrip('\n') + 'cn_eng_sp' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(FemaleVoice.split(",")[0] + Emot[0] + '<sos/eos> ' + Word1.rstrip('\n') + 'cn_eng_sp' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(MaleVoice.split(",")[0] + Emot[1] + '<sos/eos> ' + Word1.rstrip('\n') + '?' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
      TTS.write(FemaleVoice.split(",")[0] + Emot[1] + '<sos/eos> ' + Word1.rstrip('\n') + '?' + Word2.rstrip('\n') + '<sos/eos>|Hey Jarvis\n')
print(Count)

