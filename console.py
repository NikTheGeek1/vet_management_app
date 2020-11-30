import pdb
import datetime as dt
from models.owner import Owner
from models.pet import Pet
from models.feedback import Feedback
from models.pet_treatment import PetTreatment
from models.testimonial import Testimonial
from models.treatment import Treatment
from models.vet import Vet
from models.visit import Visit


from repositories.owner_rep import OwnerRep
from repositories.feedback_rep import FeedbackRep
from repositories.pet_rep import PetRep
from repositories.testimonial_rep import TestimonialRep
from repositories.treatment_pet import PetTreatmentsRep
from repositories.treatment_rep import TreatmentRep
from repositories.vet_rep import VetRep
from repositories.visit_rep import VisitRep

from utils.read_file import read_file

VisitRep().delete_all()
FeedbackRep().delete_all()
TestimonialRep().delete_all()
PetRep().delete_all()
OwnerRep().delete_all()
PetTreatmentsRep().delete_all()
TreatmentRep().delete_all()
VetRep().delete_all()

helen = Owner('Helen', 'Theo', 'htheo@outlook.com', '+33 6972845697', True)
OwnerRep().save(helen)

maria = Owner('Maria', 'Jeyck', 'mjeyck@outlook.com', '+33 6972849697', True)
OwnerRep().save(maria)

lola = Owner('Lola', 'Markelo', 'lmarkelo@outlook.com', '+33 6934449697', True)
OwnerRep().save(lola)

kost = Owner('Kost', 'Theo', 'ktheo@outlook.com', '+33 6945645697', True)
OwnerRep().save(kost)

evi = Owner('Evi', 'Prountz', 'eprountz@outlook.com', '+33 6972454337', True)
evi_obj = OwnerRep().save(evi)

marios = Owner('Marios', 'Charo', 'mtheocharo@outlook.com', '+33 6944449697', True)
marios_obj = OwnerRep().save(marios)

vet1 = Vet('Alan', 'Smith')
VetRep().save(vet1)

vet2 = Vet('Theresa', 'Talbot')
VetRep().save(vet2)

vet3 = Vet('Melissa', 'Dudley')
melissa_obj = VetRep().save(vet3)

evi_pet1_img = read_file('pet-1.txt')
evi_pet1 = Pet('Dobby', dt.date(2020, 7, 23), False, 'cat', evi_obj.id, melissa_obj.id, evi_pet1_img[0], evi_pet1_img[1])
PetRep().save(evi_pet1)

evi_pet2_img = read_file('pet-2.txt')
evi_pet2 = Pet('Pirpi', dt.date(2020, 3, 23), False, 'cat', evi_obj.id, melissa_obj.id, evi_pet2_img[0], evi_pet2_img[1])
PetRep().save(evi_pet2)

evi_pet3_img = read_file('pet-3.txt')
evi_pet3 = Pet('Pirps', dt.date(2020, 2, 3), False, 'cat', evi_obj.id, melissa_obj.id, evi_pet3_img[0], evi_pet3_img[1])
PetRep().save(evi_pet3)


feedback1 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', marios_obj.id)
FeedbackRep().save(feedback1)

pdb.set_trace()