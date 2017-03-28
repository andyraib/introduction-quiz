import json
import requests
data = json.loads(open('introduction_quiz.json').read())
response = requests.post('http://localhost:9200/quiz/post/1',json=data)

