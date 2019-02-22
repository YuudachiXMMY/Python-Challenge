'''
# 6
http://www.pythonchallenge.com/pc/def/oxygen.html
'''

# In this question, there's only a picture with something strange on it.
# So I try to use PTL to deal with these strange things.
#
# Here I will directly use the urllib to get the picture.


from PIL import Image
import numpy as np

image = Image.open("7.png", 'r')

# I use Adobe Photoshop to find the range of that strange thing orz.
data = [image.getpixel((i, j)) for i in range(0, 607, 5) for j in range(43, 51, 9)]

def transLetter(data):
  result = ''
  for i in data:
    try:
      result += chr(i[0])
    except:
      result += chr(i)
  return result

# transLetter(data) returns the following:
'''
smmarrt gguyy, yyouu maadee itt.  thee nnextt lleveel  is  [1105,, 1110,, 1116,, 1101,, 1103,, 1114,, 1105,, 1116,, 1121]]
'''
# There're several dups :(
# The dupping rule is 'ABBCDDE'

def rmDup(str):
  result = ''
  for i in range(0,len(str)):
    if (i+1) % 7 == 2 or (i+1) % 7 == 5:
      pass
    else:
      result += str[i]
  return result

print rmDup(str(transLetter(data)))

# Result:
'''
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
'''
# Keep translating the '[105, 110, 116, 101, 103, 114, 105, 116, 121]' part~~

ans = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print transLetter(ans)

'''
# Answer
integrity
http://www.pythonchallenge.com/pc/def/integrity.html
'''