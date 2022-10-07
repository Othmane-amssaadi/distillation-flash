Z1 = 0.1
Z2 = 0.2
Z3 = 0.3
Z4 = 0.4
Tf = 200
Pf = 100
F = 100
K1 = 4.2
K2 = 1.75
K3 = 0.74
K4 = 0.34
xi = 0.66
epsilon = 0.001

def RR (Z1, Z2, Z3,Z4, K1, K2, K3, K4):
    result = ((Z1*(1-K1))/(1+xi*(K1-1)))+((Z2*(1-K2))/(1+xi*(K2-1)))+((Z3*(1-K3))/(1+xi*(K3-1)))+((Z4*(1-K4))/(1+xi*(K4-1)))
    return result

def RRD (Z1, Z2, Z3, Z4, K1, K2, K3, K4):
    result = ((Z1*pow(1-K1, 2))/(pow(1+xi*(K1-1), 2)))+((Z2*pow(1-K2, 2))/(pow(1+xi*(K2-1), 2)))+((Z3*pow(1-K3, 2))/(pow(1+xi*(K3-1), 2)))+((Z4*pow(1-K4, 2))/(pow(1+xi*(K4-1), 2)))
    return result

Objfunction = RR(Z1, Z2, Z3, Z4, K1, K2, K3, K4)
while Objfunction>=epsilon:
    xi = xi-((RR(Z1, Z2, Z3, Z4, K1, K2, K3, K4))/(RRD(Z1, Z2, Z3, Z4, K1, K2, K3, K4)))
    Objfunction = RR(Z1, Z2, Z3, Z4, K1, K2, K3, K4)
print ("value of xi is =", xi)
print("result of Rachford-Rice equation is =", Objfunction)