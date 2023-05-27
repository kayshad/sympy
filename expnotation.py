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
    return lat
            


def shownbr(i,nbr):
    nbr = nbr
    n = Float(str(nbr))
    s = f"{S(StrPrinter({'full_prec': True}).doprint(n)):e}"
    r = Rational(s)
    cte = f"{S(StrPrinter({'full_prec': True}).doprint(Float(nbr))):e}".split('.')[0]
    if nbr != 0 :
        ctm = f"{S(StrPrinter({'full_prec': True}).doprint(Float(nbr))):e}".split('.')[1].split('e')[0].rstrip('0')
        noe = f"{S(StrPrinter({'full_prec': True}).doprint(Float(nbr))):e}".split('.')[1].split('e')[1]
        if ctm == '':
            s = "${}{}e{}$".format(latex(cte), latex(ctm),latex(noe)) 
        else :
            s = "${}.{}e{}$".format(latex(cte), latex(ctm),latex(noe))
    else :
        s = '$0$'
    display(i, Latex(nbrexpos(nbr)))


    
malist = [S(f"{S(StrPrinter({'full_prec': True}).doprint(1e7*(1-1e-7)**i)):e}") for i in range(21)]


for i  in range(21) :
    shownbr(i,malist[i])
