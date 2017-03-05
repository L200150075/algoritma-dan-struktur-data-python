import string

g =[]
for i in range (100):
    a = string.printable
    e = len(a)
    f = a[i]
    g.append(f)

index_ascii = []
for i in range(len(g)):
    h = int(ord(g[i]))
    index_ascii.append(h)

j = {}
for i in range (len(g)):
    j[int(index_ascii[i])] = str(g[i])

print ("--------------------------")    
print (" No |" + " oktal |"+ "  hex |"+" sim |")
print ("--------------------------")
for i in range(128):
    b = str(bin(i))
    c = str(hex(i))
    d = str(oct(i))

    if  int(i) in index_ascii:
        if len(str(i)) == 3 :
            if len(str(d)) == 4 :
                if len(str(c)) == 3:
                    print (str(i)+" |  %s | %s |   %s  | ")%(d,c,j[i])
                else:
                    print (str(i)+" |  %s | %s |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 3 :
                if len(str(c)) == 3:
                    print (str(i)+" |   %s | %s |   %s  | ")%(d,c,j[i])
                else:
                    print (str(i)+" |   %s | %s  |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 2 :
                if len(str(c)) == 3:
                    print (str(i)+" |    %s | %s |   %s  | ")%(d,c,j[i])
                else:
                    print (str(i)+" |    %s | %s  |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 1 :
                if len(str(c)) == 3:
                    print (str(i)+" |     %s | %s |   %s  | ")%(d,c,j[i])
                else:
                    print (str(i)+" |     %s | %s |  %s  | ")%(d,c,j[i])
        elif len(str(i)) == 2:
            if len(str(d)) == 4 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |  %s | %s |   %s  | ")%(d,c,j[i])
                else:
                    print (" "+str(i)+" |  %s | %s |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 3 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |   %s |  %s |  %s  | ")%(d,c,j[i])
                else:
                    print (" "+str(i)+" |   %s | %s |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 2 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |    %s | %s |  %s  | ")%(d,c,j[i])
                else:
                    print (" "+str(i)+" |    %s | %s |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 1 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |     %s | %s |  %s  | ")%(d,c,j[i])
                else:
                    print (" "+str(i)+" |     %s | %s |  %s  | ")%(d,c,j[i])
        elif len(str(i)) == 1:
            if len(str(d)) == 4 :
                if len(str(c)) == 3:
                    print ("  "+str(i)+" |  %s | %s |  %s  | ")%(d,c,j[i])
                else:
                    print ("  "+str(i)+" |    %s | %s |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 3 :
                if len(str(c)) == 3:
                    print ("  "+str(i)+" |   %s |  %s |  %s  | ")%(d,c,j[i])
                else:
                    print ("  "+str(i)+" |    %s | %s |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 2 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |    %s | %s |   %s  | ")%(d,c,j[i])
                else:
                    print (" "+str(i)+" |    %s | %s |  %s  | ")%(d,c,j[i])
            elif len(str(d)) == 1 :
                if len(str(c)) == 3:
                    print ("  "+str(i)+" |     %s | %s |  %s  | ")%(d,c,j[i])
                else:
                    print ("  "+str(i)+" |     %s | %s |  %s  | ")%(d,c,j[i])

    else :
        if len(str(i)) == 3 :
            if len(str(d)) == 4 :
                if len(str(c)) == 3:
                    print (str(i)+" |  %s | %s |      | ")%(d,c)
                else:
                    print (str(i)+" |  %s | %s |     | ")%(d,c)
            elif len(str(d)) == 3 :
                if len(str(c)) == 3:
                    print (str(i)+" |   %s | %s |     | ")%(d,c)
                else:
                    print (str(i)+" |   %s | %s  |     | ")%(d,c)
            elif len(str(d)) == 2 :
                if len(str(c)) == 3:
                    print (str(i)+" |    %s | %s |     | ")%(d,c)
                else:
                    print (str(i)+" |    %s | %s  |     | ")%(d,c)
            elif len(str(d)) == 1 :
                if len(str(c)) == 3:
                    print (str(i)+" |     %s | %s |     | ")%(d,c)
                else:
                    print (str(i)+" |     %s | %s |     | ")%(d,c)
        elif len(str(i)) == 2:
            if len(str(d)) == 4 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |  %s | %s |      | ")%(d,c)
                else:
                    print (" "+str(i)+" |  %s | %s |     | ")%(d,c)
            elif len(str(d)) == 3 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |   %s |  %s |     | ")%(d,c)
                else:
                    print (" "+str(i)+" |   %s | %s |     | ")%(d,c)
            elif len(str(d)) == 2 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |    %s | %s |      | ")%(d,c)
                else:
                    print (" "+str(i)+" |    %s | %s |     | ")%(d,c)
            elif len(str(d)) == 1 :
                if len(str(c)) == 3:
                    print (" "+str(i)+" |     %s | %s |      | ")%(d,c)
                else:
                    print (" "+str(i)+" |     %s | %s |     | ")%(d,c)
        elif len(str(i)) == 1:
            if len(str(d)) == 4 :
                if len(str(c)) == 3:
                    print ("  "+str(i)+" |  %s | %s |      | ")%(d,c)
                else:
                    print ("  "+str(i)+" |    %s | %s |     | ")%(d,c)
            elif len(str(d)) == 3 :
                if len(str(c)) == 3:
                    print ("  "+str(i)+" |   %s |  %s |     | ")%(d,c)
                else:
                    print ("  "+str(i)+" |    %s | %s |     | ")%(d,c)
            elif len(str(d)) == 2 :
                if len(str(c)) == 3:
                    print ("  "+str(i)+" |    %s |  %s |     | ")%(d,c)
                else:
                    print ("  "+str(i)+" |    %s |  %s |     | ")%(d,c)
            elif len(str(d)) == 1 :
                if len(str(c)) == 3:
                    print ("  "+str(i)+" |     %s |  %s |     | ")%(d,c)
                else:
                    print ("  "+str(i)+" |     %s | %s |     | ")%(d,c)
