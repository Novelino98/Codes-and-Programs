'''
Lista 1 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino
'''
'''
Exercício 4
Estime EL, ET , GLT e nu_LT (coef poisson principal) para os compósitos de epóxi-fibra de vidro, epóxi-fibra de
carbono, epóxi-Kevlar, alumínio-boro com Vf igual a 25%, 50% e 75%. As propriedades
dos constituintes são dadas abaixo.
'''
''' Resolução '''
Vf = [0.25, 0.5, 0.75]

# Módulo de elasticidade
E_epoxi = 3.5
E_vidro = 70
E_carbono = 250
E_kevlar = 140
E_boro = 350
E_aluminio = 70

#Coeficiente de poisson
nu_epoxi = 0.35
nu_vidro = 0.2
nu_carbono = 0.2
nu_kevlar = 0.2
nu_boro = 0.3
nu_aluminio = 0.33

# Modulo de cisalhamento
G_epoxi = E_epoxi/(2*(1+nu_epoxi))
G_vidro = E_vidro/(2*(1+nu_vidro))
G_carbono = E_carbono/(2*(1+nu_carbono))
G_kevlar = E_kevlar/(2*(1+nu_kevlar))
G_boro = E_boro/(2*(1+nu_boro))
G_aluminio = E_aluminio/(2*(1+nu_aluminio))

############### 1 - Epoxi-fibra de vidro ############################

El1 = []
for i in Vf:
    El1_posicao = (E_vidro*i) + (E_epoxi*(1-i))
    El1.append(El1_posicao)

Et1 = []
epsi = 2  #fibras circulares
Eta_E1 = ((E_vidro/E_epoxi)- 1) / ((E_vidro/E_epoxi)+epsi)

for j in Vf:
    Et1_posicao = E_epoxi*((1+(epsi*Eta_E1*j)) / (1-(Eta_E1*j)))  #Método analítico Halpin-Tsai
    Et1_posicao = round(Et1_posicao, 3)  #arrendodamento 3 casas decimais
    Et1.append(Et1_posicao)

Glt1 = []
epsiG = 1
Eta_G1 = ((G_vidro/G_epoxi)- 1) / ((G_vidro/G_epoxi)+epsiG)
for k in Vf:
    Glt1_posicao = G_epoxi*((1+(epsiG*Eta_G1*k)) / (1-(Eta_G1*k)))  #Método analítico Halpin-Tsai para o mod. de cisalhamento
    Glt1_posicao = round(Glt1_posicao, 3)  # arrendodamento 3 casas decimais
    Glt1.append(Glt1_posicao)

nu_LT1 = []
for l in Vf:
    nu_LT1_posicao = nu_vidro*l + nu_epoxi*(1-l)
    nu_LT1_posicao = round(nu_LT1_posicao, 3) #arredondamento 3 casas decimais
    nu_LT1.append(nu_LT1_posicao)

print('Para o compósito *EPOXI - FIBRA DE VIDRO* temos EL, ET , GLT e nu_LT, '
      'para as concentrações de 25%, 50% e 75% de fibra respectivamente:')
print(f'EL = {El1}- GPa')
print(f'ET = {Et1}- GPa')
print(f'GLT = {Glt1}- GPa')
print(f'nu_LT = {nu_LT1}')

############################# 2- Epoxi-fibra de carbono ################################

El2 = []
for i2 in Vf:
    El2_posicao = (E_carbono*i2) + (E_epoxi*(1-i2))
    El2.append(El2_posicao)

Et2 = []
epsi = 2  #fibras circulares
Eta_E2 = ((E_carbono/E_epoxi)- 1) / ((E_carbono/E_epoxi)+epsi)

for j2 in Vf:
    Et2_posicao = E_epoxi*((1+(epsi*Eta_E2*j2)) / (1-(Eta_E2*j2)))  #Método analítico Halpin-Tsai
    Et2_posicao = round(Et2_posicao, 3)  #arrendodamento 3 casas decimais
    Et2.append(Et2_posicao)

Glt2 = []
Eta_G2 = ((G_carbono/G_epoxi)- 1) / ((G_carbono/G_epoxi)+epsiG)
for k2 in Vf:
    Glt2_posicao = G_epoxi*((1+(epsiG*Eta_G2*k2)) / (1-(Eta_G2*k2)))  #Método analítico Halpin-Tsai para o mod. de cisalhamento
    Glt2_posicao = round(Glt2_posicao, 3)  # arrendodamento 3 casas decimais
    Glt2.append(Glt2_posicao)

nu_LT2 = []
for l2 in Vf:
    nu_LT2_posicao = nu_carbono*l2 + nu_epoxi*(1-l2)
    nu_LT2_posicao = round(nu_LT2_posicao, 3) #arredondamento 3 casas decimais
    nu_LT2.append(nu_LT2_posicao)

print('Para o compósito *EPOXI - FIBA DE CARBONO* temos EL, ET , GLT e nu_LT,'
      'para as concentrações de 25%, 50% e 75% de fibra, respectivamente:')
print(f'EL = {El2}- GPa')
print(f'ET = {Et2}- GPa')
print(f'GLT = {Glt2}- GPa')
print(f'nu_LT = {nu_LT2}')

############################# 3- Epoxi-Kevlar ################################

El3 = []
for i3 in Vf:
    El3_posicao = (E_kevlar*i3) + (E_epoxi*(1-i3))
    El3.append(El3_posicao)

Et3 = []
epsi = 2  #fibras circulares
Eta_E3 = ((E_kevlar/E_epoxi)- 1) / ((E_kevlar/E_epoxi)+epsi)

for j3 in Vf:
    Et3_posicao = E_epoxi*((1+(epsi*Eta_E3*j3)) / (1-(Eta_E3*j3)))  #Método analítico Halpin-Tsai
    Et3_posicao = round(Et3_posicao, 3)  #arrendodamento 3 casas decimais
    Et3.append(Et3_posicao)

Glt3 = []
Eta_G3 = ((G_kevlar/G_epoxi)- 1) / ((G_kevlar/G_epoxi)+epsiG)
for k3 in Vf:
    Glt3_posicao = G_epoxi*((1+(epsiG*Eta_G3*k3)) / (1-(Eta_G3*k3)))  #Método analítico Halpin-Tsai para o mod. de cisalhamento
    Glt3_posicao = round(Glt3_posicao, 3)  # arrendodamento 3 casas decimais
    Glt3.append(Glt3_posicao)

nu_LT3 = []
for l3 in Vf:
    nu_LT3_posicao = nu_kevlar*l3 + nu_epoxi*(1-l3)
    nu_LT3_posicao = round(nu_LT3_posicao, 3) #arredondamento 3 casas decimais
    nu_LT3.append(nu_LT3_posicao)

print('Para o compósito *EPOXI - KEVLAR* temos EL, ET , GLT e nu_LT,'
      'para as concentrações de 25%, 50% e 75% de fibra, respectivamente:')
print(f'EL = {El3} - GPa')
print(f'ET = {Et3} - GPa')
print(f'GLT = {Glt3} - GPa')
print(f'nu_LT = {nu_LT3}')

########################## 4 - Alumínio-Boro ##################################################
El4 = []
for i4 in Vf:
    El4_posicao = (E_boro*i4) + (E_aluminio*(1-i4))
    El4.append(El4_posicao)

Et4 = []
epsi = 2  #fibras circulares
Eta_E4 = ((E_boro/E_aluminio)- 1) / ((E_boro/E_aluminio)+epsi)

for j4 in Vf:
    Et4_posicao = E_aluminio*((1+(epsi*Eta_E4*j4)) / (1-(Eta_E4*j4)))  #Método analítico Halpin-Tsai
    Et4_posicao = round(Et4_posicao, 3)  #arrendodamento 3 casas decimais
    Et4.append(Et4_posicao)

Glt4 = []
Eta_G4 = ((G_boro/G_aluminio)- 1) / ((G_boro/G_aluminio)+epsiG)
for k4 in Vf:
    Glt4_posicao = G_aluminio*((1+(epsiG*Eta_G4*k4)) / (1-(Eta_G4*k4)))  #Método analítico Halpin-Tsai para o mod. de cisalhamento
    Glt4_posicao = round(Glt4_posicao, 3)  # arrendodamento 3 casas decimais
    Glt4.append(Glt4_posicao)

nu_LT4 = []
for l4 in Vf:
    nu_LT4_posicao = nu_boro*l4 + nu_aluminio*(1-l4)
    nu_LT4_posicao = round(nu_LT4_posicao, 3) #arredondamento 3 casas decimais
    nu_LT4.append(nu_LT4_posicao)

print('Para o compósito *ALUMÍNIO - BORO* temos EL, ET , GLT e nu_LT,'
      'para as concentrações de 25%, 50% e 75% de fibra, respectivamente:')
print(f'EL = {El4} - GPa')
print(f'ET = {Et4} - GPa')
print(f'GLT = {Glt4} - GPa')
print(f'nu_LT = {nu_LT4}')