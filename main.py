

#get input from command line
#iterate through string
#if consonant, then do the think to it
#print out the new string

def rovarspraket(s):
    newstr = ''
    for c in s:
        if c.isalpha():
            if c in ('a', 'e', 'i', 'o', 'u','y'): 
                newstr+= c
            else:
                newstr+= c +'o' + c.lower()
        else:
            newstr+=c
    return newstr
print 'Hello', rovarspraket('Hello')
while True:
    print rovarspraket(str(raw_input('Enter the string:')))