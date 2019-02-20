'''
# 1
http://www.pythonchallenge.com/pc/def/map.html
'''

def decry(input):
    return chr(((ord(input)+2) - ord('a')) % 26 + ord('a'))

def main(txt):
    result = ''
    for i in txt:
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            result += decry(i)
        else:
            result += i
    print result

tar = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = 'map'

main(tar)
main(url)

'''
# Answer
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
http://www.pythonchallenge.com/pc/def/ocr.html
'''

'''
# To use Maketrans
import string
temp = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print tar.translate(temp)
'''