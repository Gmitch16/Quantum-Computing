from qiskit import QuantumCircuit, assemble, Aer
from qiskit import transpile
from math import pi, sqrt
from qiskit.visualization import plot_bloch_multivector, plot_histogram
sim = Aer.get_backend('aer_simulator')

# Let's do an X-gate on a |0> qubit
qc = QuantumCircuit(9)
qc.mct([0, 1, 2, 3, 4], 5, [6, 7, 8],  mode='v-chain')
qc.draw()

transpile(qc,basis_gates=['cx','u']).count_ops()['cx']








