// remove single line comments
function single_comments(text){
	var re = '/\/\/.*/g';
	return text.replace(re, '');
}

// removes multi-line comments
function multi_comments(text){
	var text = text.replace('\n', '');
	var re = '/(\/\*)(.*)(\*\/)/g';
	return text.replace(re, '');
}

// parser
function parser(text){
	text = single_comments(text);
	text = multi_comments(text);
	return text.split(/\s+/).join(' ');
}

