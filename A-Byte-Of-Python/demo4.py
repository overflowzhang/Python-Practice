#文件读写

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt','w')

f.write(poem)

f.close()

f = open('poem.txt')

while True:
    line = f.readline()