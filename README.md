![alt text](https://raw.githubusercontent.com/Konsta00/Air-Travellers-Challenge/main/LOGO.png)                      
                                                                                                                                                    
Lentokenttäseikkailu:

Pelaaja on seikkailija, joka matkustaa eri lentokentille ympäri maailmaa. Pelaaja ratkaisee ohjelmointi kysymyksiä, jolla ansaitsee €-budjettia, samalla pelaaja voi löytää poweruppeja ja oppia samalla lentokenttien historiasta ja kulttuurista. 

-Pelaaja valitsee pelin alussa hahmon. Hahmo määrittää kysymyksien vaikeuden ja aloitus paikan maailmassa. 
-Pelin aluksi pelaaja pystyy matkustamaan 10 lähimpään lentokenttään
-Mitä suurempi pelaajan taso, sitä kauemmas pystyy matkustamaan
-Matkustaminen kuluttaa pelaajan budjettia
- Pelaajan taso vaikuttaa myös kysymyksien vaikeuteen.
- difficult_coutry  = higher reward
-player_level > esim. 15 = difficult_queestion = higher reward


higher_reward = $$$ + points

Jokaisella on lentokentällä on vaikeustaso, joka määrittää ko. kysymyksen vaikeuden ja mahdollisen powerupin. 
Kaava pisteiden laskemiseen: lopulliset_pisteet = lentokenttä_vaikeustaso * pisteet_kysymyksestä.
- 3 kysymystä per lentokenttä, jos pelaaja saa yli 1 kysymyksen väärin tulee miinus pisteitä
- Jos pelaaja vastaan oikein 2/3 kysymyksistä voi voittaa Powerup
- Jokaisella pelaajalla on pelin aluksi 3 ilmaista vihjettä, jos vihjeet loppuvat niitä pystyy ostamaan lisää
-Myös Poweruppeja voi ostaa lisää, mutta ne ovat arvokkaampia

Powerups:
- Ilmainen matkustus mihin tahansa lentokenttään
- 3 lisävihjettä
- Käteispalkinto
- Skip kysymys


Kestävän matkustamisen ja ympäristönsuojelun teemat voivat olla osa seikkailua, esimerkiksi auttamalla paikallista ympäristöä.


Kestävän matkustamisen ja ympäristönsuojelun teemat voivat olla osa seikkailua, esimerkiksi auttamalla paikallista ympäristöä.
![alt text](https://github.com/Konsta00/Air-Travellers-Challenge/blob/main/BANNER_X_SNAKE.png)
                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                             
                                    
                _________      .__    ___________      __________              
               /   _____/ _____|  |   \__    ___/___   \______   \__ __  ____  
               \_____  \ / ____/  |     |    | /  _ \   |       _/  |  \/    \ 
               /        < <_|  |  |__   |    |(  <_> )  |    |   \  |  /   |  \
              /_______  /\__   |____/   |____| \____/   |____|_  /____/|___|  /
                      \/    |__|                               \/           \/ 

Lataa flight_game tietokanta: 
https://moodle2.metropolia.fi/pluginfile.php/1561494/mod_resource/content/1/lp.sql

SEN JÄLKEEN JUOKSE MYSQL-KONSOLISSA:

DROP TABLE IF EXISTS goal;
DROP TABLE IF EXISTS goal_reached;

ALTER TABLE airport DROP COLUMN elevation_ft;
ALTER TABLE airport DROP COLUMN iso_region;
ALTER TABLE airport DROP COLUMN municipality;
ALTER TABLE airport DROP COLUMN scheduled_service;
ALTER TABLE airport DROP COLUMN gps_code;
ALTER TABLE airport DROP COLUMN iata_code;
ALTER TABLE airport DROP COLUMN local_code;
ALTER TABLE airport DROP COLUMN home_link;
ALTER TABLE airport DROP COLUMN keywords;
ALTER TABLE airport DROP COLUMN wikipedia_link;

ALTER TABLE game DROP COLUMN co2_budget;
ALTER TABLE game CHANGE COLUMN `screen_name` name varchar(255);
ALTER TABLE game ADD budget int NOT NULL DEFAULT(0);
ALTER TABLE game CHANGE COLUMN `location` current_airport varchar(10);
ALTER TABLE game RENAME player;

ALTER TABLE country DROP COLUMN keywords;
ALTER TABLE country DROP COLUMN wikipedia_link;

-----------------------------------------------
TABLES BASIC DESC:

id | varchar(40)
co2_consumed | int(8)
current_airport | varchar(10)
name | varchar(255)
budget | int(11)

id | int(11)
ident | varchar(40)
name | varchar(40)
latitude_deg | double
longitude_deg | double
continent | varchar(40)
iso_country | varchar(40)

iso_country | varchar(40)
name | varchar(40)
continent | varchar(40)
                                                                                                                              
                                                                                                                              
![alt text](https://github.com/Konsta00/Air-Travellers-Challenge/blob/main/ER.png)                      

                                                                                                                              
                                                                                                                              
