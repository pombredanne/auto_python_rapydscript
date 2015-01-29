import os

def compile_include_quick_tags_python(file):
	compiled = file[:-3] + '_compiled.py'

	os.system('"python.exe simple_preprocessor.py -TW '+file+' '+compiled+'  2>&1"')
	
	return compiled # run pre_processor on it, with file being the source and  it as the dest
	
include = "include.py"
execfile(os.path.abspath(compile_include_quick_tags_python(include))) # require fullpath, includes file


import sys
from subprocess import PIPE, Popen, STDOUT
               # experimental, just testing PHP called within Python
def php(code): # shell execute PHP from Python (that is being called from php5_module in Apache), for fun...
	p = Popen(['php'], stdout=PIPE, stdin=PIPE, stderr=STDOUT) # open process
	o = p.communicate('<?php '+ code +'\n ?>')[0]
	try:
		os.kill(p.pid, signal.SIGTERM)	# kill process
	except:
		pass
	return o

def top_content():
	return 'header'
	
def mid_content():
	return training_wheels_bit_slower_to_remove("""

This is a test, <br>it is actually within a triple double quoted string

""")
	
def end_content():
	return 'footer'
	
# in the case not transferring data from php using multiple domains, simply revert to a previous version, commit 
def domain_name(s):   
	if(s == 'A'):
		return 'us'
	elif(s == 'WIDE'):
		return 'com'
		
def training_wheels_bit_slower_to_remove(s): # recommend: to remove this function for production code and edit code as required
                                             # just chose an arbitrary tag to represent the python format variables, works nicely, for now
	return s.replace('{', '{{').replace('}', '}}').replace('{{**{{', '{').replace('}}**}}', '}')

# test example, don't forget to have php.exe and php5ts.dll in PATH
width = 100
height = 100	
code = """
echo ('   """ + str(width) + """, """ + str(height) + """  ');
"""

# Note, any JavaScript or any other code that contains a curly brace 
# must double the curly brace when using the python format function with the triple double-quoted string, 
# but not in a JavaScript src file (regardless of using the format function or not).

# It further verifies that the compiled Python-like RapydScript JavaScript will indeed run,
# with the use of jQuery's .ready and .getScript that also verifies the JavaScript is syntactically correct.
# If it is correct to the browser's JavaScript engine, the console.log will successfully print to the browser's console.

def output(name):
# With this New Feature: Open and Close Tags for this Python file 
# (It allows syntax highlighting within the tags, and eases coding)
# Note that the following opening tag, (less-than sign and percent sign) will be replaced by the simple_preprocessor.py
# with this:  PRINT training_wheels_bit_slower_to_remove(""" (lowercase) NOTE: this exact comment line obviously does not run.
	print training_wheels_bit_slower_to_remove("""

<!DOCTYPE html>
<html lang="en">
<head>
<title></title>
<script src="js/jquery-1.11.2.min.js"></script>
<link rel="stylesheet" type="text/css" href="css/page_frame_{**{domain}**}.css" />
<script src="first.js"></script>

<script>
$(document).ready(function() {
	console.log('jquery 1.11.2 initialized');
	console.log('app.js loading...  if capitalized done. statement does not appear next, or as the print line to the console, there is an error occurring');
});

jQuery.getScript("first.js", function() {
	console.log('DONE.');
});
</script>

</head>
<body>
{**{testing_output}**}<br>
<div id="container">

<div id="top">{**{top_content}**}</div>

<div id="mid">{**{mid_content}**}</div>

<div id="end">{**{end_content}**}</div>

</div>

PHP test: {**{php_test}**}
</body>
</html>

""").format (  
	# variables used
	top_content = top_content(),
	mid_content = mid_content(),
	end_content = end_content(),
	php_test    = php(code),  # just testing, remove if coding anything serious
	
	domain      = domain_name(name), # or something like whether a mobile device,
                                     # resolution information, etc. to select which css that fits	

testing_output = this_is_a_test()    # test of include file using quick tags python syntax
)



# ALSO NOTE: On the line immediately starting with the (percent sign and greater-than sign), this is the closing tag
# gets replaced back to (triple double quotes and open parenthesis).

if __name__ == "__main__":  # in the case not transferring data from php, then simply revert to a previous version, commit

	if( not len(sys.argv) >= 2 ):
		print "argument is required, which domain name from the initial, starting PHP"
		sys.exit(1)
		
	output(sys.argv[1])