""" 
Audio Manager:
Console application that allows the user to register his/her audio collection.
Auther: 
    Andrew Evans
Functionality:
    1 - Register Album
    2 - Register Song
    3 - Display catalog
    4 - Print Songs of Album
    5 - Count all songs in the system
    6 - Total $ in the catalog
    7 - Delete song
    8 - Delete Album # only delete empty albums
    9 - Print the most expensive album
"""

#imports
from display import clear_screen, print_header, print_menu
from album import Album
from song import Song
import pickle

#global vars

catalog =[]


#functions

def serialize_data():
    try:
        writer = open('sngManager.data', 'wb') # wb = writter binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data saved!")
    
    except:
        print("** Error saving data")    


def deserialize_data():
    try:
        reader = open('sngManager.data', 'rb') #rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for item in temp_list:
            catalog.append(item)

        print(f"** Loaded {len(catalog)} albums ")
    
    except:
        print("** Error loading data")

def register_album():
    print_header("Register Album")

    title = input("Provide Title: ")
    genre = input("Provide Genre: ")
    artist = input("Provide Artist Name: ")
    price = float(input("Provide Price: "))
    year = int(input("Provide Release Year: "))
    id = 1
    if(len(catalog) > 0):
        last = catalog[-1]
        id = last.id + 1


    album = Album(id,title,genre,artist,price,year)
    catalog.append(album)
    

def register_song():
    print_catalog()

    album_id = int(input("Select an album from the list: which album?"))
    
    found = False
    for album in catalog:
        if(album.id == album_id):
            found = True
            print_header(f"Add song to album: {album.title}") 
            title = input("Provide title: ")
            length = int(input("Provide length of song: "))
            writter = input("Provide artist name: ")
            
            id = 1
            if(len(album.songs) > 0):
                id = album.songs[-1].id + 1
            
            song = Song(id,title,length,writter)
            album.songs.append(song)
    
    if not found:
        print("Error: Wrong album id, try again!")




    song = Song(id,title,length,writter)
    serialize_data()


def print_catalog():
    print_header("Print Catalog")

    for album in catalog:
        print(album)

def count_songs():
    print_header("Total songs in the system")

    num = len([al.songs for al in catalog])
    
    print(f"You have: {num}")

def total_money():
    print_header("Total $ of the catalog")

    total = 0
    for album in catalog:
        total += album.price
    print(f"The total is ${total}")

def delete_song():
    print_catalog()
    id = int(input("Provide album id: "))

    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            print_header(f"Songs inside album: {album.title} choose one to delete: ")
            for song in album.songs:
                print(f"{song.id} | {song.title}")
                target_album = album.songs
            song_to_delete = int(input("Selete song id to delete"))
            for song in target_album:
                if song.id == song_to_delete:
                    target_album.remove(song)
        serialize_data()

            

        if not found:
            print("Error: Wrong album id. try again!")

def delete_album():
    print_catalog()
    id = int(input("Provide the id of the album you wish to delete: "))

    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            target_album = album
            if(len(target_album.songs) == 0):
                catalog.remove(target_album)
    serialize_data()
    if not found:
        print("no such album to delete")


def print_songs():
    print_catalog()
    id = int(input("Provide album id: "))

    found = False
    for album in catalog:
        if(album.id == id):
            found = True
            print_header(f"Songs inside album: {album.title}")
            for song in album.songs:
                print(f"{song.id} | {song.title}")
        if not found:
            print("Error: WRong album id. try again!")

#instructions

#read data
deserialize_data()

opc = ""
while(opc!= "q"):
    print_menu()
    opc = input("Please select an option: ")
    if(opc == "1"):
        register_album()
        serialize_data()

    elif(opc == "2"):
        register_song()

    elif(opc == "3"):
        print_catalog()

    elif(opc == "4"):
        print_songs()
    
    elif(opc == "5"):
        count_songs()

    elif(opc == "6"):
        total_money()

    elif(opc == "7"):
        delete_song()
    
    elif(opc == "8"):
        delete_album()

    elif(opc == "q"):
        clear_screen()
