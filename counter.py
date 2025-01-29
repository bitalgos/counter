count=0
print(f"Current number: {count}")
while True:
    user_input = input("Enter - count next number (press 'r' to restart): ")
    if user_input.lower() == 'r':
        count = 0  
        print(f"Restart counter. Current number: {count}")
    else:
        count+=1 
        print(f"Current number: {count}")
