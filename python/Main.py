import Weibull as wb
import time as tm
# **********************************************************
def main():


#    mu  = float(input('Entre com a media:\n'))
#    sig = float(input('Entre com o desvido padrao:\n'))

    mu  =99884.95e0
    sig =255.84e0

    time  = tm.time()
    b, c = wb.get_b_c(mu,sig,tol=1e-11,maxIt=1500000)
    time = tm.time() - time

    print('\n***************************************')
    print('Time(s) =',time)
    print('***************************************')


    print('\n***************************************')
    print('c = {0}\nb = {1}'.format(c,b))
    print('***************************************\n')

    mui  = wb.media(c,b)
    sig1 = wb.desv(c,b)
    
    print('***************************************')
    print('mu    = {0}\nmui   = {1}\n|res| = {2}\n'.format(mu ,mui,abs(mu-mui)))
    print('sig   = {0}\nsigi  = {1}\n|res| = {2}\n'.format(sig,sig1,abs(sig-sig1)))
    print('***************************************')
# **********************************************************

if(__name__ == "__main__"):
    main()
