'''
# 2
http://www.pythonchallenge.com/pc/def/ocr.html
'''

# In this question, you could use a Browser to view the website's source code. And then you will find this:
# <!-- find rare characters in the mess below: -->
# Just find the letters in the character sea
# Show time~~
#
# FYI, Here I will directly use the urlib to deal those characters, instead of viewing sourcee code through a browser XD.

import urllib2

res = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
html = str(res.read())
res.close()

pos = html.rfind('<!--')
pos_end = html.rfind('-->')
tar = html[pos:pos_end]
result = ''

for i in tar:
    io = ord(i)
    if io >= 65 and io <= 90 or io >= 97 and io<=122:
        result+=i

print result

'''
# Answer
equality
http://www.pythonchallenge.com/pc/def/equality.html
'''