/*
Navicat MySQL Data Transfer

Source Server         : 本机
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : pylearn

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2018-11-09 14:10:12
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for segment-data-archive
-- ----------------------------
DROP TABLE IF EXISTS `segment-data-archive`;
CREATE TABLE `segment-data-archive` (
  `id` varchar(255) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `auth` varchar(255) DEFAULT NULL,
  `catalog` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `hits` bigint(20) DEFAULT NULL,
  `read` bigint(20) DEFAULT NULL,
  `votes` bigint(20) DEFAULT NULL,
  `collect` bigint(20) DEFAULT NULL,
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
