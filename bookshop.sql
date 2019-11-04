/*
Navicat MySQL Data Transfer

Source Server         : ysz
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : bookshop

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2019-10-31 02:20:42
*/

show DATABASES;

use bookshop;

show tables;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('10', '会员管理组');
INSERT INTO `auth_group` VALUES ('5', '图书管理组');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('12', '5', '5');
INSERT INTO `auth_group_permissions` VALUES ('16', '10', '109');
INSERT INTO `auth_group_permissions` VALUES ('14', '10', '110');
INSERT INTO `auth_group_permissions` VALUES ('15', '10', '111');
INSERT INTO `auth_group_permissions` VALUES ('13', '10', '112');

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add users', '7', 'add_users');
INSERT INTO `auth_permission` VALUES ('26', 'Can change users', '7', 'change_users');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete users', '7', 'delete_users');
INSERT INTO `auth_permission` VALUES ('28', 'Can view users', '7', 'view_users');
INSERT INTO `auth_permission` VALUES ('29', 'Can add booktype', '8', 'add_booktype');
INSERT INTO `auth_permission` VALUES ('30', 'Can change booktype', '8', 'change_booktype');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete booktype', '8', 'delete_booktype');
INSERT INTO `auth_permission` VALUES ('32', 'Can view booktype', '8', 'view_booktype');
INSERT INTO `auth_permission` VALUES ('33', 'Can add books', '9', 'add_books');
INSERT INTO `auth_permission` VALUES ('34', 'Can change books', '9', 'change_books');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete books', '9', 'delete_books');
INSERT INTO `auth_permission` VALUES ('36', 'Can view books', '9', 'view_books');
INSERT INTO `auth_permission` VALUES ('37', 'Can add bookimgs', '10', 'add_bookimgs');
INSERT INTO `auth_permission` VALUES ('38', 'Can change bookimgs', '10', 'change_bookimgs');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete bookimgs', '10', 'delete_bookimgs');
INSERT INTO `auth_permission` VALUES ('40', 'Can view bookimgs', '10', 'view_bookimgs');
INSERT INTO `auth_permission` VALUES ('41', 'Can add cart', '11', 'add_cart');
INSERT INTO `auth_permission` VALUES ('42', 'Can change cart', '11', 'change_cart');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete cart', '11', 'delete_cart');
INSERT INTO `auth_permission` VALUES ('44', 'Can view cart', '11', 'view_cart');
INSERT INTO `auth_permission` VALUES ('45', 'Can add order item', '12', 'add_orderitem');
INSERT INTO `auth_permission` VALUES ('46', 'Can change order item', '12', 'change_orderitem');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete order item', '12', 'delete_orderitem');
INSERT INTO `auth_permission` VALUES ('48', 'Can view order item', '12', 'view_orderitem');
INSERT INTO `auth_permission` VALUES ('49', 'Can add order', '13', 'add_order');
INSERT INTO `auth_permission` VALUES ('50', 'Can change order', '13', 'change_order');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete order', '13', 'delete_order');
INSERT INTO `auth_permission` VALUES ('52', 'Can view order', '13', 'view_order');
INSERT INTO `auth_permission` VALUES ('53', 'Can add address', '14', 'add_address');
INSERT INTO `auth_permission` VALUES ('54', 'Can change address', '14', 'change_address');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete address', '14', 'delete_address');
INSERT INTO `auth_permission` VALUES ('56', 'Can view address', '14', 'view_address');
INSERT INTO `auth_permission` VALUES ('105', '查看图书分类列表', '8', 'show_Booktype');
INSERT INTO `auth_permission` VALUES ('106', '添加图书分类', '8', 'create_Booktype');
INSERT INTO `auth_permission` VALUES ('107', '修改图书分类', '8', 'edit_Booktype');
INSERT INTO `auth_permission` VALUES ('108', '删除图书分类', '8', 'remove_Booktype');
INSERT INTO `auth_permission` VALUES ('109', '查看用户列表', '7', 'show_Users');
INSERT INTO `auth_permission` VALUES ('110', '添加用户', '7', 'create_Users');
INSERT INTO `auth_permission` VALUES ('111', '修改用户', '7', 'edit_Users');
INSERT INTO `auth_permission` VALUES ('112', '删除用户', '7', 'remove_Users');
INSERT INTO `auth_permission` VALUES ('113', '查看图书列表', '9', 'show_Books');
INSERT INTO `auth_permission` VALUES ('114', '添加图书', '9', 'create_Books');
INSERT INTO `auth_permission` VALUES ('115', '修改图书', '9', 'edit_Books');
INSERT INTO `auth_permission` VALUES ('116', '删除图书', '9', 'remove_Books');
INSERT INTO `auth_permission` VALUES ('117', '查看订单列表', '13', 'show_Order');
INSERT INTO `auth_permission` VALUES ('118', '添加订单', '13', 'create_Order');
INSERT INTO `auth_permission` VALUES ('119', '修改订单', '13', 'edit_Order');
INSERT INTO `auth_permission` VALUES ('120', '删除订单', '13', 'remove_Order');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('8', 'pbkdf2_sha256$150000$thpY8PkmPieJ$WSEO2XvUDF+LRl3a4aRlK+g34vgo9UTFRfRQFc5GXxc=', '2019-10-29 14:38:21.723055', '1', '于凤明', '', '', '3352439264@qq.com', '1', '1', '2019-10-29 03:11:05.724172');
INSERT INTO `auth_user` VALUES ('10', 'pbkdf2_sha256$150000$1tSemUtKtPYr$/8ifcbbQFKLl7gTpu9Aaz7aLh7oU1ygdNPGNLx3g/Ew=', '2019-10-29 09:12:26.824745', '0', '彭柳杨', '', '', '3352439264@qq.com', '0', '1', '2019-10-29 09:09:36.436384');
INSERT INTO `auth_user` VALUES ('11', 'pbkdf2_sha256$150000$c2jrvGdczQ9Y$jSjn7sq3oSVXsN5aNHy5+g+KuBQ2SRgasmmyiDCuSV0=', '2019-10-29 14:46:42.542359', '1', 'dell', '', '', '32@qq.com', '1', '1', '2019-10-29 14:45:32.636379');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES ('12', '8', '5');
INSERT INTO `auth_user_groups` VALUES ('11', '8', '10');
INSERT INTO `auth_user_groups` VALUES ('8', '10', '5');
INSERT INTO `auth_user_groups` VALUES ('7', '10', '10');

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('14', 'myadmin', 'address');
INSERT INTO `django_content_type` VALUES ('10', 'myadmin', 'bookimgs');
INSERT INTO `django_content_type` VALUES ('9', 'myadmin', 'books');
INSERT INTO `django_content_type` VALUES ('8', 'myadmin', 'booktype');
INSERT INTO `django_content_type` VALUES ('11', 'myadmin', 'cart');
INSERT INTO `django_content_type` VALUES ('13', 'myadmin', 'order');
INSERT INTO `django_content_type` VALUES ('12', 'myadmin', 'orderitem');
INSERT INTO `django_content_type` VALUES ('7', 'myadmin', 'users');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-10-17 16:10:09.246496');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-10-17 16:10:14.995706');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-10-17 16:10:39.244597');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-10-17 16:10:46.374876');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2019-10-17 16:10:46.582321');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2019-10-17 16:10:49.499861');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2019-10-17 16:10:51.103008');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2019-10-17 16:10:51.420158');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2019-10-17 16:10:51.700408');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2019-10-17 16:10:53.140637');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2019-10-17 16:10:53.308195');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2019-10-17 16:10:53.579986');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2019-10-17 16:10:55.735480');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2019-10-17 16:11:02.084947');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0010_alter_group_name_max_length', '2019-10-17 16:11:03.037705');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0011_update_proxy_permissions', '2019-10-17 16:11:03.254142');
INSERT INTO `django_migrations` VALUES ('17', 'myadmin', '0001_initial', '2019-10-17 16:11:04.238865');
INSERT INTO `django_migrations` VALUES ('18', 'myadmin', '0002_delete_users', '2019-10-17 16:11:05.031254');
INSERT INTO `django_migrations` VALUES ('19', 'myadmin', '0003_users', '2019-10-17 16:11:05.869532');
INSERT INTO `django_migrations` VALUES ('20', 'sessions', '0001_initial', '2019-10-17 16:11:06.364381');
INSERT INTO `django_migrations` VALUES ('21', 'myadmin', '0004_auto_20191017_1700', '2019-10-17 17:00:51.441379');
INSERT INTO `django_migrations` VALUES ('22', 'myadmin', '0005_users_createtime', '2019-10-18 09:11:50.157634');
INSERT INTO `django_migrations` VALUES ('23', 'myadmin', '0006_auto_20191018_0923', '2019-10-18 09:23:05.759401');
INSERT INTO `django_migrations` VALUES ('24', 'myadmin', '0007_auto_20191018_0938', '2019-10-18 09:38:47.697157');
INSERT INTO `django_migrations` VALUES ('25', 'myadmin', '0008_delete_users', '2019-10-18 10:49:03.238633');
INSERT INTO `django_migrations` VALUES ('26', 'myadmin', '0009_booktype_users', '2019-10-18 10:49:06.748376');
INSERT INTO `django_migrations` VALUES ('27', 'myadmin', '0010_auto_20191018_2159', '2019-10-18 22:00:06.257050');
INSERT INTO `django_migrations` VALUES ('28', 'myadmin', '0011_auto_20191018_2225', '2019-10-18 22:25:49.658531');
INSERT INTO `django_migrations` VALUES ('29', 'myadmin', '0012_auto_20191019_1638', '2019-10-19 16:38:51.793206');
INSERT INTO `django_migrations` VALUES ('30', 'myadmin', '0013_books_booktype_users', '2019-10-19 16:48:14.145592');
INSERT INTO `django_migrations` VALUES ('31', 'myadmin', '0014_auto_20191021_1441', '2019-10-21 14:41:47.832567');
INSERT INTO `django_migrations` VALUES ('32', 'myadmin', '0015_bookimgs_books_booktype_users', '2019-10-21 14:42:18.462834');
INSERT INTO `django_migrations` VALUES ('33', 'myadmin', '0016_cart', '2019-10-25 08:55:28.936311');
INSERT INTO `django_migrations` VALUES ('34', 'myadmin', '0017_order_orderitem', '2019-10-26 00:25:41.636810');
INSERT INTO `django_migrations` VALUES ('35', 'myadmin', '0018_address', '2019-10-26 18:59:30.305741');
INSERT INTO `django_migrations` VALUES ('36', 'myadmin', '0019_auto_20191028_2212', '2019-10-28 22:12:23.645679');
INSERT INTO `django_migrations` VALUES ('37', 'myadmin', '0020_auto_20191028_2226', '2019-10-28 22:26:31.938260');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('4tjn4lwwiz0ar6fdgvloktb8mnhn69kt', 'ODA0NWY1ZTY3ZjNkMmZhOGEwZGNjOTQ3MmExNjMwMzg4NjI5NDVkMDp7InZlcmlmeWNvZGUiOiJaRDZPIn0=', '2019-11-12 14:34:40.137755');
INSERT INTO `django_session` VALUES ('92fx0h78e3u5f4s57o1x3yep5uf7sit1', 'YWYxNmM1ZmZmYzU3YmMzOGEzMDIxY2QxODY4ZDY0OWYzMWYwMTM1ZDp7InZlcmlmeWNvZGUiOiJMMEI4In0=', '2019-11-12 14:34:42.659006');
INSERT INTO `django_session` VALUES ('al6qgmy7y6va04fjpsi5uzpunafx9ftp', 'ZWUxYjM0NWZjODVlMGQxZDM4MjcyOWM4NzFiNzg1ZDA1ZWM3NTY3Mzp7InZlcmlmeWNvZGUiOiJMMU5LIn0=', '2019-11-12 14:31:51.872853');
INSERT INTO `django_session` VALUES ('hi0dfu2v5b7rnwty90j3a0vpkwoeepl0', 'NDRiMTU4NWM0NjY3OWI2NGY2NGRlNDQ4ZWY0OTFmMTNjYzlhOWNjZDp7InZlcmlmeWNvZGUiOiJQTTg2In0=', '2019-11-12 14:34:42.394713');
INSERT INTO `django_session` VALUES ('hxlho7pvy248y9z6g8okzfqhyd7b97t1', 'OTBlN2Q4YzEzZjFjM2U3MGFkOGU3ZTRlZmY2YWRmYmJiZGZhYTNlZTp7InZlcmlmeWNvZGUiOiJJUEowIn0=', '2019-11-12 14:34:42.043651');
INSERT INTO `django_session` VALUES ('t73r0fdgngb3ms0cyhz9hm4nk1v2klu1', 'NjkxZTZmZTM2MzYyZmIzNjcyMzNjMzViM2M4YWIzODRlMGY3ZDUwMzp7InZlcmlmeWNvZGUiOiJMOVFLIn0=', '2019-11-12 14:31:41.678124');
INSERT INTO `django_session` VALUES ('uicl0l5rkf09w1ebxhxg0on5lmx8km6l', 'NWJiZDg4OTBjOGM4OGQzYTdjOTUzNTllYWVhNDU3ZDczYjg5OTYyNjp7IkFkbWluVXNlciI6eyJpZCI6OSwicGhvbmUiOiIxMzQ3MDAzODIzOSJ9fQ==', '2019-11-12 22:39:04.250635');
INSERT INTO `django_session` VALUES ('wdnu14zwhfdtxur7p1m36xxrwmliuavj', 'NGE2ZDlhODI1MGFiMDlhYzZlMmIwOTA0MTBlMWMzY2I3ZGJlYTU0ODp7InZlcmlmeWNvZGUiOiJVRjRHIiwiX2F1dGhfdXNlcl9pZCI6IjExIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhMDFlNzJjYTdhYzc3MTZlYWM2MGEwNjhmNjc0NzM1MGQyMDEwNzZhIiwiQWRtaW5Vc2VyIjp7InVpZCI6MTEsInVzZXJuYW1lIjoiZGVsbCJ9fQ==', '2019-11-12 14:46:42.623131');

-- ----------------------------
-- Table structure for myadmin_address
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_address`;
CREATE TABLE `myadmin_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `user_address` varchar(200) NOT NULL,
  `isdefault` varchar(1) NOT NULL,
  `isdel` varchar(1) NOT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myadmin_address_uid_id_79af8acf_fk_myadmin_users_id` (`uid_id`),
  CONSTRAINT `myadmin_address_uid_id_79af8acf_fk_myadmin_users_id` FOREIGN KEY (`uid_id`) REFERENCES `myadmin_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_address
-- ----------------------------
INSERT INTO `myadmin_address` VALUES ('16', '于凤明', '12312312312', '辽宁省沈阳市铁西区兴华南街', '0', '0', '10');

-- ----------------------------
-- Table structure for myadmin_bookimgs
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_bookimgs`;
CREATE TABLE `myadmin_bookimgs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_url` varchar(100) NOT NULL,
  `bookid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myadmin_bookimgs_bookid_id_b1db4d79_fk_myadmin_books_id` (`bookid_id`),
  CONSTRAINT `myadmin_bookimgs_bookid_id_b1db4d79_fk_myadmin_books_id` FOREIGN KEY (`bookid_id`) REFERENCES `myadmin_books` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_bookimgs
-- ----------------------------
INSERT INTO `myadmin_bookimgs` VALUES ('65', 'static/myadmin/book_img/人间失格1.jpg', '47');
INSERT INTO `myadmin_bookimgs` VALUES ('66', 'static/myadmin/book_img/人间失格2.jpg', '47');
INSERT INTO `myadmin_bookimgs` VALUES ('67', 'static/myadmin/book_img/我喜欢生命本来的样子1.jpg', '48');
INSERT INTO `myadmin_bookimgs` VALUES ('68', 'static/myadmin/book_img/正面管教.jpg', '49');
INSERT INTO `myadmin_bookimgs` VALUES ('69', 'static/myadmin/book_img/正面管教2jpg.jpg', '49');
INSERT INTO `myadmin_bookimgs` VALUES ('70', 'static/myadmin/book_img/正面管教3.jpg', '49');
INSERT INTO `myadmin_bookimgs` VALUES ('71', 'static/myadmin/book_img/活着.jpg', '50');
INSERT INTO `myadmin_bookimgs` VALUES ('72', 'static/myadmin/book_img/活着2.jpg', '50');
INSERT INTO `myadmin_bookimgs` VALUES ('73', 'static/myadmin/book_img/活着3.jpg', '50');
INSERT INTO `myadmin_bookimgs` VALUES ('74', 'static/myadmin/book_img/小熊和最好的爸爸1.jpg', '51');
INSERT INTO `myadmin_bookimgs` VALUES ('75', 'static/myadmin/book_img/小熊和最好的爸爸2.jpg', '51');
INSERT INTO `myadmin_bookimgs` VALUES ('76', 'static/myadmin/book_img/神奇校车1.jpg', '52');
INSERT INTO `myadmin_bookimgs` VALUES ('77', 'static/myadmin/book_img/神奇校车2.jpg', '52');
INSERT INTO `myadmin_bookimgs` VALUES ('78', 'static/myadmin/book_img/神奇校车3.jpg', '52');

-- ----------------------------
-- Table structure for myadmin_books
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_books`;
CREATE TABLE `myadmin_books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bookname` varchar(70) NOT NULL,
  `recommend` varchar(255) DEFAULT NULL,
  `author` varchar(50) NOT NULL,
  `publisher` varchar(150) NOT NULL,
  `pdate` date NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `num` int(11) NOT NULL,
  `isbn` varchar(13) NOT NULL,
  `bookdetail` longtext,
  `cate` varchar(1) NOT NULL,
  `isdel` varchar(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_books
-- ----------------------------
INSERT INTO `myadmin_books` VALUES ('47', '人间失格（日本小说家太宰治的自传体小说，李现推荐', '超燃！“丧文化”流行，《人间失格》成了现象级畅销书，创当当3天销售50000+册的奇迹！收录作者绝笔之作《Good bye》。一个“丧失为人资格”少年的心灵独白，一个对村上春树影响至深的绝望凄美故事', '太宰治', '作家出版社', '2015-08-07', '18.80', '100', '9787506380263', '<p><img src=\"/static/media/article/20191024/20191024221311605.jpg\" title=\"20191024/20191024221311605.jpg\" alt=\"20191024/20191024221311605.jpg\"/></p>', '0', '004001');
INSERT INTO `myadmin_books` VALUES ('48', '我喜欢生命本来的样子(周国平经典散文作品集)', '影响和改变万千年轻人对人生的思考和生活的态度！上市半年以来，销售突破10万册，4万读者诚挚推荐！2017年，周国平散文ZUI佳精选集！裸书脊精装，四色印刷，林帝浣插图，但愿你保持住一份生命的本色! ', '周国平', '作家出版社', '2017-02-03', '20.00', '20', '9787506391542', '<p>&lt;p&gt;&lt;img src=&quot;/static/media/article/20191024/20191024221536485.jpg&quot; title=&quot;20191024/20191024221536485.jpg&quot; alt=&quot;20191024/20191024221536485.jpg&quot;/&gt;&lt;/p&gt;</p>', '2', '004001');
INSERT INTO `myadmin_books` VALUES ('49', '正面管教(修订版)', '如何不惩罚、不娇纵地有效管教孩子。畅销美国400多万册，被翻译成16种语言畅销全球；让数百万孩子、父母和老师受益终身的经典之作；自1981年本书*版出版以来，《正面管教》已经成为管教孩子的... ', '简尼尔森', '北京联合出版公司', '2016-07-15', '32.00', '50', '9787550268517', '<p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; list-style-type: none; border: 0px; color: rgb(101, 101, 101); font-family: &quot;Hiragino Sans GB&quot;, Verdana, Simsun; font-size: 14px; white-space: normal; background-color: rgb(255, 255, 255);\">没有哪个父母不为了孩子而竭尽全力，但*美好的愿望却不一定给孩子带来*好的结果。</p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; list-style-type: none; border: 0px; color: rgb(101, 101, 101); font-family: &quot;Hiragino Sans GB&quot;, Verdana, Simsun; font-size: 14px; white-space: normal; background-color: rgb(255, 255, 255);\">&nbsp; 自1981年本书*版初版以来，《正面管教》已经成为了管教孩子的“黄金准则”，本书被翻译成16中语言，在美国销量超过400万册，在美国之外的国家销量超过200万册。自1987年*次修订之后，每10年修订一次，本书根据英文原版的第三次修订版(2006年出版)翻译，该版首印数为70多万册。</p><p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; list-style-type: none; border: 0px; color: rgb(101, 101, 101); font-family: &quot;Hiragino Sans GB&quot;, Verdana, Simsun; font-size: 14px; white-space: normal; background-color: rgb(255, 255, 255);\">&nbsp; 正面管教是一种既不惩罚也不娇纵的管教孩子的方法……孩子只有在一种和善而坚定的气氛中，才能培养出自律、责任感、合作以及自己解决问题的能力，才能学会使他们受益终身的社会技能和生活技能，才能取得良好的学业成绩……如何运用正面管教方法使孩子获得这种能力，就是本书的主要内容。</p><p><br/></p>', '0', '004001');
INSERT INTO `myadmin_books` VALUES ('50', '活着（2017年新版）', '余华是我国当代著名作家，也是享誉世界的小说家，曾荣获众多国内外奖项。《活着》是其代表作，在全球广泛传播，销量逾千万册，获得了普遍好评，已成为中国乃至世界当代文学的经典。', '余华', '作家出版社', '2012-08-18', '26.60', '30', '9787506365437', '<p><img src=\"/static/media/article/20191024/20191024222120742.jpg\" title=\"20191024/20191024222120742.jpg\" alt=\"20191024/20191024222120742.jpg\"/></p>', '0', '004001');
INSERT INTO `myadmin_books` VALUES ('51', '小熊和最好的爸爸（全7册）', '和爸爸一起读的绘本，极易操作学习增强父子情感的图画书。孩子学习做男子汉：粗犷、睿智、谦逊、幽默，细致；爸爸学习父爱的技巧：了解孩子的梦想，为孩子的勇气而骄傲，成为孩子眼中的英雄。（蒲公英童书馆出品）', '阿兰德丹姆', '贵州人民出版社', '2007-11-07', '31.90', '60', '9787221078803', '<p><img src=\"/static/media/article/20191024/20191024222503652.jpg\" style=\"\" title=\"20191024/20191024222503652.jpg\"/></p><p><img src=\"/static/media/article/20191024/20191024222503990.jpg\" style=\"\" title=\"20191024/20191024222503990.jpg\"/></p><p><br/></p>', '0', '004001');
INSERT INTO `myadmin_books` VALUES ('52', '神奇校车·图画书版（全12册，新增《科学博览会》1册）', '风靡全世界的“神奇校车”再次出发！搭乘神奇校车，跟着卷毛老师来一次时空穿越之旅，去认识那些闪耀在历史星河中的伟大科学家！（蒲公英童书馆出品）', '乔安娜柯尔', '贵州人民出版社', '2018-05-17', '136.60', '20', '2525240811111', '<p><img src=\"/static/media/article/20191024/20191024222809277.jpg\" title=\"20191024/20191024222809277.jpg\" alt=\"20191024/20191024222809277.jpg\"/></p>', '0', '004001');

-- ----------------------------
-- Table structure for myadmin_books_typeid
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_books_typeid`;
CREATE TABLE `myadmin_books_typeid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `books_id` int(11) NOT NULL,
  `booktype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myadmin_books_typeid_books_id_booktype_id_60f6451f_uniq` (`books_id`,`booktype_id`),
  KEY `myadmin_books_typeid_booktype_id_a8e4e7c5_fk_myadmin_booktype_id` (`booktype_id`),
  CONSTRAINT `myadmin_books_typeid_books_id_9564ca90_fk_myadmin_books_id` FOREIGN KEY (`books_id`) REFERENCES `myadmin_books` (`id`),
  CONSTRAINT `myadmin_books_typeid_booktype_id_a8e4e7c5_fk_myadmin_booktype_id` FOREIGN KEY (`booktype_id`) REFERENCES `myadmin_booktype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_books_typeid
-- ----------------------------
INSERT INTO `myadmin_books_typeid` VALUES ('82', '47', '15');
INSERT INTO `myadmin_books_typeid` VALUES ('83', '48', '15');
INSERT INTO `myadmin_books_typeid` VALUES ('87', '51', '11');
INSERT INTO `myadmin_books_typeid` VALUES ('86', '51', '16');
INSERT INTO `myadmin_books_typeid` VALUES ('89', '52', '2');
INSERT INTO `myadmin_books_typeid` VALUES ('88', '52', '16');

-- ----------------------------
-- Table structure for myadmin_booktype
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_booktype`;
CREATE TABLE `myadmin_booktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `catename` varchar(20) NOT NULL,
  `pid` int(11) NOT NULL,
  `path` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_booktype
-- ----------------------------
INSERT INTO `myadmin_booktype` VALUES ('1', '教育', '0', '0,');
INSERT INTO `myadmin_booktype` VALUES ('2', '教材', '1', '0,1,');
INSERT INTO `myadmin_booktype` VALUES ('11', '外语', '1', '0,1,');
INSERT INTO `myadmin_booktype` VALUES ('12', '考试', '1', '0,1,');
INSERT INTO `myadmin_booktype` VALUES ('13', '青春文学', '0', '0,');
INSERT INTO `myadmin_booktype` VALUES ('14', '文艺', '0', '0,');
INSERT INTO `myadmin_booktype` VALUES ('15', '文学', '14', '0,14,');
INSERT INTO `myadmin_booktype` VALUES ('16', '|--校园', '13', '0,13,');
INSERT INTO `myadmin_booktype` VALUES ('26', '古代言情', '13', '0,13,');

-- ----------------------------
-- Table structure for myadmin_cart
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_cart`;
CREATE TABLE `myadmin_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) NOT NULL,
  `select` int(11) NOT NULL,
  `bookid_id` int(11) NOT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myadmin_cart_bookid_id_8d3f2a9e_fk_myadmin_books_id` (`bookid_id`),
  KEY `myadmin_cart_uid_id_26f2428c_fk_myadmin_users_id` (`uid_id`),
  CONSTRAINT `myadmin_cart_bookid_id_8d3f2a9e_fk_myadmin_books_id` FOREIGN KEY (`bookid_id`) REFERENCES `myadmin_books` (`id`),
  CONSTRAINT `myadmin_cart_uid_id_26f2428c_fk_myadmin_users_id` FOREIGN KEY (`uid_id`) REFERENCES `myadmin_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_cart
-- ----------------------------

-- ----------------------------
-- Table structure for myadmin_order
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_order`;
CREATE TABLE `myadmin_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `totalprice` decimal(7,2) NOT NULL,
  `status` int(11) NOT NULL,
  `ordertime` datetime(6) NOT NULL,
  `paytime` datetime(6) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myadmin_order_uid_id_bcf75806_fk_myadmin_users_id` (`uid_id`),
  CONSTRAINT `myadmin_order_uid_id_bcf75806_fk_myadmin_users_id` FOREIGN KEY (`uid_id`) REFERENCES `myadmin_users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_order
-- ----------------------------
INSERT INTO `myadmin_order` VALUES ('9', '于凤明', '12312312312', '辽宁省沈阳市铁西区兴华南街', '18.80', '1', '2019-10-29 14:28:55.395111', '2019-10-29 14:30:08.000000', '10');

-- ----------------------------
-- Table structure for myadmin_orderitem
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_orderitem`;
CREATE TABLE `myadmin_orderitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `bookid_id` int(11) NOT NULL,
  `orderid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myadmin_orderitem_bookid_id_3cc8a268_fk_myadmin_books_id` (`bookid_id`),
  KEY `myadmin_orderitem_orderid_id_d57bf1a7_fk_myadmin_order_id` (`orderid_id`),
  CONSTRAINT `myadmin_orderitem_bookid_id_3cc8a268_fk_myadmin_books_id` FOREIGN KEY (`bookid_id`) REFERENCES `myadmin_books` (`id`),
  CONSTRAINT `myadmin_orderitem_orderid_id_d57bf1a7_fk_myadmin_order_id` FOREIGN KEY (`orderid_id`) REFERENCES `myadmin_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_orderitem
-- ----------------------------
INSERT INTO `myadmin_orderitem` VALUES ('8', '1', '18', '47', '9');

-- ----------------------------
-- Table structure for myadmin_users
-- ----------------------------
DROP TABLE IF EXISTS `myadmin_users`;
CREATE TABLE `myadmin_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) NOT NULL,
  `password` varchar(80) NOT NULL,
  `face` varchar(100) NOT NULL,
  `nickname` varchar(20) DEFAULT NULL,
  `homeaddress` varchar(100) DEFAULT NULL,
  `sex` varchar(6) DEFAULT NULL,
  `usertype` varchar(1) DEFAULT NULL,
  `createtime` datetime(6) NOT NULL,
  `isdel` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of myadmin_users
-- ----------------------------
INSERT INTO `myadmin_users` VALUES ('9', '13470038239', 'pbkdf2_sha256$150000$ayvSHAembVcN$7dd5u/YWumGcxD7YVvq6dU1E0U9nn9ei5xBqgitMHi4=', '/static/myadmin/assets/img/user06.png', null, null, null, null, '2019-10-29 14:23:49.472077', '004001');
INSERT INTO `myadmin_users` VALUES ('10', '17645122048', 'pbkdf2_sha256$150000$16q2j2kUIQ9H$OGB/HEet+S68eGDQO23NakrqxXOZRmkKsT/3MlBobHw=', '/static/myadmin/assets/img/user06.png', null, null, null, null, '2019-10-29 14:25:24.491517', '004001');
