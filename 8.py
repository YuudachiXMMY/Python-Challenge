'''
# 7
http://www.pythonchallenge.com/pc/def/integrity.html
'''

# In this question, you could use a Browser to view the website's source code. And then you will find this:
'''
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->
'''
# There's a hint:
'''
Where is the missing link?
'''
# 
# Interesting. We can click on the bee photo. It asks us to sign in with a username and password
# We just use the bz2' lib. ez~~

import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un = bz2.decompress(un)
pw = bz2.decompress(pw)

print 'Username:', un
print 'Password:', pw

'''
# Answer
un : huge
pw : file
http://www.pythonchallenge.com/pc/return/good.html
'''