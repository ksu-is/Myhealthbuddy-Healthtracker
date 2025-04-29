import json
import os
from datetime import datetime

DATA_FILE = "data/health_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {
            "exercise_logs": [],
            "sleep_logs": [],
            "hydration_logs": [],
            "mood_logs": []
        }
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def log_exercise():
    print("\n--- Log New Exercise ---")
    exercise_type = input("Exercise type (e.g., running, yoga): ")
    duration = input("Duration in minutes: ")
    notes = input("Any notes? (press Enter to skip): ")

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": exercise_type,
        "duration": duration,
        "notes": notes
    }

    data = load_data()
    data["exercise_logs"].append(entry)
    save_data(data)
    print("Exercise logged!")

def log_sleep():
    print("\n--- Log Sleep ---")
    hours = input("How many hours did you sleep?: ")
    quality = input("Sleep quality (e.g., good, average, poor): ")

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "hours": hours,
        "quality": quality
    }

    data = load_data()
    data["sleep_logs"].append(entry)
    save_data(data)
    print("Sleep logged!")

def log_hydration():
    print("\n--- Log Hydration ---")
    glasses = input("How many glasses of water did you drink today?: ")

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "glasses": glasses
    }

    data = load_data()
    data["hydration_logs"].append(entry)
    save_data(data)
    print("Hydration logged!")

def log_mood():
    print("\n--- Mood Check-In ---")
    mood = input("How are you feeling today (e.g., happy, stressed, tired)?: ")
    notes = input("Anything you'd like to note? (press Enter to skip): ")

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "mood": mood,
        "notes": notes
    }

    data = load_data()
    data["mood_logs"].append(entry)
    save_data(data)
    print("Mood logged!")

def main():
    while True:
        print("\nMy Health Buddy - Wellness Tracker")
        print("1. Log Exercise")
        print("2. Log Sleep")
        print("3. Log Hydration")
        print("4. Mood Check-In")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            log_exercise()
        elif choice == "2":
            log_sleep()
        elif choice == "3":
            log_hydration()
        elif choice == "4":
            log_mood()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
