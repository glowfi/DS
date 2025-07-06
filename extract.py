import json


def parse_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    difficulty = ""
    question_lines = []
    approaches = {}

    current_approach = None
    current_data = {}
    code_lines = []
    intuition_lines = []
    in_question = False
    in_intuition = False
    in_code = False

    approach_headers = [
        "Recursion",
        "Memoization",
        "Tabulation",
        "Space Optimized",
        "Brute",
        "Better",
        "Optimal",
    ]

    for _, line in enumerate(lines):
        stripped = line.strip()

        # Get difficulty
        if stripped.startswith("#") and any(
            d in stripped for d in ["Easy", "Medium", "Hard"]
        ):
            difficulty = stripped.replace("#", "").strip()

        # Start capturing question
        if stripped == "# Question":
            in_question = True
            continue

        # Stop capturing question at first approach
        if in_question and any(
            f"# {header}" in stripped for header in approach_headers
        ):
            in_question = False

        if in_question:
            question_lines.append(stripped.lstrip("#").strip())

        # Detect approach start
        if any(stripped == f"# {header}" for header in approach_headers):
            # Save previous approach if any
            if current_approach:
                current_data["intuition"] = " ".join(intuition_lines).strip()
                current_data["code"] = "\n".join(code_lines).strip()
                approaches[current_approach] = current_data

            # Reset for new approach
            current_approach = stripped.replace("#", "").strip()
            current_data = {}
            code_lines = []
            intuition_lines = []
            in_intuition = False
            in_code = False
            continue

        # Capture T.C. and S.C.
        if stripped.startswith("# T.C."):
            current_data["tc"] = stripped.split("-")[-1].strip()
        elif stripped.startswith("# S.C"):
            current_data["sc"] = stripped.split("-")[-1].strip()

        # Start capturing intuition
        elif stripped.startswith("# Intuition"):
            in_intuition = True
            in_code = False
            continue

        # Switch from intuition to code when code starts
        elif in_intuition and (
            stripped.startswith("class ") or stripped.startswith("def ")
        ):
            in_intuition = False
            in_code = True

        # Collect intuition
        if in_intuition:
            intuition_lines.append(stripped.lstrip("#").strip())

        # Collect code
        if in_code:
            code_lines.append(line.rstrip())

    # Save last approach
    if current_approach:
        current_data["intuition"] = " ".join(intuition_lines).strip()
        current_data["code"] = "\n".join(code_lines).strip()
        approaches[current_approach] = current_data

    # Final structured output
    result = {
        "difficulty": difficulty,
        "question": " ".join(question_lines).strip(),
        "approaches": approaches,
    }

    return result


# Example usage
parsed_data = parse_file(
    "/home/ayush/cdx/DS/Programs/python/3_String/2_Reverse_words_in_a_given_string.py"
)

# Save to JSON file
with open("output.json", "w") as f:
    json.dump(parsed_data, f, indent=4)

print("✅ Fixed and saved to output.json")
