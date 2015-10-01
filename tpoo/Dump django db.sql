CREATE DATABASE  IF NOT EXISTS `tpoo` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `tpoo`;
-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (i686)
--
-- Host: 127.0.0.1    Database: tpoo
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add usability test',7,'add_usabilitytest'),(20,'Can change usability test',7,'change_usabilitytest'),(21,'Can delete usability test',7,'delete_usabilitytest'),(22,'Can add app version',8,'add_appversion'),(23,'Can change app version',8,'change_appversion'),(24,'Can delete app version',8,'delete_appversion'),(25,'Can add refactoring',9,'add_refactoring'),(26,'Can change refactoring',9,'change_refactoring'),(27,'Can delete refactoring',9,'delete_refactoring'),(28,'Can add task',10,'add_task'),(29,'Can change task',10,'change_task'),(30,'Can delete task',10,'delete_task'),(31,'Can add scenario',11,'add_scenario'),(32,'Can change scenario',11,'change_scenario'),(33,'Can delete scenario',11,'delete_scenario'),(34,'Can add participant',12,'add_participant'),(35,'Can change participant',12,'change_participant'),(36,'Can delete participant',12,'delete_participant'),(37,'Can add scenario execution',13,'add_scenarioexecution'),(38,'Can change scenario execution',13,'change_scenarioexecution'),(39,'Can delete scenario execution',13,'delete_scenarioexecution'),(40,'Can add task scenario execution',14,'add_taskscenarioexecution'),(41,'Can change task scenario execution',14,'change_taskscenarioexecution'),(42,'Can delete task scenario execution',14,'delete_taskscenarioexecution'),(43,'Can add interaction step execution',15,'add_interactionstepexecution'),(44,'Can change interaction step execution',15,'change_interactionstepexecution'),(45,'Can delete interaction step execution',15,'delete_interactionstepexecution'),(46,'Can add scenario task',16,'add_scenariotask'),(47,'Can change scenario task',16,'change_scenariotask'),(48,'Can delete scenario task',16,'delete_scenariotask'),(49,'Can add interaction step',17,'add_interactionstep'),(50,'Can change interaction step',17,'change_interactionstep'),(51,'Can delete interaction step',17,'delete_interactionstep');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$4zTSLPr9PUT5$T407a8EneUjuC95uORl8SEDLgQJC4ALwHEtJDNXyPcs=',NULL,1,'admin','','','admin@gmail.com',1,1,'2015-09-30 18:50:51');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(17,'tasks','interactionstep'),(16,'tasks','scenariotask'),(8,'usability_tests','appversion'),(9,'usability_tests','refactoring'),(11,'usability_tests','scenario'),(10,'usability_tests','task'),(7,'usability_tests','usabilitytest'),(15,'usability_tests_executions','interactionstepexecution'),(12,'usability_tests_executions','participant'),(13,'usability_tests_executions','scenarioexecution'),(14,'usability_tests_executions','taskscenarioexecution');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-09-30 18:17:36'),(2,'auth','0001_initial','2015-09-30 18:17:38'),(3,'admin','0001_initial','2015-09-30 18:17:39'),(4,'contenttypes','0002_remove_content_type_name','2015-09-30 18:17:39'),(5,'auth','0002_alter_permission_name_max_length','2015-09-30 18:17:40'),(6,'auth','0003_alter_user_email_max_length','2015-09-30 18:17:40'),(7,'auth','0004_alter_user_username_opts','2015-09-30 18:17:40'),(8,'auth','0005_alter_user_last_login_null','2015-09-30 18:17:40'),(9,'auth','0006_require_contenttypes_0002','2015-09-30 18:17:41'),(10,'sessions','0001_initial','2015-09-30 18:17:41'),(11,'usability_tests','0001_initial','2015-09-30 18:17:41'),(12,'usability_tests','0002_appversion_refactoring_scenario_task','2015-09-30 18:17:44'),(13,'usability_tests','0003_auto_20150917_1427','2015-09-30 18:17:47'),(14,'tasks','0001_initial','2015-09-30 18:17:48'),(15,'usability_tests_executions','0001_initial','2015-09-30 18:17:51'),(16,'usability_tests','0004_auto_20150930_1914','2015-09-30 19:14:52');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks_interactionstep`
--

DROP TABLE IF EXISTS `tasks_interactionstep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tasks_interactionstep` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scenario_task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tasks_interactionstep_130cbdcf` (`scenario_task_id`),
  CONSTRAINT `tasks_interac_scenario_task_id_637645b3_fk_tasks_scenariotask_id` FOREIGN KEY (`scenario_task_id`) REFERENCES `tasks_scenariotask` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks_interactionstep`
--

LOCK TABLES `tasks_interactionstep` WRITE;
/*!40000 ALTER TABLE `tasks_interactionstep` DISABLE KEYS */;
/*!40000 ALTER TABLE `tasks_interactionstep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks_scenariotask`
--

DROP TABLE IF EXISTS `tasks_scenariotask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tasks_scenariotask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scenario_id` int(11) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tasks_scenar_scenario_id_7659e6a6_fk_usability_tests_scenario_id` (`scenario_id`),
  KEY `tasks_scenariotask_task_id_53514977_fk_usability_tests_task_id` (`task_id`),
  CONSTRAINT `tasks_scenariotask_task_id_53514977_fk_usability_tests_task_id` FOREIGN KEY (`task_id`) REFERENCES `usability_tests_task` (`id`),
  CONSTRAINT `tasks_scenar_scenario_id_7659e6a6_fk_usability_tests_scenario_id` FOREIGN KEY (`scenario_id`) REFERENCES `usability_tests_scenario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks_scenariotask`
--

LOCK TABLES `tasks_scenariotask` WRITE;
/*!40000 ALTER TABLE `tasks_scenariotask` DISABLE KEYS */;
/*!40000 ALTER TABLE `tasks_scenariotask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_appversion`
--

DROP TABLE IF EXISTS `usability_tests_appversion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_appversion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `usability_test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `u_usability_test_id_1c4e4937_fk_usability_tests_usabilitytest_id` (`usability_test_id`),
  CONSTRAINT `u_usability_test_id_1c4e4937_fk_usability_tests_usabilitytest_id` FOREIGN KEY (`usability_test_id`) REFERENCES `usability_tests_usabilitytest` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_appversion`
--

LOCK TABLES `usability_tests_appversion` WRITE;
/*!40000 ALTER TABLE `usability_tests_appversion` DISABLE KEYS */;
INSERT INTO `usability_tests_appversion` VALUES (1,'Non Refactored',1),(2,'Non Refactored',2),(4,'Refactored',1),(5,'Refactored',2);
/*!40000 ALTER TABLE `usability_tests_appversion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_executions_interactionstepexecution`
--

DROP TABLE IF EXISTS `usability_tests_executions_interactionstepexecution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_executions_interactionstepexecution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `interaction_step_id` int(11) NOT NULL,
  `task_scenario_execution_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usabili_interaction_step_id_48b17ed7_fk_tasks_interactionstep_id` (`interaction_step_id`),
  KEY `usability_tests_executions_interactionstepexecution_7dc83367` (`task_scenario_execution_id`),
  CONSTRAINT `b1a014863560d02718aa0c1319185344` FOREIGN KEY (`task_scenario_execution_id`) REFERENCES `usability_tests_executions_taskscenarioexecution` (`id`),
  CONSTRAINT `usabili_interaction_step_id_48b17ed7_fk_tasks_interactionstep_id` FOREIGN KEY (`interaction_step_id`) REFERENCES `tasks_interactionstep` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_executions_interactionstepexecution`
--

LOCK TABLES `usability_tests_executions_interactionstepexecution` WRITE;
/*!40000 ALTER TABLE `usability_tests_executions_interactionstepexecution` DISABLE KEYS */;
/*!40000 ALTER TABLE `usability_tests_executions_interactionstepexecution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_executions_participant`
--

DROP TABLE IF EXISTS `usability_tests_executions_participant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_executions_participant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_executions_participant`
--

LOCK TABLES `usability_tests_executions_participant` WRITE;
/*!40000 ALTER TABLE `usability_tests_executions_participant` DISABLE KEYS */;
INSERT INTO `usability_tests_executions_participant` VALUES (1,'Lluna_Diaz_E3'),(2,'Elena_Collado_E4'),(3,'Elena_Garcia_E3'),(4,'Laura_Meseguer_E1'),(5,'ines_orti_E4'),(6,'Frank'),(7,'pablo_jover_E1'),(8,'Elena_Garcia_E1'),(9,'Jennifer_Criado_E2'),(10,'Amira_Richani_F3'),(11,'mariluz_martinez_E1'),(12,'Sin Nombre'),(13,'noelia_catalan_E2'),(14,'Isabel_Bonet_E1'),(15,'Cristina'),(16,'Amira_Richani_E3'),(17,'Olga Bonet E2'),(18,'Alejandra_LÃ³pez_E2'),(19,'TERESA_CANTERO_E1'),(20,'Cristina_Calpe_E2'),(21,'Amaia_Retolaza_2'),(22,'silvia_caceres_E4'),(23,'Hector_Tordera_E3'),(24,'Macarena_Navarro_E4'),(25,'Alejandra_Lopez_E2'),(26,'Alejandr_LÃ³pez_E2'),(27,'TECANES_CANTERO_E1'),(28,'Ana_Poveda_E2'),(29,'silvia_olaria_E4'),(30,'Maria_Urbano_E2'),(31,'Alba_Nebot_E4'),(32,'Olaria_Silvia_E4'),(33,'Maria_Urbano-E2'),(34,'Erik_Boluda_Roig_E3'),(35,'Erik_Boluda_Roig'),(37,'Mary_Martinez_Rubio_E1'),(39,'Guido_E2'),(40,'Lisandro_E3'),(41,'Veronica_E2'),(42,'Diego_E3'),(43,'Francisco PeÃ±a Baraibar_E4'),(44,'Maximiliano_E1'),(45,'Andres_E3'),(47,'Julian_E3'),(48,'Alejandra_E1'),(49,'guido_e3'),(50,'Ivan Dackiewicz_e1'),(51,'agustin_e4'),(52,'matiasR_E1'),(53,'JuanManuelRivero_e2'),(54,'Herna_E3'),(55,'tomas_e4'),(56,'Julian_E2'),(57,'jorge_eu1'),(58,'IgnacioVidal_E2'),(59,'Nati_E4'),(60,'fede_e3'),(61,'Gabriela_e4'),(62,'juliangll_G4'),(63,'Jesus_E1'),(64,'e3'),(65,'leandro_e2'),(66,'Franco_E2');
/*!40000 ALTER TABLE `usability_tests_executions_participant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_executions_scenarioexecution`
--

DROP TABLE IF EXISTS `usability_tests_executions_scenarioexecution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_executions_scenarioexecution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `participant_id` int(11) NOT NULL,
  `scenario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D4c4f6263b331315019670c804eff95e` (`participant_id`),
  KEY `usability_te_scenario_id_395c5887_fk_usability_tests_scenario_id` (`scenario_id`),
  CONSTRAINT `D4c4f6263b331315019670c804eff95e` FOREIGN KEY (`participant_id`) REFERENCES `usability_tests_executions_participant` (`id`),
  CONSTRAINT `usability_te_scenario_id_395c5887_fk_usability_tests_scenario_id` FOREIGN KEY (`scenario_id`) REFERENCES `usability_tests_scenario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_executions_scenarioexecution`
--

LOCK TABLES `usability_tests_executions_scenarioexecution` WRITE;
/*!40000 ALTER TABLE `usability_tests_executions_scenarioexecution` DISABLE KEYS */;
/*!40000 ALTER TABLE `usability_tests_executions_scenarioexecution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_executions_taskscenarioexecution`
--

DROP TABLE IF EXISTS `usability_tests_executions_taskscenarioexecution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_executions_taskscenarioexecution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scenario_execution_id` int(11) NOT NULL,
  `scenario_task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `e1cf07b402899db6478699d7c6b39f87` (`scenario_execution_id`),
  KEY `usability_tes_scenario_task_id_1a808b1b_fk_tasks_scenariotask_id` (`scenario_task_id`),
  CONSTRAINT `e1cf07b402899db6478699d7c6b39f87` FOREIGN KEY (`scenario_execution_id`) REFERENCES `usability_tests_executions_scenarioexecution` (`id`),
  CONSTRAINT `usability_tes_scenario_task_id_1a808b1b_fk_tasks_scenariotask_id` FOREIGN KEY (`scenario_task_id`) REFERENCES `tasks_scenariotask` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_executions_taskscenarioexecution`
--

LOCK TABLES `usability_tests_executions_taskscenarioexecution` WRITE;
/*!40000 ALTER TABLE `usability_tests_executions_taskscenarioexecution` DISABLE KEYS */;
/*!40000 ALTER TABLE `usability_tests_executions_taskscenarioexecution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_refactoring`
--

DROP TABLE IF EXISTS `usability_tests_refactoring`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_refactoring` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `app_version_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usabili_app_version_id_1160b615_fk_usability_tests_appversion_id` (`app_version_id`),
  CONSTRAINT `usabili_app_version_id_1160b615_fk_usability_tests_appversion_id` FOREIGN KEY (`app_version_id`) REFERENCES `usability_tests_appversion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_refactoring`
--

LOCK TABLES `usability_tests_refactoring` WRITE;
/*!40000 ALTER TABLE `usability_tests_refactoring` DISABLE KEYS */;
/*!40000 ALTER TABLE `usability_tests_refactoring` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_scenario`
--

DROP TABLE IF EXISTS `usability_tests_scenario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_scenario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `app_version_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usabilit_app_version_id_6300b68_fk_usability_tests_appversion_id` (`app_version_id`),
  CONSTRAINT `usabilit_app_version_id_6300b68_fk_usability_tests_appversion_id` FOREIGN KEY (`app_version_id`) REFERENCES `usability_tests_appversion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_scenario`
--

LOCK TABLES `usability_tests_scenario` WRITE;
/*!40000 ALTER TABLE `usability_tests_scenario` DISABLE KEYS */;
INSERT INTO `usability_tests_scenario` VALUES (1,'Zencart Refactored',4),(2,'Zencart Non Refactored',1),(3,'WeBid Refactored',5),(4,'WeBid Non Refactored',2);
/*!40000 ALTER TABLE `usability_tests_scenario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_task`
--

DROP TABLE IF EXISTS `usability_tests_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `usability_test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `u_usability_test_id_336ecbeb_fk_usability_tests_usabilitytest_id` (`usability_test_id`),
  CONSTRAINT `u_usability_test_id_336ecbeb_fk_usability_tests_usabilitytest_id` FOREIGN KEY (`usability_test_id`) REFERENCES `usability_tests_usabilitytest` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_task`
--

LOCK TABLES `usability_tests_task` WRITE;
/*!40000 ALTER TABLE `usability_tests_task` DISABLE KEYS */;
INSERT INTO `usability_tests_task` VALUES (1,'Zencart Test 1 Crear una nueva cuenta de usuario',1),(2,'Zencart Test 4 Realizar una compra de varios productos',1),(5,'Zencart Test 3 Buscar una cantidad de productos en el catÃ¡logo de la pÃ¡gina',1),(6,'Zencart Test 2 Actualizar la informaciÃ³n del usuario',1),(9,'Webid Test 1 Crear una nueva cuenta de usuario',2),(10,'Webid Test 2 Editar cuenta de usuario',2),(11,'Webid Test 3 Buscar productos',2),(14,'Webid Test 4 Ofertar',2),(18,'Webid Test 5 Subastar un producto',2);
/*!40000 ALTER TABLE `usability_tests_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usability_tests_usabilitytest`
--

DROP TABLE IF EXISTS `usability_tests_usabilitytest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usability_tests_usabilitytest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usability_tests_usabilitytest_owner_id_45aa0cc0_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `usability_tests_usabilitytest_owner_id_45aa0cc0_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usability_tests_usabilitytest`
--

LOCK TABLES `usability_tests_usabilitytest` WRITE;
/*!40000 ALTER TABLE `usability_tests_usabilitytest` DISABLE KEYS */;
INSERT INTO `usability_tests_usabilitytest` VALUES (1,'ZenCart',1),(2,'WeBid',1);
/*!40000 ALTER TABLE `usability_tests_usabilitytest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-01 20:02:12
