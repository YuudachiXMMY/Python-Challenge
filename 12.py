'''
# 11
http://www.pythonchallenge.com/pc/return/evil.html
'''

# 

from PIL import Image

im=Image.open("12.png")
 
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

even.save('12_even.jpg')
odd.save('12_odd.jpg')


'''
# Answer
'''