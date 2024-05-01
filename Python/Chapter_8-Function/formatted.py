def get_formated_name(first_name,last_name):
    """Возрощение аккуратно отформатированного текста"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('jimi','hendrix')
print(musician)