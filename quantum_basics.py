"""
Basic Quantum Computing Examples
This file contains simple examples of quantum computing concepts
"""

def create_bell_state():
    """
    Creates a Bell state (maximally entangled qubits)
    """
    # Pseudocode for demonstration
    # In practice, you would use a quantum computing framework like Qiskit
    print("Creating Bell state:")
    print("1. Initialize two qubits to |0⟩")
    print("2. Apply Hadamard gate to first qubit")
    print("3. Apply CNOT gate with first qubit as control")
    print("Result: (|00⟩ + |11⟩)/√2")

def quantum_teleportation():
    """
    Demonstrates quantum teleportation protocol
    """
    print("Quantum Teleportation Protocol:")
    print("1. Create Bell pair")
    print("2. Perform Bell measurement")
    print("3. Transmit classical bits")
    print("4. Apply correction operations")

if __name__ == "__main__":
    create_bell_state()
    quantum_teleportation()