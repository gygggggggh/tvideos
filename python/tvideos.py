import random
import sqlite3
from faker import Faker
from faker.providers import BaseProvider

fake = Faker("fr_FR")


class Key(BaseProvider):
    def video_keyword(self):
        return random.choice(['NSI', 'rick roll', 'linux', 'math', 'walid', 'yanis', 'diego', 'lucky', 'jorris', 'yorris', 'lucasb', 'lucasz', 'aurelien', 'dylan', 'emeric', 'lyan', 'liam', 'M. fuchs', 'louca', 'salle F319'])  # noqa: E501

    def id(self):
        characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-'
        video_id = ''.join(random.sample(characters, 11))
        return f'https://www.tvideos.com/watch?v={video_id}'


fake.add_provider(Key)


class Video:
    def __init__(self):
        self.title = self.random_title()
        self.description = self.random_description()
        self.likes = self.random_like()
        self.dislikes = self.random_dislike()
        self.views = self.random_view()
        self.id = self.video_id()
        self.timestamp = str(random.randrange(946684800, 2145916800))

    def random_title(self):
        rnd = [fake.video_keyword()] + [fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None) for _ in range(6)]  # noqa: E501
        random.shuffle(rnd)
        return ' '.join(rnd[:-1]).replace(".", "")

    def random_description(self):
        description = fake.video_keyword() + " "
        description += ' '.join([fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None) for _ in range(random.randint(10, 50))]) + " "  # noqa: E501
        return description.replace(".", "")

    def random_like(self):
        return str(random.randint(0, 100000))

    def random_dislike(self):
        return str(random.randint(0, 100000))

    def random_view(self):
        return str(random.randint(0, 100000000))

    def video_id(self):
        return fake.id()


class Chaine:
    def __init__(self):
        self.pseudo = self.random_pseudo()
        self.abonnes = str(random.randint(0, 1000000))
        self.bio = self.random_bio()
        self.timestamp = str(random.randrange(946684800, 2145916800))
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
        self.like = str(random.randint(0, 1000000))
        self.timestamp = str(random.randrange(946684800, 2145916800))

    def random_contenu(self):
        return fake.text(max_nb_chars=150)


conn = sqlite3.connect("db/tvideos.db")
cursor = conn.cursor()


def create_tables(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        titre TEXT,
        lien TEXT,
        description TEXT,
        likes TEXT,
        dislikes TEXT,
        id_chaine  TEXT,
        views TEXT,
        timestamp TEXT,
        FOREIGN KEY (id_chaine) REFERENCES chaines(id)
        );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS chaines (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        pseudo TEXT,
        abonnes TEXT,
        bio TEXT,
        timestamp TEXT,
        email TEXT
        );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS commentaires (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        contenu TEXT,
        likes TEXT,
        id_chaine TEXT,
        id_video TEXT,
        timestamp TEXT,
        FOREIGN KEY (id_chaine) REFERENCES chaines(id),
        FOREIGN KEY (id_video) REFERENCES videos(id)
        );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS n_com ( 
        id_video TEXT,
        id_commentaire TEXT,
        PRIMARY KEY (id_video, id_commentaire),
        FOREIGN KEY (id_video) REFERENCES videos(id),
        FOREIGN KEY (id_commentaire) REFERENCES commentaires(id)
        );
        """)


create_tables(cursor)


def insert_table_base(cursor):
    maChaine = Chaine()

    cursor.execute("""INSERT INTO chaines(pseudo, abonnes, bio, timestamp, email)
        VALUES(?, ?, ?, ?, ?)""", (maChaine.pseudo, maChaine.abonnes, maChaine.bio, maChaine.timestamp, maChaine.email))  # noqa: E501

    id_chaine = cursor.lastrowid

    maVideo = Video()
    cursor.execute("""INSERT INTO videos(titre, lien, description, likes, dislikes, id_chaine, views, timestamp)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (maVideo.title, maVideo.id, maVideo.description, maVideo.likes, maVideo.dislikes, id_chaine, maVideo.views, maVideo.timestamp))  # noqa: E501

    id_video = cursor.lastrowid

    monCommentaire = Commentaire()
    cursor.execute("""INSERT INTO commentaires(contenu, likes, id_chaine, id_video, timestamp)
        VALUES(?, ?, ?, ?, ?)""", (monCommentaire.contenu, monCommentaire.like, id_chaine, id_video, monCommentaire.timestamp))  # noqa: E501

    id_commentaire = cursor.lastrowid

    cursor.execute("""INSERT INTO n_com(id_video, id_commentaire)
        VALUES(?, ?)""", (id_video, id_commentaire))


def clear_database(cursor):
    cursor.execute("DELETE FROM n_com")
    cursor.execute("DELETE FROM commentaires")
    cursor.execute("DELETE FROM videos")
    cursor.execute("DELETE FROM chaines")
    cursor.execute("UPDATE sqlite_sequence SET seq = 0")


for i in range(120):
    insert_table_base(cursor)

# clear_database(cursor)

conn.commit()
conn.close()
