using SpecialFunctions
using LinearAlgebra

#******************************************************************************
function med(c, b)
    return c*gamma(1.e0 + 1.e0/b)
end
#******************************************************************************

#******************************************************************************
function desv(c, b)

    mu = med(c, b)
    dev = (c^2)*gamma(1.e0+2.e0/b) - mu^2
    return sqrt(dev)
end
#******************************************************************************


#******************************************************************************
function get_b_c(mu, sig, tol = 1e-11, maxIt=100000)

    function solv(A, x, F)
        x[1] = F[1]/A[1]
        x[2] = F[2]/A[2]
        x[3] = (F[3] - A[4]*x[2])/A[3]
    end


    function vetorF(F, sig, mu)
        F[1] = mu
        F[2] = mu^2 + sig^2
        F[3] = 0.e0
    end

    function matvec(A, x)
        y1 = A[1]*x[1]
        y2 = A[2]*x[2]
        y3 = A[3]*x[3] + A[4]*x[2]
        return [y1, y2, y3]
    end

    function Matriz(A, x)
# linha 1
         A[1] = x[3]*gamma(x[3])   # A11
# linha 2
         A[2] = (x[1]^2)*gamma(x[2]) # A22
# linha 3
        A[3] =  2.e0               # A33
        A[4] = -1.e0               # A23
    end

# ... inicializado arranjos
    A   = zeros(Float64, 4)
    x   = zeros(Float64, 3)
    F   = zeros(Float64, 3)
    alf = 0.5e0
# ... chute inicial
    x[1] = mu        # c
    x[2] = sig/mu    # y
    x[3] = 2.e00*x[2]  # x
# ...
    vetorF(F, sig, mu)

# ...
    global res, j
    j = 0
    while j < maxIt
# ...
        x0 = copy(x)
# ...
        Matriz(A, x)
# ... residuo
        R = F - matvec(A ,x)
# ... |R*R|
        res = norm(R, 2)
        if res < tol
            break
        end
        j+=1
# ...
        solv(A, x, F)
# ... relaxamento
        x = alf*x + (1.e0 - alf)*x0
    end
# .............................................................................

    println("**********************************************************")
    println("Res final ", res , " para it ", j)
    println("**********************************************************")

# ...
    c = x[1]
    b = 2.0/x[2]

    return b, c
end
#******************************************************************************

#******************************************************************************
function main()

    mu  = 99884.95e0
    sig = 255.84e0

    @timev b, c = get_b_c(mu, sig, 1.e-15, 1500000)

    println("**********************************************************")
    println("c = ", c)
    println("b = ", b)
    println("**********************************************************")

    mui  = med(c, b)
    sigi = desv(c, b)

    println("**********************************************************")
    println("mu    = ", mu)
    println("mui   = ", mui)
    println("|res| = ", abs(mu - mui))
    println()
    println("sig   = ", sig)
    println("sig   = ", sigi)
    println("|res| = ", abs(sig - sigi))
    println("**********************************************************")

end
#******************************************************************************

main()
