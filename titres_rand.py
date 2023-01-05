import random
from faker import Faker
from faker.providers import BaseProvider

fake = Faker("fr_FR")

class Titres(BaseProvider):
    
    def video_title(self):
        return random.choice(['NSI','rick roll','linux','math','walid','yanis','diego','lucky','jorris','yorris','lucasb','lucasz','aurelien','dylan','emeric','lyan','liam','M. fuchs','louca','salle F319'])

fake.add_provider(Titres)

titres = []
rnd = []
for _ in range(10000):
    rnd.append(fake.video_title())
    rnd.append(fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None))
    random.shuffle(rnd)
    for i in range(len(rnd)-1):
        titre = rnd[i] + " " + rnd[i+1]
        # Enlève les points de fin de phrase du titre
        titre = titre.replace(".", "")
        titres.append(titre)
        popeped = rnd.pop(0)
    titres.append(popeped)
    titres.pop()
    rnd = []
    

# Enregistre les titres dans un fichier texte
with open("titres.txt", "w", newline="") as f:
    for i in range(len(titres)):
        f.write(titres[i] + "\n")
