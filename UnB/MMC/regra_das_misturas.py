"""
# Exercício 1 (revisado)

Um teste de queima foi realizado para determinar a fração volumétrica
dos constituintes de um compósito de epóxi-fibra de vidro.
As seguintes observações foram realizadas:

Peso do recipiente vazio: 47,6504 g.

Peso do recipiente com um pequeno pedaço do material compósito: 50,1817 g.

Peso do recipiente com a fibra de vidro depois da queima: 49,4476 g.

Calcule as frações de peso e de volume de fibra de vidro no compósito.
Assuma que a densidade da fibra e da resina são iguais a 2,5 e 1,2 g/cm$^3$, respectivamente.

"""

W_recipiente = 47.6504
W1 = 50.1817   # recipiente com um pedaço do material compósito
W2 = 49.4476   # Recipiente com fibra após a queima
rho_f= 2.5
rho_r = 1.2

Wc = W1 - W_recipiente
Wf = W2 - W_recipiente

Rf = Wf/Wc  #fração de fibra
Vf = Wf / rho_f

# densidade do composito
rho_c = rho_f*Rf + rho_r*(1-Rf)

# densidade experimental
rho_exp = 1.86  # medido localmente

Rv = (rho_c - rho_exp) / rho_c
Vol_c = Wc * rho_c
Vol_v = Rv* Vol_c

print(f'A fração de peso da fibra de vidro é {Rf:.2f} e o volume de fibra é {Vf:.2f} cm^3.')

print(f'A densidade do compósito é {rho_c:.2f} g/cm^3')

print(f'A razão de vazios é de {Rv:.2f}, com um volume de {Vol_v:.2f} cm^3')

