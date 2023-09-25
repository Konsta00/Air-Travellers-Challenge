                                                                                    
 <p>                                                                  ____             
     ,. -  .,                             _,.,  °                    ,.,   '          ;'*¨'`·- .,  ‘                                   ,·'´¨;.  '                                  _,.,  °    
   ,' ,. -  .,  `' ·,               ,.·'´  ,. ,  `;\ '                ;´   '· .,         \`:·-,. ,   '` ·.  '                             ;   ';:\           .·´¨';\           ,.·'´  ,. ,  `;\ '  
   '; '·~;:::::'`,   ';\          .´   ;´:::::\`'´ \'\              .´  .-,    ';\        '\:/   ;\:'`:·,  '`·, '                         ;     ';:'\      .'´     ;:'\        .´   ;´:::::\`'´ \'\  
    ;   ,':\::;:´  .·´::\'       /   ,'::\::::::\:::\:'            /   /:\:';   ;:'\'       ;   ;'::\;::::';   ;\                         ;   ,  '·:;  .·´,.´';  ,'::;'       /   ,'::\::::::\:::\:' 
    ;  ·'-·'´,.-·'´:::::::';     ;   ;:;:-·'~^ª*';\'´            ,'  ,'::::'\';  ;::';       ;  ,':::;  `·:;;  ,':'\'                      ;   ;'`.    ¨,.·´::;'  ;:::;       ;   ;:;:-·'~^ª*';\'´   
  ;´    ':,´:::::::::::·´'      ;  ,.-·:*'´¨'`*´\::\ '       ,.-·'  '·~^*'´¨,  ';::;      ;   ;:::;    ,·' ,·':::;                      ;  ';::; \*´\:::::;  ,':::;‘       ;  ,.-·:*'´¨'`*´\::\ '  
   ';  ,    `·:;:-·'´          ;   ;\::::::::::::'\;'        ':,  ,·:²*´¨¯'`;  ;::';      ;  ;:::;'  ,.'´,·´:::::;                     ';  ,'::;   \::\;:·';  ;:::; '      ;   ;\::::::::::::'\;'   
   ; ,':\'`:·.,  ` ·.,         ;  ;'_\_:;:: -·^*';\        ,'  / \::::::::';  ;::';     ':,·:;::-·´,.·´\:::::;´'                      ;  ';::;     '*´  ;',·':::;‘        ;  ;'_\_:;:: -·^*';\   
   \·-;::\:::::'`:·-.,';       ';    ,  ,. -·:*'´:\:'\°     ,' ,'::::\·²*'´¨¯':,'\:;       \::;. -·´:::::;\;·´                         \´¨\::;          \¨\::::;         ';    ,  ,. -·:*'´:\:'\° 
    \::\:;'` ·:;:::::\::\'      \`*´ ¯\:::::::::::\;' '    \`¨\:::/          \::\'        \;'\::::::::;·´'                             '\::\;            \:\;·'           \`*´ ¯\:::::::::::\;' '
     '·-·'       `' · -':::''       \:::::\;::-·^*'´          '\::\;'            '\;'  '         `\;::-·´                                   '´¨               ¨'               \:::::\;::-·^*'´  
</p>                                                                  
```markdown
![Lentokenttäseikkailu Logo](https://raw.githubusercontent.com/Konsta00/Air-Travellers-Challenge/main/images/LOGO.png)

# Lentokenttäseikkailu

**Pelin Kuvaus:**

Pelaaja on seikkailija, joka matkustaa eri lentokentille ympäri maailmaa. Pelaaja ratkaisee ohjelmointi kysymyksiä, jolla ansaitsee €-budjettia, samalla pelaaja voi löytää poweruppeja ja oppia samalla lentokenttien historiasta ja kulttuurista.

**Pelin Toiminnot:**

- Pelaaja valitsee pelin alussa hahmon, mikä määrittää kysymyksien vaikeuden ja aloituspaikan maailmassa.
- Pelin aluksi pelaaja pystyy matkustamaan 10 lähimpään lentokenttään.
- Mitä suurempi pelaajan taso, sitä kauemmas pystyy matkustamaan.
- Matkustaminen kuluttaa pelaajan budjettia.
- Pelaajan taso vaikuttaa myös kysymyksien vaikeuteen.
- difficult_country = korkeampi palkinto.
- player_level > esim. 15 = difficult_question = korkeampi palkinto.

**Palkinnot:**

- Jokaisella lentokentällä on vaikeustaso, joka määrittää kysymyksen vaikeuden ja mahdollisen powerupin.
- Kaava pisteiden laskemiseen: lopulliset_pisteet = lentokenttä_vaikeustaso * pisteet_kysymyksestä.
- 3 kysymystä per lentokenttä, jos pelaaja saa yli 1 kysymyksen väärin, tulee miinuspisteitä.
- Jos pelaaja vastaa oikein 2/3 kysymyksestä, voi voittaa Powerupin.
- Jokaisella pelaajalla on pelin alussa 3 ilmaista vihjettä, jos vihjeet loppuvat, niitä pystyy ostamaan lisää.
- Myös Poweruppeja voi ostaa lisää, mutta ne ovat arvokkaampia.

**Powerupit:**

- Ilmainen matkustus mihin tahansa lentokenttään.
- 3 lisävihjettä.
- Käteispalkinto.
- Kysymyksen ohittaminen.

**Pelin Idea:**

Pelaaja valitsee hahmonsa, ja aloituslentokenttä liittyy jotenkin aloitushahmoon. Esimerkiksi hahmon valinta: Donald Trump, jolloin aloituspaikkana olisi Yhdysvallat (Lentokenttä siellä).

Pelin tavoitteena on saavuttaa 1000 pistettä mahdollisimman vähäisellä lentämisellä.

Pelaaja vastaa lentokentälle saavuttaessa kysymykseen, ja mikäli kysymyksen saa ensimmäisellä vastauksella oikein, pelaaja saa +100 pistettä. Mikäli vastaa yrityksellä oikein, saa +70 pistettä, ja kolmannella yrityksellä +50 pistettä.

Kun pelaaja on vastannut kysymykseen oikein, hän voi matkustaa uuteen kohteeseen. Täällä taas vastaa kysymykseen.

Jos pelaaja saa kysymyksen ensimmäisellä oikein, hän saattaa saada "power upin", jolla voi "skipata" kysymyksen jollakin kentällä ja saada suoraan 100 pistettä.

Kestävän matkustamisen ja ympäristönsuojelun teemat voivat olla osa seikkailua, esimerkiksi auttamalla paikallista ympäristöä.

## BANNER

Travel safe and check your cabon dioxide emissions

![Lentokenttäseikkailu Banner](https://raw.githubusercontent.com/Konsta00/Air-Travellers-Challenge/main/images/BANNER_X_SNAKE.png)
```