--Luodaan uusi taulu Kentat:

DROP TABLE IF EXISTS kentat;
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
  PRIMARY KEY (`ident`)

    );

--Syötetään halutut kentät:
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
