CREATE TABLE IF NOT EXISTS videos (
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
CREATE TABLE IF NOT EXISTS chaines (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        pseudo TEXT,
        abonnes INTEGER,
        bio TEXT,
        timestamp INTEGER,
        email TEXT
        );

CREATE TABLE IF NOT EXISTS commentaires (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        contenue TEXT,
        like INTEGER,
        id_chaine INTEGER,
        id_video INTEGER,
        timestamp INTEGER,
        FOREIGN KEY (id_chaine) REFERENCES chaines(id),
        FOREIGN KEY (id_video) REFERENCES videos(id)
        );

CREATE TABLE IF NOT EXISTS n_com ( 
        id_video INTEGER,
        id_commentaire INTEGER,
        PRIMARY KEY (id_video, id_commentaire),
        FOREIGN KEY (id_video) REFERENCES Video(id),
        FOREIGN KEY (id_commentaire) REFERENCES Commentaire(id)
        );
