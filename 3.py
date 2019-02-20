'''
# 3
http://www.pythonchallenge.com/pc/def/equality.html
'''

# In this question, you could use a Browser to view the website's source code. And then you will still find a:
# <!-- ...... -->
# Show time~~
# Just find a low case letter surrounded by EXACTELY three upper case letters XXXD.
#
# Here I will directly use the urlib to deal those characters, instead of viewing sourcee code through a browser XD.

import urllib2

res = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
html = str(res.read())
res.close()

pos = html.rfind('<!--')
pos_end = html.rfind('-->')
tar = html[pos:pos_end]
loc = 4
result = ''
counts =0

def checkUpperCase(list):
    for t in list:
        if ord(t)<65 and ord(t)>90:
            return False
    return True

def checkLowCase(list):
    for t in list:
        if ord(t)<97 and ord(t)>122:
            return False
    return True

for i in tar[4:len(tar)-4]:
    io = ord(i)
    if io >= 97 and io<=122:
        outer = [tar[loc-4],tar[loc+4]]
        list_check = [tar[loc-1],tar[loc-2],tar[loc-3],tar[loc+1],tar[loc+2],tar[loc+3]]
        if checkUpperCase(list_check) and checkLowCase(outer):
            result += i
    loc+=1

print result

'''
# Answer
http://www.pythonchallenge.com/pc/def/.html
'''