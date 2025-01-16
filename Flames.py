def flames_game(name1, name2):
    # Convert names to lowercase and remove spaces
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    # Convert names into lists of characters
    list1 = list(name1)
    list2 = list(name2)
    
    # Remove common characters from both lists
    for char in list1[:]:
        if char in list2:
            list2.remove(char)
            list1.remove(char)
    
    # The remaining number of characters after elimination
    total_left = len(list1) + len(list2)
    
    # FLAMES game logic
    flames = ["Friend", "Love", "Affection", "Marriage", "Enemies", "Siblings"]
    
    # Calculate the position to eliminate in the FLAMES list
    while len(flames) > 1:
        index = (total_left % len(flames)) - 1
        if index >= 0:
            flames.pop(index)
        else:
            flames.pop(len(flames) - 1)
    
    return flames[0]

# Get input from users
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate the relationship
result = flames_game(name1, name2)

# Display the result
print(f"The relationship between {name1} and {name2} is:{result}")
