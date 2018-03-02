CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'London', 780);
INSERT INTO flights (origin, destination, duration) VALUES ('Cairo', 'Rome', 420);
INSERT INTO flights (origin, destination, duration) VALUES ('Lisbon', 'Tehran', 880);
INSERT INTO flights (origin, destination, duration) VALUES ('Las Vegas', 'Bogota', 460);
INSERT INTO flights (origin, destination, duration) VALUES ('Cairo', 'Seoul', 810);
INSERT INTO flights (origin, destination, duration) VALUES ('Paris', 'Jakarta', 790);

INSERT INTO passengers (name, flight_id) VALUES ('Mostafa', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Saadon', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Nabil', 3);
INSERT INTO passengers (name, flight_id) VALUES ('Abdullah', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Mariam', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Manar', 5);
INSERT INTO passengers (name, flight_id) VALUES ('Tareq', 2);