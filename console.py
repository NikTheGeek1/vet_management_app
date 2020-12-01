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
PetTreatmentsRep().delete_all()
PetRep().delete_all()
OwnerRep().delete_all()
TreatmentRep().delete_all()
VetRep().delete_all()

# OWNERS
helen = Owner('Helen', 'Theo', 'htheo@outlook.com', '+33 6972845697', True)
OwnerRep().save(helen)

maria = Owner('Maria', 'Jeyck', 'mjeyck@outlook.com', '+33 6972849697', True)
maria_obj = OwnerRep().save(maria)

lola = Owner('Lola', 'Markelo', 'lmarkelo@outlook.com', '+33 6934449697', True)
lola_obj = OwnerRep().save(lola)

kost = Owner('Kost', 'Theo', 'ktheo@outlook.com', '+33 6945645697', True)
kost_obj = OwnerRep().save(kost)

evi = Owner('Evi', 'Prountz', 'eprountz@outlook.com', '+33 6972454337', True)
evi_obj = OwnerRep().save(evi)

marios = Owner('Marios', 'Charo', 'mtheocharo@outlook.com', '+33 6944449697', True)
marios_obj = OwnerRep().save(marios)

moore = Owner('Adam', 'Moore', 'amoore@outlook.com', '+44 7425449697', True)
moore_obj = OwnerRep().save(moore)

pickerin = Owner('Martin', 'Pickerin', 'mpickerin@outlook.com', '+44 7444449697', True)
pickerin_obj = OwnerRep().save(pickerin)

baddeley = Owner('Alan', 'Baddeley', 'abaddeley@outlook.com', '+44 7454449697', False)
baddeley_obj = OwnerRep().save(baddeley)
#################

# VETS
vet1 = Vet('Alan', 'Smith')
alan_obj = VetRep().save(vet1)

vet2 = Vet('Theresa', 'Talbot')
theresa_obj = VetRep().save(vet2)

vet3 = Vet('Melissa', 'Dudley')
melissa_obj = VetRep().save(vet3)

vet4 = Vet('John', 'Martin')
john_obj = VetRep().save(vet4)

vet5 = Vet('Elena', 'Gherri')
elena_obj = VetRep().save(vet5)

vet6 = Vet('Martin', 'Corley')
martin_obj = VetRep().save(vet6)
###########

# PETS
evi_pet1_img = read_file('pets_images_base64/pet-1.txt')
evi_pet1 = Pet('Dobby', dt.date(2020, 7, 23), False, 'Cat', evi_obj, melissa_obj, evi_pet1_img[0], evi_pet1_img[1])
pet_1 = PetRep().save(evi_pet1)

evi_pet2_img = read_file('pets_images_base64/pet-2.txt')
evi_pet2 = Pet('Smokey', dt.date(2020, 3, 23), False, 'Cat', evi_obj, melissa_obj, evi_pet2_img[0], evi_pet2_img[1])
pet_2 = PetRep().save(evi_pet2)

evi_pet3_img = read_file('pets_images_base64/pet-3.txt')
evi_pet3 = Pet('Jack', dt.date(2020, 2, 3), False, 'Cat', evi_obj, melissa_obj, evi_pet3_img[0], evi_pet3_img[1])
pet_3 = PetRep().save(evi_pet3)

mario_pet1_img = read_file('pets_images_base64/pet-4.txt')
mario_pet1 = Pet('Layla', dt.date(2018, 2, 3), False, 'Cat', marios_obj, john_obj, mario_pet1_img[0], mario_pet1_img[1])
pet_4 = PetRep().save(mario_pet1)

moore_pet1_img = read_file('pets_images_base64/pet-5.txt')
moore_pet1 = Pet('Ash', dt.date(2020, 2, 3), False, 'Cat', moore_obj, alan_obj, moore_pet1_img[0], moore_pet1_img[1])
pet_5 = PetRep().save(moore_pet1)

kost_pet1_img = read_file('pets_images_base64/pet-6.txt')
kost_pet1 = Pet('Felix', dt.date(2019, 7, 20), False, 'Cat', kost_obj, theresa_obj, kost_pet1_img[0], kost_pet1_img[1])
pet_6 = PetRep().save(kost_pet1)

kost_pet3_img = read_file('pets_images_base64/pet-7.txt')
kost_pet3 = Pet('Nala', dt.date(2019, 2, 23), False, 'Cat', kost_obj, elena_obj, kost_pet3_img[0], kost_pet3_img[1])
pet_7 = PetRep().save(kost_pet3)

lola_pet1_img = read_file('pets_images_base64/pet-8.txt')
lola_pet1 = Pet('Cleo', dt.date(2017, 10, 13), False, 'Cat', lola_obj, martin_obj, lola_pet1_img[0], lola_pet1_img[1])
pet_8 = PetRep().save(lola_pet1)

maria_pet1_img = read_file('pets_images_base64/pet-9.txt')
maria_pet1 = Pet('Millo', dt.date(2019, 12, 3), False, 'Cat', maria_obj, martin_obj, maria_pet1_img[0], maria_pet1_img[1])
pet_9 = PetRep().save(maria_pet1)

maria_pet2_img = read_file('pets_images_base64/pet-10.txt')
maria_pet2 = Pet('Ollie', dt.date(2019, 3, 1), False, 'Cat', maria_obj, theresa_obj, maria_pet2_img[0], maria_pet2_img[1])
pet_10 = PetRep().save(maria_pet2)

kost_pet2_img = read_file('pets_images_base64/pet-11.txt')
kost_pet2 = Pet('Chester', dt.date(2020, 2, 3), False, 'Cat', kost_obj, alan_obj, kost_pet2_img[0], kost_pet2_img[1])
pet_11 = PetRep().save(kost_pet2)

pickerin_pet1_img = read_file('pets_images_base64/pet-12.txt')
pickerin_pet1 = Pet('Finn', dt.date(2020, 2, 3), False, 'Cat', pickerin_obj, melissa_obj, pickerin_pet1_img[0], pickerin_pet1_img[1])
pet_12 = PetRep().save(pickerin_pet1)

evi_pet4_img = read_file('pets_images_base64/pet-13.txt')
evi_pet4 = Pet('Jinx', dt.date(2020, 2, 3), False, 'Dog', evi_obj, melissa_obj, evi_pet4_img[0], evi_pet4_img[1])
pet_13 = PetRep().save(evi_pet4)

evi_pet5_img = read_file('pets_images_base64/pet-14.txt')
evi_pet5 = Pet('Ditton', dt.date(2020, 2, 3), False, 'Cat', evi_obj, melissa_obj, evi_pet5_img[0], evi_pet5_img[1])
pet_14 = PetRep().save(evi_pet5)

evi_pet6_img = read_file('pets_images_base64/pet-15.txt')
evi_pet6 = Pet('Jasmine', dt.date(2020, 2, 3), False, 'Cat', evi_obj, melissa_obj, evi_pet6_img[0], evi_pet6_img[1])
pet_15 = PetRep().save(evi_pet6)

evi_pet7_img = read_file('pets_images_base64/pet-16.txt')
evi_pet7 = Pet('Inka', dt.date(2020, 2, 3), False, 'Dog', evi_obj, melissa_obj, evi_pet7_img[0], evi_pet7_img[1])
pet_16 = PetRep().save(evi_pet7)

# FEEDBACKS
feedback1 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', marios_obj)
FeedbackRep().save(feedback1)

feedback2 = Feedback(4, 3, 4, 3, 'You could lower the prices', 'Nice staff', maria_obj)
FeedbackRep().save(feedback2)

feedback3 = Feedback(4, 3, 4, 3, 'What about doing...', 'An amazing job', evi_obj)
FeedbackRep().save(feedback3)

feedback4 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', lola_obj)
FeedbackRep().save(feedback4)

feedback5 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', kost_obj)
FeedbackRep().save(feedback5)

feedback6 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', moore_obj)
FeedbackRep().save(feedback6)

feedback7 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', pickerin_obj)
FeedbackRep().save(feedback7)

feedback8 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', baddeley_obj)
FeedbackRep().save(feedback8)

feedback9 = Feedback(4, 3, 4, 3, 'Not really', 'Great job', marios_obj)
FeedbackRep().save(feedback9)

#########

# Testimonials
testimonial1 = Testimonial('This was a great experience for me and my pet -thank you so much guys!!', marios_obj)
TestimonialRep().save(testimonial1)

testimonial2 = Testimonial('This was a life changing experience for me and my pet -thank you so much guys!!', moore_obj)
TestimonialRep().save(testimonial2)

testimonial3 = Testimonial('This was a great experience for me and my pet -thank you so much guys!!', evi_obj)
TestimonialRep().save(testimonial3)

testimonial4 = Testimonial('This was a great experience for me and my pet -thank you so much guys!!', pickerin_obj)
TestimonialRep().save(testimonial4)

testimonial5 = Testimonial('This was a life changing experience for me and my pet -thank you so much guys!!', lola_obj)
TestimonialRep().save(testimonial5)

testimonial6 = Testimonial('This was a great experience for me and my pet -thank you so much guys!!', kost_obj)
TestimonialRep().save(testimonial6)
##############


# TREATMENTS 
anthelmintics = Treatment('Anthelmintics', 'These are used to eliminate parasitic worms, which infest their systems and steal important nutrients.')
treatment1 = TreatmentRep().save(anthelmintics)

dermatological = Treatment('Dermatological drugs', 'Oral, topical, or injected medications might be used to treat common skin and ear conditions in animals.')
treatment2 = TreatmentRep().save(dermatological)

cnsmed = Treatment('Central nervous system medications', 'Drugs like aminocaproic acid or potassium bromide might be prescribed to help animals suffering from seizures or epilepsy.')
treatment3 = TreatmentRep().save(cnsmed)

resp_drugs = Treatment('Respiratory drugs', 'A variety of medications can be used to help animals suffering from respiratory issues. For example, a veterinarian might prescribe inhaled or oral steroids to assist animals suffering from asthma or other disorders that cause wheezing.')
treatment4 = TreatmentRep().save(resp_drugs)

antibiotics = Treatment('Antibiotics', 'These medications help animals\' systems fight infection and disease. They can be used once an illness is diagnosed, or a veterinarian might prescribe them preventively before a surgical procedure.')
treatment5 = TreatmentRep().save(antibiotics)

kid_meds = Treatment('Kidney medications', 'Many animals are prone to kidney issues and these treatments can help slow or stop the progress of these disorders.')
treatment6 = TreatmentRep().save(kid_meds)

ophth_drugs = Treatment('Ophthalmological drugs', 'Oral medications or eye drops can be used to treat infection and other ocular issues, such as cataracts and glaucoma.')
treatment7 = TreatmentRep().save(ophth_drugs)

bmt = Treatment('Behavioral modification treatments', 'f your animal appears neurotic, obsessive, or overly aggressive and other treatments have not been successful, your veterinarian may prescribe behavioral modifiers like antidepressants or antipsychotics.')
treatment8 = TreatmentRep().save(bmt)
##############


# VISITS
visit1 = Visit(pet_1.id, dt.date(2020, 7, 28), dt.date(2020, 7, 30), 'In this visit the pet was so cute the disease cured itself')
VisitRep().save(visit1)

visit2 = Visit(pet_2.id, dt.date(2020, 8, 28), dt.date(2020, 8, 30), 'In this visit the pet was so cute the disease cured itself')
VisitRep().save(visit2)

visit3 = Visit(pet_3.id, dt.date(2020, 9, 28), dt.date(2020, 9, 30), 'In this visit the pet was so cute the disease cured itself')
VisitRep().save(visit3)

visit4 = Visit(pet_4.id, dt.date(2020, 11, 28), dt.date(2020, 12, 30), 'In this visit the pet was so cute the disease cured itself')
VisitRep().save(visit4)

visit5 = Visit(pet_5.id, dt.date(2020, 11, 28), dt.date(2020, 12, 30), 'In this visit the pet was so cute the disease cured itself')
VisitRep().save(visit5)

visit6 = Visit(pet_6.id, dt.date(2020, 11, 28), dt.date(2020, 12, 30), 'In this visit the pet was so cute the disease cured itself')
VisitRep().save(visit6)
######


# TREATMENTS to PETS
PetTreatmentsRep().save(PetTreatment(pet_1, treatment1))
PetTreatmentsRep().save(PetTreatment(pet_1, treatment2))
PetTreatmentsRep().save(PetTreatment(pet_1, treatment3))
PetTreatmentsRep().save(PetTreatment(pet_1, treatment4))
PetTreatmentsRep().save(PetTreatment(pet_2, treatment2))
PetTreatmentsRep().save(PetTreatment(pet_3, treatment3))
PetTreatmentsRep().save(PetTreatment(pet_4, treatment4))
PetTreatmentsRep().save(PetTreatment(pet_5, treatment5))
PetTreatmentsRep().save(PetTreatment(pet_6, treatment6))
PetTreatmentsRep().save(PetTreatment(pet_7, treatment1))
PetTreatmentsRep().save(PetTreatment(pet_8, treatment2))
PetTreatmentsRep().save(PetTreatment(pet_9, treatment3))
PetTreatmentsRep().save(PetTreatment(pet_10, treatment4))
PetTreatmentsRep().save(PetTreatment(pet_11, treatment5))
PetTreatmentsRep().save(PetTreatment(pet_12, treatment6))
PetTreatmentsRep().save(PetTreatment(pet_13, treatment1))
PetTreatmentsRep().save(PetTreatment(pet_14, treatment7))
PetTreatmentsRep().save(PetTreatment(pet_15, treatment8))
PetTreatmentsRep().save(PetTreatment(pet_16, treatment4))

pdb.set_trace()