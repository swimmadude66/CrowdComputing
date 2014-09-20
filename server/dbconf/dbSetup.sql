CREATE DATABASE CrowdComputing;
USE CrowdComputing;

CREATE TABLE UserInfo
(
    UserID          INT             NOT NULL    AUTO_INCREMENT  ,
    userName        VARCHAR(50)     NOT NULL                ,
    thePassword     VARCHAR(50)     NOT NULL                ,
    CONSTRAINT pk_InfoUserID                PRIMARY KEY (UserID)
);