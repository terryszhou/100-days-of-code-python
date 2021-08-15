import requests
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()["results"]

htmlCodes = (
    ("'", '&#039;'),
    ('"', '&quot;'),
    ('>', '&gt;'),
    ('<', '&lt;'),
    ('&', '&amp;')
)

for question in question_data:
    for code in htmlCodes:
        question["question"] = question["question"].replace(code[1], code[0])