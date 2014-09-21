SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema crowdcomputing
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `crowdcomputing` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `crowdcomputing` ;

-- -----------------------------------------------------
-- Table `crowdcomputing`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`users` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `userName` VARCHAR(45) NOT NULL,
  `thePassword` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `idtable1_UNIQUE` (`user_id` ASC),
  UNIQUE INDEX `userName_UNIQUE` (`userName` ASC),
  UNIQUE INDEX `thePass_UNIQUE` (`thePassword` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crowdcomputing`.`clusters`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`clusters` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`clusters` (
  `cluster_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `idclusters_UNIQUE` (`cluster_id` ASC),
  PRIMARY KEY (`cluster_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crowdcomputing`.`nodes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`nodes` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`nodes` (
  `node_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `GUID` VARCHAR(45) NOT NULL,
  `publicKey` VARCHAR(45) NOT NULL,
  `IPaddress` VARCHAR(45) NOT NULL,
  `status` VARCHAR(45) BINARY NOT NULL,
  PRIMARY KEY (`node_id`),
  UNIQUE INDEX `idnodes_UNIQUE` (`node_id` ASC),
  UNIQUE INDEX `publicKey_UNIQUE` (`publicKey` ASC),
  UNIQUE INDEX `GUID_UNIQUE` (`GUID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crowdcomputing`.`groups`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`groups` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`groups` (
  `group_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`group_id`),
  UNIQUE INDEX `group_id_UNIQUE` (`group_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crowdcomputing`.`user_cluster`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`user_cluster` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`user_cluster` (
  `user_cluster_id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`user_cluster_id`),
  UNIQUE INDEX `user_cluster_id_UNIQUE` (`user_cluster_id` ASC),
  INDEX `fk_user_cluster_group_id_idx` (`group_id` ASC),
  INDEX `fk_user_cluster_group_id_idx1` (`user_id` ASC),
  CONSTRAINT `fk_user_cluster_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `crowdcomputing`.`groups` (`group_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_cluster_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `crowdcomputing`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crowdcomputing`.`group_cluster`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`group_cluster` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`group_cluster` (
  `group_cluster_id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `cluster_id` INT NOT NULL,
  PRIMARY KEY (`group_cluster_id`),
  UNIQUE INDEX `group_cluster_id_UNIQUE` (`group_cluster_id` ASC),
  INDEX `fk_group_cluster_group_id_idx` (`group_id` ASC),
  INDEX `fk_group_cluster_cluster_id_idx` (`cluster_id` ASC),
  CONSTRAINT `fk_group_cluster_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `crowdcomputing`.`groups` (`group_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_group_cluster_cluster_id`
    FOREIGN KEY (`cluster_id`)
    REFERENCES `crowdcomputing`.`clusters` (`cluster_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crowdcomputing`.`user_node`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`user_node` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`user_node` (
  `user_node_id` INT NOT NULL AUTO_INCREMENT,
  `node_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`user_node_id`),
  UNIQUE INDEX `user_node_id_UNIQUE` (`user_node_id` ASC),
  INDEX `fk_user_node_node_id_idx` (`node_id` ASC),
  INDEX `fk_user_node_user_id_idx` (`user_id` ASC),
  CONSTRAINT `fk_user_node_node_id`
    FOREIGN KEY (`node_id`)
    REFERENCES `crowdcomputing`.`nodes` (`node_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_node_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `crowdcomputing`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crowdcomputing`.`cluster_node`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crowdcomputing`.`cluster_node` ;

CREATE TABLE IF NOT EXISTS `crowdcomputing`.`cluster_node` (
  `cluster_node_id` INT NOT NULL AUTO_INCREMENT,
  `cluster_id` INT NOT NULL,
  `node_id` INT NOT NULL,
  PRIMARY KEY (`cluster_node_id`),
  UNIQUE INDEX `cluster_node_id_UNIQUE` (`cluster_node_id` ASC),
  INDEX `fk_cluster_node_node_id_idx` (`node_id` ASC),
  INDEX `fk_cluster_node_cluster_id_idx` (`cluster_id` ASC),
  CONSTRAINT `fk_cluster_node_node_id`
    FOREIGN KEY (`node_id`)
    REFERENCES `crowdcomputing`.`nodes` (`node_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cluster_node_cluster_id`
    FOREIGN KEY (`cluster_id`)
    REFERENCES `crowdcomputing`.`clusters` (`cluster_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
