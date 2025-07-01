# Initialize a dictionary to store start times and a set for waiting people
times = {}
waiting = set()
# Initialize a list to store the total wait time for each person
total_time = [0] * 101
# Initialize the current time
time = 0

# Loop for each input entry
for _ in range(int(input())):
    entry, name = input().split()
    name = int(name)

    # Handle the case where a person starts waiting
    if entry == 'R':
        times[name] = time  # Record the start time for the person
        waiting.add(name)  # Add the person to the waiting set

    # Handle the case where a person stops waiting
    elif entry == 'S':
        total_time[name] += time - times[name]  # Update the total wait time for the person
        waiting.remove(name)  # Remove the person from the waiting set

    # Handle the case of a time skip
    else:
        time += name - 2  # Adjust the current time based on the time skip
    time += 1  # Increment the current time

# Output the total wait time for each person
for name, wait in enumerate(total_time):
    # Check if the person has a non-zero wait time or is still waiting
    if wait != 0 or name in waiting:
        # If the person is still waiting, output -1
        if name in waiting:
            print(name, -1)
        # Otherwise, output the total wait time
        else:
            print(name, wait)
