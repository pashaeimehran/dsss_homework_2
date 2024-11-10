import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between the minimum and maximum values.
    
    Args:
        min_value (int): The minimum integer value.
        max_value (int): The maximum integer value.
    
    Returns:
        int: A random integer within the given range.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Randomly select a math operator (+, -, *) for use in a math problem.
    
    Returns:
        str: A randomly selected operator from ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Create a math problem based on two numbers and an operator.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): The operator.
    
    Returns:
        tuple: A tuple containing the math problem as a string and the correct answer as an integer.
    """
    problem = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # operator == '*'
        answer = num1 * num2

    return problem, answer

def math_quiz():
    """
    Run the Math Quiz game, presenting the user with math problems and calculating their score.
    """
    score = 0
    total_questions = 5  # Define the number of questions per quiz
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for _ in range(total_questions):
        # Generate two random numbers and a random operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        # Create a math problem and retrieve the correct answer
        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            # Get user answer and check if it is correct
            user_answer = int(input("Your answer: "))
            
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
