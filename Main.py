import json
import os
from datetime import datetime

DATA_FILE = "data/health_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"exercise_logs": []}
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

    print("\n Exercise logged successfully!")

def view_logs():
    print("\n--- Exercise Logs ---")
    data = load_data()
    for entry in data.get("exercise_logs", []):
        print(f"{entry['date']} - {entry['type']} for {entry['duration']} min | Notes: {entry['notes']}")

def main():
    while True:
        print("\nMy Health Buddy - Exercise Tracker")
        print("1. Log Exercise")
        print("2. View Logs")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            log_exercise()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
