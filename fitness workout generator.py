import random

# Sample exercises categorized by muscle group and difficulty
exercises = {
    "beginner": {
        "full_body": [
            "Bodyweight Squats - 3 sets of 12 reps",
            "Wall Push-ups - 3 sets of 10 reps",
            "Glute Bridges - 3 sets of 15 reps",
            "Plank - 3 sets of 20 seconds",
            "Walking Lunges - 3 sets of 10 reps per leg"
        ],
        "upper_body": [
            "Wall Push-ups - 3 sets of 10 reps",
            "Dumbbell Rows (light) - 3 sets of 12 reps",
            "Bicep Curls (light) - 3 sets of 15 reps",
            "Overhead Dumbbell Press (light) - 3 sets of 12 reps"
        ],
        "lower_body": [
            "Bodyweight Squats - 3 sets of 12 reps",
            "Glute Bridges - 3 sets of 15 reps",
            "Step-ups - 3 sets of 10 reps per leg",
            "Calf Raises - 3 sets of 20 reps"
        ]
    },
    "intermediate": {
        "full_body": [
            "Goblet Squats - 4 sets of 10 reps",
            "Push-ups - 4 sets of 15 reps",
            "Dumbbell Deadlifts - 4 sets of 12 reps",
            "Plank - 4 sets of 45 seconds",
            "Walking Lunges - 4 sets of 12 reps per leg"
        ],
        "upper_body": [
            "Push-ups - 4 sets of 15 reps",
            "Dumbbell Rows - 4 sets of 12 reps",
            "Bicep Curls - 4 sets of 15 reps",
            "Overhead Dumbbell Press - 4 sets of 12 reps"
        ],
        "lower_body": [
            "Goblet Squats - 4 sets of 10 reps",
            "Dumbbell Deadlifts - 4 sets of 12 reps",
            "Step-ups - 4 sets of 12 reps per leg",
            "Calf Raises - 4 sets of 25 reps"
        ]
    },
    "advanced": {
        "full_body": [
            "Barbell Back Squats - 5 sets of 8 reps",
            "Pull-ups - 5 sets of 10 reps",
            "Deadlifts - 5 sets of 8 reps",
            "Plank with Arm Lift - 5 sets of 1 minute",
            "Jumping Lunges - 5 sets of 12 reps per leg"
        ],
        "upper_body": [
            "Pull-ups - 5 sets of 10 reps",
            "Barbell Bench Press - 5 sets of 8 reps",
            "Barbell Rows - 5 sets of 8 reps",
            "Overhead Barbell Press - 5 sets of 8 reps"
        ],
        "lower_body": [
            "Barbell Back Squats - 5 sets of 8 reps",
            "Deadlifts - 5 sets of 8 reps",
            "Bulgarian Split Squats - 5 sets of 12 reps per leg",
            "Calf Raises with Weights - 5 sets of 30 reps"
        ]
    }
}

def generate_workout(level, focus):
    level = level.lower()
    focus = focus.lower()

    if level not in exercises:
        return "Sorry, fitness level not recognized. Choose beginner, intermediate, or advanced."
    
    if focus not in ["full_body", "upper_body", "lower_body"]:
        return "Sorry, focus area not recognized. Choose full_body, upper_body, or lower_body."
    
    workout_plan = random.sample(exercises[level][focus], k=min(4, len(exercises[level][focus])))
    return workout_plan

def main():
    print("Welcome to the Fitness Workout Generator!\n")
    level = input("Enter your fitness level (beginner, intermediate, advanced): ").strip()
    focus = input("Enter workout focus (full_body, upper_body, lower_body): ").strip()
    
    print("\nYour personalized workout plan:\n")
    workout = generate_workout(level, focus)
    
    if isinstance(workout, list):
        for idx, exercise in enumerate(workout, 1):
            print(f"{idx}. {exercise}")
    else:
        print(workout)

if __name__ == "__main__":
    main()

