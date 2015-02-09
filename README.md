auto_python_rapydscript
=======================

The purpose is automatic compiling of python like Rapydscript to JavaScript for client side; 
in addition to a web page written in python, output through minimal php code using the php module

The project has since grown to innovate quick tags for python source code that use asp like tags
of <% and %> to denote triple quoted strings, useful new format variable tags to allow curly braces
within JavaScript without escaping them (i.e., two curly braces to represent one within python triple quoted stings),
it allows syntax highlighting by text editors of a programming language keywords within the source code 
between these open and close tags,
as well as the innovative feature of hexadecimal tags to send content to the web browser.
Also added the feature of making all quick tag <% %> strings (that represent triple double quoted strings) 
to be raw literal strings for the reason that the output intended to be displayed in a web browser, therefore
less escaping of special characters, and the newline is of course the html (br tag with angle backets) on the web.

In addition to the <hex></hex> I created, another feature I have innovated is a 
html like "unicode python quick tag" of <unicode></unicode> for improved structure to html markup.



Requirements:

node.exe   (to compile rapydscript)

python.exe (to use a python script for server side web page creation, 
			optional perhaps but nice to have python server side 
			and (python like) client side with rapydscript)
			
php.exe    (to initialize the page, for its superglobal variable access 
            due to its maturity access, for now)
			
RapydScript note:

*.pyj files are edited by the user.

*.js  files generated by RapydScript are auto created and should not be manually edited.

*_compiled.py files are auto generated and also should not be manually edited.

Also note:

The RapydScript simple example provided displays its output 
through the browser's console log, Firebug's console log, etc.

2015-02-08
Added a feature by removing the trailing backslash issue in Python string implementation in two ways so as to simply 
run without this issue by automatically dealing with it in an optional manner (see simple_preprocessor.py for details).
This improves python quick tags <% %> triple double quoted strings to be more wysiwyg, that is the intent.

2015-01-05
Small edit to display a canvas tag using Python like Rapydscript (via Javascript).

In another update to source, added feature to allow python quick tags between parentheses, this is in addition to
quick tags (being <% %> triple quoted strings) are allowed to be used to an assignment operator to a variable, and
can be used to print out to the web page (see simple_preprocessor.py for details).

2015-02-03
Added a way to optionally show unicode type python quick tags with a boolean from index.php to display source code with or without unicode type python quick tags.  
Note that this feature is commented out initially, by default.

2015-02-02
Added a comment at the end of index.php to explain a found senario to further recommend the different file format
and NOT the one file format, this comment explanation then makes the simple_postprocessor.py  unnecessary and during a source code refactoring can be removed.
In another update to source code, add the feature of making the quick python tags of <%  %> to now represent 
raw literal triple double quotes.  This is as a prelude step to a new innovative feature of unicode type python quick tags that is yet to be added later today.
 
In addition to the <hex></hex> I previously created, another feature I have innovated is a html like "unicode python quick tag" for improved structure to html markup.
 
In the third update to source code, I've now added the feature of html like unicode type python quick tags to wrap the
quick tags feature of <% %> that represents a triple double quoted string.  In this initial version the way it works
is by the programmer adding     .unicode_markup()      to the dynamically added object,class to be used ONLY
as a transition step that drops the <unicode> and </unicode> tags, leaving the content within the tag unchanged.
Perhaps later version will dynamically include the  .unicode_markup()  method as long as I create a nice way to transfer its
boolean switch.
Note that in this version, the method should be appended to  %>.unicode_markup(False)  but if using format variables, before  the .format() method
otherwise it is required by you to make a small edit to put the string that is the argument to utags  around the format method also.
Perhaps a later version will address that when dynamically appending the  .unicode_markup()

2015-01-31
With a second implementation, having discovered that raw literal strings are the solution to dealing with the
tedious python escaping of characters when outputing messages to the browser console window (instead of .encode('ascii'))
I create a second pre processor step by the name of simple_preprocessor_auto_print_literal.py to convert these print_wwwlog()
statements to the browser's console log to raw strings automatically.  Also this is prelude to a ascii representation
form of unicode within innovative unicode type python quick tags, in the works, stay tuned.
This is a sample of the new feature I'm creating:
print r'hello (br tag with angle brackets)  <!-- <unicode>\xe5</unicode>lpha   <unicode>\xdf</unicode>ravo, <unicode>\u1e09</unicode>harlie  -->   (br tag with angle brackets) world \a'
And instead of the html comments, the idea is to use html div tags and show the unicode only when JavaScript has easily, correctly
converted the "ascii unicode text" of the unicode character.  For perhaps many to actually enjoy unicode instead of tediously
reading of for example many lines of source code to examine what escape characters need to be done.	

2015-01-30
Added a very innovative feature of hexadecimal open and close tags of <hex> and </hex> to reliably transport content 
of hexadecimal type converted from a string to the web browser, from there it is converted back to a string. 
For the initial purpose to deal with tedious python escape characters.
In another update to source code, added the feature to have quick tags for python triple quoted strings 
for the assignment operator (to a variable).  For the third update this day, a compromise to print lines of statements
so that escaping characters not required, and perhaps an innovative idea on unicode tags.

2015-01-29
Added the feature to compile the include python files only when its been edited, modified (similar to the feature added on 2015-01-26 
that compiles the python generated webpage only when edits to the source file happen).
In a second update to source code, I've refactored the code to better deal with strings 
from PHP to Python by escaping in the include files as an improvement and added plenty of comments 
to make apparent how the internals work to date.

2015-01-28
Added a feature to allow writing print statements to the browser's console for demonstration purposes,
to show a working example of python string compatibility with that of PHP and JavaScript strings.

2015-01-27
Added to now allow including files in python using the quick tags feature.
Quick tags are what I refer to as the open and close <%  %> tags and the optional feature of using custom tags
for format variables within triple quoted strings that then allows to use one curly brace at a time without escaping it
with a second curly brace.

2015-01-26
Added a new feature to compile the python generated webpage only when edits to the source file.

2015-01-15
Added to the previous feature of open and close <%  %> tags for triple quoted strings so that it's able to be returned 
as a string from a function or method.

2015-01-13
Added the feature of python tags, open and close <%  %> for triple quoted strings with a few format text replacements 
to deal with curly brackets within triple quoted strings when used together with the format function.


NOTES:

2015.02.02
With widespead adoption: Browser implementation may decide to abbreviate the "unicode type python quick tag" 
to <uni></uni> (equivalent in length to the innovated <hex></hex> python quick tag) 
from <unicode></unicode> a feature that at face value seem reasonable.

2015.02.02
Motivation behind the <unicode></unicode> tags (unicode type python quick tags):
Premise: For too long have programmers been burdened by unicode to internally mentally parse whether 
what they see is what they get (spin on the wysiwyg principle).  Therefore, I've created the innovative pyton quick tags 
as a step to structure unicode in addition to the feature of reducing the need to escape characters with the use of 
raw string literals as a side issue that has been added, with this additional feature of unicode tags, 
it improves readability of source code by the use of this <unicode></unicode> html like markup tag feature
as an extension to html tags.

