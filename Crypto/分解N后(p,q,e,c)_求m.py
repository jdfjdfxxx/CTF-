import gmpy2
import libnum

p=
q=
e=
c=

n=p*q
phi_n=(p-1)*(q-1)

#求逆元
#d=libnum.invmod(e,phi_n)
d=gmpy2.invert(e,phi_n)

m=pow(c,d,n)
print(m)
print(libnum.n2s(int(m)).decode())