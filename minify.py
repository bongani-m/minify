import re

# remove single line comments
def single_comments(text):
	return re.sub(r'//.*', '', text)

# removes multi-line comments
def multi_comments(text):
	return re.sub(r'(\/\*)(.*)(\*\/)', '', text.replace('\n', ''))

# parser
def parser(text):
	text = single_comments(text)
	text = multi_comments(text)
	return ' '.join(text.split())
