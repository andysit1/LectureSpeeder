import openai
from settings import key

openai.api_key = key

def openAiReponse(prompt):
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt=prompt,
    temperature=0.2,
    max_tokens=60
  )
  print(response)
  return response.choices[0].text.strip()

def recursiveCallAi(prompt):
  parts = []
  answer = openAiReponse(prompt)
  parts.append(answer)

  while not answer.endswith('.'):
    prompt = "Continue this prompt " + answer
    answer = openAiReponse(prompt)
    parts.append(answer)

  totalAnswer = ""
  for part in parts:
    totalAnswer += " " + part
  print(totalAnswer)


class textAnalysis():
  def __init__(self):
    self.outline = ''
    self.questionsGenerated = []
    self.answerSummary = ''
    self.answerSummarySimple = ''

  def analysis(self):
    #find the summary to reduce token count
    self.answerSummary = openAiReponse(self.text + "\nTl;dr")
    self.outline = openAiReponse("Return the outline of the topics found in " + self.answerSummary)

  def summarize(self, text):
    return openAiReponse("Summarize this for a second-grade student: " + text)

  def results(self):
    print("Outline of Content: " + self.outline)
    print("Summary:" + self.answerSummary)

