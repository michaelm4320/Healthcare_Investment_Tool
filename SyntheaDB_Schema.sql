
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Patient` (
  `Id` INT NOT NULL,
  `BirthDate` DATE NOT NULL,
  `DeathDate` DATE NULL,
  `SSN` VARCHAR(45) NOT NULL,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `Race` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Encounter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Encounter` (
  `Id` INT NOT NULL,
  `Start` DATE NOT NULL,
  `Stop` DATE NULL,
  `EncounterClass` VARCHAR(45) NOT NULL,
  `Code` VARCHAR(45) NULL,
  `Description` LONGTEXT NULL,
  `Base_Encounter_Cost` FLOAT NULL,
  `Total_Claim_Cost` FLOAT NULL,
  `Patient` INT NULL,
  PRIMARY KEY (`Id`),
  INDEX `Patient_idx` (`Patient` ASC) VISIBLE,
  CONSTRAINT `Patient`
    FOREIGN KEY (`Patient`)
    REFERENCES `mydb`.`Patient` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Condition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Condition` (
  `Start` DATE NOT NULL,
  `Stop` DATE NULL,
  `Patient` INT NOT NULL,
  `Encounter` INT NOT NULL,
  `Code` VARCHAR(45) NOT NULL,
  `Description` LONGTEXT NOT NULL,
  INDEX `Patient_idx` (`Patient` ASC) VISIBLE,
  INDEX `Encounter_idx` (`Encounter` ASC) VISIBLE,
  CONSTRAINT `Patient`
    FOREIGN KEY (`Patient`)
    REFERENCES `mydb`.`Patient` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Encounter`
    FOREIGN KEY (`Encounter`)
    REFERENCES `mydb`.`Encounter` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Medication`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Medication` (
  `Start` DATE NOT NULL,
  `Stop` DATE NULL,
  `Patient` INT NOT NULL,
  `Encounter` INT NOT NULL,
  `Code` VARCHAR(45) NOT NULL,
  `Description` MEDIUMTEXT NOT NULL,
  `Base_Cost` FLOAT NOT NULL,
  `Dispenses` INT NULL,
  `TotalCost` FLOAT NOT NULL,
  `ReasonCode` VARCHAR(45) NULL,
  `ReasonDescrption` MEDIUMTEXT NULL,
  INDEX `Patient_idx` (`Patient` ASC) VISIBLE,
  INDEX `Encounter_idx` (`Encounter` ASC) VISIBLE,
  CONSTRAINT `Patient`
    FOREIGN KEY (`Patient`)
    REFERENCES `mydb`.`Patient` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Encounter`
    FOREIGN KEY (`Encounter`)
    REFERENCES `mydb`.`Encounter` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Observation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Observation` (
  `Date` DATE NOT NULL,
  `Patient` INT NOT NULL,
  `Encounter` INT NOT NULL,
  `Category` VARCHAR(45) NULL,
  `Code` VARCHAR(45) NOT NULL,
  `Description` MEDIUMTEXT NULL,
  `Value` VARCHAR(45) NOT NULL,
  INDEX `Patient_idx` (`Patient` ASC) VISIBLE,
  INDEX `Encounter_idx` (`Encounter` ASC) VISIBLE,
  CONSTRAINT `Patient`
    FOREIGN KEY (`Patient`)
    REFERENCES `mydb`.`Patient` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Encounter`
    FOREIGN KEY (`Encounter`)
    REFERENCES `mydb`.`Encounter` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Procedure`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Procedure` (
  `Start` DATE NOT NULL,
  `Stop` DATE NULL,
  `Patient` INT NOT NULL,
  `Encounter` INT NOT NULL,
  `Code` VARCHAR(45) NOT NULL,
  `Description` MEDIUMTEXT NULL,
  `Base_Cost` FLOAT NOT NULL,
  `ReasonCode` VARCHAR(45) NULL,
  `ReasonDescription` MEDIUMTEXT NULL,
  INDEX `Patient_idx` (`Patient` ASC) VISIBLE,
  INDEX `Encounter_idx` (`Encounter` ASC) VISIBLE,
  CONSTRAINT `Patient`
    FOREIGN KEY (`Patient`)
    REFERENCES `mydb`.`Patient` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Encounter`
    FOREIGN KEY (`Encounter`)
    REFERENCES `mydb`.`Encounter` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Treatment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Treatment` (
)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
