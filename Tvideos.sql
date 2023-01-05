CREATE TABLE Video (
  id INTEGER PRIMARY KEY,
  titre VARCHAR(30),
  lien TEXT,
  description TEXT,
  like INTEGER,
  dislike INTEGER,
  id_chaine INTEGER,
  FOREIGN KEY (id_chaine) REFERENCES Chaine(id)
);

CREATE TABLE Chaine (
  id INTEGER PRIMARY KEY,
  pseudo VARCHAR(25),
  abonnes INTEGER,
  bio TEXT,
  email VARCHAR(30)
);

CREATE TABLE Commentaire (
  id INTEGER PRIMARY KEY,
  contenue VARCHAR(150),
  like INTEGER,
  id_chaine VARCHAR(25),
  FOREIGN KEY (id_chaine) REFERENCES Chaine(id)
);

CREATE TABLE n_com (
  id_video INTEGER,
  id_commentaire INTEGER,
  PRIMARY KEY (id_video, id_commentaire),
  FOREIGN KEY (id_video) REFERENCES Video(id),
  FOREIGN KEY (id_commentaire) REFERENCES Commentaire(id)
);