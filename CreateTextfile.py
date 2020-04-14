fh = open('example.txt','w')

for i in range(1,11):
    print(fh.write("you are reading Line : %d \n"%i))

fh.close()

fh = open('example.txt','r')
# print(fh.read(3))
# print(fh.read(10))
#print(fh.readline())
#print(fh.readlines()) #convert lines intolist
# print(fh.readlines()[0])
#print(len(fh.readlines()[0]))

# for line in fh:
#     print(line.split(" "))

#now read the file and copy to the next file

kt =open('test.txt','w')
kt.write(fh.readlines()[0])

kt.close()

fh.close()
