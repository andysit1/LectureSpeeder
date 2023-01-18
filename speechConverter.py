#imports
from openAiResponse import recursiveCallAi, gpt2ModelSummary
from pdfGenerator import PDF
import whisper
import os
from pydub import AudioSegment, silence

model = whisper.load_model("base.en")
maker = PDF('P', 'mm', 'Letter')

class SpeechConverterAudio():
  def __init__(self, filename):
    self.filename = filename
    self.path = self.filename + "/"
    self.sections = []
    self.start = 0

  def process(self):
    for file in os.listdir(self.filename):
      if file.endswith(".mp3"):
        self.sections.append(model.transcribe(self.path + file, fp16=False, language='English')['text'])

    time = 0
    maker.set_auto_page_break(auto = True, margin = 15)
    maker.add_page()
    for section in self.sections:
      time += 15
      text = recursiveCallAi("Rewrite context with all the information in a textbook format instead of dialog also get rid of sentences that do not make sense\n[" + section + ']')
      text2 = text.encode('latin-1', 'replace').decode('latin-1') #important to stop encoding problems
      maker.print_chapter(str(time), 'Lecture Notes', text2)
    maker.output("output/Lecture-Notes-{}.pdf".format(self.filename))
    print('Made')

  def convertAudioText(self):
    self.text = model.transcribe(self.filename + '/fullVideo.mp3', fp16=False, language='English')['text']

  def detectSilence(self):
    myAudio = AudioSegment.from_mp3(self.audioFile)
    silence = silence.detect_silence(myAudio, min_silence_len=1000, silence_thresh=-16)
    silence = [((start/1000),(stop/1000)) for start,stop in silence] #convert to sec
    print(silence)

