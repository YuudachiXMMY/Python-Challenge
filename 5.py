'''
# 4
http://www.pythonchallenge.com/pc/def/peak.html
'''

# In this question, you could use a Browser to view the website's source code. And then you will still find this:
'''
<!-- peak hell sounds familiar ? -->
'''
# peak hell? pickle?
# Yep!
# 
# Here I will directly use the urlib to deal those letters, instead of viewing sourcee code through a browser XD.

from urllib import urlretrieve
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

urlretrieve(url, filename = '5_banner.pkl')

with open('5_banner.pkl', 'rb') as fp:
    result = pickle.load(fp)
    #print result
    # It returns a matrix.

for i in result:
    for j in i:
        print j[0] * j[1],
    print '\n'

'''
# Answer
channel
http://www.pythonchallenge.com/pc/def/channel.html
'''