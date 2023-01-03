#imports
from openAiReponse import textAnalysis
import whisper
import os
import moviepy.editor as mp
from pydub import AudioSegment, silence

#wants just a SHORT summary of content of lecture...

model = whisper.load_model("base")
model.cuda()

# myaudio = intro = AudioSegment.from_mp3("sample2.mp4-audioExact.mp3")
# dBFS=myaudio.dBFS
# silence = silence.detect_silence(myaudio, min_silence_len=1000, silence_thresh=dBFS-16)

# silence = [((start/1000),(stop/1000)) for start,stop in silence] #in sec
# print(silence)

#converts the speech to audio
#may need to process audio in the future for better recongitions


class SpeechConverterAudio(textAnalysis):
  def __init__(self, filename):
    self.filename = filename
    self.text = ""
    self.textList = []
    self.path = ""
    self.audioFile = ""
    self.audio = None
    self.videoclip = None

  def process(self):
    self.audioFile = str(self.filename) + "-audioExact.mp3"
    self.path = "E:\Projects\CURRENT_PROJECTS\LectureSpeeder\{}".format(self.audioFile)
    if not os.path.exists(self.path):
      os.makedirs(self.path)
      #intervals of 15
    self.videoclip = mp.VideoFileClip(self.filename)
    self.audio = self.videoclip.audio.write_audiofile(self.audioFile)
    print('processed')

  def detectSilence(self):
    myAudio = AudioSegment.from_mp3(self.audioFile)
    silence = silence.detect_silence(myAudio, min_silence_len=1000, silence_thresh=-16)
    silence = [((start/1000),(stop/1000)) for start,stop in silence] #convert to sec
    print(silence)

  def convertAudioText(self):
    self.text = model.transcribe(self.audioFile, fp16=False, language='English')['text']


sr = SpeechConverterAudio('sample3.mp4')
sr.process()
sr.convertAudioText()

#TMR Goal



