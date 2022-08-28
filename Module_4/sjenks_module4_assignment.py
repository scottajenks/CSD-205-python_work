# 1 Create office items tuple
office_items = ('TV', 'fan', 'textbook', 'iPhone', 'laptop', 'mouse', 'coffee cup', 'pen',
                'bed', 'pillow', 'desk', 'lamp', 'book shelve', 'desk chair', 'water glass', 'picture')
print(office_items)
print()

for office_item in office_items:
    print(f"In my home office I have a {office_item}.")

print()

# Change office items tuple into a list and reverse it
office_items_list = list(office_items)
office_items_list.reverse()

i = 0
while i < len(office_items_list):
    print(f"In my home office I have a {office_items_list[i]}.")
    i = i + 1

# Exit program
input("\n\tPress ENTER to exit")
