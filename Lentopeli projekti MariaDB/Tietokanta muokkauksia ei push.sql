-- kirjoitusasun muokkauksia

update kentat set country_fi = "Venäjä" where iso_country = "RU";
update kentat set country_fi = "Valko-Venäjä" where iso_country = "BY";
update kentat set country_fi = "Itävalta" where iso_country = "AT";
update kentat set country_fi = "Tsekki" where iso_country = "CZ";
update kentat set country_fi = "Färsaaret" where iso_country = "FO";


----

SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;


-- Uudet taulut

DROP TABLE IF EXISTS "visited";
CREATE TABLE "visited" (
  `game_id` int(10) NOT NULL,
  `ident` varchar(40) NOT NULL,
PRIMARY KEY ("game_id", "ident"),
KEY "game_id" ("game_id"),
KEY "ident" ("ident"),
CONSTRAINT `visited_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
CONSTRAINT `visited_ibfk_2` FOREIGN KEY (`ident`) REFERENCES `kentat` (`ident`)
  );


DROP TABLE IF EXISTS "game";
CREATE TABLE "game" (
    `id` int(10) NOT NULL,
    `name` varchar(40) NOT NULL,
    `location` varchar(40) NOT NULL,
    `money` FLOAT(10) NOT NULL,
    `co2` FLOAT(10) NOT NULL,
    `money_gained` FLOAT(10) NOT NULL,
    `money_spent` FLOAT(10) NOT NULL,
    `distance` FLOAT(10) NOT NULL,
    `flights` INT(10) NOT NULL,
PRIMARY KEY ("id"),
KEY "location" ("location"),
CONSTRAINT `game_ibfk_1` FOREIGN KEY (`location`) REFERENCES `kentat` (`ident`)
  );


DROP TABLE IF EXISTS goal;
CREATE TABLE goal (
    `game_id` int(10) NOT NULL,
    `ident` varchar(40) NOT NULL,
    `reached` int(10) NOT NULL,
PRIMARY KEY (game_id, ident),
KEY game_id (game_id),
KEY ident (ident),
CONSTRAINT goal_ibfk_1 FOREIGN KEY (`game_id`) REFERENCES game (id),
CONSTRAINT `goal_ibfk_2` FOREIGN KEY (`ident`) REFERENCES kentat (`ident`)
  );

---- EI TOIMI --- TEEN NÄMÄ ILMAN CONSTRAINTTEJA !

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
    `id`           int(10) NOT NULL,
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


