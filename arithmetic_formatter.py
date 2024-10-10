def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems
    
    operations = list(map(lambda x: x.split()[1], problems))

    if set(operations) != {'+', '-'} and len(set(operations)) != 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems
    
    numbers = []
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = 'Error: Numbers must contain only digits.'
        return arranged_problems
    
    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Errors: Numbers cannot be more than four digits."
        return arranged_problems
    
    top_part = ''
    dashes = ''
    results = list(map(lambda x: eval(x), problems))
    solutions = ''

    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_part += numbers[i].rjust(space_width)
        dashes += '_' * space_width
        solutions += str(results[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_part += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_part = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_part += operations[i // 2]
        bottom_part += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_part += ' ' * 4

    if show_answers:
        arranged_problems = '\n'.join((top_part, bottom_part, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_part, bottom_part, dashes))
    return arranged_problems
        
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))