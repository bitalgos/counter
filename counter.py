count=0
def save_number(count):
    try:
        with open("nums.txt", "w") as file:
            file.write(str(count))  
    except PermissionError:
        print("You don't have permission to save this file.")
def write_number():
    try:
        with open("nums.txt", "r") as file:
            return int(file.read()) 
    except FileNotFoundError:
        return 0
    except ValueError:
        print("The file has invalid data, set to 0.")
print(f"Current number: {count}")
while True:
    u_input = input("Enter - count next number (press 'r' to restart, 's' to save, 'w' to load): ")
    if u_input.lower() == 'r':
        count = 0  
        print(f"Restart counter. Current number: {count}")
    elif u_input.lower() == 'w': 
        count=write_number()  
        print(f"loaded: {count}")
    elif u_input.lower() == 's':
        print(f"Saved: {count}")
        save_number(count)
    else:
        count+=1 
        print(f"Current number: {count}")
    #bitalgos
