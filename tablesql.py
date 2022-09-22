#Projet BDD Coquet Jean-Philippe, Larivière Aurélien, Mouton William

import sqlite3

#Fonction qui crée la base de donnée de départ
def creer_base():
    con = sqlite3.connect("database.db")
    c = con.cursor()

    c.execute("DROP TABLE IF EXISTS Stock;")
    c.execute("DROP TABLE IF EXISTS Reservation;")
    c.execute("DROP TABLE IF EXISTS Fidelite;")
    c.execute("DROP TABLE IF EXISTS Facture;")
    c.execute("DROP TABLE IF EXISTS Client;")
    c.execute("DROP TABLE IF EXISTS Tables;")
    c.execute("DROP TABLE IF EXISTS Menu;")

    c.execute("""
            CREATE TABLE IF NOT EXISTS Stock (
                id_plat integer primary key,
                nom_plat varchar(30) not NULL,
                quantite_plat INTEGER check(quantite_plat >= 0) not NULL
            );""")

    c.execute("""
            CREATE TABLE IF NOT EXISTS Reservation (
                id_client integer references Client(id_client),
                id_table integer references Tables(id_table),
                date date not NULL,
                heure_debut time not NULL,
                heure_fin time check(heure_fin > heure_debut) not NULL,
                constraint reservation_pk primary key (id_client, id_table)
            );""")

    c.execute("""
            CREATE TABLE IF NOT EXISTS Fidelite(
                reduction varchar(30) not NULL,
                id_client integer REFERENCES client(id_client)  
            );""")

    c.execute("""
            CREATE TABLE IF NOT EXISTS Facture(
                id_facture integer primary key autoincrement,
                id_client integer references Client(id_client),
                total INTEGER NOT NULL  
            );""")
    
    c.execute("""
            CREATE TABLE IF NOT EXISTS Client(
                id_client integer primary key autoincrement,
                nom varchar(30),
                prenom varchar(30),
                argent_depense integer not null
            );""")
    
    c.execute("""
            CREATE TABLE IF NOT EXISTS Tables(
                id_table integer primary key autoincrement,
                numero_table integer not null,
                nb_places integer not null
            );""")
    
    c.execute("""
            CREATE TABLE IF NOT EXISTS Menu(
                id_menu integer primary key,
                id_plat integer REFERENCES stock(id_plat),
                prix_plat float not NULL
            );""")
    
    c.execute("""
            INSERT INTO Client(id_client, nom, prenom, argent_depense) 
            VALUES  (1, 'Dupont', 'Jean', 10),
            (2, 'Thompson', 'Robert', 50),
            (3, 'Sheperd', 'John', 40),
            (4, 'Miller', 'Donald', 30),
            (5, 'Jeffords', 'Amanda', 100);
            """)
    
    c.execute("""
            INSERT INTO Facture(id_facture, id_client, total)
            VALUES  (1,1,50),
                    (2,2,32),
                    (3,3,12),
                    (4,4,88),
                    (5,5,122),
                    (6,3,23),
                    (7,4,44);
            """)
    
    c.execute("""
            INSERT INTO Fidelite(reduction, id_client)
            VALUES  (10,2),
                    (5,4),
                    (15,5);
            """)
    
    c.execute("""
            INSERT INTO Tables(id_table, numero_table, nb_places)
            VALUES  (1,1,6),
                        (2,2,2),
                        (3,3,8),
                        (4,4,4),
                        (5,5,4),
                        (6,6,2),
                        (7,7,6),
                        (8,8,10),
                        (9,9,2);
            """)
    
    c.execute("""
            INSERT INTO Reservation(id_client, id_table, date, heure_debut, heure_fin)
            VALUES  (3,4,"2021-04-05","12:00","14:00"),
                        (1,2,"2021-04-05","12:30","13:30"),
                        (2,3,"2021-04-06","12:00","14:00"),
                        (4,1,"2021-04-07","12:00","13:00"),
                        (5,5,"2021-04-08","11:30","13:00");

            """)
    
    c.execute("""
            INSERT INTO Stock(id_plat, nom_plat, quantite_plat)
            VALUES  (1, 'Musty Burger', 50),
                        (2, 'Pizza Napolitaine', 100),
                        (3, 'Pates Carbonara', 100),
                        (4, 'Steak frites', 200),
                        (5, 'Gratin Dauphinois', 30),
                        (6, 'Raclette', 20),
                        (7, 'Rosti Burger', 50);
            """)
    
    c.execute("""
            INSERT INTO Menu(id_menu,id_plat,prix_plat)
            VALUES  (1,1,15),
                        (2,2,12),
                        (3,3,11),
                        (4,4,10),
                        (5,5,15),
                        (6,6,13),
                        (7,7,20);
            """)

    con.commit()