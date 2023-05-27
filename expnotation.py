%matplotlib widget
from IPython.display import display, Latex
from sympy import *
init_printing(use_latex=True)


def nbrexpos(nbr):
    nbr = nbr
    n = Float(str(nbr))
    s = f"{S(StrPrinter({'full_prec': True}).doprint(n)):e}"
    r = Rational(s)
    if nbr == 0 :
        lat = '$0$'
    elif nbr != 0 and isinstance(nbr,int) and nbr < 10:
        lat = '$'+s[0]+'.10^{'+ s.split('e')[1]+'}'+'$'
    else :
        if nbr >0 and nbr < 1 :
            if s.split('e')[0].split('.')[1].rstrip('0') != '':
                lat = '$'+s[0]+','+s.split('e')[0].split('.')[1].rstrip('0')+'.10^{'+ s.split('e')[1]+'}'+'$'
            else :
                lat = '$'+s[0]+s.split('e')[0].split('.')[1].rstrip('0')+'.10^{'+ s.split('e')[1]+'}'+'$'
        else :
            if s.split('e')[0].split('.')[1].rstrip('0') != '':
                lat = '$'+s[0]+ ',' +s.split('e')[0].split('.')[1].rstrip('0')+'.10^{'+ s.split('e')[1]+'}'+'$'
            else :
                lat = '$'+s[0] +s.split('e')[0].split('.')[1].rstrip('0')+'.10^{'+ s.split('e')[1]+'}'+'$'
    return lat, r
            

#display(nbr,n,s,r,Latex(lat))
#display(n,r.evalf(),Latex(lat))
display(nbrexpos(1)[1].evalf(),Latex(nbrexpos(1)[0]))
