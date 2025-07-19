# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for priority level and convert to lowercase for consistency
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize message
message = ""

# Match case for priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Check if time-bound and append appropriate message
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium", "low"]:
    message += ". Consider completing it when you have free time."

# Print the final customized reminder
print("\n" + message)
