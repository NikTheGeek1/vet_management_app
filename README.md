# VET MANAGEMENT APP
* **
### Technologies used
* Python/flask
* HTML
* CSS
* PostgreSQL
* **
### Instructions
##### 1) Setting up the database
After cloning the repo, one can make the app run by first setting up the database ```vet_management```.
    
* ```createdb```
    
* ```psql -d vet_management -f db/vet_management```

That should set up an empty database with the name ```vet_management```.
##### 2) Adding data to the database
* ```python3 console.py```
The dummy data that will be added are:
* owners
* onwer's feedbacks
* owner's testimonials
* vets
* pets
* treatments
* pet -> treatment relations
* visits

#### 3) Running the app  
Then, running the app should be as easy as just running
* ```flask run```

### Brief
This app can:
* register/track/edit pets
    * Name
    * Date of birth (or years old if not known)
    * Type of animal
    * Visit notes
* register/track/edig pet owners
    * Full name
    * email address
    * phone
    * registration status
* register/track/edit vets
    * Full name
    * access to vet's animals
* register/track/edit pet's visits
    * check in/outs
    * visit notes
* register/track owner's feedbacks
* register/track/change owner's testimonials
##### Relationships between data
** *
* a pet can only have **one** vet
* a vet can be responsible for **many** animals
** *
* a pet can only have **one** onwer
* an owner can have **many** pets
* **
* a pet can have **many** visits 
* a visit can only have **one** pet (duh)
* **
* a pet can have **many** treatments
* a treatment can have **many** pets
* **
* an owner can have **many** feedbacks
* a feedback can only have **one** owner
* **
* an onwer can only have **one** testimonial
* a testimonial can only have **one** owner
* **
[You can find a relationships and other diagrams used here](https://github.com/NikTheGeek1/vet_management_app/tree/main/diagrams)

##### Other
* pets can be added to an owner only if the owner is registered
* if the DoB of a pet is not know, the user can enter years of age
* the user can have access to all pets that have ever passed from the clinic, but also only the ones that are currently checked in
* all data can be changed/deleted besides owner's feedback history and visit history
* the user can upload/change profile images of owner's pets
* an attempt to make the webb app responsive was made. Added a few media queries and worked with rem's instead of px's so to be easier to make it responsive. The app looks decent up until 500x500 dimensions, less than that and divs turn into werewolves.