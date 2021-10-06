'''
Lista 2 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''

'''
Um laminado cruzado balanceado possui um plano medio de simetria e suas laminas tem as seguintes
propriedades elasticas: EL = 15 GPa, ET = 6 GPa, GLT = 3 GPa e nuLT = 0,5. O laminado
e sujeito a una carga normal Nx = 15000 N/mm e de cisalhamento de Nxy = 1000 N/mm. Cada
camada tem 3 mm de espessura. Calcule as tensoes normais sigma_L e sigma_T e de cisalhamento Tau_LT nas
laminas de 0o e 90o.
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

EL = 15e9
ET = 6e9
nuLT = 0.5
GLT = 3e9

Q=calc_Q(EL,ET,GLT,nuLT)
Qs=np.zeros((3,3,2))
thetas=np.array([0, 90])
Qs[:,:,0]=Q
Qs[:,:,1]=Q
hs=np.array([3,3])
ABD=calc_ABD2(Qs,thetas,hs)

Nx=15000
Ny=0
Nxy=1000
Mx=0
My=0
Mxy=0
NM=np.array([Nx, Ny, Nxy, Mx, My, Mxy])
epkappa=np.linalg.inv(ABD).dot(NM)
Qbar90=calc_Qbar(Q,90)
sigma_90=Qbar90.dot(epkappa[0:3])
sigma_0=Q.dot(epkappa[0:3])

print('Para a lâmina de 0 graus:')
print(f'Sigma_L = {sigma_0[0]} MPa')
print(f'Sigma_T = {sigma_0[1]} MPa')
print(f'Tau_LT = {sigma_0[2]} MPa')

print('Para a lâmina de 90 graus:')
print(f'Sigma_L = {sigma_90[1]} MPa')
print(f'Sigma_T = {sigma_90[0]} MPa')
print(f'Tau_LT = {sigma_90[2]} MPa')