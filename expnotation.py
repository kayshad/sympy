%matplotlib widget
from IPython.display import display, Latex
from sympy import *
init_printing(use_latex=True)
from sympy.printing.str import StrPrinter
nbr = 1000.0023500814000
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
            

#display(nbr,n,s,r,Latex(lat))
display(n,r.evalf(),Latex(lat))