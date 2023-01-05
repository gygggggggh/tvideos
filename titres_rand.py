import random
from faker import Faker
from faker.providers import BaseProvider

fake = Faker("fr_FR")

class Titres(BaseProvider):
    
    def video_keyword(self):
        return random.choice(['NSI','rick roll','linux','math','walid','yanis','diego','lucky','jorris','yorris','lucasb','lucasz','aurelien','dylan','emeric','lyan','liam','M. fuchs','louca','salle F319'])



fake.add_provider(Titres)

    
def random_title():
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

print(random_title())
print("############################################")
def random_description():
    description = ""
    description += fake.video_keyword() + " "
    for i in range(random.randint(10, 50)):
        description += fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None) + " "
    return description.replace(".", "")

print(random_description())