import matplotlib.pyplot as plt
from math import pi
from qiskit import QuantumCircuit

circuits = []
for i in range(3):
    c = QuantumCircuit(2, name='circuit%d'%i)
    c.h(0); c.cx(0,1)# Bell state
    circuits.append(c)

# rotate direction of measurements
circuits[0].ry( pi, 0)
circuits[1].ry(-pi, 1)
circuits[2].ry( pi, 0)
circuits[2].ry(-pi, 1)
for c in circuits: c.measure_all()

for c in circuits:
    ax = plt.figure().add_subplot()
    c.draw('mpl', ax=ax)

counts = [result.get_counts(c) for c in circuits]
Q = [(c['01'] + c['10'])/shots for c in counts]
bell = Q[0] + Q[1] - Q[2] # LHS-RHS of inequality
print(counts)
print('Q_1 + Q_2 - Q_3 =', bell)
if bell > 2: print("Bell's inequality violated")
