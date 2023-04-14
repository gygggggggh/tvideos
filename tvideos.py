import random
import sqlite3
from faker import Faker
from faker.providers import BaseProvider
from  tkinter import *

# Créer un objet Faker avec la localelisation française
fake = Faker("fr_FR")

# Définir un fournisseur pour générer des mots-clés 
    
class Key(BaseProvider):
    def video_keyword(self):
        return random.choice(['NSI','rick roll','linux','math','walid','yanis','diego','lucky','jorris','yorris','lucasb','lucasz','aurelien','dylan','emeric','lyan','liam','M. fuchs','louca','salle F319'])

    def id(self):
        # Génère un ID de vidéo aléatoire
        characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-'
        id = ''.join(random.sample(characters, 11))
        return f'https://www.tvideos.com/watch?v={id}'
    
# Ajouter le fournisseur à l'objet Faker
fake.add_provider(Key)

class Video:
    def __init__(self):
        self.title = self.random_title()
        self.description = self.random_description()
        self.likes = self.random_like()
        self.dislikes = self.random_dislike()
        self.views = self.random_view()
        self.id = self.video_id()
        self.timestamp = random.randrange(946684800, 2145916800)

    def random_title(self):
        titre = ""
        rnd = []
        rnd.append(fake.video_keyword())
        for i in range(6):
            rnd.append(fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None))
        random.shuffle(rnd)
        for i in range(len(rnd)-1):
            titre += rnd[i] + " "
        # Enlève les points de fin de phrase du titre
        return titre.replace(".", "")

    def random_description(self):
        description = ""
        description += fake.video_keyword() + " "
        for i in range(random.randint(10, 50)):
            description += fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None) + " "
        return description.replace(".", "")
    
    def random_like(self):
        return random.randint(0, 100000)

    def random_dislike(self):
        return random.randint(0, 100000)

    def random_view(self):
        return random.randint(0, 100000000)

    def video_id(self):
        # Génère un ID de vidéo aléatoire
        _id_ = ""
        _id_ += fake.id()
        return _id_
    
import random

class Chaine:
    def __init__(self):
        self.pseudo = self.random_pseudo()
        self.abonnes = random.randint(0, 1000000)
        self.bio = self.random_bio()
        self.timestamp = random.randrange(946684800, 2145916800)
        self.email = self.random_email()

    def random_pseudo(self):
        return fake.user_name()

    def random_bio(self):
        return fake.text(max_nb_chars=200)
    def random_email(self):
        return fake.email()

class Commentaire:
    def __init__(self):
        self.contenu = self.random_contenu()
        self.like = random.randint(0, 1000000)
        self.timestamp = random.randrange(946684800, 2145916800)

    def random_contenu(self):
        return fake.text(max_nb_chars=150)

# connexion à la base de données
conn = sqlite3.connect("tvideos.db")

# creation du curseur
cursor = conn.cursor()

def create_tables(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        titre TEXT,
        lien TEXT,
        description TEXT,
        like INTEGER,
        dislike INTEGER,
        id_chaine INTEGER,
        vue INTEGER,
        timestamp INTEGER,
        FOREIGN KEY (id_chaine) REFERENCES chaines(id)
        );
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS chaines (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        pseudo TEXT,
        abonnes INTEGER,
        bio TEXT,
        timestamp INTEGER,
        email TEXT
        );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS commentaires (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        contenue TEXT,
        like INTEGER,
        id_chaine INTEGER,
        id_video INTEGER,
        timestamp INTEGER,
        FOREIGN KEY (id_chaine) REFERENCES chaines(id),
        FOREIGN KEY (id_video) REFERENCES videos(id)
        );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS n_com ( 
        id_video INTEGER,
        id_commentaire INTEGER,
        PRIMARY KEY (id_video, id_commentaire),
        FOREIGN KEY (id_video) REFERENCES Video(id),
        FOREIGN KEY (id_commentaire) REFERENCES Commentaire(id)
        );
        """)

# Utiliser la fonction pour créer les tables
create_tables(cursor)

def insert_table_base(cursor):
    maChaine = Chaine()
    
    cursor.execute("""INSERT INTO chaines(pseudo, abonnes, bio, timestamp, email)
        VALUES(?, ?, ?, ?, ?)""", (maChaine.pseudo, maChaine.abonnes, maChaine.bio, maChaine.timestamp, maChaine.email))
    # Récupérer l'ID de la chaîne insérée
    id_chaine = cursor.lastrowid
    maVideo = Video()
    cursor.execute("""INSERT INTO videos(titre, lien, description, like, dislike, id_chaine, vue, timestamp)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (maVideo.title, maVideo.id, maVideo.description, maVideo.likes, maVideo.dislikes, id_chaine, maVideo.views, maVideo.timestamp))
    # Récupérer l'ID de la vidéo insérée
    id_video = cursor.lastrowid

    monCommentaire = Commentaire()
    cursor.execute("""INSERT INTO commentaires(contenue, like, id_chaine, id_video, timestamp)
        VALUES(?, ?, ?, ?, ?)""", (monCommentaire.contenu, monCommentaire.like, id_chaine, id_video, monCommentaire.timestamp))
    # Récupérer l'ID du commentaire inséré
    id_commentaire = cursor.lastrowid
    
    cursor.execute("""INSERT INTO n_com(id_video, id_commentaire)
        VALUES(?, ?)""", (id_video, id_commentaire))


def clear_database(cursor):
    cursor.execute("DELETE FROM n_com")
    cursor.execute("DELETE FROM commentaires")
    cursor.execute("DELETE FROM videos")
    cursor.execute("DELETE FROM chaines")
    cursor.execute("UPDATE `sqlite_sequence` SET `seq` = 0 ")




# for i in range(120):
#     insert_table_base(cursor)

#clear_database(cursor)

# Enregistrer les changements dans la base de données
conn.commit()
# Fermer la connexion à la base de données
conn.close()




                