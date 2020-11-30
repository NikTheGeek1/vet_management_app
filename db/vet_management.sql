DROP TABLE IF EXISTS pets_treatments;
DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS testimonials;
DROP TABLE IF EXISTS feedbacks;
DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(320),
    phone VARCHAR(50),
    registered BOOLEAN
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    dob DATE,
    yo NUMERIC,
    animal_type VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id),
    img VARCHAR,
    img_type VARCHAR(255)
);

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    pet_id INT REFERENCES pets(id),
    check_in DATE,
    check_out DATE,
    description TEXT
);

CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    qos INT,
    fs INT,
    cf INT,
    recommend INT,
    suggestions TEXT,
    other_comment TEXT,
    owner_id INT REFERENCES owners(id)
);

CREATE TABLE testimonials (
    id SERIAL PRIMARY KEY,
    testimonial TEXT,
    owner_id INT REFERENCES owners(id)
);

CREATE TABLE pets_treatments (
    id SERIAL PRIMARY KEY,
    pet_id INT REFERENCES pets(id),
    treatment_id INT REFERENCES treatments(id)
);
