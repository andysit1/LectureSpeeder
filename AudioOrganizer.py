import os
from openAiReponse import openAiReponse, recursiveCallAi
from moviepy.editor import VideoFileClip
from pprint import pprint as pp
from pydub import AudioSegment
from speechConverter import SpeechConverterAudio


class AudioOrganizer():
  def __init__(self, filename):
    self.filename = filename
    self.path = filename.strip('.mp4')

  def processFolder(self):
    if not os.path.exists(self.path):
      os.mkdir(self.path)
      self.processAudio()
      self.splitAudio()
      return
    print("audio has been made before")

  def processAudio(self):
    video = VideoFileClip(self.filename)
    audioclip = video.audio
    os.mkdir(self.path + "/fullVideo")
    audioclip.write_audiofile('{}/test.mp3'.format(self.path + "/fullVideo"))

  def splitAudio(self):
    audio = AudioSegment.from_mp3('{}/test.mp3'.format(self.path + "/fullVideo"))
    interval = 15 * 60 * 1000
    for i, chunk in enumerate(audio[::interval]):
      print(i)
      chunk.export('{}/test{}.mp3'.format(self.path, i), format('mp3'))

fr = AudioOrganizer('sample2.mp4')
fr.processFolder()
sr = SpeechConverterAudio('sample2')
sr.process()

for section in sr.sections:
  print("---------------------------------")
  print('promot: ', section)
  print(openAiReponse("write a summary in your own words with the given context " + section + "!"))
  print("----")
  test = openAiReponse("You are a universtiy professor, return the most important parts and rewrite them in a summary given " + section)
  print(test)
  recursiveCallAi("You are a universtiy professor, return the most important parts and rewrite them in a summary given " + section)
