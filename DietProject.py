# Importing necessary libraries
import random

# Sample data for workout and diet plans
workout_data = {
    "weight_loss": [
        "30 minutes of cardio (running, cycling)",
        "15 minutes of HIIT",
        "Core exercises: planks, crunches, mountain climbers"
    ],
    "muscle_gain": [
        "30 minutes of strength training (push-ups, pull-ups, squats)",
        "Upper body weight training",
        "Lower body weight training"
    ],
    "flexibility": [
        "30 minutes of yoga",
        "15 minutes of stretching exercises",
        "Pilates session"
    ]
}

diet_data = {
    "weight_loss": [
        "Breakfast: Smoothie with spinach, banana, and protein powder",
        "Lunch: Grilled chicken salad",
        "Dinner: Steamed vegetables with lean protein (e.g., fish)"
    ],
    "muscle_gain": [
        "Breakfast: Oatmeal with peanut butter and banana",
        "Lunch: Chicken breast with quinoa and vegetables",
        "Dinner: Salmon with sweet potatoes and broccoli"
    ],
    "flexibility": [
        "Breakfast: Fruit salad with yogurt",
        "Lunch: Whole grain pasta with vegetables",
        "Dinner: Stir-fried tofu with vegetables"
    ]
}

# Function to calculate caloric needs (simplified Harris-Benedict equation)
def calculate_calories(age, gender, weight, height, activity_level):
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    activity_multiplier = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    
    calories_needed = bmr * activity_multiplier[activity_level.lower()]
    return round(calories_needed)

# Collect user information
def get_user_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    goal = input("Enter your fitness goal (weight_loss/muscle_gain/flexibility): ").lower()
    activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ").lower()

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "weight": weight,
        "height": height,
        "goal": goal,
        "activity_level": activity_level
    }

# Generate workout plan
def generate_workout_plan(goal):
    return workout_data.get(goal, ["General workout: 30 minutes of jogging, 15 minutes of stretching"])

# Generate diet plan
def generate_diet_plan(goal):
    return diet_data.get(goal, ["Balanced diet: vegetables, lean protein, and whole grains"])

# Display personalized plan
def display_plan(user_data):
    print(f"\nPersonalized Workout and Diet Plan for {user_data['name']}")
    print("="*40)
    
    # Calculate caloric needs
    calories = calculate_calories(
        user_data['age'],
        user_data['gender'],
        user_data['weight'],
        user_data['height'],
        user_data['activity_level']
    )
    
    print(f"\nDaily Caloric Need: {calories} kcal\n")
    
    # Workout Plan
    print("Workout Plan:")
    workout_plan = generate_workout_plan(user_data['goal'])
    for exercise in workout_plan:
        print(f" - {exercise}")
    
    # Diet Plan
    print("\nDiet Plan:")
    diet_plan = generate_diet_plan(user_data['goal'])
    for meal in diet_plan:
        print(f" - {meal}")

# Main function to run the program
def main():
    user_data = get_user_data()
    display_plan(user_data)

# Run the program
if __name__ == "__main__":
    main()
