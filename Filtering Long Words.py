words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters
four_letters = [word for word in words if len(word) > 4]

# Display the filtered list
print(four_letters)
