# alien_0 = {'color': 'green','point': 5}
# alien_1 = {'color': 'yellow','point': 10}
# alien_2 = {'color': 'red','point': 15}

# aliens = [alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)


aliens = []
for alien_number in range(0,30):
    new_alian = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alian)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


for alien in aliens[:10]:
    print(alien)
print('...')
print(f"Totol number of aliens: {len(aliens)}")