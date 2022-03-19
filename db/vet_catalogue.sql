DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact VARCHAR(255),
    status VARCHAR(255)

);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    contact VARCHAR(255),
    notes TEXT,
    vet_id INT REFERENCES vets(id)
);