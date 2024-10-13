#name = input("Whats your Name?")

#removes the whitespaces from the beggening and the end
#name = name.strip();

#capatalizes the first letter  
#name = name.capitalize()

#capatilizes all the first letter of the word
#name = name.title()

#method chaining
name = input("Whats your Name? ").strip().title()

first , last = name.split(); #this will split the name in two halves the first part will be stored in the first and last part in the last...

print(f"Hello, {name}")
print(f"Hello, {first}");
