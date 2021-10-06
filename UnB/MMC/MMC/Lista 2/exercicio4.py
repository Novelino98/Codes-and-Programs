'''
Lista 2 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''
'''
exercicio 4
Um corpo de prova para um ensaio de tracao de um composito unidirecional com secao transversal
retangular de dimens~oes 12,5 mm x 4 mm tem as fibras orientadas a 45o com o eixo longitudinal
do corpo de prova. A forca axial aplicada no corpo de prova e de 500 N. Calcule as deformacoes
normais nas direcoes axial e perpendicular do corpo de prova. As propriedades do corpo de prova
s~ao: EL = 14 GPa, ET = 3,5 GPa, GLT = 4,2 GPa e nu_LT = 0,4.
'''
import numpy as np

def  calc_T(theta):
    # Calcula a matriz de transformação
    theta = theta*np.pi/180
    m = np.cos(theta)
    n = np.sin(theta)
    T = np.array([[m**2,n**2,2*m*n],
         [n**2,  m**2,  -2*m*n],
        [-m*n,  m*n , m**2-n**2]])
    return T
def  calc_Qbar(Q,theta):
    # Entre  com theta em graus
    T = calc_T(theta)
    Qbar = np.linalg.inv(T).dot(Q.dot(np.transpose(np.linalg.inv(T))))
    return Qbar

def calc_Q(EL,ET,GLT,nuLT):
    nuTL = nuLT*ET/EL# Coeficiente de Poisson secundário
    Q11 = EL/(1-nuLT*nuTL)
    Q22 = ET/(1-nuLT*nuTL)
    Q66 = GLT
    Q16 = 0
    Q26 = 0
    Q12 = nuTL*EL/(1-nuLT*nuTL)
    Q = np.array([[Q11, Q12, Q16],
         [Q12, Q22, Q26],
         [Q16, Q26, Q66]])
    return  Q

# Tensões atuantes nas lâminas

# Tensões atuantes na lâmina
F = 500 #N
A = (12.5e-3)*(4e-3)
sigx= F/A
sigy=0
tauxy=0
tensoesxy=np.array([sigx,sigy,tauxy]) # vetor que contém as 3 componentes de tensões

# Propriedades elásticas da lâmina
EL=14e9
nuLT=0.4
ET=3.5e9
GLT=4.2e9

# ângulo de inclinação das fibras
theta=45

# Calcula as tensões sigL, sigT e tauLT
T=calc_T(theta)
tensoesLT=T.dot(tensoesxy)
sigL=tensoesLT[0]
sigT=tensoesLT[1]
tauLT=tensoesLT[2]

# Calcula as deformações epsilonL, epsilonT e gammaLT
Q=calc_Q(EL,ET,GLT,nuLT)
defLT=np.linalg.inv(Q).dot(tensoesLT)
epsilonL=defLT[0]
epsilonT=defLT[1]
gammaLT=defLT[2]

# Calcula as deformações epsilonx, epsilony e gammaxy
# Primeira forma de cálculo
Qbar=calc_Qbar(Q,theta)
defxy=np.linalg.inv(Qbar).dot(tensoesxy)
epsilonx=defxy[0]
epsilony=defxy[1]
gammaxy=defxy[2]


print(f'Epsilon_x = {round(epsilonx, 5)}')
print(f'Epsilon_y = {round(epsilony, 5)}')
print(f'Gamma_xy = {round(gammaxy, 5)}')