Males = open('Voices-Male.csv', 'r')
Females = open('Voices-Female.csv', 'r')
TTS = open('tts-text.txt', 'w')
Emot=['|高兴|','|兴奋|','|悲伤|','|生气|']
Count = 0
while True:
  MaleVoice = Males.readline()
  FemaleVoice = Females.readline()
  if not MaleVoice:
    break
  if not FemaleVoice:
    break
  Count += 1          
  print(MaleVoice.split(",")[0], FemaleVoice.split(",")[0])
  TTS.write(MaleVoice.split(",")[0] + Emot[1] + '<sos/eos> [HH] [EY1] sp0 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[1] + '<sos/eos> [HH] [EY1] sp0 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[0] + '<sos/eos> [HH] [EY1] sp1 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[0] + '<sos/eos> [HH] [EY1] sp1 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[3] + '<sos/eos> [HH] [EY1] sp2 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[3] + '<sos/eos> [HH] [EY1] sp2 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[2] + '<sos/eos> [HH] [EY1] sp3 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[2] + '<sos/eos> [HH] [EY1] sp3 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[1] + '<sos/eos> [HH] [EY1] sp4 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[1] + '<sos/eos> [HH] [EY1] sp4 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[0] + '<sos/eos> [HH] [EY1] engsp1 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[0] + '<sos/eos> [HH] [EY1] engsp1 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[3] + '<sos/eos> [HH] [EY1] engsp2 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[3] + '<sos/eos> [HH] [EY1] engsp2 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[2] + '<sos/eos> [HH] [EY1] engsp4 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[2] + '<sos/eos> [HH] [EY1] engsp4 [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[0] + '<sos/eos> [HH] [EY1] cn_eng_sp [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[0] + '<sos/eos> [HH] [EY1] cn_eng_sp [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[3] + '<sos/eos> [HH] [EY1] eng_cn_sp [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[3] + '<sos/eos> [HH] [EY1] eng_cn_sp [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  TTS.write(MaleVoice.split(",")[0] + Emot[2] + '<sos/eos> [HH] [EY1] ? [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n' + FemaleVoice.split(",")[0] + Emot[2] + '<sos/eos> [HH] [EY1] ? [JH] [AA1] [R] [V] [AH0] [S] <sos/eos>|Hey Jarvis\n')
  break
print(Count)

