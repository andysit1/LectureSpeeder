import openai

from settings import key
openai.api_key = key

def openAiReponse(prompt):
  response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt=prompt,
    temperature=0.2,
    max_tokens=400
  )
  return response.choices[0].text.strip()

def recursiveCallAi(prompt):
  parts = []
  answer = openAiReponse(prompt)
  parts.append(answer)

  while not (answer.endswith('.') or answer.endswith('?') or answer.endswith('!')):
    prompt = "Continue"
    answer = openAiReponse(prompt)
    parts.append(answer)

  totalAnswer = ""
  for part in parts:
    totalAnswer += " " + part
  return totalAnswer.strip()


from summarizer import Summarizer,TransformerSummarizer
def gpt2ModelSummary(body):
  GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
  full = ''.join(GPT2_model(body, min_length=30))
  return full.strip()

