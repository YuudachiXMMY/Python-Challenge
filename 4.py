'''
# 4
http://www.pythonchallenge.com/pc/def/linkedlist.html
http://www.pythonchallenge.com/pc/def/linkedlist.php
'''

# In this question, you could use a Browser to view the website's source code. And then you will still find this:
'''
<!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough. -->
'''
# Really Cool. And the content got by clicking the photo is:
'''
and the next nothing is 44827
'''
# Now show time~~
#
# Here I will follow the advice by using the urlib XD.

import urllib,re

tar = re.compile(r"and the next nothing is (\d+)")
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'

def read(nothing):
    res = urllib.urlopen(url+nothing)
    html = res.read()
    print html
    if 'Divide' in html:
        # Damn
        # Dealling this freaking condition:
        # 'Yes. Divide by two and keep going.'
        read(str(int(nothing)/2))
    elif nothing == None:
        print 'Finally~'
        print html
    else:
        # Finally, there might be a:
        # 'list index out of range'
        # Whatever, I don't wanna do this coding again. So if you know how to fix it, plz plz let me know orz.
        read(re.findall(tar,html)[-1])

read(nothing)

'''
# Answer
peak.html
http://www.pythonchallenge.com/pc/def/peak.html
'''