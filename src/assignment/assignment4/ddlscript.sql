CREATE DATABASE IF NOT EXISTS `chatapp` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `chatapp`;

CREATE TABLE IF NOT EXISTS `connections` (
	`sessionid` varchar(50) NOT NULL ,
  	`ip` varchar(50) NOT NULL,
  	`email` varchar(50) NOT NULL,
  	`username` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `chatmessage` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
    `fk_sessionid` varchar(50) NOT NULL,
  	`sender` varchar(50) NOT NULL,
	 `message` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;