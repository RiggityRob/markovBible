import markovify
from pathlib import Path

#requires pip install of markovify

files = Path("bible/").iterdir()

for file in files:
	with file.open('r') as file:
		text = file.read()

text_model = markovify.Text(text)

for i in range(10):
	print(text_model.make_sentence())
