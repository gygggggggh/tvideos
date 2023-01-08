CREATE TABLE Video (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  titre TEXT ,
  lien TEXT ,
  description TEXT ,
  like INTEGER ,
  dislike INTEGER ,
  id_chaine INTEGER ,
  vue INTEGER,
  timestamp INTEGER ,
  FOREIGN KEY (id_chaine) REFERENCES Chaine(id)
);

CREATE TABLE Chaine (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  pseudo TEXT,
  abonnes INTEGER,
  bio TEXT,
  timestamp INTEGER ,
  email TEXT 
);

CREATE TABLE Commentaire (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  contenue TEXT,
  like INTEGER,
  id_chaine TEXT,
  timestamp INTEGER,
  FOREIGN KEY (id_chaine) REFERENCES Chaine(id)
);

CREATE TABLE n_com (
  id_video INTEGER,
  id_commentaire INTEGER,
  PRIMARY KEY (id_video, id_commentaire),
  FOREIGN KEY (id_video) REFERENCES Video(id),
  FOREIGN KEY (id_commentaire) REFERENCES Commentaire(id)
);
