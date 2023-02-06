/*
    Title: db_init.sql
    Author: Rebecca Robinson
    Date: 01.26.23
    Description: Pysports Starting Database
*/

-- drop for duplication protection
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create user
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'M662Lhmi2U!-BK&B';

-- apply priveleges to user for database
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop table for duplicate protection
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create team tables 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create player tables and foreign keys
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Enterprise', 'Starfleet');

INSERT INTO team(team_name, mascot)
    VALUES('Team Bortas', 'Klingon Honor Guard');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Jean Luc', 'Picard', (SELECT team_id FROM team WHERE team_name = 'Team Enterprise'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('William', 'Riker', (SELECT team_id FROM team WHERE team_name = 'Team Enterprise'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Deanna', 'Troi', (SELECT team_id FROM team WHERE team_name = 'Team Enterprise'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Chancellor', 'Gowron', (SELECT team_id FROM team WHERE team_name = 'Team Bortas'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('General', 'Chang', (SELECT team_id FROM team WHERE team_name = 'Team Bortas'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Commander', 'Kruge', (SELECT team_id FROM team WHERE team_name = 'Team Bortas'));

