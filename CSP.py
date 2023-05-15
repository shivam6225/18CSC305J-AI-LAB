def solutions():
    #letters=('b','a','s','e','l','g','m')
    solution=list()
    for b in range(9,0,-1):
        for a in range(9,-1,-1):
            for s in range(9,-1,-1):
                for e in range(9,-1,-1):
                    for l in range(9,-1,-1):
                        for g in range(9,0,-1):
                            for m in range(9,-1,-1):
                                if len(set([b,a,s,e,l,g,m]))==7:
                                    base=1000*b+100*a+10*s+e
                                    ball=1000*b+100*a+10*l+l
                                    games=10000*g+1000*a+100*m+10*e+s
                                    
                                    if base+ball==games:
                                        solution.append({'b':b,'a':a,'s':s,'e':e,'l':l,'g':g,'m':m})
    return solution

print(solutions())
