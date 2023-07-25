-- MySQL dump 10.13  Distrib 8.0.33, for macos13.3 (arm64)
--
-- Host: localhost    Database: siputa
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_prodi`
--

DROP TABLE IF EXISTS `admin_prodi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_prodi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `kode_prodi` varchar(2) NOT NULL,
  `request_reset` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `kode_prodi` (`kode_prodi`),
  CONSTRAINT `admin_prodi_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `admin_prodi_ibfk_2` FOREIGN KEY (`kode_prodi`) REFERENCES `prodi` (`kode_prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_prodi`
--

LOCK TABLES `admin_prodi` WRITE;
/*!40000 ALTER TABLE `admin_prodi` DISABLE KEYS */;
INSERT INTO `admin_prodi` VALUES (6,24,'04',NULL),(7,25,'01',NULL),(8,26,'09',NULL),(9,27,'08',0);
/*!40000 ALTER TABLE `admin_prodi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('a0462e2f9822');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mahasiswa`
--

DROP TABLE IF EXISTS `mahasiswa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mahasiswa` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nim` char(8) NOT NULL,
  `name` varchar(50) NOT NULL,
  `state` char(20) DEFAULT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `batch_year` varchar(4) DEFAULT NULL,
  `gpa_score` float NOT NULL,
  `parents_income` float DEFAULT NULL,
  `address` text,
  `sertifikat` int DEFAULT NULL,
  `prestasi` int DEFAULT NULL,
  `organisasi` int DEFAULT NULL,
  `pekerjaan_ortu` varchar(70) DEFAULT NULL,
  `relevan` tinyint(1) DEFAULT NULL,
  `predict_proba` int DEFAULT NULL,
  `prodi` varchar(2) DEFAULT NULL,
  `semester` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prodi` (`prodi`),
  CONSTRAINT `mahasiswa_ibfk_1` FOREIGN KEY (`prodi`) REFERENCES `prodi` (`kode_prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=146 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahasiswa`
--

LOCK TABLES `mahasiswa` WRITE;
/*!40000 ALTER TABLE `mahasiswa` DISABLE KEYS */;
INSERT INTO `mahasiswa` VALUES (141,'20011009','SYAHRUL GHUFRON','A',1,'2020',3.29,50000000,NULL,0,2,2,'buruh',NULL,NULL,'01',6),(142,'19010010','MUHAIMIN MAJID','A',1,'2019',3.42,50000000,NULL,0,3,0,'buruh',0,39,'01',6),(143,'19041143','DEDE FAOZAN FELANY','A',1,'2019',3.42,50000000,NULL,0,0,1,'buruh',0,41,'04',6),(144,'19010015','TRI FEBRYANSYAH PUTRA','A',1,'2019',3.42,50000000,NULL,0,0,0,'buruh',0,32,'01',6),(145,'19090074','M.GALIH FIKRAN SYAH','A',1,'2019',3.8,50000000,NULL,0,3,3,'kurir',1,66,'09',8);
/*!40000 ALTER TABLE `mahasiswa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organisasi`
--

DROP TABLE IF EXISTS `organisasi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organisasi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mahasiswa_id` int DEFAULT NULL,
  `nama_organisasi` varchar(70) DEFAULT NULL,
  `peran_organisasi` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mahasiswa_id` (`mahasiswa_id`),
  CONSTRAINT `organisasi_ibfk_1` FOREIGN KEY (`mahasiswa_id`) REFERENCES `mahasiswa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organisasi`
--

LOCK TABLES `organisasi` WRITE;
/*!40000 ALTER TABLE `organisasi` DISABLE KEYS */;
INSERT INTO `organisasi` VALUES (18,141,'pramuka',2),(19,143,'pramuka',1),(38,145,'Paskibra',2),(39,145,'Pramuka',1);
/*!40000 ALTER TABLE `organisasi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prestasi`
--

DROP TABLE IF EXISTS `prestasi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prestasi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mahasiswa_id` int DEFAULT NULL,
  `nama_prestasi` varchar(70) DEFAULT NULL,
  `jenis_prestasi` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mahasiswa_id` (`mahasiswa_id`),
  CONSTRAINT `prestasi_ibfk_1` FOREIGN KEY (`mahasiswa_id`) REFERENCES `mahasiswa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestasi`
--

LOCK TABLES `prestasi` WRITE;
/*!40000 ALTER TABLE `prestasi` DISABLE KEYS */;
INSERT INTO `prestasi` VALUES (20,141,'Juara 1 menangis',2),(21,142,'Juara TikTok',3),(37,145,'Juara 1 Mobile Legend',3);
/*!40000 ALTER TABLE `prestasi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prodi`
--

DROP TABLE IF EXISTS `prodi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prodi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_prodi` varchar(50) DEFAULT NULL,
  `kode_prodi` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_kode_prodi` (`kode_prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prodi`
--

LOCK TABLES `prodi` WRITE;
/*!40000 ALTER TABLE `prodi` DISABLE KEYS */;
INSERT INTO `prodi` VALUES (1,'Teknik Informatika','09'),(2,'Teknik Komputer','04'),(7,'Teknik Elektronika','01'),(8,'Teknik Mesin','02'),(9,'Akuntansi','03'),(11,'Kebidanan','07'),(12,'Farmasi','08'),(13,'Akuntansi Sektor Publik','11'),(14,'Perhotelan','10'),(15,'Desain Komunikasi Visual','12'),(16,'Keperawatan','13');
/*!40000 ALTER TABLE `prodi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sertifikat`
--

DROP TABLE IF EXISTS `sertifikat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sertifikat` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mahasiswa_id` int DEFAULT NULL,
  `nama_sertifikat` varchar(70) DEFAULT NULL,
  `jenis_sertifikat` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mahasiswa_id` (`mahasiswa_id`),
  CONSTRAINT `sertifikat_ibfk_1` FOREIGN KEY (`mahasiswa_id`) REFERENCES `mahasiswa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sertifikat`
--

LOCK TABLES `sertifikat` WRITE;
/*!40000 ALTER TABLE `sertifikat` DISABLE KEYS */;
/*!40000 ALTER TABLE `sertifikat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(200) NOT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `no_hp` varchar(20) DEFAULT NULL,
  `foto` text,
  `website` varchar(60) DEFAULT NULL,
  `level` int DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Galih Syah','galih11120@gmail.com','sha256$mz8XGURVXdby4A7G$aaec21198bdc2418ebba9d10292a430597de54420721b07a2c46a52013bb67a4',0,'08986676180',NULL,'galihkhyff.co.id',1,NULL,'2023-07-25 19:13:19'),(20,'Eva','eva@gmail.com','sha256$ja6F9drC4vmHc7SG$cb5f903f5a1b83d6e43d4a8175559b8b972bea62d6318c59d61c6f9a40323dbb',0,'087772472900',NULL,NULL,2,NULL,NULL),(22,'Jeje','jeje@gmail.com','sha256$DYfsd2ssx7FH8Fuk$48d22fd76166d4781f7a95cc601ea144f5c3f860e4de3c7a758e515db5998f12',NULL,NULL,NULL,NULL,2,NULL,NULL),(23,'wawa','wawa@gmail.com','sha256$k5UVKVqS1Sqjqv6d$98640cf8ab020a4c3bf893d41ad4772390bfe1d67ebdc4b55db35f175b35f803',NULL,NULL,NULL,NULL,2,NULL,NULL),(24,'Mega','mega@gmail.com','sha256$owCx0aDjgM0OsRVG$544f3c329e98fc626f6d12ce3935a391d0e25504f4041349a85e888d77399246',NULL,NULL,NULL,NULL,2,'2023-07-25 00:05:20','2023-07-25 18:39:05'),(25,'Samsudin','samsudin@gmail.com','sha256$rkMDQFHdNAhO4g3t$5b9d0161b9547ddb3a1f35e2c3069959cb6ccefbb1a928df298f3565590a3c5d',NULL,NULL,NULL,NULL,2,'2023-07-25 00:05:53','2023-07-25 19:01:21'),(26,'satya','satya@gmail.com','sha256$cGh0YQfXOWpyWjdT$617926ff1d9150385f80c0a6576b85c48c0dfae8e0e67862960825f633ad3fea',NULL,NULL,NULL,NULL,2,'2023-07-25 19:02:14','2023-07-25 19:02:25'),(27,'firman','webgalih04@gmail.com','sha256$ItxXwJQezcIJjsVF$2b1789158020fc0da1c507e6161790063bf6bfe9c2c09854c8b76cb563de47a5',NULL,NULL,NULL,NULL,2,'2023-07-25 19:10:05','2023-07-25 19:12:14');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-25 22:23:07
