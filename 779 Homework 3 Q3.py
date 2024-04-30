import numpy as np
from scipy import constants as const
from qutip import *
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 22})

"Define the wavefunctions as state kets"

psi1=Qobj([[1] , [0]]),
psi2=Qobj([[1/np.sqrt(2)] , [1/np.sqrt(2)]]),
psi3=Qobj([[1/np.sqrt(2)] , [(1/2)*(1+1j)]]),

"Calculate the expectation values"

sigX=expect(sigmax(),psi1)
sigY=expect(sigmay(),psi1)
sigZ=expect(sigmaz(),psi1)

#Construct the vector
sigVec=np.array([sigX,sigY,sigZ])
print("The expectation value with Psi 1 is- "+str(np.round(sigVec,2)))

# psi2
sigX=expect(sigmax(),psi2)
sigY=expect(sigmay(),psi2)
sigZ=expect(sigmaz(),psi2)
#Construct the vector
sigVec=np.array([sigX,sigY,sigZ])
print("The expectation value with Psi 2 is- "+str(np.round(sigVec,2)))

# psi3
sigX=expect(sigmax(),psi3)
sigY=expect(sigmay(),psi3)
sigZ=expect(sigmaz(),psi3)
#Construct the vector
sigVec=np.array([sigX,sigY,sigZ])
print("The expectation value with Psi 3 is- "+str(np.round(sigVec,2)))

#Create a Bloch sphere
b=Bloch()

#Add states
b.add_states([psi1,psi2,psi3])

#Here psi1=green, psi2=yellow, psi3=blue
b.show()

# Constants of the problem
h = 1
g = 2
muB = 1.4e6  # [MHz/Gauss]
Bx = 100  # [Gauss]

# Define the hamiltonian
H = -(1 / 2) * g * muB * (h / (2 * 2 * np.pi)) * Bx * sigmax()

# Calculate the eigenvalues and eigenvectors
eigenData = H.eigenstates()

# Eigenvalues
eigenvalues = eigenData[0]
print('The eigenvalues for H are- ' + str(eigenvalues))

# Eigenvectors
eigenvectors = eigenData[1]
print('Eigenvector 1- ' + str(eigenvectors[0]))
print('Eigenvector 2- ' + str(eigenvectors[1]))


# Magnetic filed strength array
BxArr = np.linspace(1, 1000, 100)

# Array to store the eigenenergies
eigenvalArr = []

# Go over each Bx value
for BxCurr in BxArr:
    # Define the Hamiltonian
    H = -(1 / 2) * g * muB * (h / (2 * 2 * np.pi)) * BxCurr * sigmax()

    # Calculate the eigenvalues and eigenvectors
    eigenData = H.eigenstates()

    # Eigenvalues
    eigenvalues = eigenData[0]

    # Append to the array
    eigenvalArr.append(eigenvalues)

# Convert to numpy
eigenvalArr = np.array(eigenvalArr)

# Plot the data
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(BxArr, eigenvalArr[:, 0] / 1e6, label=r'$\lambda_1$')
ax.plot(BxArr, eigenvalArr[:, 1] / 1e6, label=r'$\lambda_2$')

ax.set_xlabel(r'$B_x$ [Gauss]')
ax.set_ylabel(r'Eigenvalue [MHz]')
ax.set_xlim(0, np.max(BxArr))
ax.legend()
ax.grid(True)
plt.show()














