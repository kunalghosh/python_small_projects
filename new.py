import sys

f = open(sys.argv[1])

res = dict()

for entry in f:

    resource = entry.split('"')[1]
    resource = resource.split(" ")[1]
    res.setdefault(resource,0)
    res[resource]+=1

#d = [(count,resource) for resource,count in res.items()]
#d.sort()
#d.reverse()

d=sorted([(count,resource) for resource,count in res.items()],reverse=True)

#result = [(resource,count) for (count,resource) in d[:10]]

for i in range(10):
    print "%s:%s" %(d[i][1],d[i][0])
    #if i[0] == "-":
    #    print str("Main Website (Document Root) :")+str(i[1])
    #else:
    #    print str(i[0])+" : "+str(i[1])
