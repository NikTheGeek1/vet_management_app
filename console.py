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
evi_pet1 = Pet('Dobby', dt.date(2020, 7, 23), False, 'cat', evi_obj, melissa_obj, evi_pet1_img[0], evi_pet1_img[1])
PetRep().save(evi_pet1)

evi_pet2_img = read_file('pet-2.txt')
evi_pet2 = Pet('Pirpi', dt.date(2020, 3, 23), False, 'cat', evi_obj, melissa_obj, evi_pet2_img[0], evi_pet2_img[1])
PetRep().save(evi_pet2)

evi_pet3_img = read_file('pet-3.txt')
evi_pet3 = Pet('Pirps', dt.date(2020, 2, 3), False, 'cat', evi_obj, melissa_obj, evi_pet3_img[0], evi_pet3_img[1])
PetRep().save(evi_pet3)


feedback1 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', marios_obj)
FeedbackRep().save(feedback1)

# TREATMENTS 
anthelmintics = Treatment('Anthelmintics', 'These are used to eliminate parasitic worms, which infest their systems and steal important nutrients.')
TreatmentRep().save(anthelmintics)

dermatological = Treatment('Dermatological drugs', 'Oral, topical, or injected medications might be used to treat common skin and ear conditions in animals.')
TreatmentRep().save(dermatological)

cnsmed = Treatment('Central nervous system medications', 'Drugs like aminocaproic acid or potassium bromide might be prescribed to help animals suffering from seizures or epilepsy.')
TreatmentRep().save(cnsmed)

resp_drugs = Treatment('Respiratory drugs', 'A variety of medications can be used to help animals suffering from respiratory issues. For example, a veterinarian might prescribe inhaled or oral steroids to assist animals suffering from asthma or other disorders that cause wheezing.')
TreatmentRep().save(resp_drugs)

antibiotics = Treatment('Antibiotics', 'These medications help animals\' systems fight infection and disease. They can be used once an illness is diagnosed, or a veterinarian might prescribe them preventively before a surgical procedure.')
TreatmentRep().save(antibiotics)

kid_meds = Treatment('Kidney medications', 'Many animals are prone to kidney issues and these treatments can help slow or stop the progress of these disorders.')
TreatmentRep().save(kid_meds)

ophth_drugs = Treatment('Ophthalmological drugs', 'Oral medications or eye drops can be used to treat infection and other ocular issues, such as cataracts and glaucoma.')
TreatmentRep().save(ophth_drugs)

bmt = Treatment('Behavioral modification treatments', 'f your animal appears neurotic, obsessive, or overly aggressive and other treatments have not been successful, your veterinarian may prescribe behavioral modifiers like antidepressants or antipsychotics.')
TreatmentRep().save(bmt)


pdb.set_trace()