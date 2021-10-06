'''
Lista 2 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''
'''
Determine as matrizes A, B e D para uma tira bimetalica de aluminio, com 5 mm de espessura
cada camada. Mostre como esta tira se deforma quando carregada sob tracao uniaxial. Considere
Eaco = 210 GPa, EAl = 70 GPa e nu_aco = nu_Al = 0. 29.
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
    # Calcula a matriz de rigidez da lâmina no sistema xy
    # Entre  com theta em graus
    T = calc_T(theta)
    Qbar = np.linalg.inv(T).dot(Q.dot(np.transpose(np.linalg.inv(T))))
    return Qbar

def calc_Q(EL,ET,GLT,nuLT):
    # Calcula a matriz de rigidez da lâmina no sistema LT
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


def calc_ABD(Material):
    n_laminae=Material.shape[0]
    thickness=np.sum(Material,0)[4]
    hant=-thickness/2
    A=np.zeros((3,3))
    B=np.zeros((3,3))
    D=np.zeros((3,3))
    for i in range(n_laminae):
        EL=Material[i,0]
        ET=Material[i,1]
        GLT=Material[i,2]
        nuLT=Material[i,3]
        h = Material[i,4]
        theta=Material[i,5]
 #       nuTL=nuLT*ET/EL
        Q=calc_Q(EL,ET,GLT,nuLT)
        Qbar=calc_Qbar(Q,theta)
        A=A+Qbar*((h+hant)-hant)
        B=B+1/2*Qbar*((h+hant)**2-hant**2)
        D=D+1/3*Qbar*((h+hant)**3-hant**3)
        hant=hant+h
    AB= np.concatenate((A,B),axis=0)
    BD= np.concatenate((B,D),axis=0)
    ABD=np.concatenate((AB,BD),axis=1)
    return ABD


def calc_ABD2(Qs,thetas,hs):
    n_laminae=len(hs)
    thickness=np.sum(hs)
    hant=-thickness/2
    A=np.zeros((3,3))
    B=np.zeros((3,3))
    D=np.zeros((3,3))
    for i in range(n_laminae):
        Q=Qs[:,:,i]
        Qbar=calc_Qbar(Q,thetas[i])
        A=A+Qbar*((hs[i]+hant)-hant)
        B=B+1/2*Qbar*((hs[i]+hant)**2-hant**2)
        D=D+1/3*Qbar*((hs[i]+hant)**3-hant**3)
        hant=hant+hs[i]
    AB= np.concatenate((A,B),axis=0)
    BD= np.concatenate((B,D),axis=0)
    ABD=np.concatenate((AB,BD),axis=1)
    return ABD


Eaco = 210e9
Eal = 70e9
nuaco = 0.29
nual = 0.29
Gaco = Eaco/(2*(1+nuaco))
Gal = Eal/(2*(1+nual))

Qaco=calc_Q(Eaco,Eaco,Gaco,nuaco)
Qal=calc_Q(Eal,Eal,Gal,nual)
Qs=np.zeros((3,3,2))
thetas=np.array([0, 0])
Qs[:,:,0]=Qaco
Qs[:,:,1]=Qal
hs=np.array([5,5])
ABD=calc_ABD2(Qs,thetas,hs)
A=ABD[0:3,0:3]
B=ABD[0:3,3:6]
D=ABD[3:6,3:6]

print('A matriz A é dada por:')
print(A)
print('A matriz B é dada por:')
print(B)
print('A matriz D é dada por:')
print(D)



