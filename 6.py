'''
# 5
http://www.pythonchallenge.com/pc/def/channel.html
'''

# In this question, you could use a Browser to view the website's source code. And then you will still find the following:
'''
<!-- <-- zip -->

<!-- The following has nothing to do with the riddle itself. I just
# thought it would be the right point to offer you to donate to the
# Python Challenge project. Any amount will be greatly appreciated.
# -thesamet-->
''' 
# You could donate if you want, and I suggest to do so. But, this has NOTHING to do with the ridle itself...
# Well, back to the question. There's a 'zip' so I tried to replace the '.html' with '.zip':
# http://www.pythonchallenge.com/pc/def/channel.zip
# And we do download an archive. There are 910 '.txt' files in it. But no worries, there's also an 'readme.txt':
'''
welcome to my zipped list.
hint1: start from 90052
hint2: answer is inside the zip
'''
# I think we are asked to find files in the 910s...

num = '90052'
while True:
  try:
    with open('6_channel/'+num+'.txt', 'rb') as fp:
      data = fp.read()
      print data
      num = data.split(' ')[-1]
  except:
    break
    
# Results:
'''
Collect the comments.
'''

import zipfile

num = '90052'
comments = []

with zipfile.ZipFile('6_channel.zip') as zf:
  while True:
    try:
      zi = zf.getinfo(num+'.txt')
      comments.append(zi.comment.decode('utf-8'))
      data = zf.read(num+'.txt').decode('utf-8')
      num = data.split(' ')[-1]
    except:
      break

print ''.join(comments)

# Results:
'''
HOCKEY
'''
# Then go to: http://www.pythonchallenge.com/pc/def/HOCKEY.html
# We find:
'''
it's in the air. look at the letters.
'''
# So the correct answer is
'''
oxygen
'''
# FYI, Just run the code and you'll find that the 'H' is written in 'o',
# 'O' in 'X', 'C' in 'Y', 'K' in 'G', 'E' in 'E', and 'Y' in 'N'.

'''
# Answer
oxygen
http://www.pythonchallenge.com/pc/def/oxygen.html
'''