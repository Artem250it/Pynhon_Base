sandwich_order = ['cheeze','tomato','cucimber','paper','becon','pastrami','pastrami','pastrami']
finiched_sandvich = []

while sandwich_order:
    current = sandwich_order.pop(0)
    print(f"I made your {current} sandwich.")
    finiched_sandvich.append(current)

print('\nMade sandwich:')
for sandwich in finiched_sandvich:
    print(sandwich)