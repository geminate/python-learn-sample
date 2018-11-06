/*
Navicat MySQL Data Transfer

Source Server         : 本机
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : pylearn

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2018-11-06 16:44:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bilibili-data-archive
-- ----------------------------
DROP TABLE IF EXISTS `bilibili-data-archive`;
CREATE TABLE `bilibili-data-archive` (
  `aid` bigint(20) NOT NULL COMMENT '序号',
  `view` bigint(20) DEFAULT NULL COMMENT '姓名',
  `danmaku` bigint(20) DEFAULT NULL COMMENT '联系方式',
  `reply` bigint(20) DEFAULT NULL,
  `favorite` bigint(20) DEFAULT NULL,
  `coin` bigint(20) DEFAULT NULL,
  `share` bigint(20) DEFAULT NULL,
  `now_rank` bigint(20) DEFAULT NULL,
  `his_rank` bigint(20) DEFAULT NULL,
  `like` bigint(20) DEFAULT NULL,
  `dislike` bigint(20) DEFAULT NULL,
  `no_reprint` bigint(20) DEFAULT NULL,
  `copyright` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
