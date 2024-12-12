
--Muokkaus 1:
--Lisätään kentat tauluun sarake country_fi jossa on maan nimi suomeksi.
--Siltä varalta, että tarvitaan myöhemmin.
alter table kentat
add column country_fi varchar(40) NULL;


UPDATE kentat SET country_fi = 'Afganistan' WHERE iso_country = 'AF';
UPDATE kentat SET country_fi = 'Ahvenanmaa' WHERE iso_country = 'AX';
UPDATE kentat SET country_fi = 'Alankomaat' WHERE iso_country = 'NL';
UPDATE kentat SET country_fi = 'Alankomaiden Karibia' WHERE iso_country = 'BQ';
UPDATE kentat SET country_fi = 'Albania' WHERE iso_country = 'AL';
UPDATE kentat SET country_fi = 'Algeria' WHERE iso_country = 'DZ';
UPDATE kentat SET country_fi = 'Amerikan Samoa' WHERE iso_country = 'AS';
UPDATE kentat SET country_fi = 'Andorra' WHERE iso_country = 'AD';
UPDATE kentat SET country_fi = 'Angola' WHERE iso_country = 'AO';
UPDATE kentat SET country_fi = 'Anguilla' WHERE iso_country = 'AI';
UPDATE kentat SET country_fi = 'Antarktis' WHERE iso_country = 'AQ';
UPDATE kentat SET country_fi = 'Antigua ja Barbuda' WHERE iso_country = 'AG';
UPDATE kentat SET country_fi = 'Arabiemiirikunnat' WHERE iso_country = 'AE';
UPDATE kentat SET country_fi = 'Argentiina' WHERE iso_country = 'AR';
UPDATE kentat SET country_fi = 'Armenia' WHERE iso_country = 'AM';
UPDATE kentat SET country_fi = 'Aruba' WHERE iso_country = 'AW';
UPDATE kentat SET country_fi = 'Australia' WHERE iso_country = 'AU';
UPDATE kentat SET country_fi = 'Azerbaid?an' WHERE iso_country = 'AZ';
UPDATE kentat SET country_fi = 'Bahama' WHERE iso_country = 'BS';
UPDATE kentat SET country_fi = 'Bahrain' WHERE iso_country = 'BH';
UPDATE kentat SET country_fi = 'Bangladesh' WHERE iso_country = 'BD';
UPDATE kentat SET country_fi = 'Barbados' WHERE iso_country = 'BB';
UPDATE kentat SET country_fi = 'Belgia' WHERE iso_country = 'BE';
UPDATE kentat SET country_fi = 'Belize' WHERE iso_country = 'BZ';
UPDATE kentat SET country_fi = 'Benin' WHERE iso_country = 'BJ';
UPDATE kentat SET country_fi = 'Bermuda' WHERE iso_country = 'BM';
UPDATE kentat SET country_fi = 'Bhutan' WHERE iso_country = 'BT';
UPDATE kentat SET country_fi = 'Bolivia' WHERE iso_country = 'BO';
UPDATE kentat SET country_fi = 'Bosnia ja Hertsegovina' WHERE iso_country = 'BA';
UPDATE kentat SET country_fi = 'Botswana' WHERE iso_country = 'BW';
UPDATE kentat SET country_fi = 'Bouvet?nsaari' WHERE iso_country = 'BV';
UPDATE kentat SET country_fi = 'Brasilia' WHERE iso_country = 'BR';
UPDATE kentat SET country_fi = 'Brittil?inen Intian valtameren alue' WHERE iso_country = 'IO';
UPDATE kentat SET country_fi = 'Brittil?iset Neitsytsaaret' WHERE iso_country = 'VG';
UPDATE kentat SET country_fi = 'Brunei' WHERE iso_country = 'BN';
UPDATE kentat SET country_fi = 'Bulgaria' WHERE iso_country = 'BG';
UPDATE kentat SET country_fi = 'Burkina Faso' WHERE iso_country = 'BF';
UPDATE kentat SET country_fi = 'Burundi' WHERE iso_country = 'BI';
UPDATE kentat SET country_fi = 'Caymansaaret' WHERE iso_country = 'KY';
UPDATE kentat SET country_fi = 'Chile' WHERE iso_country = 'CL';
UPDATE kentat SET country_fi = 'Cookinsaaret' WHERE iso_country = 'CK';
UPDATE kentat SET country_fi = 'Costa Rica' WHERE iso_country = 'CR';
UPDATE kentat SET country_fi = 'Cura?ao' WHERE iso_country = 'CW';
UPDATE kentat SET country_fi = 'Djibouti' WHERE iso_country = 'DJ';
UPDATE kentat SET country_fi = 'Dominica' WHERE iso_country = 'DM';
UPDATE kentat SET country_fi = 'Dominikaaninen tasavalta' WHERE iso_country = 'DO';
UPDATE kentat SET country_fi = 'Ecuador' WHERE iso_country = 'EC';
UPDATE kentat SET country_fi = 'Egypti' WHERE iso_country = 'EG';
UPDATE kentat SET country_fi = 'El Salvador' WHERE iso_country = 'SV';
UPDATE kentat SET country_fi = 'Eritrea' WHERE iso_country = 'ER';
UPDATE kentat SET country_fi = 'Espanja' WHERE iso_country = 'ES';
UPDATE kentat SET country_fi = 'Etiopia' WHERE iso_country = 'ET';
UPDATE kentat SET country_fi = 'Etel?-Afrikka' WHERE iso_country = 'ZA';
UPDATE kentat SET country_fi = 'Etel?-Georgia ja Etel?iset Sandwichsaaret' WHERE iso_country = 'GS';
UPDATE kentat SET country_fi = 'Etel?-Sudan' WHERE iso_country = 'SS';
UPDATE kentat SET country_fi = 'Falklandinsaaret' WHERE iso_country = 'FK';
UPDATE kentat SET country_fi = 'F?rsaaret' WHERE iso_country = 'FO';
UPDATE kentat SET country_fi = 'Fid?i' WHERE iso_country = 'FJ';
UPDATE kentat SET country_fi = 'Filippiinit' WHERE iso_country = 'PH';
UPDATE kentat SET country_fi = 'Gabon' WHERE iso_country = 'GA';
UPDATE kentat SET country_fi = 'Gambia' WHERE iso_country = 'GM';
UPDATE kentat SET country_fi = 'Georgia' WHERE iso_country = 'GE';
UPDATE kentat SET country_fi = 'Ghana' WHERE iso_country = 'GH';
UPDATE kentat SET country_fi = 'Gibraltar' WHERE iso_country = 'GI';
UPDATE kentat SET country_fi = 'Grenada' WHERE iso_country = 'GD';
UPDATE kentat SET country_fi = 'Gr?nlanti' WHERE iso_country = 'GL';
UPDATE kentat SET country_fi = 'Guadeloupe' WHERE iso_country = 'GP';
UPDATE kentat SET country_fi = 'Guam' WHERE iso_country = 'GU';
UPDATE kentat SET country_fi = 'Guatemala' WHERE iso_country = 'GT';
UPDATE kentat SET country_fi = 'Guernsey' WHERE iso_country = 'GG';
UPDATE kentat SET country_fi = 'Guinea' WHERE iso_country = 'GN';
UPDATE kentat SET country_fi = 'Guinea-Bissau' WHERE iso_country = 'GW';
UPDATE kentat SET country_fi = 'Guyana' WHERE iso_country = 'GY';
UPDATE kentat SET country_fi = 'Haiti' WHERE iso_country = 'HT';
UPDATE kentat SET country_fi = 'Heard ja McDonaldinsaaret' WHERE iso_country = 'HM';
UPDATE kentat SET country_fi = 'Honduras' WHERE iso_country = 'HN';
UPDATE kentat SET country_fi = 'Hongkong' WHERE iso_country = 'HK';
UPDATE kentat SET country_fi = 'Indonesia' WHERE iso_country = 'ID';
UPDATE kentat SET country_fi = 'Intia' WHERE iso_country = 'IN';
UPDATE kentat SET country_fi = 'Irak' WHERE iso_country = 'IQ';
UPDATE kentat SET country_fi = 'Iran' WHERE iso_country = 'IR';
UPDATE kentat SET country_fi = 'Irlanti' WHERE iso_country = 'IE';
UPDATE kentat SET country_fi = 'Islanti' WHERE iso_country = 'IS';
UPDATE kentat SET country_fi = 'Israel' WHERE iso_country = 'IL';
UPDATE kentat SET country_fi = 'Italia' WHERE iso_country = 'IT';
UPDATE kentat SET country_fi = 'It?-Timor' WHERE iso_country = 'TL';
UPDATE kentat SET country_fi = 'It?valta' WHERE iso_country = 'AT';
UPDATE kentat SET country_fi = 'Jamaika' WHERE iso_country = 'JM';
UPDATE kentat SET country_fi = 'Japani' WHERE iso_country = 'JP';
UPDATE kentat SET country_fi = 'Jemen' WHERE iso_country = 'YE';
UPDATE kentat SET country_fi = 'Jersey' WHERE iso_country = 'JE';
UPDATE kentat SET country_fi = 'Jordania' WHERE iso_country = 'JO';
UPDATE kentat SET country_fi = 'Joulusaari' WHERE iso_country = 'CX';
UPDATE kentat SET country_fi = 'Kambod?a' WHERE iso_country = 'KH';
UPDATE kentat SET country_fi = 'Kamerun' WHERE iso_country = 'CM';
UPDATE kentat SET country_fi = 'Kanada' WHERE iso_country = 'CA';
UPDATE kentat SET country_fi = 'Kap Verde' WHERE iso_country = 'CV';
UPDATE kentat SET country_fi = 'Kazakstan' WHERE iso_country = 'KZ';
UPDATE kentat SET country_fi = 'Kenia' WHERE iso_country = 'KE';
UPDATE kentat SET country_fi = 'Keski-Afrikan tasavalta' WHERE iso_country = 'CF';
UPDATE kentat SET country_fi = 'Kiina' WHERE iso_country = 'CN';
UPDATE kentat SET country_fi = 'Kirgisia' WHERE iso_country = 'KG';
UPDATE kentat SET country_fi = 'Kiribati' WHERE iso_country = 'KI';
UPDATE kentat SET country_fi = 'Kolumbia' WHERE iso_country = 'CO';
UPDATE kentat SET country_fi = 'Komorit' WHERE iso_country = 'KM';
UPDATE kentat SET country_fi = 'Kongon demokraattinen tasavalta' WHERE iso_country = 'CD';
UPDATE kentat SET country_fi = 'Kongon tasavalta' WHERE iso_country = 'CG';
UPDATE kentat SET country_fi = 'Kookossaaret' WHERE iso_country = 'CC';
UPDATE kentat SET country_fi = 'Korean demokraattinen kansantasavalta' WHERE iso_country = 'KP';
UPDATE kentat SET country_fi = 'Korean tasavalta' WHERE iso_country = 'KR';
UPDATE kentat SET country_fi = 'Kreikka' WHERE iso_country = 'GR';
UPDATE kentat SET country_fi = 'Kroatia' WHERE iso_country = 'HR';
UPDATE kentat SET country_fi = 'Kuuba' WHERE iso_country = 'CU';
UPDATE kentat SET country_fi = 'Kuwait' WHERE iso_country = 'KW';
UPDATE kentat SET country_fi = 'Kypros' WHERE iso_country = 'CY';
UPDATE kentat SET country_fi = 'Laos' WHERE iso_country = 'LA';
UPDATE kentat SET country_fi = 'Latvia' WHERE iso_country = 'LV';
UPDATE kentat SET country_fi = 'Lesotho' WHERE iso_country = 'LS';
UPDATE kentat SET country_fi = 'Libanon' WHERE iso_country = 'LB';
UPDATE kentat SET country_fi = 'Liberia' WHERE iso_country = 'LR';
UPDATE kentat SET country_fi = 'Libya' WHERE iso_country = 'LY';
UPDATE kentat SET country_fi = 'Liechtenstein' WHERE iso_country = 'LI';
UPDATE kentat SET country_fi = 'Liettua' WHERE iso_country = 'LT';
UPDATE kentat SET country_fi = 'Luxemburg' WHERE iso_country = 'LU';
UPDATE kentat SET country_fi = 'L?nsi-Sahara' WHERE iso_country = 'EH';
UPDATE kentat SET country_fi = 'Macao' WHERE iso_country = 'MO';
UPDATE kentat SET country_fi = 'Madagaskar' WHERE iso_country = 'MG';
UPDATE kentat SET country_fi = 'Malawi' WHERE iso_country = 'MW';
UPDATE kentat SET country_fi = 'Malediivit' WHERE iso_country = 'MV';
UPDATE kentat SET country_fi = 'Malesia' WHERE iso_country = 'MY';
UPDATE kentat SET country_fi = 'Mali' WHERE iso_country = 'ML';
UPDATE kentat SET country_fi = 'Malta' WHERE iso_country = 'MT';
UPDATE kentat SET country_fi = 'Mansaari' WHERE iso_country = 'IM';
UPDATE kentat SET country_fi = 'Marokko' WHERE iso_country = 'MA';
UPDATE kentat SET country_fi = 'Marshallinsaaret' WHERE iso_country = 'MH';
UPDATE kentat SET country_fi = 'Martinique' WHERE iso_country = 'MQ';
UPDATE kentat SET country_fi = 'Mauritania' WHERE iso_country = 'MR';
UPDATE kentat SET country_fi = 'Mauritius' WHERE iso_country = 'MU';
UPDATE kentat SET country_fi = 'Mayotte' WHERE iso_country = 'YT';
UPDATE kentat SET country_fi = 'Meksiko' WHERE iso_country = 'MX';
UPDATE kentat SET country_fi = 'Mikronesian liittovaltio' WHERE iso_country = 'FM';
UPDATE kentat SET country_fi = 'Moldova' WHERE iso_country = 'MD';
UPDATE kentat SET country_fi = 'Monaco' WHERE iso_country = 'MC';
UPDATE kentat SET country_fi = 'Mongolia' WHERE iso_country = 'MN';
UPDATE kentat SET country_fi = 'Montenegro' WHERE iso_country = 'ME';
UPDATE kentat SET country_fi = 'Montserrat' WHERE iso_country = 'MS';
UPDATE kentat SET country_fi = 'Mosambik' WHERE iso_country = 'MZ';
UPDATE kentat SET country_fi = 'Myanmar' WHERE iso_country = 'MM';
UPDATE kentat SET country_fi = 'Namibia' WHERE iso_country = 'NA';
UPDATE kentat SET country_fi = 'Nauru' WHERE iso_country = 'NR';
UPDATE kentat SET country_fi = 'Nepal' WHERE iso_country = 'NP';
UPDATE kentat SET country_fi = 'Nicaragua' WHERE iso_country = 'NI';
UPDATE kentat SET country_fi = 'Niger' WHERE iso_country = 'NE';
UPDATE kentat SET country_fi = 'Nigeria' WHERE iso_country = 'NG';
UPDATE kentat SET country_fi = 'Niue' WHERE iso_country = 'NU';
UPDATE kentat SET country_fi = 'Norfolkinsaari' WHERE iso_country = 'NF';
UPDATE kentat SET country_fi = 'Norja' WHERE iso_country = 'NO';
UPDATE kentat SET country_fi = 'Norsunluurannikko' WHERE iso_country = 'CI';
UPDATE kentat SET country_fi = 'Oman' WHERE iso_country = 'OM';
UPDATE kentat SET country_fi = 'Pakistan' WHERE iso_country = 'PK';
UPDATE kentat SET country_fi = 'Palau' WHERE iso_country = 'PW';
UPDATE kentat SET country_fi = 'Palestiina' WHERE iso_country = 'PS';
UPDATE kentat SET country_fi = 'Panama' WHERE iso_country = 'PA';
UPDATE kentat SET country_fi = 'Papua-Uusi-Guinea' WHERE iso_country = 'PG';
UPDATE kentat SET country_fi = 'Paraguay' WHERE iso_country = 'PY';
UPDATE kentat SET country_fi = 'Peru' WHERE iso_country = 'PE';
UPDATE kentat SET country_fi = 'Pohjois-Mariaanit' WHERE iso_country = 'MP';
UPDATE kentat SET country_fi = 'Pitcairn' WHERE iso_country = 'PN';
UPDATE kentat SET country_fi = 'Pohjois-Makedonia' WHERE iso_country = 'MK';
UPDATE kentat SET country_fi = 'Portugali' WHERE iso_country = 'PT';
UPDATE kentat SET country_fi = 'Puerto Rico' WHERE iso_country = 'PR';
UPDATE kentat SET country_fi = 'Puola' WHERE iso_country = 'PL';
UPDATE kentat SET country_fi = 'P?iv?ntasaajan Guinea' WHERE iso_country = 'GQ';
UPDATE kentat SET country_fi = 'Qatar' WHERE iso_country = 'QA';
UPDATE kentat SET country_fi = 'Ranska' WHERE iso_country = 'FR';
UPDATE kentat SET country_fi = 'Ranskan etel?iset alueet' WHERE iso_country = 'TF';
UPDATE kentat SET country_fi = 'Ranskan Guayana' WHERE iso_country = 'GF';
UPDATE kentat SET country_fi = 'Ranskan Polynesia' WHERE iso_country = 'PF';
UPDATE kentat SET country_fi = 'R?union' WHERE iso_country = 'RE';
UPDATE kentat SET country_fi = 'Romania' WHERE iso_country = 'RO';
UPDATE kentat SET country_fi = 'Ruanda' WHERE iso_country = 'RW';
UPDATE kentat SET country_fi = 'Ruotsi' WHERE iso_country = 'SE';
UPDATE kentat SET country_fi = 'Saint Barth?lemy' WHERE iso_country = 'BL';
UPDATE kentat SET country_fi = 'Saint Helena, Ascension ja Tristan da Cunha' WHERE iso_country = 'SH';
UPDATE kentat SET country_fi = 'Saint Kitts ja Nevis' WHERE iso_country = 'KN';
UPDATE kentat SET country_fi = 'Saint Lucia' WHERE iso_country = 'LC';
UPDATE kentat SET country_fi = 'Saint Martin (Ranska)' WHERE iso_country = 'MF';
UPDATE kentat SET country_fi = 'Saint-Pierre ja Miquelon' WHERE iso_country = 'PM';
UPDATE kentat SET country_fi = 'Saint Vincent ja Grenadiinit' WHERE iso_country = 'VC';
UPDATE kentat SET country_fi = 'Saksa' WHERE iso_country = 'DE';
UPDATE kentat SET country_fi = 'Salomonsaaret' WHERE iso_country = 'SB';
UPDATE kentat SET country_fi = 'Sambia' WHERE iso_country = 'ZM';
UPDATE kentat SET country_fi = 'Samoa' WHERE iso_country = 'WS';
UPDATE kentat SET country_fi = 'San Marino' WHERE iso_country = 'SM';
UPDATE kentat SET country_fi = 'S?o Tom? ja Pr?ncipe' WHERE iso_country = 'ST';
UPDATE kentat SET country_fi = 'Saudi-Arabia' WHERE iso_country = 'SA';
UPDATE kentat SET country_fi = 'Senegal' WHERE iso_country = 'SN';
UPDATE kentat SET country_fi = 'Serbia' WHERE iso_country = 'RS';
UPDATE kentat SET country_fi = 'Seychellit' WHERE iso_country = 'SC';
UPDATE kentat SET country_fi = 'Sierra Leone' WHERE iso_country = 'SL';
UPDATE kentat SET country_fi = 'Singapore' WHERE iso_country = 'SG';
UPDATE kentat SET country_fi = 'Sint Maarten (Alankomaat)' WHERE iso_country = 'SX';
UPDATE kentat SET country_fi = 'Slovakia' WHERE iso_country = 'SK';
UPDATE kentat SET country_fi = 'Slovenia' WHERE iso_country = 'SI';
UPDATE kentat SET country_fi = 'Somalia' WHERE iso_country = 'SO';
UPDATE kentat SET country_fi = 'Sri Lanka' WHERE iso_country = 'LK';
UPDATE kentat SET country_fi = 'Sudan' WHERE iso_country = 'SD';
UPDATE kentat SET country_fi = 'Suomi' WHERE iso_country = 'FI';
UPDATE kentat SET country_fi = 'Suriname' WHERE iso_country = 'SR';
UPDATE kentat SET country_fi = 'Svalbard ja Jan Mayen' WHERE iso_country = 'SJ';
UPDATE kentat SET country_fi = 'Swazimaa' WHERE iso_country = 'SZ';
UPDATE kentat SET country_fi = 'Sveitsi' WHERE iso_country = 'CH';
UPDATE kentat SET country_fi = 'Syyria' WHERE iso_country = 'SY';
UPDATE kentat SET country_fi = 'Tad?ikistan' WHERE iso_country = 'TJ';
UPDATE kentat SET country_fi = 'Taiwan' WHERE iso_country = 'TW';
UPDATE kentat SET country_fi = 'Tansania' WHERE iso_country = 'TZ';
UPDATE kentat SET country_fi = 'Tanska' WHERE iso_country = 'DK';
UPDATE kentat SET country_fi = 'Thaimaa' WHERE iso_country = 'TH';
UPDATE kentat SET country_fi = 'Togo' WHERE iso_country = 'TG';
UPDATE kentat SET country_fi = 'Tokelau' WHERE iso_country = 'TK';
UPDATE kentat SET country_fi = 'Tonga' WHERE iso_country = 'TO';
UPDATE kentat SET country_fi = 'Trinidad ja Tobago' WHERE iso_country = 'TT';
UPDATE kentat SET country_fi = 'T?ad' WHERE iso_country = 'TD';
UPDATE kentat SET country_fi = 'T?ekki' WHERE iso_country = 'CZ';
UPDATE kentat SET country_fi = 'Tunisia' WHERE iso_country = 'TN';
UPDATE kentat SET country_fi = 'Turkki' WHERE iso_country = 'TR';
UPDATE kentat SET country_fi = 'Turkmenistan' WHERE iso_country = 'TM';
UPDATE kentat SET country_fi = 'Turks- ja Caicossaaret' WHERE iso_country = 'TC';
UPDATE kentat SET country_fi = 'Tuvalu' WHERE iso_country = 'TV';
UPDATE kentat SET country_fi = 'Uganda' WHERE iso_country = 'UG';
UPDATE kentat SET country_fi = 'Ukraina' WHERE iso_country = 'UA';
UPDATE kentat SET country_fi = 'Unkari' WHERE iso_country = 'HU';
UPDATE kentat SET country_fi = 'Uruguay' WHERE iso_country = 'UY';
UPDATE kentat SET country_fi = 'Uusi-Kaledonia' WHERE iso_country = 'NC';
UPDATE kentat SET country_fi = 'Uusi-Seelanti' WHERE iso_country = 'NZ';
UPDATE kentat SET country_fi = 'Uzbekistan' WHERE iso_country = 'UZ';
UPDATE kentat SET country_fi = 'Valko-Ven?j?' WHERE iso_country = 'BY';
UPDATE kentat SET country_fi = 'Vanuatu' WHERE iso_country = 'VU';
UPDATE kentat SET country_fi = 'Vatikaanivaltio?(Pyh? istuin)' WHERE iso_country = 'VA';
UPDATE kentat SET country_fi = 'Venezuela' WHERE iso_country = 'VE';
UPDATE kentat SET country_fi = 'Ven?j?' WHERE iso_country = 'RU';
UPDATE kentat SET country_fi = 'Vietnam' WHERE iso_country = 'VN';
UPDATE kentat SET country_fi = 'Viro' WHERE iso_country = 'EE';
UPDATE kentat SET country_fi = 'Wallis ja Futunasaaret' WHERE iso_country = 'WF';
UPDATE kentat SET country_fi = 'Yhdistynyt kuningaskunta' WHERE iso_country = 'GB';
UPDATE kentat SET country_fi = 'Yhdysvallat' WHERE iso_country = 'US';
UPDATE kentat SET country_fi = 'Yhdysvaltain Neitsytsaaret' WHERE iso_country = 'VI';
UPDATE kentat SET country_fi = 'Yhdysvaltain pienet erillissaaret' WHERE iso_country = 'UM';
UPDATE kentat SET country_fi = 'Zimbabwe' WHERE iso_country = 'ZW';
UPDATE kentat SET country_fi = 'Kosovo' WHERE iso_country = 'XK';


--Muokkaus 2:
--Lisätää kentat tauluun GDP ja syötetään arvot:

alter table kentat
add column GDP int;

UPDATE kentat SET GDP = '6' WHERE iso_country = 'AL';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'AD';
UPDATE kentat SET GDP = '54' WHERE iso_country = 'AT';
UPDATE kentat SET GDP = '10' WHERE iso_country = 'BY';
UPDATE kentat SET GDP = '50' WHERE iso_country = 'BE';
UPDATE kentat SET GDP = '7' WHERE iso_country = 'BA';
UPDATE kentat SET GDP = '11' WHERE iso_country = 'BG';
UPDATE kentat SET GDP = '16' WHERE iso_country = 'HR';
UPDATE kentat SET GDP = '26' WHERE iso_country = 'CZ';
UPDATE kentat SET GDP = '67' WHERE iso_country = 'DK';
UPDATE kentat SET GDP = '26' WHERE iso_country = 'EE';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'FO';
UPDATE kentat SET GDP = '56' WHERE iso_country = 'FI';
UPDATE kentat SET GDP = '45' WHERE iso_country = 'FR';
UPDATE kentat SET GDP = '54' WHERE iso_country = 'DE';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'GI';
UPDATE kentat SET GDP = '20' WHERE iso_country = 'GR';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'GG';
UPDATE kentat SET GDP = '18' WHERE iso_country = 'HU';
UPDATE kentat SET GDP = '72' WHERE iso_country = 'IS';
UPDATE kentat SET GDP = '95' WHERE iso_country = 'IE';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'IM';
UPDATE kentat SET GDP = '35' WHERE iso_country = 'IT';
UPDATE kentat SET GDP = '5' WHERE iso_country = 'JE';
UPDATE kentat SET GDP = '4' WHERE iso_country = 'XK';
UPDATE kentat SET GDP = '20' WHERE iso_country = 'LV';
UPDATE kentat SET GDP = '184' WHERE iso_country = 'LI';
UPDATE kentat SET GDP = '22' WHERE iso_country = 'LT';
UPDATE kentat SET GDP = '139' WHERE iso_country = 'LU';
UPDATE kentat SET GDP = '32' WHERE iso_country = 'MT';
UPDATE kentat SET GDP = '3' WHERE iso_country = 'MD';
UPDATE kentat SET GDP = '234' WHERE iso_country = 'MC';
UPDATE kentat SET GDP = '10' WHERE iso_country = 'ME';
UPDATE kentat SET GDP = '62' WHERE iso_country = 'NL';
UPDATE kentat SET GDP = '7' WHERE iso_country = 'MK';
UPDATE kentat SET GDP = '82' WHERE iso_country = 'NO';
UPDATE kentat SET GDP = '15' WHERE iso_country = 'PL';
UPDATE kentat SET GDP = '25' WHERE iso_country = 'PT';
UPDATE kentat SET GDP = '15' WHERE iso_country = 'RO';
UPDATE kentat SET GDP = '12' WHERE iso_country = 'RU';
UPDATE kentat SET GDP = '52' WHERE iso_country = 'SM';
UPDATE kentat SET GDP = '9' WHERE iso_country = 'RS';
UPDATE kentat SET GDP = '22' WHERE iso_country = 'SK';
UPDATE kentat SET GDP = '28' WHERE iso_country = 'SI';
UPDATE kentat SET GDP = '31' WHERE iso_country = 'ES';
UPDATE kentat SET GDP = '60' WHERE iso_country = 'SE';
UPDATE kentat SET GDP = '95' WHERE iso_country = 'CH';
UPDATE kentat SET GDP = '4' WHERE iso_country = 'UA';
UPDATE kentat SET GDP = '46' WHERE iso_country = 'GB';
UPDATE kentat SET GDP = '21' WHERE iso_country = 'VA';




--Muokkaus 3
--Kirjoitusasun muokkauksia

update kentat set country_fi = "Venäjä" where iso_country = "RU";
update kentat set country_fi = "Valko-Venäjä" where iso_country = "BY";
update kentat set country_fi = "Itävalta" where iso_country = "AT";
update kentat set country_fi = "Tsekki" where iso_country = "CZ";
update kentat set country_fi = "Färsaaret" where iso_country = "FO";



--Muokkaus 4
--Luodaan käyttäjä "Game" jolla tietokantaa käytetään.

CREATE USER game@localhost;
GRANT SELECT, INSERT, UPDATE ON flight_game.* to game@localhost;

--Muokkaus 5
--Tietokannan lopullinen muoto?

--Sallitaan taulujen poistaminen vierasavaimista huolimatta
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

--Poistetaan turhat taulut
DROP TABLE IF EXISTS country;
DROP TABLE IF EXISTS goal_reached;
DROP TABLE IF EXISTS airport;

--GOAL
DROP TABLE IF EXISTS goal;
CREATE TABLE goal (
    `game_id` int(10) NOT NULL,
    `ident` varchar(40) NOT NULL,
    `reached` int(1) NOT NULL,
PRIMARY KEY (game_id, ident),
KEY game_id (game_id),
KEY ident (ident)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

--GAME
DROP TABLE IF EXISTS game;
CREATE TABLE game
(
    `id`           int(10) NOT NULL auto_increment,
    `name`         varchar(40) NOT NULL,
    `location`     varchar(40) NOT NULL,
    `money`        FLOAT(10)   NOT NULL,
    `co2`          FLOAT(10)   NOT NULL,
    `money_gained` FLOAT(10)   NOT NULL,
    `money_spent`  FLOAT(10)   NOT NULL,
    `distance`     FLOAT(10)   NOT NULL,
    `flights`      INT(10) NOT NULL,
    PRIMARY KEY (id),
    KEY            location (location)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

--VISITED
DROP TABLE IF EXISTS visited;
CREATE TABLE visited
(
    `game_id` int(10) NOT NULL,
    `ident`   varchar(40) NOT NULL,
    PRIMARY KEY (game_id, ident),
    KEY       game_id (game_id),
    KEY       ident (ident)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


--- Muokkaus 6 poistetaan islanti ja färsaaret
DELETE FROM kentat WHERE iso_country = 'FO';
DELETE FROM kentat WHERE iso_country = 'IS';

--- Muokkaus 7 korjataan pristinan nimi

UPDATE kentat SET name = "Pristina Adem Jashari International" WHERE iso_country = "xk";
UPDATE kentat SET name = "Henri Coanda International Airport" WHERE iso_country = "RO";
UPDATE kentat SET name = "Humberto Delgado Airport" WHERE iso_country = "PT";
UPDATE kentat SET name = "Chisinau International Airport" WHERE iso_country = "MD";



