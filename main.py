

#get input from command line
#iterate through string
#if consonant, then do the think to it
#print out the new string

def rovarspraket(s):
    newstr
    for c in s:
        if c.isalpha():
            if c in ('a', 'e', 'i', 'o', 'u',' ','y'): 
                newstr+= c
            else:
                newstr+= c +'o' + c