'''
Lista 1 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino
'''
'''
# Exercício 1-2
# Um teste de queima foi realizado para determinar a fração volumétrica dos constituintes
# de um compósito de epóxi-fibra de vidro. As seguintes observações foram realizadas:

Peso do recipiente vazio: 47,6504 g.
 Peso do recipiente com um pequeno pedaço do material compósito: 50,1817 g.
 Peso do recipiente com a fibra de vidro depois da queima: 49,4476 g.

1) Calcule as frações de peso e de volume de fibra de vidro no compósito. Assuma que a
densidade da fibra e da resina são iguais a 2,5 e 1,2 g/cm3, respectivamente.

2) Calcule a densidade do compóito do exercício anterior. Se a densidade determinada experimentalmente
foi de 1,86 g/cm3, calcule o volume de vazios no compósito.
'''

W_recipiente = 47.6504
W1 = 50.1817   # recipiente com um pedaço do material compósito
W2 = 49.4476   # Recipiente com fibra após a queima
rho_f= 2.5      # massa específica da fibra (g/cm^3)
rho_r = 1.2    # massa específica da resina (g/cm^3)

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

#exercicio 1
print('Exercício 1:')
print(f'A fração de peso da fibra de vidro é {Rf:.2f} e o volume de fibra é {Vf:.2f} cm^3.')

#exercício 2
print('Exercicio 2:')
print(f'A densidade do compósito é {rho_c:.2f} g/cm^3')

print(f'A razão de vazios é de {Rv:.2f}, com um volume de {Vol_v:.2f} cm^3')