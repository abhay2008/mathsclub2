def get_coefficients_from_equation(equation):
    # Split the equation into terms
    terms = equation.split()

    # Initialize coefficients
    a = b = c = 0
    sign = 1  # To keep track of the sign of the constant term

    # Parse the terms to extract coefficients
    for term in terms:
        if 'x' in term:
            a_str = term.replace('x', '')
            a = int(a_str) if a_str and a_str not in {'-', '+'} else 1
            if term.startswith('-'):
                a *= -1
        elif 'y' in term:
            b_str = term.replace('y', '')
            b = int(b_str) if b_str and b_str not in {'-', '+'} else 1
            if term.startswith('-'):
                b *= -1
        elif '=' in term:
            continue
        else:
            if term.startswith('-'):
                sign = -1
            elif term.startswith('+'):
                sign = 1
            else:
                c += sign * int(term)

    return a, b, c

def solve_linear_system():
    # Get equations from the user
    equation1 = input("\033[1;34mEnter the first equation in the form ax + by + c = 0: \033[0m")
    equation2 = input("\033[1;34mEnter the second equation in the form ax + by + c = 0: \033[0m")

    # Extract coefficients from the equations
    a1, b1, c1 = get_coefficients_from_equation(equation1)
    a2, b2, c2 = get_coefficients_from_equation(equation2)

    # Calculate the determinant
    determinant = a1 * b2 - a2 * b1

    # Check if the system of equations is solvable
    if determinant == 0:
        return None  # No unique solution

    # Calculate the values of x and y using the cross-multiplication formula
    x = (b1 * c2 - b2 * c1) // determinant
    y = (a2 * c1 - a1 * c2) // determinant

    # Print the steps of the calculation
    print("\033[1;32mCalculation Steps:\033[0m")
    print(f"\033[1;32mDeterminant (\u0394) = a1 * b2 - a2 * b1 = {a1} * {b2} - {a2} * {b1} = {determinant}\033[0m")
    print(f"\033[1;32mCross-Multiplication Formula:\033[0m")
    print(f"\033[1;32mx = (\u0394x) / \u0394 = (b1 * c2 - b2 * c1) / {determinant} = ({b1} * {c2} - {b2} * {c1}) / {determinant} = {x}\033[0m")
    print(f"\033[1;32my = (\u0394y) / \u0394 = (a2 * c1 - a1 * c2) / {determinant} = ({a2} * {c1} - {a1} * {c2}) / {determinant} = {y}\033[0m")

    return x, y

# Example usage:
solution = solve_linear_system()

if solution:
    print("\033[1;35mThe solution is x = {}, y = {}\033[0m".format(solution[0], solution[1]))
else:
    print("\033[1;31mThe system of equations has no unique solution.\033[0m")
