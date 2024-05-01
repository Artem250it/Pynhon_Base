# def build_person(first_name,last_name):
#     """Возращает словарь с информации о человеке"""
#     person = {'first': first_name, 'last':last_name}
#     return person

# musision = build_person('jimi', 'hendrih')
# print(musision)


def city_contry(city,contry):
    """Return city and country"""
    s_c = f"'{city},{contry}'"
    return s_c.title()

geo = city_contry('santiago','chile')
print(geo)