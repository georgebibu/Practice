emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
c,store=0,[]
for i in emails:
    domain=""
    stack=i.split('@')
    domain=stack[1]
    stack[0]=stack[0].replace('.','')
    stack=stack[0].split('+')
    if stack[0]+'@'+domain not in store:
        store.append(stack[0]+'@'+domain)
        c+=1
print(c)