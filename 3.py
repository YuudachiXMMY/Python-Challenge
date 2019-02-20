'''
# 3
http://www.pythonchallenge.com/pc/def/equality.html
'''

# In this question, you could use a Browser to view the website's source code. And then you will still find a:
# <!-- ...... -->
# Show time~~
# Just find a low case letter surrounded by EXACTELY three upper case letters XXXD. E.g, in 'aBCDeFGHi', 'e' is the answer
#
# Here I will directly use the urlib to deal those characters, instead of viewing sourcee code through a browser XD.

import urllib2

res = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
html = str(res.read())
res.close()

import re

pos = html.rfind('<!--')
pos_end = html.rfind('-->')
tar = html[pos:pos_end]

result = re.findall( '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]' , tar)

print  ''.join(result)

'''
# Answer
linkedlist
http://www.pythonchallenge.com/pc/def/linkedlist.html
'''