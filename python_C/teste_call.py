import weibull.weibull_C as wb

lib = wb.Weibull_C()

b = 10
c = 2

mu  = lib.media(b, c)
var = lib.var(b, c)
std = lib.std(b, c)

print('Media         :', mu )
print('Variancia     :', var)
print('Desvio padrao :', std)

print (lib.weibul_get_b_c(mu, std))