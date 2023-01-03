import openai

openai.api_key = "key"

def openAiReponse(prompt):
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=64
  )
  return response.choices[0].text


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

