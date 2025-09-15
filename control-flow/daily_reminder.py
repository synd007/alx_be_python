task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = f"Reminder: '{task}' is a {priority} priority task"
match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += ". Try to complete it soon"
    case "low":
        reminder += ". Consider completing it when you have free time"
    case _:
        reminder += ". Priority level not recognized"
