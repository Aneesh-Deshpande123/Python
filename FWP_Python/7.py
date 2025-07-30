import playsound3 as ps
input1=input("Do you want to hear glassbreak or music(1:glassbreak, 2:music)? ")
if input1=="1":
    ps.playsound("sampleaudio2.wav")
else:
    ps.playsound("sampleaudio1.wav")