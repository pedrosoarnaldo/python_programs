
import mp3play

### Needs Windows XP to work
filename = r'C:\cygwin64\home\arnaldo.pedroso\projetos\python_programs\luis-fonsi-despacito-ft-daddy-yankee.mp3'
clip = mp3play.load(filename)
clip.play()
