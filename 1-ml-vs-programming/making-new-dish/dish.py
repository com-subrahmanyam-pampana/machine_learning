
import random

def make_new_dish():
    # Initial ingredients (simulating a starting recipe)
    ingredients = ['salt', 'pepper', 'garlic', 'chicken', 'tomato']
    
    # Simulate a feedback loop where the dish changes after each attempt
    feedback = ['too salty', 'too bland', 'perfect', 'too spicy', 'too sour']
    attempts = 0
    
    while attempts < 5:  # Allow up to 5 attempts to improve the dish
        attempts += 1
        print(f"Attempt {attempts}: Using ingredients {ingredients}")

        # Randomly simulate feedback after making the dish
        current_feedback = random.choice(feedback)
        print(f"Feedback: {current_feedback}")

        # Adjust the ingredients based on feedback
        if current_feedback == 'too salty':
            ingredients.remove('salt')
        elif current_feedback == 'too bland':
            ingredients.append('spices')
        elif current_feedback == 'too spicy':
            ingredients.remove('garlic')
        elif current_feedback == 'too sour':
            ingredients.remove('tomato')
        elif current_feedback == 'perfect':
            print("Dish is perfect!")
            break

        print()  # Just to separate attempts

    if attempts == 5:
        print("Max attempts reached. Final ingredients:", ingredients)
        print("Dish is ready, but might need further adjustments.")
    
# Call the function to make a new dish
make_new_dish()




# Explanation:
# This program simulates the process of learning and experimenting, similar to AI/ML.

# Initially, we have a list of ingredients for the dish, and the program "learns" from feedback (like a model would learn from data).

# Each time the program runs, it adjusts the ingredients based on feedback, simulating how a machine learning model might adjust its parameters to improve.

# The goal is to get "perfect" feedback, which would stop the loop—just like an AI model finding the optimal solution after enough iterations.