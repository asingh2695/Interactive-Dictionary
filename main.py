import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word1):
	word1 = word1.lower()
	if word1 in data:
		return data[word1]
	elif word1.title() in data: #if user entered "delhi" then to check for "Delhi"
		return data[word1.title()]
	elif len(get_close_matches(word1, data.keys())) > 0:
		yn = input("Did you mean %s instead? Enter Y for Yes or N for No." % get_close_matches(word1, data.keys())[0])
		if yn == "Y":
			return data[get_close_matches(word1, data.keys())[0]]
		elif yn == "N":
			return "The word doesn't exist, Please check it again"
		else:
			return "We didn't understand your response"
	else:
		return "The word doesn't exist, Please check it again"


word = input("Enter the word you would like to search for: ")
output = translate(word)

if type(output) == list:
	for item in output:
		print(item)

else:
	print(output)
