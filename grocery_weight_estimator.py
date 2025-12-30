# 🛒 Grocery Weight Estimator
# This program calculates the total estimated weight of groceries
# based on item type and quantity entered by the user.

# Dictionary: grocery item → weight per unit (lbs)
item_weights = {
    "apple": 0.33,
    "banana": 0.25,
    "tomato": 0.2,
    "orange": 0.4,
    "potato": 0.5
}

# Function to calculate weight of a given item and quantity
def estimate_weight(item, quantity):
    if item in item_weights:  # Check if the item exists in the dictionary
        return item_weights[item] * quantity
    else:
        print(f"Sorry, we don't have {item}.")  # Warn user if item not found
        return 0

# Lists to store weights and detailed entries
weights = []
items_entered = []

# Welcome message
print("🛒 Welcome to the Grocery Weight Estimator!\n")

# Loop to get user input until 'done' is entered
while True:
    item_name = input("Enter item name (or 'done' to finish): ").lower()
    if item_name == "done":  # Exit loop if user is finished
        break
    try:
        quantity = int(input(f"Enter quantity of {item_name}: "))  # Get quantity
    except ValueError:
        print("Please enter a valid number for quantity.\n")
        continue

    weight = estimate_weight(item_name, quantity)  # Calculate weight

    if weight > 0:  # Only store valid entries
        weights.append(weight)  # Add weight to list for total calculation
        items_entered.append((item_name, quantity, weight))  # Store full entry
        print(f"{quantity} {item_name}(s) weigh {weight} lbs\n")

# Calculate total weight
total_weight = sum(weights)

# Print summary of all entries
print("---- SUMMARY ----")
for i, (item, qty, w) in enumerate(items_entered, start=1):
    print(f"{i}. {qty} {item}(s) → {w} lbs")
print(f"Total estimated weight: {total_weight} lbs")
