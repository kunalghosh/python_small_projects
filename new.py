import sys
f = open(sys.argv[1])
log = f.readlines()
res = dict()
for entry in log: 
    resource = entry.split('"')[1]
    if resource == "GET / HTTP/1.1" or resource == "GET / HTTP/1.0":
        # This indicates that a webpage was requested
        resource = entry.split('"')[3]
    
    else:
        # This indicates some other mime resource was requested
        # get the resource only
        resource=resource.split(" ")[1]
    

    if res.has_key(resource):
        res[resource] +=1
    else:
        res[resource]=1

d = [(count,resource) for resource,count in res.items()]

d.sort()
d.reverse()
result = [(resource,count) for (count,resource) in d[:10]]
for i in result:
    if i[0] == "-":
        print str("Main Website (Document Root) :")+str(i[1])
    else:
        print str(i[0])+" : "+str(i[1])
