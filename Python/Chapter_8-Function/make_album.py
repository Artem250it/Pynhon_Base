# def make_album(artist_name,album_name,numer_sing=None):
#     """"Возращает имя группы и альбома"""
#     info_album = {'artist' : artist_name, 'title': album_name}
#     if numer_sing:
#         info_album['numer_sing'] = numer_sing
#     return info_album.title()

# while True :
#     print("\nEnter album details (or 'q' to quit):  ")
#     f_name = input('Artist name: ')
#     l_name = input('Album name:  ')
#     if f_name.lower()== 'q':
#         break
#     format = make_album(f_name,l_name)
#     print(f"\nHello, {format}!")

#     print("Created album dictionary:")
#     print(format)


def make_album():
    name = input("Enter name: ")
    album = input("Enter album: ")
    traks = input("Enter numer track: ")
    return [traks, [album, name]]
my_album={}
while True:
    isit = make_album()
    my_album[isit[0]] = isit[1]
    repeat = input("Again?(y/n): ")
    if repeat == 'n':
        break
print(my_album)