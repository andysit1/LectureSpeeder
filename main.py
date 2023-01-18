#GOAL: I want to send in a lecture mp4
#seperate the audio -> change to words and let openai convert it properly
#response with a pdf analysis of important/piroties
#summarize lecture at the start of pdf
#make questions [maybe]

import sys
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from AudioOrganizer import AudioOrganizer
from speechConverter import SpeechConverterAudio

# from AudioOrganizer import AudioOrganizer
# from speechConverter import SpeechConverterAudio
class MyHandler(FileSystemEventHandler):
  def on_modified(self, event):
    if event.is_directory:
      print('working', event.src_path)
      #makes file
      AudioObject = AudioOrganizer('{}.mp4'.format(event.src_patb))
      AudioObject.processFolder()
    
      Converter = SpeechConverterAudio(event.src_path)
      Converter.process()

#make output/inout file
def main():
  try:
    if not (os.path.isdir("output") and os.path.isdir("input")):
      os.mkdir("output")
      os.mkdir("input")
    print('file in system inplace')
  except:
    print("Made")

  path = "./input"
  event_handler = MyHandler()
  observer = Observer()
  observer.schedule(event_handler, path, recursive=True)
  observer.start()

  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    observer.stop()
  observer.join()

main()