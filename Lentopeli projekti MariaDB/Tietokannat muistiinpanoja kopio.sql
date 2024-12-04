--- 3 viivaa kommentteihin
-- Näköjään 2 viivaa riittää kommenttiin.

--- ISOT KIRJAIMET ei ole pakollisia

---tehdään käyttäjä
CREATE USER testi@localhost IDENTIFIED BY 'salasana'


---poistetaan tietokanta jos se on olemassa
DROP DATABASE IF EXISTS ankkalinna;

---luodaan ankkalinna
CREATE DATABASE ankkalinna;


---annetaan oikeuksia tietokantaan ankkalinna käyttäjälle testi
GRANT SELECT, INSERT, UPDATE ON ankkalinna.* to testi@localhost;

---Peruskomentoja

---näyttää taulut databasessa
SHOW TABLES;

--- * merkki on 'mikä tahansa/kaikki'
---Näyttää kaikki tietueet taulussa ankkalinnalainen.
SELECT * FROM ankkalinnalainen

---Kuvaa taulun rakenteen.
-- Tällä saa tietää mitä tietoja pitää syöttää ja mikä tyyppi (int, varchar)
DESCRIBE ankkalinnalainen;


---Lisää aku ankka:n tauluun ankkalinnalainen
---(etunimi, sukunimi) on fieldit taulussa
INSERT INTO ankkalinnalainen (etunimi, sukunimi)
 VALUES ("aku", "ankka");

---taulun luominen
create table ankkalinnalainen(
ID int not null auto_increment,
etunimi varchar(40),
sukunimi varchar(40),
primary key (id)
);
---not null tarkoittaa että saako kenttä olla tyhjä
---auto_increment antaa tietokannan numeroida id itse, käyttäjä ei saa/tarvitse
---

---Rajatut haut...

---Hae kaikki sarakkeet joissa "Ankka" sukunimi taulusta ankkalinnalainen
SELECT * FROM ankkalinnalainen WHERE SUKUNIMI = "Ankka";

---Hae kaikki ETUNIMET joiden sukunimi on "Ankka"
SELECT etunimi FROM ankkalinnalainen WHERE SUKUNIMI = "Ankka";

---Sumea haku. Kuin Jeeves :D
--- Hakee kaikki sarakkeet joissa sukunimessä on A. %-merkki tarkoittaa mitä tahansa/ei mitään.
SELECT * FROM ankkalinnalainen WHERE SUKUNIMI like "%A%";
---Tämä hakee sukunimet jotka alkaa A:lla
SELECT * FROM ankkalinnalainen WHERE SUKUNIMI like "A%";

---Hekee kaikki ankkalinnalaiset id numeron laskevassa järjestyksessä
select * from ankkalinnalainen order by id desc;

---select as-komento
---antaa listan jossa id:n alias on tunnistenumero, ja etunimet
SELECT id as tunnistenumero, etunimi from ankkalinnalainen;
---Antaa listan jossa ensin perhen nimi ja sitten (etu)nimi
Select sukunimi as perhe, etunimi as nimi from ankkalinnalainen;

---FROM - WHERE - AND

---Kaikki sarakkeet joissa omistussuhde omistaa taulussa ja lemmikki.nimi on Pulivari
select * from ankkalinnalainen, omistaa, lemmikki
where omistaa.ankkalinnalainen_id = ankkalinnalainen.id
and omistaa.lemmikki_id = lemmikki.id
and lemmikki.nimi = "pulivari"

---Kaikki sarakkeet, joissa ankkalinnalainen yhdistyy lemmikkiin.
select * from ankkalinnalainen, omistaa, lemmikki
where omistaa.ankkalinnalainen_id = ankkalinnalainen.id
and omistaa.lemmikki_id = lemmikki.id

---INNER LEFT- ja RIGHT JOIN
--- ON x = y kertoo millä sarakkeilla taulut liitetään. Kannattaa olla vierasavain.



---INNER JOIN
--- Inner join ei näytä tietueita joissa yhdistyy null arvo?? Toimii käytännössä samalla tavalla kuin WHERE ehto.
---Tämä antaa myös kaikki sarakkeet, joissa ankkalinnalainen yhdistyy lemmikkiin. Tähän voisi listätä
---WHERE jos halutaan tiettyyn lemmikkiin liitttyvät ankkalinnalaiset.
select *
from ankkalinnalainen
inner join omistaa on ankkalinnalainen.id = omistaa.ankkalinnalainen_id
inner join lemmikki on omistaa.lemmikki_id = lemmikki.id

---LEFT JOIN
-- Left join tulostaa ensimmäisenä kirjoitetun taulun kaikki tietueet vaikka
-- niihin liittyisi NULL arvo toisena kirjoitetussa taulussa.
-- Tämä antaa kaikki sarakkeet. Roope Ankka näkyy tulosteessa vaikka omistussuhteet ja lemmmikki ovat NULL
select *
from ankkalinnalainen
left join omistaa on ankkalinnalainen.id = omistaa.ankkalinnalainen_id
left join lemmikki on omistaa.lemmikki_id = lemmikki.id

---RIGHT JOIN
---Right join tulostaa kaikki rivit jälkimmäisenä mainitusta taulusta vaikka ensimmäisenä mainutuissa olisi
---liitettynä NULL arvo.
---Sama komento kuin edellisessä esimerkissä. Roope Ankka ei tulostu, koska lemmikki taulussa oleva NULL tieto
---ei ole rivi, vaan rivin puute.
select *
from ankkalinnalainen
right join omistaa on ankkalinnalainen.id = omistaa.ankkalinnalainen_id
right join lemmikki on omistaa.lemmikki_id = lemmikki.id


----Näyttää, että JOIN pitää tehdä oikeassa järjestyksessä:
---Tämä komento toimii.
select *
from lemmikki
right join omistaa on omistaa.lemmikki_id = lemmikki.id
right join ankkalinnalainen on ankkalinnalainen.id = omistaa.ankkalinnalainen_id

---Tämä komento EI TOIMI. Ilmeisesti koska Ensimmäinen JOIN on tauluun "omistaa" joka liitetään vasta sen jälkeen.
select *
from lemmikki
right join ankkalinnalainen on ankkalinnalainen.id = omistaa.ankkalinnalainen_id
right join omistaa on omistaa.lemmikki_id = lemmikki.id


---Sisäkyselyt
---Uloimpaan kyselyyn haluttu lopputulos/tuloste
---Keskimmäiseen kyselyyn polku kohti lopputietoa.
---Sisimpään kyselyyn lähtötieto.
---Lähtötieto: "pulivari", haluttu tieto omistajien nimet.
select etunimi, sukunimi
from ankkalinnalainen
where id in (select ankkalinnalainen_id from omistaa where lemmikki_id in ( select id from lemmikki where nimi = "Pulivari")
)
---Tässä paskassa on sisäkkäisiä kyselyitä. Muista sulkeet. Jokainen kysely kohdistuu suoraan johonkin tauluuun,
-- eli ei tarvitse täsmentää missä taulussa kukin sarake on.
--.Kokeillaaan kirjoittaa sama selkeämmin:
select etunimi, sukunimi
from ankkalinnalainen
where id in
      (select ankkalinnalainen_id from omistaa where lemmikki_id in
                  (select id from lemmikki where nimi = "Pulivari")
        )
---Silti perseestä. Huomaan, että - where id in() - ottaa ankkalinnalainen_id:n numeroarvon id:ksi.
--- Käytännössä on muotoa:  "WHERE x in () " missä x saa arvon sulkeiden sisältä.

---Tämä listaa kaikki Akun lemmikit
select lemmikki.nimi
from lemmikki
where lemmikki.id
          in (select lemmikki_id from omistaa where ankkalinnalainen_id
                in (select id from ankkalinnalainen where etunimi = "aku")
              )

---Tämä opetetaan tarpeettoman vaikeasti
---Tämä antaa lemmikkien nimet joiden id lemmikki taulussa on 1:
select nimi
from lemmikki
where id in(1)
---Helppoa.







---Tämä antaa sukunimet ja montako niitä on
select sukunimi, count(*) from ankkalinnalainen group by sukunimi;

---Laskee ankkalinnalaiset. Count näyttää olevan piilotettu sarake, joka on ylimmällä rivillä
select count(*) from ankkalinnalainen;
---Tämä on jännä. Rivilä on count sarake jossa saman sukunimen määrä.
-- Muut sarakkeet antaa ensimmäisen sen nimisen tiedot. esim. id = 1 , Aku, Ankka
select *, count(*) from ankkalinnalainen group by sukunimi;

--- 07 Koostetietokyselyt
---DISTINCT




---MAX . MIN , AVG ,SUM

---MAX
---Tämä ei toimi oikein
select etunimi, id from ankkalinnalainen where id in (select max(ankkalinnalainen.id) );
---ankkalinnalainen.id ei kohdista oikein
---Pitää olla:
select etunimi, id from ankkalinnalainen where id in (select max(id) from ankkalinnalainen );



--- UPDATE - SET
--Testi Ankasta tehdään epäkuollut. Tärkeää laittaa WHERE-ehto, muuten päivittää kaikki nimet!
update ankkalinnalainen
set etunimi = "Zombi"
where etunimi = "Testi" and sukunimi = "Ankka"

--- DELETE
delete from ankkalinnalainen
where etunimi ="Zombi" and sukunimi = "Ankka"

-- Tulostaminen tiedostoon
-- Tämä on vähän huono, koska sarakkeita ei eroteltu pilkuilla?
select * from ankkalinnalainen into outfile '/testi/ankkalinnalainen.out';

--testataan tehdä uusi taulu afganistanin kentistä
select *
into table1
from table2
where


-- Tämä kertoo merkistön:
-- Jos ääkköset ei toimi tms.
select @@character_set_database, @@collation_database;
