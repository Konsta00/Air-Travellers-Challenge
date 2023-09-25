                                                                                                                                                    
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

https://docs.google.com/document/d/1S8WWbmltN4jDnygLBXsgCFfJzgW93RzI8U38FrUqCWk/edit

PELIN IDEA:
--------------
Pelaaja valitsee hahmonsa ja aloituslentokenttä on jotenkin aloitushahmoon liittyvä. ESIM. hahmon valinta: Donald Trump,
jolloin aloituspaikkana olisis Yhdysvallat (Lentokenttä siellä).

Pelin ideana on saavuttaa 1000 pistettä mahdollisimman vähäisellä lentämisellä.

Pelaaja vastaa lentokentälle saavuttaessa kysymykseen ja mikäli kysymyksen saa ensimmäisellä vastauksella oikein
saa pelaaja +100 pistettä. Mikäli vastaa yrityksellä oikein saa +70 pistettä ja kolmannella yrityksellä +50.

Kun pelaaja on vastannut kysymykseen oikein voi hän matkustaa uuteen kohteeseen. Täällä taas vastaa kysymykseen.

Jos pelaaja saa kysymyksen ensimmäisellä oikein hän saattaa saada "power upin" jolla voi "skipata" kysymyksen jollakin
kentällä ja saada suoraan 100pistettä. 

Kestävän matkustamisen ja ympäristönsuojelun teemat voivat olla osa seikkailua, esimerkiksi auttamalla paikallista ympäristöä.
 <pre>                                                                  ____             
    8 888888888o.   8 8888888888            .8.          8 888888888o.                        ,8.       ,8.          8 8888888888   
    8 8888    `88.  8 8888                 .888.         8 8888    `^888.                    ,888.     ,888.         8 8888         
    8 8888     `88  8 8888                :88888.        8 8888        `88.                 .`8888.   .`8888.        8 8888         
    8 8888     ,88  8 8888               . `88888.       8 8888         `88                ,8.`8888. ,8.`8888.       8 8888         
    8 8888.   ,88'  8 888888888888      .8. `88888.      8 8888          88               ,8'8.`8888,8^8.`8888.      8 888888888888 
    8 888888888P'   8 8888             .8`8. `88888.     8 8888          88              ,8' `8.`8888' `8.`8888.     8 8888         
    8 8888`8b       8 8888            .8' `8. `88888.    8 8888         ,88             ,8'   `8.`88'   `8.`8888.    8 8888         
    8 8888 `8b.     8 8888           .8'   `8. `88888.   8 8888        ,88'            ,8'     `8.`'     `8.`8888.   8 8888         
    8 8888   `8b.   8 8888          .888888888. `88888.  8 8888    ,o88P'             ,8'       `8        `8.`8888.  8 8888         
    8 8888     `88. 8 888888888888 .8'       `8. `88888. 8 888888888P'               ,8'         `         `8.`8888. 8 888888888888  
</pre>


![alt text](https://raw.githubusercontent.com/Konsta00/Air-Travellers-Challenge/main/images/LOGO.png)                      

```markdown

![Lentokenttäseikkailu Logo](https://raw.githubusercontent.com/Konsta00/Air-Travellers-Challenge/main/images/LOGO.png)

# Lentokenttäseikkailu

## Pelin Kuvaus:

Pelaaja on seikkailija, joka matkustaa eri lentokentille ympäri maailmaa. Pelaaja ratkaisee ohjelmointi kysymyksiä, jolla ansaitsee €-budjettia, samalla pelaaja voi löytää poweruppeja ja oppia samalla lentokenttien historiasta ja kulttuurista.

## Pelin Toiminnot:

- Pelaaja valitsee pelin alussa hahmon, mikä määrittää kysymyksien vaikeuden ja aloituspaikan maailmassa.
- Pelin aluksi pelaaja pystyy matkustamaan 10 lähimpään lentokenttään.
- Mitä suurempi pelaajan taso, sitä kauemmas pystyy matkustamaan.
- Matkustaminen kuluttaa pelaajan budjettia ja nostaa päästöjä.
- Pelaajan taso vaikuttaa myös kysymyksien vaikeuteen.

## Palkinnot:

- Kaava pisteiden laskemiseen: lopulliset_pisteet = lentokenttä_vaikeustaso * pisteet_kysymyksestä.
- 1 kysymys per lentokenttä, jos pelaaja saa yli 1 kysymyksen väärin, tulee miinuspisteitä.
- Jos pelaaja vastaa oikein 2/3 kysymyksestä, voi voittaa Powerupin.
- Jokaisella pelaajalla on pelin alussa 3 ilmaista vihjettä, jos vihjeet loppuvat, niitä pystyy ostamaan lisää.
- Myös Poweruppeja voi ostaa lisää, mutta ne ovat arvokkaampia.

## Powerupit:

- Ilmainen matkustus mihin tahansa lentokenttään.
- 3 ilmaista lisävihjettä.
- Käteispalkinto.
- Kysymyksen ohittaminen.

## Pelin Idea:

Pelaaja valitsee hahmonsa, ja aloituslentokenttä liittyy jotenkin aloitushahmoon. Esimerkiksi hahmon valinta: Donald Trump, jolloin aloituspaikkana olisi Yhdysvallat (Lentokenttä siellä).

Pelin tavoitteena on saavuttaa 1000 pistettä mahdollisimman vähäisellä lentämisellä.

Pelaaja vastaa lentokentälle saavuttaessa kysymykseen, ja mikäli kysymyksen saa ensimmäisellä vastauksella oikein, pelaaja saa +100 pistettä. Mikäli vastaa yrityksellä oikein, saa +70 pistettä, ja kolmannella yrityksellä +50 pistettä.

Kun pelaaja on vastannut kysymykseen oikein, hän voi matkustaa uuteen kohteeseen. Täällä taas vastaa kysymykseen.

Jos pelaaja saa kysymyksen ensimmäisellä oikein, hän saattaa saada "power upin", jolla voi "skipata" kysymyksen jollakin kentällä ja saada suoraan 100 pistettä.

Kestävän matkustamisen ja ympäristönsuojelun teemat voivat olla osa seikkailua, esimerkiksi auttamalla paikallista ympäristöä.
```
![alt text](https://github.com/Konsta00/Air-Travellers-Challenge/blob/main/images/BANNER_X_SNAKE.png)                                                                                                                              
                                                                                                                              
