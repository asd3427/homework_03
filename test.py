
def splitlist(l,o):
    if isinstance(l,list):
        result= []
        for i in range(l.count(o)):
            end  =l.index(o,0,len(l))
            result.append(l[0:end])
            l = l[end + 1:len(l)]
        if len(l) != 0:
            result.append(l)
        return result
with open("hmmData.txt")  as f :
    data = f.read()
    f.close()
labeList=[]
for row in data:
    labeList.append(row[len(row)-1])
if __name__ =="__main__":
    data = splitlist(labeList,'\n')






hex('a')
