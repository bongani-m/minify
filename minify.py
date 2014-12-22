import re

#remove single line comments
def single_comments(text):
	return re.sub(r'//.*', '', text)

def multi_comments(text):
	return re.sub(r'(\/\*)(.*)(\*\/)', '', text.replace('\n', ''))
def remove_space(text):
	return "".join(text.split())


f = open('test.js')
text = reduce(lambda a,x: a+x, f)

def parser(text):
	text = single_comments(text)
	text = multi_comments(text)
	text = remove_space(text)
	return text

print [parser(text)]