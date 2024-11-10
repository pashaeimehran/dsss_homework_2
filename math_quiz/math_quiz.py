import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between the specified min and max values.
    Parameters:
    min_value (int): The minimum value of the range.
    max_value (int): The maximum value of the range.
    Returns:
    int: A random integer between min_value and max_value (inclusive).
    """
    try:
        return random.randint(min_value, max_value)
    except ValueError:
        print("Error: Invalid range values.")
        return None

def generate_random_operator():
    """
    Randomly selects one of the three basic arithmetic operators: '+', '-', or '*'.
    Returns:
    str: A randomly chosen arithmetic operator.
    """
    try:
        return random.choice(['+', '-', '*'])
    except IndexError:
        print("Error: No operators available.")
        return None

def calculate_expression(num1, num2, operator):
    """
    Calculates the result of an arithmetic expression based on the two numbers and operator.
    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    operator (str): The operator for the arithmetic operation ('+', '-', or '*').
    Returns:
    tuple: A tuple containing the problem string (str) and the result (int or float).
    """
    try:
        problem = f"{num1} {operator} {num2}"
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        else:
            raise ValueError("Invalid operator.")
        return problem, result
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

def math_quiz():
    """
    Starts the math quiz game, asks the user math questions, and tracks the score.
    The game consists of presenting a few random math problems, where the user has to provide the correct answers.
    After answering each question, the user's score is updated and displayed at the end.
    """
    score = 0
    total_questions = 5  # Set the number of questions for the quiz.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # Ensure num2 is an integer
        operator = generate_random_operator()

        if num1 is None or num2 is None or operator is None:
            print("Error generating the question. Please try again.")
            break

        # Calculate the problem and expected answer
        problem, correct_answer = calculate_expression(num1, num2, operator)
        if problem is None:
            print("Error in generating the question. Try again later.")
            break

        print(f"\nQuestion: {problem}")

        # Input and validate user answer
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
