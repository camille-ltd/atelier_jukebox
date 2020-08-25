import datetime # modules/libraries that come with Python must be imported first
import database as db
menu = """S il vous plait veuillez selectionner une des options suivantes:
1) Ajouter une musique
2) Voir toutes les musiques
3) Marquer votre/vos musique(s) préférées
4) Voir vos musiques préférées
0) Sortir

Votre selection: """

print("Bienvenue à notre Jukebox App!")
# TO DO: create the movies table - implementation code must be in a file named database.py
db.create_tables()

# TO DO: use the right function in database.py (don't forget to pass needed parameters/arguments)
def add_music():
    music_title = input("Titre musique: ")
    release_date = input("Date de sortie (dd-mm-YYYY): ")
    release_date = datetime.datetime.strptime(release_date, "%d-%m-%Y").timestamp()
    db.add_music(music_title, release_date)
# TO DO: use the right function in database.py (don't forget to pass needed parameters/arguments)
def mark_music_as_pref():
    music_title = input("Titre musique: ")
    db.mark_music_as_pref(music_title)

def print_music_list(heading, movies):
    print(f"\n-- {heading} musique --")
    for music in musics:
        music_date = datetime.datetime.fromtimestamp(music[2])
        human_date = music_date.strftime("%b %d %Y")
        print(f"{music[1]} (sortie le {human_date})")
    print("---- \n")


user_input = input(menu)
while user_input != "0":
    if user_input == "1":
        add_music()
    elif user_input == "2":
        # TO DO: create the music variable (use the right function in database.py)
        musics = db.get_music() # Added
        print_music_list("Toutes tes", musics)
    elif user_input == "3":
        mark_music_as_pref()
    elif user_input == "4":
        # TO DO: create the movies variable (use the right function in database.py)
        musics = db.get_pref_music() # Added
        print_music_list("Préférences", musics)
    else:
        print("S il vous plait selectionner un nombre de 1 à 4 ou 0 pour sortir")
    user_input = input(menu)
