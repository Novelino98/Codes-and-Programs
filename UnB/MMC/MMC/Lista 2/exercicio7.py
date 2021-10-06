'''
Lista 2 - Mecânica dos materiais compósitos
Profº Eder Lima de Albuquerque

Aluno - André Luiz Brito Novelino

'''

'''
Dois laminados, um com quatro l^aminas e sequ^encia de empilhamento [45o/0o]S e o segundo com 3
l^aminas e sequ^encia de empilhamento [45o/0o/45o] onde cada l^amina tem 4 mm de espessura tem
a seguinte matriz de rigidez Q. Se Nx = Ny = 4000 N/mm,Nxy =0, Mx=25000 N mm/mm eMy = Mxy = 0, calcule as deformac~oes
no plano medio, as curvaturas e as tens~oes na l^amina.
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

##################################### LAMINADO 4 CAMADAS ##################################


Q=np.array([[30,1,0],[1,3,0],[0,0,1]])
Qs=np.zeros((3,3,4))
thetas=np.array([45, 0, 45, 0])
Qs[:,:,0]=Q
Qs[:,:,1]=Q
Qs[:,:,2]=Q
Qs[:,:,3]=Q

hs=np.array([4,4,4,4])
ABD=calc_ABD2(Qs,thetas,hs)

Nx=4000
Ny=4000
Nxy=0
Mx=25000
My=0
Mxy=0
NM=np.array([Nx, Ny, Nxy, Mx, My, Mxy])
epkappa=np.linalg.inv(ABD).dot(NM)
Qbar45=calc_Qbar(Q,45)
sigma_45=Qbar45.dot(epkappa[0:3])
sigma_0=Q.dot(epkappa[0:3])

epsilonx=epkappa[0]
epsilony=epkappa[1]
gammaxy=epkappa[2]
kappax=epkappa[3]
kappay=epkappa[4]
kappaxy=epkappa[5]


print('LAMINADO DE QUATRO LAMINAS 45º/0ºs')
print('*****************Tensão na lâmina de 0 graus****************')
print(f'Sigma_x = {sigma_0[0]} MPa')
print(f'Sigma_y = {sigma_0[1]} MPa')
print(f'Tau_xy = {sigma_0[2]} MPa')

print('*************Tensão na lâmina de 45 graus**************')
print(f'Sigma_x = {sigma_45[0]} MPa')
print(f'Sigma_y = {sigma_45[1]} MPa')
print(f'Tau_xy = {sigma_45[2]} MPa')

print('*************Deformação do laminado*****************')
print(f'Epsilon_x = {epsilonx}')
print(f'Epsilon_y = {epsilony}')
print(f'Gamma_xy = {gammaxy}')

print('************Curvatura do laminado*************')
print(f'Kappa_x = {kappax}')
print(f'Kappa_y = {kappay}')
print(f'Kappa_xy = {kappaxy}')

##################################### LAMINADO 3 CAMADAS ##################################

Q2=np.array([[30,1,0],[1,3,0],[0,0,1]])
Qs2=np.zeros((3,3,3))
thetas2=np.array([45, 0, 45])
Qs2[:,:,0]=Q2
Qs2[:,:,1]=Q2
Qs2[:,:,2]=Q2

hs2=np.array([4,4,4])
ABD2=calc_ABD2(Qs2,thetas2,hs2)

NM=np.array([Nx, Ny, Nxy, Mx, My, Mxy])
epkappa2=np.linalg.inv(ABD2).dot(NM)
Q2bar45=calc_Qbar(Q2,45)
sigma2_45=Q2bar45.dot(epkappa2[0:3])
sigma2_0=Q2.dot(epkappa2[0:3])

epsilonx2=epkappa2[0]
epsilony2=epkappa2[1]
gammaxy2=epkappa2[2]
kappax2=epkappa2[3]
kappay2=epkappa2[4]
kappaxy2=epkappa2[5]

print('#####################################################################################')
print('LAMINADO DE 3 LAMINAS 45º/0º/45º')
print('*****************Tensão na lâmina de 0 graus****************')
print(f'Sigma_x = {sigma2_0[0]} MPa')
print(f'Sigma_y = {sigma2_0[1]} MPa')
print(f'Tau_xy = {sigma2_0[2]} MPa')

print('*************Tensão na lâmina de 45 graus**************')
print(f'Sigma_x = {sigma2_45[0]} MPa')
print(f'Sigma_y = {sigma2_45[1]} MPa')
print(f'Tau_xy = {sigma2_45[2]} MPa')

print('*************Deformação do laminado*****************')
print(f'Epsilon_x = {epsilonx2}')
print(f'Epsilon_y = {epsilony2}')
print(f'Gamma_xy = {gammaxy2}')

print('************Curvatura do laminado*************')
print(f'Kappa_x = {kappax2}')
print(f'Kappa_y = {kappay2}')
print(f'Kappa_xy = {kappaxy2}')