
# DFA Simulator
# States: A, B, C, D, E
# Alphabet: 0, 1
# Start State: A
# Final State: E

states = {"A", "B", "C", "D", "E"}
alphabet = {"0", "1"}

start_state = "A"
final_states = {"E"}

# Transition table
transitions = {
    ("A", "0"): "B",
    ("A", "1"): "C",

    ("B", "0"): "B",
    ("B", "1"): "D",

    ("C", "0"): "B",
    ("C", "1"): "C",

    ("D", "0"): "B",
    ("D", "1"): "E",

    ("E", "0"): "B",
    ("E", "1"): "C",
}


def simulate(input_string):
    current_state = start_state

    for symbol in input_string:
        if symbol not in alphabet:
            return False, "Invalid symbol"

        current_state = transitions[(current_state, symbol)]

    if current_state in final_states:
        return True, current_state
    else:
        return False, current_state


# Original inputs from the example
# Additional accepted and rejected inputs
inputs = [
    "0110",    # Original input 1
    "011011",  # Original input 2
    "011",     # Additional: Accepted
    "010"      # Additional: Rejected
]


# Display results
for text in inputs:
    accepted, result = simulate(text)

    if accepted:
        print(f"Input: {text}")
        print(f"Result: ACCEPTED")
        print(f"Final State: {result}\n")
    else:
        print(f"Input: {text}")
        print(f"Result: REJECTED")
        print(f"Final State: {result}\n")