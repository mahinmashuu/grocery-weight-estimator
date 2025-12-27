item_weights = {
    "apple": 0.33,
    "banana": 0.25,
    "tomato": 0.2,
    "orange": 0.4,
    "potato": 0.5
}


def estimate_weight(item, quantity):
    if item in item_weights:
        return item_weights[item] * quantity
    else:
        print(f"Sorry, we don't have {item}.")
        return 0


weights = []
items_entered = []

while True:
    item_name = input("Enter item name (or 'done' to finish): ").lower()
    if item_name == "done":
        break
    quantity = int(input(f"Enter quantity of {item_name}: "))

    weight = estimate_weight(item_name, quantity)

    if weight > 0:
        weights.append(weight)
        items_entered.append((item_name, quantity, weight))
        print(f"{quantity} {item_name}(s) weigh {weight} lbs\n")

total_weight = sum(weights)
print("---- SUMMARY ----")
for i, (item, qty, w) in enumerate(items_entered, start=1):
    print(f"{i}. {qty} {item}(s) → {w} lbs")
print(f"Total estimated weight: {total_weight} lbs")

