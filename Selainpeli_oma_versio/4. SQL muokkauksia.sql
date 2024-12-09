-- 4. SQL muokkaus tiedosto. Tarvitaan selainpeliin
-- Aja SQL tiedostot järjestyksessä 1. 2. 3. 4. ...
-- Tiedostot 1,2,3 tarvitaan pelin vanhaan versioon. Tiedosto 4 (tämä tiedosto) tarvitaan selainpelin backend v8 kanssa.

--Lisätään vaikeusaste ja aloitusrahat game tauluun
alter table game add column difficulty varchar(40) NULL;
alter table game add column start_money float NULL;

alter table game add column status varchar(40) NULL;
alter table game add column message varchar(40) NULL;
alter table game add column debugmessage varchar(40) NULL;

