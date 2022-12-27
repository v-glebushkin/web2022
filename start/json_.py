import json
import pprint # красивый вывод в консоль

person = '{"name": "Alex", "languages": ["Python", "Java"], "active": true, "age": 18, "experience": null}'

person_dict = json.loads(person)
print(person_dict)

person_json = json.dumps(person_dict)
print(person_json)

with open('quiz.json', 'r') as f:
    data = json.load(f)

# print(data['quiz']['sport']['q1']['answer'])
# pprint.pprint(data)

"""
1) Прочитать содержимое файла
2) Дописать третий вопрос в блок math
3) Записать в файл
"""

data['quiz']['maths']['q3'] = {'question': '5 * 5 = ?', 'options': ['15', '25', '35', '45'], 'answer': '25'}

print(json.dumps(data, indent = 2))

with open('quiz.json', 'w') as f:
    json.dump(data, f, indent = 4)