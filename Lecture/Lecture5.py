fobj = open(SRCFILE, mode='r')
print(type(fobj))
print(fobj)

cnts = fobj.read()
print(type(cnts))
print(cnts)

fobj.close()
print(fobj.closed)

fobj = open(SRCFILE, mode='r')

cnts_copy = ''
for line in fobj:
    cnts_copy += line
print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")
print(type(cnts_copy))
