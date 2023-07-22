-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: siputa
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

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
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `kode_prodi` (`kode_prodi`),
  CONSTRAINT `admin_prodi_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `admin_prodi_ibfk_2` FOREIGN KEY (`kode_prodi`) REFERENCES `prodi` (`kode_prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_prodi`
--

LOCK TABLES `admin_prodi` WRITE;
/*!40000 ALTER TABLE `admin_prodi` DISABLE KEYS */;
INSERT INTO `admin_prodi` VALUES (2,20,'09'),(4,22,'02'),(5,23,'04');
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
  `toefl_score` float DEFAULT NULL,
  `parents_income` float DEFAULT NULL,
  `address` text,
  `sertifikat` int DEFAULT NULL,
  `prestasi` int DEFAULT NULL,
  `organisasi` int DEFAULT NULL,
  `pekerjaan_ortu` varchar(70) DEFAULT NULL,
  `relevan` tinyint(1) DEFAULT NULL,
  `predict_proba` int DEFAULT NULL,
  `prodi` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `prodi` (`prodi`),
  CONSTRAINT `mahasiswa_ibfk_1` FOREIGN KEY (`prodi`) REFERENCES `prodi` (`kode_prodi`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mahasiswa`
--

LOCK TABLES `mahasiswa` WRITE;
/*!40000 ALTER TABLE `mahasiswa` DISABLE KEYS */;
INSERT INTO `mahasiswa` VALUES (126,'19090074','Galih',NULL,1,'2019',3,NULL,50000000,NULL,3,3,3,'buruh',1,62,'09'),(127,'19090076','Reaz',NULL,1,'2019',3.2,NULL,50000000,NULL,8,3,2,'buruh',1,66,'04'),(128,'19090079','Andre',NULL,1,'2019',3.4,NULL,50000000,NULL,8,5,3,'buruh',1,67,'09'),(129,'19090080','Rojali',NULL,1,'2019',3.7,NULL,4500000,NULL,2,0,0,'buruh',1,68,'09'),(130,'19090081','Kibuli',NULL,1,'2019',2,NULL,100000,NULL,0,0,0,'buruh',0,18,'04'),(131,'19090082','Sasa',NULL,0,'2019',2,NULL,3000000,NULL,0,0,0,'buruh',0,36,'09'),(132,'19090083','Dicky',NULL,1,'2019',3.2,NULL,50000000,NULL,8,3,2,'buruh',1,66,'09');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organisasi`
--

LOCK TABLES `organisasi` WRITE;
/*!40000 ALTER TABLE `organisasi` DISABLE KEYS */;
INSERT INTO `organisasi` VALUES (5,126,'plugin',2),(6,126,'pramuka',1),(7,127,'PLUGIN',2),(8,128,'PLUGIN',1),(9,128,'RANA',1),(10,128,'Banyu Biru',1),(11,132,'PLUGIN',2);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prestasi`
--

LOCK TABLES `prestasi` WRITE;
/*!40000 ALTER TABLE `prestasi` DISABLE KEYS */;
INSERT INTO `prestasi` VALUES (6,126,'Lomba Catur ',3),(7,127,'Loba catur',3),(8,128,'Juara 1 Lomba Porgramming',2),(9,128,'Juara 1 Lomba Networking',2),(10,128,'Juara 2 Lomba Membaca Puisi',1),(11,132,'Loba catur',3);
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prodi`
--

LOCK TABLES `prodi` WRITE;
/*!40000 ALTER TABLE `prodi` DISABLE KEYS */;
INSERT INTO `prodi` VALUES (1,'Teknik Informatika','09'),(2,'Teknik Komputer','04'),(3,'Farmasi','02'),(5,'Teknik Mesin','06');
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sertifikat`
--

LOCK TABLES `sertifikat` WRITE;
/*!40000 ALTER TABLE `sertifikat` DISABLE KEYS */;
INSERT INTO `sertifikat` VALUES (5,126,'HUAWEI Certification Artificial Intelligence',3),(6,127,'Sertifikat HUAWEI',3),(7,127,'Sertifikat Dicoding',2),(8,127,'Sertifikat Junior Web Developer',3),(9,128,'Sertifikat HUAWEI',3),(10,128,'Sertifikat Dicoding',2),(11,128,'Sertifikat Junior Web Developer',3),(12,129,'Sertifikat Menanam Padi',2),(13,132,'Sertifikat HUAWEI',3),(14,132,'Sertifikat Dicoding',2),(15,132,'Sertifikat Junior Web Developer',3);
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Galih Syah','galih11120@gmail.com','sha256$mz8XGURVXdby4A7G$aaec21198bdc2418ebba9d10292a430597de54420721b07a2c46a52013bb67a4',0,'08986676180',NULL,'galihkhyff.co.id',1,NULL,NULL),(20,'Eva','eva@gmail.com','sha256$ja6F9drC4vmHc7SG$cb5f903f5a1b83d6e43d4a8175559b8b972bea62d6318c59d61c6f9a40323dbb',0,'087772472900',NULL,NULL,2,NULL,NULL),(22,'Jeje','jeje@gmail.com','sha256$DYfsd2ssx7FH8Fuk$48d22fd76166d4781f7a95cc601ea144f5c3f860e4de3c7a758e515db5998f12',NULL,NULL,NULL,NULL,2,NULL,NULL),(23,'wawa','wawa@gmail.com','sha256$k5UVKVqS1Sqjqv6d$98640cf8ab020a4c3bf893d41ad4772390bfe1d67ebdc4b55db35f175b35f803',NULL,NULL,NULL,NULL,2,NULL,NULL);
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

-- Dump completed on 2023-07-21 19:16:52
