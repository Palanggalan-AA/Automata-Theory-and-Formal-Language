# C-STYLE COMMENT RECOGNIZER

def dfa(input_string):
    state = "q0"

    for symbol in input_string:

        if state == "q0":
            state = "q1" if symbol == "/" else "dead"

        elif state == "q1":
            state = "q2" if symbol == "*" else "dead"

        elif state == "q2":
            state = "q3" if symbol == "*" else "q2"

        elif state == "q3":
            if symbol == "/":
                state = "q4"
            elif symbol == "*":
                state = "q3"
            else:
                state = "q2"

        elif state == "q4":
            state = "dead"

        if state == "dead":
            return False

    return state == "q4"


# Test Cases
tests = [
    ("/*a*/", "Accepted"),
    ("/**/", "Accepted"),
    ("/***/", "Accepted"),
    ("/*aaa*aaa*/", "Accepted"),
    ("/*a*a*/", "Accepted"),
    ("/**", "Rejected"),
    ("/*/a/*aaa*/", "Rejected"),
    ("aaa/**/a", "Rejected"),
    ("/*/", "Rejected"),
    ("/**a/", "Rejected"),
    ("//aaaa", "Rejected")
]


# Display Results
print("=" * 65)
print("        C-STYLE COMMENT RECOGNIZER (AUTOMATON)")
print("=" * 65)

print(f"{'Input String':<25} | {'Result':<12} | Evaluation")
print("-" * 65)

for string, expected in tests:
    result = "ACCEPTED" if dfa(string) else "REJECTED"
    print(f"{string:<25} | {result:<12} | Expected: {expected}")


# User Input
print("\n" + "=" * 65)

user_input = input("Enter your own string to test: ")

result = "ACCEPTED" if dfa(user_input) else "REJECTED"

print(f'Input: "{user_input}" -> Status: {result}')