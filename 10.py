'''
# 9
http://www.pythonchallenge.com/pc/return/bull.html
'''

# Question: 
'''
len(a[30]) = ?
'''
# NOTICE: Now, while getting the url, we have to login with the username 'huge' and  password 'file'.
# In this question, you could use a Browser to view the website's source code. We find this:
'''
coords="146,399,..."
'''
# But this isn't what we want. Keep looking and this is what we are looking forward:
'''
a = [1, 11, 21, 1211, 111221, 
'''
# This is 'a'!
# Explanation:
'''
After 1, the next number is 'one 1': 11
After 11, the next number is 'two 1': 21
After 21, the next number is 'one 2, then one 1': 1211
After 1211, the next number is 'one 1, then one 2, then two 1': 111221
'''
# I met the same Problem in C before so it becomes really ez.

seq_list = ['1']

def seq(start):
    nextnum = ''
    counts = 1
    for i in range(0,len(start)):
        if start[i] == ' ':
            break
        elif start[i] == start[i+1]:
            counts += 1
        else:
            nextnum += str(counts) + start[i]
            counts = 1
    return nextnum

for i in range(1,31):
    seq_list.append(seq(seq_list[i-1]+" "))

print len(seq_list[30])

'''
# Answer
5808
http://www.pythonchallenge.com/pc/return/5808.html
'''