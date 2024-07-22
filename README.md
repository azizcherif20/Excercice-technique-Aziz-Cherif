# Excercice-technique-Aziz-Cherif
Création de la base de données :
CREATE DATABASE projet_amiral_gestion_db;

CREATE TABLE referentiel_fonds ( id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255) NOT NULL, description TEXT );

CREATE TABLE referentiel_instruments ( id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255) NOT NULL, type VARCHAR(100), description TEXT );

CREATE TABLE positions ( id INT AUTO_INCREMENT PRIMARY KEY, fond_id INT, instrument_id INT, quantite DECIMAL(10, 2), date_achat DATE, FOREIGN KEY (fond_id) REFERENCES referentiel_fonds(id), FOREIGN KEY (instrument_id) REFERENCES referentiel_instruments(id) );

CREATE TABLE historique_prix ( id INT AUTO_INCREMENT PRIMARY KEY, instrument_id INT NOT NULL, date DATE NOT NULL, prix DECIMAL(18, 2) NOT NULL, FOREIGN KEY (instrument_id) REFERENCES referentiel_instruments(id) );

Insertion des données dans la base :
INSERT INTO referentiel_fonds (nom, description) VALUES ('Fonds Actions Europe', 'Investissement dans des actions européennes'), ('Fonds Obligations US', 'Investissement dans des obligations américaines'), ('Fonds Marchés Emergents', 'Investissement dans les marchés émergents');

INSERT INTO referentiel_instruments (nom, type, description) VALUES ('Action Apple', 'Action', 'Action de la société Apple Inc.'), ('Obligation US 10 ans', 'Obligation', 'Obligation à 10 ans du gouvernement américain'), ('ETF Marchés Emergents', 'ETF', 'Fonds négocié en bourse pour les marchés émergents');

-- Positions pour le Fonds Actions Europe (Fond ID = 1) INSERT INTO positions (fond_id, instrument_id, quantite, date_achat) VALUES (1, 1, 1000, '2023-01-01'), (1, 2, 500, '2023-01-02');

-- Positions pour le Fonds Obligations US (Fond ID = 2) INSERT INTO positions (fond_id, instrument_id, quantite, date_achat) VALUES (2, 2, 1000, '2023-01-01'), (2, 3, 800, '2023-01-02');

-- Positions pour le Fonds Marchés Emergents (Fond ID = 3) INSERT INTO positions (fond_id, instrument_id, quantite, date_achat) VALUES (3, 3, 500, '2023-01-01'), (3, 1, 200, '2023-01-02');

-- Prix historiques pour l'Instrument 1 (Instrument ID = 1) INSERT INTO historique_prix (instrument_id, date, prix) VALUES (1, '2023-01-01', 150.25), (1, '2023-01-02', 152.10), (1, '2023-01-03', 148.90), (1, '2023-01-04', 151.50), (1, '2023-01-05', 153.00);

-- Prix historiques pour l'Instrument 2 (Instrument ID = 2) INSERT INTO historique_prix (instrument_id, date, prix) VALUES (2, '2023-01-01', 98.50), (2, '2023-01-02', 98.75), (2, '2023-01-03', 99.00), (2, '2023-01-04', 98.60), (2, '2023-01-05', 99.10);

-- Prix historiques pour l'Instrument 3 (Instrument ID = 3) INSERT INTO historique_prix (instrument_id, date, prix) VALUES (3, '2023-01-01', 30.20), (3, '2023-01-02', 30.50), (3, '2023-01-03', 31.00), (3, '2023-01-04', 31.20), (3, '2023-01-05', 30.80);
 
