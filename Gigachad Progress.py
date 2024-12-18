import datetime 
 
 
# Function to get the current time in the Philippine timezone 
def get_philippine_time(): 
    return datetime.datetime.utcnow() + datetime.timedelta(hours=8) 
 
 
# Function to add activity and schedule 
def add_activity(activities): 
    activity = input("Enter the activity: ") 
    try: 
        points = int(input("Enter the Giga Chad points for this activity: ")) 
    except ValueError: 
        print("Invalid input for points. Activity not added.") 
        return 
 
    # Get current time in Philippine timezone 
    current_time = get_philippine_time().time() 
    activities.append((activity, current_time, points)) 
    print("Activity added successfully!") 
 
 
# Function to mark activity as completed 
def complete_activity(activities, yearly_points): 
    if not activities: 
        print("No activities to complete.") 
        return None 
 
    print("Activities:") 
    for i, activity in enumerate(activities, start=1): 
        print(f"{i}. {activity[0]} at {activity[1].strftime('%I:%M %p')}") 
 
    try: 
        choice = int(input("Enter the number of the activity to mark as completed: ")) 
        if 1 <= choice <= len(activities): 
            completed_activity = activities.pop(choice - 1) 
            print(f"{completed_activity[0]} completed at {completed_activity[1].strftime('%I:%M %p')}") 
 
            # Get current year 
            current_year = get_philippine_time().year 
            # Update yearly points 
            if current_year in yearly_points: 
                yearly_points[current_year] += completed_activity[2] 
            else: 
                yearly_points[current_year] = completed_activity[2] 
 
            return completed_activity[2] 
        else: 
            print("Invalid activity number.") 
            return None 
    except ValueError: 
        print("Invalid input. Please enter a valid number.") 
        return None 
 
 
# Function to track Giga Chad points 
def track_points(points): 
    total_points = sum(points) 
    print("Your total Giga Chad points:", total_points) 
 
    # Checking if threshold is reached 
    if total_points >= 100: 
        print("\033[3mCongratulations! You did many things today towards being a Giga Chad. Keep improving!\033[0m") 
 
 
# Function to display current day, month, year, and accumulated Giga Chad points 
def display_day_and_points(points): 
    current_time = get_philippine_time() 
    current_day = current_time.strftime('%A') 
    current_month = current_time.strftime('%B') 
    current_year = current_time.strftime('%Y') 
    total_points = sum(points) 
    print(f"Today is {current_day}, {current_month} {current_year}.") 
    print(f"You have accumulated {total_points} Giga Chad points this month.") 
 
 
# Function to display points accumulated each year 
def display_yearly_points(yearly_points): 
    if not yearly_points: 
        print("No points accumulated yet.") 
    else: 
        print("Points accumulated each year:") 
        for year, points in sorted(yearly_points.items()): 
            print(f"{year}: {points} Giga Chad points") 
 
 
# Main program 
def main(): 
    activities = [] 
    points = [] 
    yearly_points = {} 
    print("Welcome to our Self-Discipline program!\n \033[3mYour road to being a Giga chad starts here.\033[0m") 
 
    while True: 
        print("\n1. Add activity and schedule") 
        print("2. Mark activity as completed") 
        print("3. Track Giga Chad points") 
        print("4. Display current day and accumulated points") 
        print("5. Display points accumulated each year") 
        print("6. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == '1': 
            add_activity(activities) 
        elif choice == '2': 
            completed_points = complete_activity(activities, yearly_points) 
            if completed_points is not None: 
                points.append(completed_points) 
        elif choice == '3': 
            track_points(points) 
        elif choice == '4': 
            display_day_and_points(points) 
        elif choice == '5': 
            display_yearly_points(yearly_points) 
        elif choice == '6': 
            print("Exiting program.") 
            break 
        else: 
            print("Invalid choice. Please try again.") 
 
    # Resetting Giga Chad points daily 
    points.clear() 
 
if __name__ == "__main__": 
    main() 