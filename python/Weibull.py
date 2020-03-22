import numpy as np
import math as mt
import time as tm

# **********************************************************
def media(c,b):
    '''
    Media apartir dos paramentros c e b
    '''
    return c*mt.gamma(1.e0+1.e0/b)
# **********************************************************

# **********************************************************
def desv(c,b):
    '''
    desvio padrao apartir dos paramentros c e b
    '''
    mu = media(c,b)

    dev = mt.sqrt((c**2)*mt.gamma(1.e0+2.e0/b) - mu**2)  

    return dev
# **********************************************************

# **********************************************************
def get_b_c(mu,sig,tol=1.e-11,maxIt=10000):
    '''
    ***********************************************************
    data criacao:     09/01/2020
    data modificacao: 00/00/0000
    -----------------------------------------------------------
    get_b_c: obtem o b e c dada uma media e um desvio padrao
    -----------------------------------------------------------
    Entrada:
    -----------------------------------------------------------
    mu    - media
    sig   - desvio padrao
    maxIt - numero maximo de iteracoes
    tol   - tolerancia desejada
    -----------------------------------------------------------
    Saida:
    -----------------------------------------------------------
    b e c - 
    -----------------------------------------------------------
    OBS:
    -----------------------------------------------------------
    ***********************************************************
    '''
    def solv(A,x,F):
        '''
        solver do Ax=F
        '''
        x[0] = F[0]/A[0]
        x[1] = F[1]/A[1]
        x[2] = (F[2] - A[3]*x[1])/A[2]

    def MatrizA(A,X):
        '''
        atualizacao da matriz A(x)
        '''
        c = X[0]
        y = X[1]
        x = X[2]

# linha 1
        A[0] = x*mt.gamma(x)   # A11
# linha 2
        A[1] = c*c*mt.gamma(y) # A22
# linha 3  
        A[2] = -2.e0            # A33
        A[3] =  1.e0            # A23

    def VetorF(F,sig,mu):
        '''
        calculo do vetor F
        '''
        F[0] = mu
        F[1] = sig**2 + mu**2
        F[2] = 0.0

    def matvec(A,x):
        '''
        operacao matriz vetor
        '''
        y = np.zeros(3,dtype=np.float64)

        y[0] = A[0]*x[0]
        y[1] = A[1]*x[1]
        y[2] = A[2]*x[2] + A[3]*x[1] 

        return y

# ...
    A = np.zeros(4,dtype=np.float64)
    x = np.zeros(3,dtype=np.float64)
    F = np.zeros(3,dtype=np.float64)

    alf   = 0.5e0
# ... chute inicial
    x[0] = mu     # c
    x[1] = sig/mu # y
    x[2] = 2.e0*x[1] # x

    VetorF(F,sig,mu)


# ... loop
    for i in range(1,maxIt+1):
        MatrizA(A,x)        
# ... residuo
        R = F - matvec(A,x)
# ... ||R||    
        Res = np.linalg.norm(R)
        if  Res < tol:       
            break
# ...
        x0 = np.copy(x)
# ... x = (A^-1)*F
        solv(A,x,F)
# ... update x
        x = alf*x + (1.e0 - alf)*x0 

    print('\n***************************************')
    print('Res final {0} para it {1}'.format(Res,i))
    print('***************************************')

    c = x[0]
    b = 2.e0/x[1]
    
    return b,c
# **********************************************************

# **********************************************************
def main():


#    mu  = float(input('Entre com a media:\n'))
#    sig = float(input('Entre com o desvido padrao:\n'))

    mu  =99884.95e0
    sig =255.84e0

    mu  = 4.0
    sig = 1.0

    time  = tm.time()
    b, c = get_b_c(mu,sig,tol=1e-10,maxIt=1500000)
    time = tm.time() - time

    print('\n***************************************')
    print('Time (s) =',time)
    print('***************************************')


    print('\n***************************************')
    print('c = {0}\nb = {1}'.format(c,b))
    print('***************************************\n')

    mui  = media(c,b)
    sig1 = desv(c,b)
    
    print('***************************************')
    print('mu    = {0}\nmui   = {1}\n|res| = {2}\n'.format(mu ,mui,abs(mu-mui)))
    print('sig   = {0}\nsigi  = {1}\n|res| = {2}\n'.format(sig,sig1,abs(sig-sig1)))
    print('***************************************')
# **********************************************************

main()




