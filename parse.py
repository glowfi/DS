from typing import TypedDict


class Approach(TypedDict):
    question: str
    tc: str
    sc: str
    intuition: str
    code: str


def parse_file(filename: str) -> dict[str, Approach]:
    with open(filename, "r") as file:
        lines = file.readlines()

    question_lines = []
    approaches: dict[str, Approach] = {}

    current_approach = None
    current_data: Approach = {}
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
            current_data: Approach = {}
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
        current_data["question"] = " ".join(question_lines).strip()
        current_data["intuition"] = "\n".join(intuition_lines).strip()
        current_data["code"] = "\n".join(code_lines).strip()
        approaches[current_approach] = current_data

    return approaches
