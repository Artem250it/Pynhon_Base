users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'eistain',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    }
for username , user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    locacation = user_info['location']
    print(f"\tFull name :{full_name.title()}")
    print(f"\tLocation:{locacation.title()}")