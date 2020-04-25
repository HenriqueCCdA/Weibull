import ctypes as ct

class Weibull_C():

    def __init__(self, path_lib = './weibull/Weibull_C.dll'):
        self.__lib = ct.cdll.LoadLibrary(path_lib)
        # parametros da funcao media
        self.__lib.media.argtypes = [ct.c_double, ct.c_double]
        self.__lib.media.restype = ct.c_double
        # parametros da funcao variancia
        self.__lib.var.argtypes = [ct.c_double, ct.c_double]
        self.__lib.var.restype = ct.c_double

        # parametros da funcao desviao padrao
        self.__lib.std.argtypes = [ct.c_double, ct.c_double]
        self.__lib.std.restype = ct.c_double

        # parametros da weibull
        self.__lib.weibull.argtypes = [ ct.c_double,
                                        ct.c_double,
                                        ct.POINTER(ct.c_double),
                                        ct.POINTER(ct.c_double),
                                        ct.c_double,
                                        ct.c_int,
                                        ct.c_double]
        self.__lib.weibull.restype = None

    def media(self, b, c):
        '''
        ****************************************************************
        data de criacao  : 25/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        Media : Cacula a media
        ----------------------------------------------------------------
        paremetros de enrada:
        ----------------------------------------------------------------
        b -> valor
        c -> valor
        ----------------------------------------------------------------
        retorno: a media de de a calculada
        ----------------------------------------------------------------
        ****************************************************************
        '''
        b_c = ct.c_double(b)
        c_c = ct.c_double(c)
        res = self.__lib.media(b_c, c_c)
        return res        
    
    def var(self, b, c):
        '''
        ****************************************************************
        data de criacao  : 25/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        Var : Cacula a variancia
        ----------------------------------------------------------------
        paremetros de enrada:
        ----------------------------------------------------------------
        b -> valor
        c -> valor
        ----------------------------------------------------------------
        retorno: variania de de a calculada
        ----------------------------------------------------------------
        OBS:
        ----------------------------------------------------------------
        ****************************************************************
        '''

        # ... convertendo para o formato ctypes
        b_c = ct.c_double(b)
        c_c = ct.c_double(c)
        # ... chamando a funcao
        res = self.__lib.var(b_c, c_c)

        return res 
    
    
    def std(self, b, c):
        '''
        ****************************************************************
        data de criacao  : 25/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        std : Cacula o desvio padrao  de a
        ----------------------------------------------------------------
        paremetros de enrada:
        ----------------------------------------------------------------
        b -> valor
        c -> valor
        ----------------------------------------------------------------
        retorno: variania de de a calculada
        ----------------------------------------------------------------
        OBS:
        ****************************************************************
        '''

        # ... convertendo para o formato ctypes
        b_c = ct.c_double(b)
        c_c = ct.c_double(c)
        # ... chamando a funcao
        res = self.__lib.std(b_c, c_c)

        return res

    def weibul_get_b_c(self, mu, sig
                       , tol = 1.e-11
                       , max_iter = 5000
                       , alf = 0.5e0):
        '''
        ****************************************************************
        data de criacao  : 25/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        weibull : caclulo de b e c apartir de mu e sig
        ----------------------------------------------------------------
        paremetros de enrada:
        ----------------------------------------------------------------
        mu       -> media
        sig      -> desvio padrao
        tol      -> tolerancia
        max_iter -> numero maximo de iteracoes no algoritimo nao linear
        alf      -> paramentro de relaxamento
        ----------------------------------------------------------------
        retorno: (b, c)
        ----------------------------------------------------------------
        OBS:
        ****************************************************************
        '''

        # ... convertendo para o formato ctypes
        mu_c       = ct.c_double(mu)
        sig_c      = ct.c_double(sig)
        tol_c      = ct.c_double(tol)
        max_iter_c = ct.c_int(max_iter)
        alf_c      = ct.c_double(alf)
        b_c       = ct.c_double()
        c_c       = ct.c_double()
        # ... chamando a funcao
        self.__lib.weibull(mu_c , sig_c,
                       ct.byref(b_c), ct.byref(c_c),
                       tol_c, max_iter_c,
                       alf_c)

        return (b_c.value, c_c.value)


