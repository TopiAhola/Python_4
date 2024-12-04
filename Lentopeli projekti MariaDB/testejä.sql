select name
from country where name ="Afghanistan";


-- Tämä toimii
--heliportit, ja closed  jää pois
select airport.name, airport.type
from airport, country
where airport.iso_country = country.iso_country
and country.name = "Afghanistan"
and not airport.type  = "heliport"
and not airport.type  =  "closed";


Kaikki afganistanin kentät:

select airport.*
from airport, country
where airport.iso_country = country.iso_country
and country.name = "Afghanistan"
into outfile "c:/testi/afg.out";


-- Luoko tämä uuden taulun? Ei. Uusi taulu pitää luoda ensin
insert into afghanistan
select *
from airport
left join country on airport.iso_country = country.iso_country
where country.name = "Afghanistan"

-- Luodaan Afghanistan:
-- Toimii
CREATE TABLE `Afghanistan` (
  `id` int(11) NOT NULL,
  `ident` varchar(40) NOT NULL,
  `type` varchar(40) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `latitude_deg` double DEFAULT NULL,
  `longitude_deg` double DEFAULT NULL,
  `elevation_ft` int(11) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `iso_country` varchar(40) DEFAULT NULL,
  `iso_region` varchar(40) DEFAULT NULL,
  `municipality` varchar(40) DEFAULT NULL,
  `scheduled_service` varchar(40) DEFAULT NULL,
  `gps_code` varchar(40) DEFAULT NULL,
  `iata_code` varchar(40) DEFAULT NULL,
  `local_code` varchar(40) DEFAULT NULL,
  `home_link` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--syöte kokeilu
--toimii
insert into Afghanistan
select   id, ident,
  type,
  airport.name,
  latitude_deg,
  longitude_deg,
  elevation_ft,
  airport.continent,
  airport.iso_country,
  iso_region,
  municipality,
  scheduled_service,
  gps_code,
  iata_code,
  local_code,
  home_link,
  airport.wikipedia_link,
  airport.keywords
from airport
left join country on airport.iso_country = country.iso_country
where country.name = "Afghanistan";


----eurppoan kentät:
select airport.name, airport.type
from airport
left join country on airport.iso_country = country.iso_country
where country.continent like "Eu%"
and not airport.type  = "small_airport"
and not airport.type  = "heliport"
and not airport.type  =  "closed";

--Euroopan kentät 2:
select airport.name, airport.type
from airport
left join country on airport.iso_country = country.iso_country
where country.continent like "Eu%"
and airport.type = "large_airport"
and airport.type = "medium_airport";

--Euroopan maat:
select country.iso_country
from country
where continent like "Eu%"
group by country.name
into outfile '/SQL/maat2.out';

--Lentokenttähaku maan nimellä
select airport.name, airport.type, airport.ident, country.name
from airport
left join country on airport.iso_country = country.iso_country
where country.continent like "Eu%"
and country.name like "ukr%"
order by airport.type;


Pelin kentät:

--versio 1:
select airport.name, country.name, airport.municipality
from airport
left join country on airport.iso_country = country.iso_country
where ident in ('lati', 'loww', 'umms', 'ebbr', 'lqsa', 'lbvn', 'ldza', 'lkpr', 'ekch', 'eetn', 'ekvg', 'efhk', 'lfpg', 'eddf', 'lgav', 'lhbp', 'bikf', 'eidw', 'limc', 'bkpr', 'evra', 'eyvi', 'lmml', 'lukk', 'lypg', 'eham', 'lwsk', 'engm', 'epwa', 'lppt', 'lrop', 'ulli', 'likd', 'lybe', 'lzib', 'ljlj', 'lemd', 'essa', 'lszh', 'ukll', 'egll', 'eddb', 'lirf', 'uuee', 'lemg', 'egph')
order by country.name
;

--versio 2, vain 1 kenttä per maa
select airport.ident, airport.name, country.name, airport.municipality
from airport
left join country on airport.iso_country = country.iso_country
where ident in ('lati', 'loww', 'umms', 'ebbr', 'lqsa', 'lbvn', 'ldza', 'lkpr', 'ekch', 'eetn', 'ekvg', 'efhk', 'lfpg', 'lgav', 'lhbp', 'bikf', 'eidw', 'bkpr', 'evra', 'eyvi', 'lmml', 'lukk', 'lypg', 'eham', 'lwsk', 'engm', 'epwa', 'lppt', 'lrop', 'likd', 'lybe', 'lzib', 'ljlj', 'lemd', 'essa', 'lszh', 'ukll', 'egll', 'eddb', 'lirf', 'uuee')
order by country.name
;

--luodaan uusi taulu:

CREATE TABLE `kentat` (
  `id` int(11) NOT NULL,
  `ident` varchar(40) NOT NULL,
  `type` varchar(40) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `latitude_deg` double DEFAULT NULL,
  `longitude_deg` double DEFAULT NULL,
  `elevation_ft` int(11) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `iso_country` varchar(40) DEFAULT NULL,
  `iso_region` varchar(40) DEFAULT NULL,
  `municipality` varchar(40) DEFAULT NULL,
  `scheduled_service` varchar(40) DEFAULT NULL,
  `gps_code` varchar(40) DEFAULT NULL,
  `iata_code` varchar(40) DEFAULT NULL,
  `local_code` varchar(40) DEFAULT NULL,
  `home_link` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ident`),
  KEY `iso_country` (`iso_country`),
    CONSTRAINT `kentat_ibfk_1` FOREIGN KEY (`iso_country`) REFERENCES `country` (`iso_country`)
  );

--syötetään:
insert into kentat
select  id,
  ident,
  type,
  airport.name,
  latitude_deg,
  longitude_deg,
  elevation_ft,
  airport.continent,
  airport.iso_country,
  iso_region,
  municipality,
  scheduled_service,
  gps_code,
  iata_code,
  local_code,
  home_link,
  airport.wikipedia_link,
  airport.keywords

from airport
left join country on airport.iso_country = country.iso_country
where ident in ('lati', 'loww', 'umms', 'ebbr', 'lqsa', 'lbvn', 'ldza', 'lkpr', 'ekch', 'eetn', 'ekvg', 'efhk', 'lfpg', 'lgav', 'lhbp', 'bikf', 'eidw', 'bkpr', 'evra', 'eyvi', 'lmml', 'lukk', 'lypg', 'eham', 'lwsk', 'engm', 'epwa', 'lppt', 'lrop', 'likd', 'lybe', 'lzib', 'ljlj', 'lemd', 'essa', 'lszh', 'ukll', 'egll', 'eddb', 'lirf', 'uuee')
;


----
--   kentat taulusta maa nimi järjestys
select country.name, kentat.municipality, kentat.name, kentat.ident
from kentat
left join country on kentat.iso_country = country.iso_country
order by country.name;

--

alter table kentat
add column country_fi varchar(40) NULL;


----

select id from game where id in (select max(id) from game);

UPDATE game
SET game.location = 'EETN',
game.money = '1500.0',
game.co2 = '0.0',
game.money_gained = '0.0',
game.money_spent = '0.0',
game.distance = '0.0',
game.flights = '0'
WHERE game.id = '41';


SELECT * from goal WHERE game_id = '{game_id}'