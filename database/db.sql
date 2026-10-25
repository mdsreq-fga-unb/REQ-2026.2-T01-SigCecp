-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dbSigCecp
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dbSigCecp
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbSigCecp` DEFAULT CHARACTER SET utf8 ;
USE `dbSigCecp` ;

-- -----------------------------------------------------
-- Table `dbSigCecp`.`Conteudo_Publicado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbSigCecp`.`Conteudo_Publicado` (
  `num_conteudo` INT NOT NULL AUTO_INCREMENT,
  `titulo_conteudo` VARCHAR(100) NOT NULL,
  `descricao_publicacao` TEXT NULL,
  `data_publicacao_conteudo` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`num_conteudo`),
  UNIQUE INDEX `Num_publicacao_UNIQUE` (`num_conteudo` ASC) VISIBLE,
  UNIQUE INDEX `Titulo_publicacao_UNIQUE` (`titulo_conteudo` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbSigCecp`.`Midia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbSigCecp`.`Midia` (
  `id_midia` INT NOT NULL AUTO_INCREMENT,
  `URL_midia` TEXT NOT NULL,
  `tipo_midia` TINYINT NOT NULL,
  PRIMARY KEY (`id_midia`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbSigCecp`.`Evento_Publicado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbSigCecp`.`Evento_Publicado` (
  `num_evento` INT NOT NULL AUTO_INCREMENT,
  `titulo_evento` VARCHAR(100) NOT NULL,
  `descricao_evento` TEXT NOT NULL,
  `data_evento` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data_publicacao_evento` DATETIME NOT NULL,
  `titulo_publicacao` VARCHAR(45) NOT NULL,
  `subtitulo_evento` VARCHAR(45) NOT NULL,
  `local_evento` VARCHAR(100) NOT NULL,
  `horario_inicio` VARCHAR(4) NOT NULL,
  `horario_fim` VARCHAR(4) NOT NULL,
  `alimentacao` TINYINT NOT NULL,
  `pesagem` TINYINT NOT NULL,
  PRIMARY KEY (`num_evento`),
  UNIQUE INDEX `Num_publicacao_UNIQUE` (`num_evento` ASC) VISIBLE,
  UNIQUE INDEX `Titulo_publicacao_UNIQUE` (`titulo_evento` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbSigCecp`.`Conteudo_Publicado_has_Midia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbSigCecp`.`Conteudo_Publicado_has_Midia` (
  `Conteudo_Publicado_num_conteudo` INT NOT NULL,
  `Midia_id_midia` INT NOT NULL,
  PRIMARY KEY (`Conteudo_Publicado_num_conteudo`, `Midia_id_midia`),
  INDEX `fk_Conteudo_Publicado_has_Midia_Midia1_idx` (`Midia_id_midia` ASC) VISIBLE,
  INDEX `fk_Conteudo_Publicado_has_Midia_Conteudo_Publicado_idx` (`Conteudo_Publicado_num_conteudo` ASC) VISIBLE,
  CONSTRAINT `fk_Conteudo_Publicado_has_Midia_Conteudo_Publicado`
    FOREIGN KEY (`Conteudo_Publicado_num_conteudo`)
    REFERENCES `dbSigCecp`.`Conteudo_Publicado` (`num_conteudo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Conteudo_Publicado_has_Midia_Midia1`
    FOREIGN KEY (`Midia_id_midia`)
    REFERENCES `dbSigCecp`.`Midia` (`id_midia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbSigCecp`.`Cobranca_evento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbSigCecp`.`Cobranca_evento` (
  `Evento_Publicado_num_evento` INT NOT NULL,
  `evento_cobrado` TINYINT NOT NULL,
  `preco_evento` REAL NULL,
  `data_limite_pagamento` DATE NULL,
  `forma_pagamento` ENUM("PIX", "CARTÃO DE CREDITO", "CARTÃO DE DEBITO", "BOLETO", "TRANSFERENCIA", "TODAS") NULL,
  PRIMARY KEY (`Evento_Publicado_num_evento`),
  CONSTRAINT `fk_Cobranca_evento_Evento_Publicado1`
    FOREIGN KEY (`Evento_Publicado_num_evento`)
    REFERENCES `dbSigCecp`.`Evento_Publicado` (`num_evento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbSigCecp`.`Midia_has_Evento_Publicado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbSigCecp`.`Midia_has_Evento_Publicado` (
  `Midia_id_midia` INT NOT NULL,
  `Evento_Publicado_num_evento` INT NOT NULL,
  PRIMARY KEY (`Midia_id_midia`, `Evento_Publicado_num_evento`),
  INDEX `fk_Midia_has_Evento_Publicado_Evento_Publicado1_idx` (`Evento_Publicado_num_evento` ASC) VISIBLE,
  INDEX `fk_Midia_has_Evento_Publicado_Midia1_idx` (`Midia_id_midia` ASC) VISIBLE,
  CONSTRAINT `fk_Midia_has_Evento_Publicado_Midia1`
    FOREIGN KEY (`Midia_id_midia`)
    REFERENCES `dbSigCecp`.`Midia` (`id_midia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Midia_has_Evento_Publicado_Evento_Publicado1`
    FOREIGN KEY (`Evento_Publicado_num_evento`)
    REFERENCES `dbSigCecp`.`Evento_Publicado` (`num_evento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
