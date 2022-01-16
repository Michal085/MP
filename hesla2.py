#import hashlib
#inFileName = input("Zadaj nazov vstupu")
#intFile = open(outfileName , 'w')

#with open (inFileName) as f:
#    lines = [line.rstrip () for line in f]
#for line in lines:
#    md5 = hashlib.md5(line.encode())
#    md5hash = md5.hexdigest()
#    print(line + " : "+md5hash)
#    outFile.write(md5hash+'\n')
#outFile.close()

param = (i*i for i in range (5))
print(type(param))







