from random import randint
def listring(x,p):
    if p == True:
        y = ''
        for z in x:
            y += z + ', '
        y = y.strip(', ')
        return y

    else:
        y = ''
        for z in x:
            y += z
        return y
    
def sort_value(x):
    l = sorted(x.items(), key = lambda t:t[1])
    
    return l

def utakmica(g,h):
    i = g-h
    if i > 0:
        k = 8.5
        if i >= k:
            x = randint(1,4)
            y = randint(0,2)
            if x > y:
                bod1 = 3
                bod2 = 0
                return bod1,bod2
            if x == y:
                bod1 = 1
                bod2 = 1
                return bod1,bod2
            else:
                bod1 = 0
                bod2 = 3
                return bod1,bod2
        if i < k:
            x = randint(1,3)
            y = randint(0,2)
            if x > y:
                bod1 = 3
                bod2 = 0
                return bod1,bod2
            if x == y:
                bod1 = 1
                bod2 = 1
                return bod1,bod2
            else:
                bod1 = 0
                bod2 = 3
                return bod1,bod2
    if i < 0:
        k = -8.5
        if i <= k:
            y = randint(1,4)
            x = randint(0,2)
            if y > x:
                bod1 = 0
                bod2 = 3
                return bod1,bod2
            if x == y:
                bod1 = 1
                bod2 = 1
                return bod1,bod2
            else:
                bod1 = 3
                bod2 = 0
        if i > k:
            y = randint(1,3)
            x = randint(0,2)
            if y > x:
                bod1 = 0
                bod2 = 3
                return bod1,bod2
            if x == y:
                bod1 = 1
                bod2 = 1
                return bod1,bod2
            else:
                bod1 = 3
                bod2 = 0
                return bod1,bod2
    else:
        x = randint(0,3)
        y = randint(0,3)
        if x > y:
            bod1 = 3
            bod2 = 0
            return bod1,bod2
        if x == y:
            bod1 = 1
            bod2 = 1
            return bod1,bod2
        else:
            bod1 = 0
            bod2 = 3
            return bod1,bod2

def bodovi(c,v,b,n):
    bodq, bodr = utakmica(c,v)
    bodu, bodp = utakmica(b,n)
    bodw, boda = utakmica(c,n)
    bodt, bodi = utakmica(v,b)
    bode, bodo = utakmica(c,b)
    bodz, bods = utakmica(v,n)
    
    bodovi1 = bodq + bodw + bode 
    bodovi2 = bodr + bodt + bodz
    bodovi3 = bodu + bodi + bodo
    bodovi4 = bodp + boda + bods

    return bodovi1,bodovi2,bodovi3,bodovi4

def sort_bodova(abcdef,prolaze,tablica123456):
    rating = {'France' : 86, 'Spain' : 84, 'Germany' : 86, 'England' : 84, 'Portugal' : 85, 'Belgium' : 86,'Italy' : 84, 'Russia' : 78, 'Switzerland' : 78, 'Austria' : 78, 'Croatia' : 79, 'Ukraine' : 76, 'Czech Republic' : 76, 'Sweeden' : 78, 'Poland' : 82, 'Finland' : 72, 'Slovakia' : 74, 'Hungary' : 73, 'Turkey' : 78, 'Netherlands' : 83, 'Denmark' : 78, 'Wales' : 76, 'North Macedonia' : 70, 'Scotland' : 74}
    bodovi1,bodovi2,bodovi3,bodovi4 = bodovi(rating[abcdef[0]],rating[abcdef[1]],rating[abcdef[2]],rating[abcdef[3]])
    x = {abcdef[0] : bodovi1, abcdef[1] : bodovi2,  abcdef[2] : bodovi3 , abcdef[3] : bodovi4}
    xs = sort_value(x)
    prolaze.extend([xs[3][0],xs[2][0]])
    tablica123456.extend([xs[3][0] + ' ' + str(xs[3][1]),'\n', xs[2][0] + ' ' + str(xs[2][1]),'\n', xs[1][0] + ' ' + str(xs[1][1]), '\n', xs[0][0] + ' ' + str(xs[0][1])])

    
    return (prolaze,tablica123456,xs)
 
def ishodskup(a,b,c,d,e,f):
    prolaze = []
    tablica1, tablica2, tablica3, tablica4, tablica5, tablica6 = [], [], [], [], [], []
    treciprolaze = []
    A,B,C,D,E,F = False, False, False, False, False, False
    prolaze,tablica1,xs = sort_bodova(a,prolaze,tablica1)
    prolaze,tablica2,ys = sort_bodova(b,prolaze,tablica2)
    prolaze,tablica3,zs = sort_bodova(c,prolaze,tablica3)
    prolaze,tablica4,ws = sort_bodova(d,prolaze,tablica4)
    prolaze,tablica5,us = sort_bodova(e,prolaze,tablica5)
    prolaze,tablica6,ts =  sort_bodova(f,prolaze,tablica6)
    treci = {xs[1][0] : xs[1][1], ys[1][0] : ys[1][1], zs[1][0] : zs[1][1], ws[1][0] : ws[1][1], us[1][0] : us[1][1], ts[1][0] : ts[1][1]}
    trecis = sort_value(treci) 
    treciprolaze.extend([trecis[5][0],trecis[4][0],trecis[3][0],trecis[2][0]])
    if xs[1][0] == treciprolaze[0]:
        A = True
        prolaze.append(xs[1][0])
    if xs[1][0] == treciprolaze[1]:
        A = True
        prolaze.append(xs[1][0])
    if xs[1][0] == treciprolaze[2]:
        A = True
        prolaze.append(xs[1][0])
    if xs[1][0] == treciprolaze[3]:
        A = True
        prolaze.append(xs[1][0])
    if ys[1][0] == treciprolaze[0]:
        B = True
        prolaze.append(ys[1][0])
    if ys[1][0] == treciprolaze[1]:
        B = True
        prolaze.append(ys[1][0])
    if ys[1][0] == treciprolaze[2]:
        B = True
        prolaze.append(ys[1][0])
    if ys[1][0] == treciprolaze[3]:
        B = True
        prolaze.append(ys[1][0])
    if zs[1][0] == treciprolaze[0]:
        C = True
        prolaze.append(zs[1][0])
    if zs[1][0] == treciprolaze[1]:
        C = True
        prolaze.append(zs[1][0])
    if zs[1][0] == treciprolaze[2]:
        C = True
        prolaze.append(zs[1][0])
    if zs[1][0] == treciprolaze[3]:
        C = True
        prolaze.append(zs[1][0])
    if ws[1][0] == treciprolaze[0]:
        D = True
        prolaze.append(ws[1][0])
    if ws[1][0] == treciprolaze[1]:
        D = True
        prolaze.append(ws[1][0])
    if ws[1][0] == treciprolaze[2]:
        D = True
        prolaze.append(ws[1][0])
    if ws[1][0] == treciprolaze[3]:
        D = True
        prolaze.append(ws[1][0])
    if us[1][0] == treciprolaze[0]:
        E = True
        prolaze.append(us[1][0])
    if us[1][0] == treciprolaze[1]:
        E = True
        prolaze.append(us[1][0])
    if us[1][0] == treciprolaze[2]:
        E = True
        prolaze.append(us[1][0])
    if us[1][0] == treciprolaze[3]:
        E = True
        prolaze.append(us[1][0])
    if ts[1][0] == treciprolaze[0]:
        F = True
        prolaze.append(ts[1][0])
    if ts[1][0] == treciprolaze[1]:
        F = True
        prolaze.append(ts[1][0])
    if ts[1][0] == treciprolaze[2]:
        F = True
        prolaze.append(ts[1][0])
    if ts[1][0] == treciprolaze[3]:
        F = True
        prolaze.append(ts[1][0])  
    p = False
    return prolaze, A,B,C,D,E,F, print('\n''\n' 'Group A - Standings: ' '\n' '{}' '\n''\n' 'Group B - Standings: ' '\n' '{}' '\n' '\n' 'Group C - Standings: ' '\n' '{}' '\n' '\n' 'Group D - Standings: ' '\n' '{}' '\n' '\n' 'Group E - Standings: ' '\n' '{}' '\n' '\n' 'Group F - Standings: ' '\n' '{}'.format(listring(tablica1,p), listring(tablica2,p), listring(tablica3,p), listring(tablica4,p), listring(tablica5,p),listring(tablica6,p)))

def utakmica2(p,z,n,m):
    rating = {'France' : 86, 'Spain' : 84, 'Germany' : 86, 'England' : 84, 'Portugal' : 85, 'Belgium' : 86,'Italy' : 84, 'Russia' : 78, 'Switzerland' : 78, 'Austria' : 78, 'Croatia' : 79, 'Ukraine' : 76, 'Czech Republic' : 76, 'Sweeden' : 78, 'Poland' : 82, 'Finland' : 72, 'Slovakia' : 74, 'Hungary' : 73, 'Turkey' : 78, 'Netherlands' : 83, 'Denmark' : 78, 'Wales' : 76, 'North Macedonia' : 70, 'Scotland' : 74}
    i = rating[z[n]] - rating[z[m]]
    if i > 0:
        k = 8.5
        if i >= k:
            x = randint(1,4)
            y = randint(0,2)
            if x > y:
                p.append(z[n])
                return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
            if x == y:
                f = randint(1,2)
                g = randint(0,1)
                if f > g:
                    p.append(z[n])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[n]))
                if f == g:
                    pen = randint(0,1)
                    if pen == 0:
                        p.append(z[n])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[n]))
                    else:
                        p.append(z[m])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[m])) 
                else:
                    p.append(z[m])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[m]))
            else:
                p.append(z[m])
                return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
        if i < k:
            x = randint(1,3)
            y = randint(0,2)
            if x > y:
                p.append(z[n])
                return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
            if x == y:
                f = randint(0,2)
                g = randint(0,1)
                if f > g:
                    p.append(z[n])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[n]))
                if f == g:
                    pen = randint(0,1)
                    if pen == 0:
                        p.append(z[n])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[n]))
                    else:
                        p.append(z[m])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[m])) 
                else:
                    p.append(z[m])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[m]))
            else:
                p.append(z[m])
                return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
            
    if i < 0:
        k = -8.5
        if i <= k:
            y = randint(1,4)
            x = randint(0,2)
            if y > x:
                p.append(z[m])
                return p,print('{}'.format('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m])))
            if x == y:
                f = randint(0,1)
                g = randint(1,2)
                if g > f:
                    p.append(z[n])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[n]))
                if f == g:
                    pen = randint(0,1)
                    if pen == 0:
                        p.append(z[n])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[n]))
                    else:
                        p.append(z[m])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[m])) 
                else:
                    p.append(z[m])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[m]))
            else:
                p.append(z[n])
                return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
        if i > k:
            y = randint(1,3)
            x = randint(0,2)
            if y > x:
                p.append(z[m])
                return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
            if x == y:
                f = randint(0,1)
                g = randint(0,2)
                if g > f:
                    p.append(z[n])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[n]))
                if f == g:
                    pen = randint(0,1)
                    if pen == 0:
                        p.append(z[n])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[n]))
                    else:
                        p.append(z[m])
                        return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[m])) 
                else:
                    p.append(z[m])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[m]))
            else:
                p.append(z[n])
                return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
    else:
        x = randint(0,3)
        y = randint(0,3)
        if x > y:
            p.append(z[n])
            return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
        if x == y:
            et = randint(0,2)
            if et == 0:
                p.append(z[n])
                return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[n]))
            if et == 1:
                pen = randint(0,1)
                if pen == 0:
                    p.append(z[n])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[n]))
                else:
                    p.append(z[m])
                    return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time and penalties {} wins)'.format(z[n],x,y,z[m],z[m])) 
            else:
                p.append(z[m])
                return p,print('{}' '  {}' '-' '{}  ' '{}' '   (after extra time {} wins)'.format(z[n],x,y,z[m],z[m]))
        else:
            p.append(z[m])
            return p,print('{}' '  {}' '-' '{}  ' '{}'.format(z[n],x,y,z[m]))
 
def osmina(l,a,b,c,d,e,f):
    prolaze2 = []
    if a == True and b == True and c == True and d == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,13)
        utakmica2(prolaze2,l,2,15)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,12)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if a == True and b == True and c == True and e == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,12)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,13)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if a == True and b == True and c == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,12)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,13)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if a == True and b == True and d == True and e == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,12)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,13)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if a == True and b == True and d == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,12)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,13)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if a == True and b == True and e == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,12)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,13)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if a == True and c == True and d == True and e == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,14)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,12)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,13)
        utakmica2(prolaze2,l,3,11)
    if a == True and c == True and d == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,14)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,12)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,13)
        utakmica2(prolaze2,l,3,11)
    if a == True and c == True and e == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,14)
        utakmica2(prolaze2,l,2,12)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,15)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,13)
        utakmica2(prolaze2,l,3,11)
    if a == True and d == True and e == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,14)
        utakmica2(prolaze2,l,2,12)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,15)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,13)
        utakmica2(prolaze2,l,3,11)
    if b == True and c == True and d == True and e == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,14)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,12)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,13)
        utakmica2(prolaze2,l,3,11)
    if b == True and c == True and d == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,14)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,12)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,13)
        utakmica2(prolaze2,l,3,11)
    if b == True and c == True and e == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,13)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,12)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if b == True and d == True and e == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,15)
        utakmica2(prolaze2,l,2,13)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,12)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,14)
        utakmica2(prolaze2,l,3,11)
    if c == True and d == True and e == True and f == True:
        utakmica2(prolaze2,l,1,5)
        utakmica2(prolaze2,l,6,14)
        utakmica2(prolaze2,l,2,13)
        utakmica2(prolaze2,l,10,9)
        utakmica2(prolaze2,l,4,15)
        utakmica2(prolaze2,l,8,7)
        utakmica2(prolaze2,l,0,12)
        utakmica2(prolaze2,l,3,11)
    
    return prolaze2

def cetvrt(l):
    prolaze3 = []
    utakmica2(prolaze3,l,0,1)
    utakmica2(prolaze3,l,2,3)
    utakmica2(prolaze3,l,4,5)
    utakmica2(prolaze3,l,6,7)

    return prolaze3

def polu(l):
    prolaze4 = []
    utakmica2(prolaze4,l,0,1)
    utakmica2(prolaze4,l,2,3)

    return prolaze4

def finale(l):
    pobjednik = []
    utakmica2(pobjednik,l,0,1)

    return print('\n''\n' 'Winner of the UEFA European Championship 2020. is {}!'.format(pobjednik[0]))
    
def main():
    a = ['Turkey', 'Italy', 'Wales', 'Switzerland']
    b = ['Denmark', 'Finland', 'Belgium', 'Russia']
    c = ['Netherlands', 'Ukraine', 'Austria', 'North Macedonia']
    d = ['England', 'Croatia', 'Scotland', 'Czech Republic']
    e = ['Spain', 'Sweeden', 'Poland', 'Slovakia']
    f = ['Hungary', 'Portugal', 'France', 'Germany']
    razmak = ' '
    print('{} UEFA European Championship 2020'.format(razmak*10))
    p = True
    print('\n' 'Group A: {}' '\n' 'Group B: {}' '\n' 'Group C: {}' '\n' 'Group D: {}' '\n' 'Group E: {}' '\n' 'Group F: {}'.format(listring(a,p),listring(b,p),listring(c,p),listring(d,p),listring(e,p),listring(f,p)))
    st = ''
    print('\n')
    while st != 'start':
        st = input('Type start: ')
    prolaze, A,B,C,D,E,F,G = ishodskup(a,b,c,d,e,f)
    nast = ''
    print('\n')
    while nast != 'continue':
        nast = input('Type continue: ')
    print('\n')
    print('Round of 16: ','\n')
    prolaze = osmina(prolaze,A,B,C,D,E,F)
    nast = ''
    print('\n')
    while nast != 'continue':
        nast = input('Type continue: ')
    print('\n')
    print('Quarterfinal: ','\n')
    prolaze = cetvrt(prolaze)
    nast = ''
    print('\n')
    while nast != 'continue':
        nast = input('Type continue: ')
    print('\n')
    print('Semifinal: ','\n')
    prolaze = polu(prolaze)
    nast = ''
    print('\n')
    while nast != 'continue':
        nast = input('Type continue: ')
    print('\n')
    print('Final: ','\n')
    pobjednik = finale(prolaze)

main()    
