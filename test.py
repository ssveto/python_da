def arithmetic_arranger(problems, show_answers=False):
    """Arranges arithmetic problems vertically and side-by-side.

    Args:
        problems: A list of strings representing arithmetic problems.
        show_answers: A boolean indicating whether to display answers.

    Returns:
        A formatted string representing the arranged problems.
    """

    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    answers = []

    for problem in problems:
        operator, operands = problem.split()
        operand1, operand2 = operands.split()

        width = max(len(operand1), len(operand2)) + 2

        arranged_problems.append(f"{operand1.rjust(width)} {operator} {operand2.rjust(width)}")
        if show_answers:
            result = eval(problem)
            answers.append(f"{str(result).rjust(width)}")

    arranged_problems = "\n".join(arranged_problems)
    if show_answers:
        answers = "\n".join(answers)
        return f"{arranged_problems}\n{'-' * len(arranged_problems)}\n{answers}"
    else:
        return arranged_problems

# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems, True)
print(result)