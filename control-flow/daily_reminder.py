def main() -> None:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    immediate_suffix = " that requires immediate attention today!" if time_bound == "yes" else ""

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task{immediate_suffix}")
            else:
                print(f"Reminder: '{task}' is a high priority task.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task{immediate_suffix}")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Plan to work on it soon.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority task{immediate_suffix}")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            if time_bound == "yes":
                print(f"Reminder: '{task}' has unspecified priority{immediate_suffix}")
            else:
                print(f"Reminder: '{task}' has unspecified priority.")


if __name__ == "__main__":
    main()


