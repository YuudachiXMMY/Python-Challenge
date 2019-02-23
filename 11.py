'''
# 10
http://www.pythonchallenge.com/pc/return/5808.html
'''

# It's pretty hard.
# Only a picture with the hint 'odd even'.
# It asks us to rearrange the photo's pixel due to odd&even row&cow.

from PIL import Image

im=Image.open("11.png")
 
width = im.size[0]
height = im.size[1]

even = Image.new(im.mode, (width/2,height/2))
odd = Image.new(im.mode, (width/2,height/2))
 
for x in range(width):
    for y in range(height):
        pixel=im.getpixel((x,y))
        if x%2^y%2:
            odd.putpixel(((x-1)/2, y/2) if x%2 else (x/2, (y-1)/2) , pixel)
        else:
            even.putpixel((x/2, y/2), pixel)

even.save('11_even.jpg')
odd.save('11_odd.jpg')

'''
# Answer
# In even pic:
evil
http://www.pythonchallenge.com/pc/return/evil.html
'''