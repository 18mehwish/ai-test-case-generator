import json

def generate_test_cases(feature_description):
    test_cases = []

    # Basic logic (can later upgrade with AI APIs)
    test_cases.append({
        "type": "Positive",
        "description": f"Valid input for: {feature_description}",
        "expected": "System works correctly"
    })

    test_cases.append({
        "type": "Negative",
        "description": f"Invalid input for: {feature_description}",
        "expected": "System handles error"
    })

    test_cases.append({
        "type": "Edge Case",
        "description": f"Boundary condition for: {feature_description}",
        "expected": "System remains stable"
    })

    return test_cases


if __name__ == "__main__":
    feature = input("Enter feature description: ")
    cases = generate_test_cases(feature)

    print("\nGenerated Test Cases:\n")
    print(json.dumps(cases, indent=4))
