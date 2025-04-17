-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: shbshop
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `adminacc`
--

DROP TABLE IF EXISTS `adminacc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adminacc` (
  `aid` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `acc` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adminacc`
--

LOCK TABLES `adminacc` WRITE;
/*!40000 ALTER TABLE `adminacc` DISABLE KEYS */;
INSERT INTO `adminacc` VALUES (1,'박관리','pa@pp.com','scrypt:32768:8:1$CpZrrjUaOVZQ9awv$5fcd19d27d739211902fc334630ea7c6a4a6fa1f2c25840bf388e6178cd6b2aa053865fd256eec3f6d1c3a970117da7f2abb86530c1a0dbf7943813b395cfdc6'),(2,'이과안','igann@innn.com','scrypt:32768:8:1$sX81X0R0s7lFyJ0m$fbf3fdc946a5151ab5888dfdf5ee20eb75d03e208e21c3f177e3828b64c9b638363d0a51626f6f68405f5166dbf5a9297b6e99d916f3c7816ab16d2932bb69d4'),(3,'김리이','klieeee@ppeeii.com','scrypt:32768:8:1$TiQf3ADQOIfvbRNh$bdb7bcb27d225946945e3887460cd2baab79dd34aa0a2140111e352ba75b794a1ebfcaef153cdba5ee28bbff9224ebba8594e08e86d58cccf865743916bb089e');
/*!40000 ALTER TABLE `adminacc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth4cfpw`
--

DROP TABLE IF EXISTS `auth4cfpw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth4cfpw` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `birth` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth4cfpw`
--

LOCK TABLES `auth4cfpw` WRITE;
/*!40000 ALTER TABLE `auth4cfpw` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth4cfpw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth4cjoin`
--

DROP TABLE IF EXISTS `auth4cjoin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth4cjoin` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth4cjoin`
--

LOCK TABLES `auth4cjoin` WRITE;
/*!40000 ALTER TABLE `auth4cjoin` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth4cjoin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth4cur`
--

DROP TABLE IF EXISTS `auth4cur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth4cur` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `birth` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth4cur`
--

LOCK TABLES `auth4cur` WRITE;
/*!40000 ALTER TABLE `auth4cur` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth4cur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth4pfpw`
--

DROP TABLE IF EXISTS `auth4pfpw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth4pfpw` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `birth` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth4pfpw`
--

LOCK TABLES `auth4pfpw` WRITE;
/*!40000 ALTER TABLE `auth4pfpw` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth4pfpw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth4pjoin`
--

DROP TABLE IF EXISTS `auth4pjoin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth4pjoin` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth4pjoin`
--

LOCK TABLES `auth4pjoin` WRITE;
/*!40000 ALTER TABLE `auth4pjoin` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth4pjoin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth4pur`
--

DROP TABLE IF EXISTS `auth4pur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth4pur` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `birth` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth4pur`
--

LOCK TABLES `auth4pur` WRITE;
/*!40000 ALTER TABLE `auth4pur` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth4pur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cbooktrade`
--

DROP TABLE IF EXISTS `cbooktrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cbooktrade` (
  `bid` bigint NOT NULL AUTO_INCREMENT,
  `cid` bigint NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `author` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `publish` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `isbn` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `price` int NOT NULL,
  `detail` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `region` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `img1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `img2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `img3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `createAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`bid`),
  KEY `FK_commercial_TO_cbooktrade_1` (`cid`),
  CONSTRAINT `FK_commercial_TO_cbooktrade_1` FOREIGN KEY (`cid`) REFERENCES `commercial` (`cid`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cbooktrade`
--

LOCK TABLES `cbooktrade` WRITE;
/*!40000 ALTER TABLE `cbooktrade` DISABLE KEYS */;
INSERT INTO `cbooktrade` VALUES (1,6,'실용음악 기초 화성학한 권으로 끝내는','이채현','1458music','9791189598228',12000,'필기가 되어있습니다.','부산광역시-부산진구','/static/product/commercial/6b0905b8ca354c54a2ac334cbdb7eefd_1.jpg','/static/product/commercial/dfc5932befba471797a4cd5ba3eda4fd_2.jpg','/static/product/commercial/476918398fbd40bc9d4b356d8c2fb3d4_3.jpg','2025-04-17 21:22:49'),(4,5,'기초 실용음악 화성학입문자도 입시생도 독학하기 쉬운 음악이론','이화균','해피엠뮤직','9791197094507',4000,'세월의 흔적이 있습니다.','부산광역시-중구','/static/product/commercial/5df101121ce84af98b2d0535a9347c93_1.jpg','/static/product/commercial/a049bf74f4864b0a8e49bf984eb6a6fa_2.jpg','/static/product/commercial/e62cfa7279ac4c0c9a8dd5c841593597_3.jpg','2025-04-17 21:34:37'),(6,4,'원예도감꽃과 채소로 가득찬 뜰 만들기','사토우치 아이','진선BOOKS','9788972216414',7000,'흙이 많이 묻어있습니다.','부산광역시-부산진구','/static/product/commercial/4bccc505e06f421090104b913af2e032_1.jpg','/static/product/commercial/1ef27543191c48c583be148cb1565e4b_2.jpg','/static/product/commercial/a1e5a1b04d7e4b66a41199684efa46c2_3.jpg','2025-04-17 21:42:28'),(7,3,'대금교본','조성래','한소리','9788995673331',4000,'색이 많이 바래있습니다.','경상남도-창원시','/static/product/commercial/b7b49c2e2c874667a921baa65216c393_1.jpg','/static/product/commercial/ae7bf6bd031942a0a142471bad0eb40d_2.jpg','/static/product/commercial/40f6b36e8d624f36ac541fa0f43a15d0_3.jpg','2025-04-17 21:48:06'),(8,2,'단소율보','김기수','은하출판사','9788931685039',3000,'상태 좋습니다.','경상남도-창원시','/static/product/commercial/fe75ccdad15f4839ae15ce875c608180_1.jpg','/static/product/commercial/793e3917fe7240de8c18356a183f2fe0_2.jpg','/static/product/commercial/eb6aa1f5fb604986b87613a7b528c5ac_3.jpg','2025-04-17 21:52:59'),(9,1,'국악교육론','윤명원,임미선,이용식,신은주,이진원','학지사','9788999714016',4000,'깨끗하게 사용했습니다.','경상남도-창원시','/static/product/commercial/f2fca8bb1f184d1681d5aae49eb89dea_1.jpg','/static/product/commercial/64a168084615471099ddb1d9fbfaedba_2.jpg','/static/product/commercial/5f1ccc7f096442a5b5bc922f1f7592fb_3.jpg','2025-04-17 21:56:15');
/*!40000 ALTER TABLE `cbooktrade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commercial`
--

DROP TABLE IF EXISTS `commercial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commercial` (
  `cid` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `presidentName` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `businessmanName` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `birth` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `businessEmail` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `nickname` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `region` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `img` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `coNumber` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `licence` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `state` int NOT NULL DEFAULT '1',
  `createAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commercial`
--

LOCK TABLES `commercial` WRITE;
/*!40000 ALTER TABLE `commercial` DISABLE KEYS */;
INSERT INTO `commercial` VALUES (1,'박도지사','박대장','박사장','1970-06-12','010-1324-3344','sdqwdq@gmail.com','qwdqwdas@gmail.com','scrypt:32768:8:1$A5voHXVb9mjikQ8q$e3c2945eaf66cdebc58fd517fff6a5acbfe54721f6fdf9a34807845ee07663a6e1187da0404e7f87d95b145a6b08a041fe43fb3633df99d476e55dc270a7dfc6','바아아악사장','경상남도 창원시 성산구 중앙대로 104 마이우스빌딩 지하 1층','경상남도-창원시','/static/user/commercial/38760f987eef40979776ccc6e6d62818_1.PNG','333-22-55555','/static/licence/5daf1d13d7de49cfac58f869ef63d07f_.pdf',1,'2025-04-17 17:30:19'),(2,'김도지사','김대장','김사장','1960-07-04','010-3333-4444','dqwdjqwkdh@naver.com','wqeqwqwd@naver.com','scrypt:32768:8:1$UIEZKW9CIWj7ojpb$591fbbae219600c9abf727bd121c11acdd24134b612f50586a917d8e41c07103901f33d7470ad63641cd31317c1c3d1f4d070a0ac59d48ca454b2563d08fc942','김김김','경상남도 창원시 성산구 원이대로 587 지하 1층','경상남도-창원시','/static/user/commercial/efae798d82e84995936e679b299bb153_2.PNG','111-22-33333','/static/licence/ec252113892b4688afafb7890059f997_.pdf',1,'2025-04-17 17:58:08'),(3,'응우옌','응우','옌옌','1982-07-08','010-1333-1446','qwdasdqw@nate.com','wqedqasdasd@nate.com','scrypt:32768:8:1$eH9ebV1krqY0ndEd$6aadc7e1dc8e0472b7d258c550b2f64d173814bab29c1721b9775bc9a9a495a9ba1bccd45cef29fcc1d934ba5559b3807dc181bd6104339302b1080c4a60f357','베트맨','경상남도 창원시 성산구 상남로 93 공영주차빌딩 B1','경상남도-창원시','/static/user/commercial/36c43c7d765b44c78fc8b18b2d09aea1_3.PNG','222-22-22222','/static/licence/90fa84f9670d499bbc9be1e4805c0c59_.pdf',1,'2025-04-17 18:03:32'),(4,'솜싹','솜싹','솜싹','1997-09-01','010-2222-3344','qwdqwd@gmail.com','qwdqwd@gmail.com','scrypt:32768:8:1$chd5bIrPCiyldNK4$b4988ba4e35c129a8d037bff276e30029d102ece51412b014328c249e07bd4cd195c28f53a638027208834bc07269a554cea4208ae24d8b00cabd61b5fe5b49a','솜사탕','부산광역시 부산진구 중앙대로 658 교보생명빌딩 1층, 지하 1층','부산광역시-부산진구','/static/user/commercial/2d866bd0d9c740659876b1619f7f51e3_1.PNG','333-33-33333','/static/licence/aab21a1899d84351be4c625a4375ce25_.pdf',1,'2025-04-17 18:15:22'),(5,'아쿠아','마쿠아','사쿠아','1999-11-13','010-7777-8888','saqdwd@naver.com','saqdwd@naver.com','scrypt:32768:8:1$cprI6P3bUdjjED95$ae2f204a7d258b3b0f6db60f500ebc0fc1bbf99fb89dd52d6d8c616138e96cbd8c4f53bf189c4dc186c1a1c8a59b9cd0748f93e00bea009921771a32ca9676e0','물물물','부산광역시 중구 중앙대로 2 아쿠아몰 5층','부산광역시-중구','/static/user/commercial/0dfeef21889b405088a989ab1533b97d_2.PNG','123-12-12312','/static/licence/b420ccba0c72409f98f7a55fd2961700_.pdf',1,'2025-04-17 18:22:11'),(6,'지니','알라딘','알라딘','1988-12-14','010-0000-0000','dqwdwqd@gmail.com','qwdasda@gmail.com','scrypt:32768:8:1$c9iWmLQBDIAJVJrz$e96ae8a586d6f7041d52da87b6b1430d82038deb38c13fb67b8f61d421997c657e139066c42a3de81121b9412b2fcf23d7dc835b8b68aaf6beeed848d0e9f18a','요술램프','부산광역시 부산진구 중앙대로 709 금융프라자빌딩 지하 2층','부산광역시-부산진구','/static/user/commercial/9e78670ed351470e860f564a45a5cebe_3.PNG','111-22-33333','/static/licence/d09cd2fe1b7d4b64a2f2965a66566f7b_.pdf',1,'2025-04-17 18:25:41');
/*!40000 ALTER TABLE `commercial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commercialcert`
--

DROP TABLE IF EXISTS `commercialcert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commercialcert` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `cid` bigint NOT NULL,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `presidentName` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `businessmanName` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `birth` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `businessEmail` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `coNumber` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `licence` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `reason` varchar(255) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '심사중',
  `state` int NOT NULL DEFAULT '1',
  `createAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx`),
  KEY `FK_commercial_TO_commercialcert_1` (`cid`),
  CONSTRAINT `FK_commercial_TO_commercialcert_1` FOREIGN KEY (`cid`) REFERENCES `commercial` (`cid`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commercialcert`
--

LOCK TABLES `commercialcert` WRITE;
/*!40000 ALTER TABLE `commercialcert` DISABLE KEYS */;
INSERT INTO `commercialcert` VALUES (1,1,'박도지사','박대장','박사장','1970-06-12','010-1324-3344','sdqwdq@gmail.com','qwdqwdas@gmail.com','경남 창원시 성산구 중앙대로 104 마이우스빌딩 지하 1층','333-22-55555','/static/licence/5daf1d13d7de49cfac58f869ef63d07f_.pdf','심사중',1,'2025-04-17 17:30:19'),(2,2,'김도지사','김대장','김사장','1960-07-04','010-3333-4444','dqwdjqwkdh@naver.com','wqeqwqwd@naver.com','경상남도 창원시 성산구 원이대로 587 지하 1층','111-22-33333','/static/licence/ec252113892b4688afafb7890059f997_.pdf','심사중',1,'2025-04-17 17:58:08'),(3,3,'응우옌','응우','옌옌','1982-07-08','010-1333-1446','qwdasdqw@nate.com','wqedqasdasd@nate.com','경상남도 창원시 성산구 상남로 93 공영주차빌딩 B1','222-22-22222','/static/licence/90fa84f9670d499bbc9be1e4805c0c59_.pdf','심사중',1,'2025-04-17 18:03:32'),(4,3,'솜싹','솜싹','솜싹','1997-09-01','010-2222-3344','qwdasdqw@nate.com','qwdqwd@gmail.com','부산광역시 부산진구 중앙대로 658 교보생명빌딩 1층, 지하 1층','333-33-33333','/static/licence/aab21a1899d84351be4c625a4375ce25_.pdf','심사중',1,'2025-04-17 18:15:22'),(5,5,'아쿠아','마쿠아','사쿠아','1999-11-13','010-7777-8888','saqdwd@naver.com','saqdwd@naver.com','부산광역시 중구 중앙대로 2 아쿠아몰 5층','123-12-12312','/static/licence/b420ccba0c72409f98f7a55fd2961700_.pdf','심사중',1,'2025-04-17 18:22:11'),(6,6,'지니','알라딘','알라딘','1988-12-14','010-0000-0000','dqwdwqd@gmail.com','qwdasda@gmail.com','부산광역시 부산진구 중앙대로 709 금융프라자빌딩 지하 2층','111-22-33333','/static/licence/d09cd2fe1b7d4b64a2f2965a66566f7b_.pdf','심사중',1,'2025-04-17 18:25:41');
/*!40000 ALTER TABLE `commercialcert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorite4c`
--

DROP TABLE IF EXISTS `favorite4c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorite4c` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `sid` bigint NOT NULL,
  `cid` bigint NOT NULL,
  PRIMARY KEY (`idx`),
  KEY `FK_shop_TO_favorite4c_1` (`sid`),
  KEY `FK_commercial_TO_favorite4c_1` (`cid`),
  CONSTRAINT `FK_commercial_TO_favorite4c_1` FOREIGN KEY (`cid`) REFERENCES `commercial` (`cid`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `FK_shop_TO_favorite4c_1` FOREIGN KEY (`sid`) REFERENCES `shop` (`sid`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorite4c`
--

LOCK TABLES `favorite4c` WRITE;
/*!40000 ALTER TABLE `favorite4c` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorite4c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorite4p`
--

DROP TABLE IF EXISTS `favorite4p`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favorite4p` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `pid` bigint NOT NULL,
  `sid` bigint NOT NULL,
  PRIMARY KEY (`idx`),
  KEY `FK_personal_TO_favorite4p_1` (`pid`),
  KEY `FK_shop_TO_favorite4p_1` (`sid`),
  CONSTRAINT `FK_personal_TO_favorite4p_1` FOREIGN KEY (`pid`) REFERENCES `personal` (`pid`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `FK_shop_TO_favorite4p_1` FOREIGN KEY (`sid`) REFERENCES `shop` (`sid`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorite4p`
--

LOCK TABLES `favorite4p` WRITE;
/*!40000 ALTER TABLE `favorite4p` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorite4p` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pbooktrade`
--

DROP TABLE IF EXISTS `pbooktrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pbooktrade` (
  `bid` bigint NOT NULL AUTO_INCREMENT,
  `pid` bigint NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `author` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `publish` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `isbn` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `price` int NOT NULL,
  `detail` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `region` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `img1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `img2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `img3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `createAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`bid`),
  KEY `FK_personal_TO_pbooktrade_1` (`pid`),
  CONSTRAINT `FK_personal_TO_pbooktrade_1` FOREIGN KEY (`pid`) REFERENCES `personal` (`pid`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pbooktrade`
--

LOCK TABLES `pbooktrade` WRITE;
/*!40000 ALTER TABLE `pbooktrade` DISABLE KEYS */;
INSERT INTO `pbooktrade` VALUES (1,1,'끝내기(이창호 정통 바둑 3)','이창호','삼호미디어','9788978491167',3000,'상태: 깨끗함','부산광역시-부산진구','/static/product/personal/294d6887feba4e8b93a7ddc476710a8c_1.jpg','/static/product/personal/03a617434fdc47a98b7e6e00b04d0db8_2.jpg','/static/product/personal/252a005373394e84ae6c3b82a7a64207_3.jpg','2025-04-17 20:39:07'),(2,1,'상수를 두려워 말자 1 아진바둑시리즈 57','조치훈','아진','9788978840712',6000,'다소 낙서가 있는점을 감안하셔야 합니다.','부산광역시-부산진구','/static/product/personal/8981c002cc184881a0cf4de612f91fc4_1.jpg','/static/product/personal/780f9c666362455fb7ab4cafe7e8193a_2.jpg','/static/product/personal/43c03e5ba0a249d1a59c3b9176274038_3.jpg','2025-04-17 20:50:49'),(3,3,'천수경','무비','창','9788974531058',2000,'색이 많이 바랬습니다.','경상남도-창원시','/static/product/personal/c24f4a3ec6954badbf860bdf9f91dfb3_1.jpg','/static/product/personal/80e1b411413c454089deb294eb15e9e5_2.jpg','/static/product/personal/1cf30494024e425a98956786b21d40a3_3.jpg','2025-04-17 20:57:03'),(4,2,'금강경','무비','창','9788974530921',2000,'거의 새것과 마찬가지입니다.','경상남도-진주시','/static/product/personal/292d817fb73841c393fa1c9159964b8a_1.jpg','/static/product/personal/f9f74846d4734b4b8a433ca50722d44a_2.jpg','/static/product/personal/3abd49f137c04c4b87495ff48a4614ff_3.jpg','2025-04-17 21:01:06'),(5,3,'반야심경','무비','창','9788974530914',3000,'미개봉 상품입니다.','경상남도-창원시','/static/product/personal/fe675eb01f7c40ed9ce9af0cea574499_1.jpg','/static/product/personal/4677f3d2256d4e8da76100dfd5c7c324_2.jpg','/static/product/personal/335691f8f9394107959ed23146b2029c_3.jpg','2025-04-17 21:05:27'),(6,1,'주역독해천명에 따라 인생의 완성을 이루는 길','강병국','김영사','9791173321382',10000,'표지에 기스가 조금 많습니다.','부산광역시-부산진구','/static/product/personal/093c21cfebdf408484c2ccbe7153f3f7_1.jpg','/static/product/personal/a933517c174d479185e001182781a540_2.jpg','/static/product/personal/fb9dc20d8a454e83bd3de0b0b2738c83_3.jpg','2025-04-17 21:10:01');
/*!40000 ALTER TABLE `pbooktrade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal`
--

DROP TABLE IF EXISTS `personal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal` (
  `pid` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `birth` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `tel` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `nickname` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `region` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `img` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal`
--

LOCK TABLES `personal` WRITE;
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` VALUES (1,'김아무개','1999-12-10','010-1111-1111','aaa@naver.com','scrypt:32768:8:1$9U6HwfAPT1ljdDuF$ff921411962cbccf51b9c2a72852368295fec1ce329b0437f4fa267cea1b925f16eebd0d861ea06e62ab2c75758e096b9167411035ce55d6d6c4cc29ae894df5','김김아무아무','부산광역시 부산진구 중앙대로 672','부산광역시-부산진구','/static/user/personal/d61a6240a5b24c99a32587d12b3c751b_1.PNG','2025-04-17 16:45:52'),(2,'신아무개','2010-10-14','010-1234-5678','aqweqwd@naver.com','scrypt:32768:8:1$HgmcdweaKsl8yAGP$8f90efbbc397001d548ba5f4a1fc19c8529ffac63a8fa57f1938dba390622a636adc3ec96501187683af487d49e7cdd442db4615316a561b526ca6c9cccdd463','신나는무개','경상남도 진주시 진주대로 501','경상남도-진주시','/static/user/personal/f439321d7976486bbc3550a4ca85fdc6_2.PNG','2025-04-17 16:52:47'),(3,'이아무개','2000-03-04','010-2222-3333','qwdjqwd@gmail.com','scrypt:32768:8:1$fzAP3uKg2EzQhglJ$0f3d59bd44107b93b910254c8bc32ca58995530c2097414da06992220fcb4355126ad81ab1be88ec7664671f4ba6de04b2f104ba2558f89c5d70f5406745f2cb','이이이잉','경상남도 창원시 의창구 중동로 34','경상남도-창원시','/static/user/personal/ba859eb4a1484b80a6c39082c6af109c_3.PNG','2025-04-17 17:03:27');
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sbooktrade`
--

DROP TABLE IF EXISTS `sbooktrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sbooktrade` (
  `bid` bigint NOT NULL AUTO_INCREMENT,
  `sid` bigint NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `author` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `publish` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `isbn` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `price` int NOT NULL,
  `detail` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `region` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `img1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `img2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `img3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `createAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`bid`),
  KEY `FK_shop_TO_sbooktrade_1` (`sid`),
  CONSTRAINT `FK_shop_TO_sbooktrade_1` FOREIGN KEY (`sid`) REFERENCES `shop` (`sid`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sbooktrade`
--

LOCK TABLES `sbooktrade` WRITE;
/*!40000 ALTER TABLE `sbooktrade` DISABLE KEYS */;
INSERT INTO `sbooktrade` VALUES (1,3,'명화 속 틀린 그림 찾기 1: 세계세계 Masterpieces Worldwide','펀앤아트 랩','펀앤아트','9788961095365',7300,'반 정도 풀었습니다.','경상남도-창원시','/static/product/shop/4467f6f09ea54bf09b7dd45d6e56e063_1.jpg','/static/product/shop/34c2a7be34174ea18c56742f2beef8fd_2.jpg','/static/product/shop/1c3481d1492c43dba0fdcfe767573387_3.jpg','2025-04-17 22:01:41'),(2,2,'당구교본','현대레저연구회','태을출판사','9788949302966',6200,'거의 새것','경상남도-창원시','/static/product/shop/0d886d7f2bfc4bb3ad79873f5fb0ded3_1.jpg','/static/product/shop/a5111a32577040009c7b627aff132c3d_2.jpg','/static/product/shop/f2f0e86877564db8bb3c17e1fee0c109_3.jpg','2025-04-17 22:05:45'),(3,3,'차 상식사전 티 소믈리에가 알려주는','리사 리처드슨','길벗','9791160500370',6100,'사놓고 방치했습니다.','경상남도-창원시','/static/product/shop/7e05862ce1ea4906804fc9fce98bb4dc_1.jpg','/static/product/shop/644c0646f99049b7be314c3232e68468_2.jpg','/static/product/shop/f7cc569736524a32bd92a733b0deb11c_3.jpg','2025-04-17 22:09:44'),(4,6,'와인상식사전소믈리에도 즐겨 보는','이재술','백산출판사','9791165676544',8600,'중간중간 술이 흘려져 있습니다.','부산광역시-부산진구','/static/product/shop/ae4aa231e6ea48d0825f758e527b5a22_1.jpg','/static/product/shop/73482d6dc2724610b11f0ad668b545b9_2.jpg','/static/product/shop/6eabd46eb5c54666b7e942352c6a7863_3.jpg','2025-04-17 22:14:33'),(5,5,'세상에서 제일 재밌는 종이접기색종이 한 장이면 장난감 뚝딱!','네모아저씨(이원표)','슬로래빗','9791186494431',6400,'종이접기 재미있어요.','부산광역시-중구','/static/product/shop/1b488f4c25db4ee59188fc05c4770b56_1.jpg','/static/product/shop/7b22ab701e08420c9a7958bd7580bd38_2.jpg','/static/product/shop/5e4d53f1565c41538518d7949b5087f2_3.jpg','2025-04-17 22:19:37'),(6,4,'내 손으로 황토집 짓기흙집 짓기 DIY','유종','한문화사','9788994997292',11000,'내용이 알찹니다.','부산광역시-부산진구','/static/product/shop/7b0403e7e934468d8f21e25084216b6f_1.jpg','/static/product/shop/b36d9258ff56459e9f0a240605c5f756_2.jpg','/static/product/shop/be550f43028a4486952551051746cd7c_3.png','2025-04-17 22:24:22');
/*!40000 ALTER TABLE `sbooktrade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop`
--

DROP TABLE IF EXISTS `shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop` (
  `sid` bigint NOT NULL AUTO_INCREMENT,
  `cid` bigint NOT NULL,
  `presidentName` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `businessmanName` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
  `shopName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `shoptel` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `businessEmail` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `region` varchar(64) COLLATE utf8mb4_general_ci NOT NULL,
  `open` varchar(16) COLLATE utf8mb4_general_ci NOT NULL,
  `close` varchar(16) COLLATE utf8mb4_general_ci NOT NULL,
  `holiday` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `shopimg1` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `shopimg2` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `shopimg3` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `etc` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `createAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`sid`),
  KEY `FK_commercial_TO_shop_1` (`cid`),
  CONSTRAINT `FK_commercial_TO_shop_1` FOREIGN KEY (`cid`) REFERENCES `commercial` (`cid`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop`
--

LOCK TABLES `shop` WRITE;
/*!40000 ALTER TABLE `shop` DISABLE KEYS */;
INSERT INTO `shop` VALUES (1,1,'박대장','박사장','교보문고 창원점','010-1324-3344','qwdqwdas@gmail.com','경상남도 창원시 성산구 중앙대로 104 마이우스빌딩 지하 1층','경상남도-창원시','11:00','21:00','연중 무휴','/static/shop/945d87cb170a4c228d6881d9da002b97_1.jpg','/static/shop/b31ac090aa9741089248916ff2fd60e0_2.jpg','/static/shop/36e5a3ff29c04c6e99c12b033a7bcb43_3.jpg','안녕하세요','2025-04-17 19:39:31'),(2,2,'김대장','김사장','그랜드문고 창원점','010-3333-4444','wqeqwqwd@naver.com','경상남도 창원시 성산구 원이대로 587 지하 1층','경상남도-창원시','10시','22시','매주 목요일 휴무','/static/shop/ab94a5695a2c4278b0857e0ba1d5b7e7_1.jpg','/static/shop/e34e60e697bd4666820ce3b21b5d3b1c_2.jpg','/static/shop/f277df60c73b44449803534a4e5b6cb5_3.jpg','반갑습니다.','2025-04-17 19:49:31'),(3,3,'응우','옌옌','알라딘 창원점','010-1333-1446','wqedqasdasd@nate.com','경상남도 창원시 성산구 상남로 93 공영주차빌딩 B1','경상남도-창원시','9','20','매주 화요일 휴무','/static/shop/72fc3757ffd743c0a0ced70f24c469f1_1.jpg','/static/shop/83b1e052b920412e8387bcbab5e4aefe_2.jpg','/static/shop/6f3b08b32e834812b0d9d1fb421d49ae_3.jpg','반갑습니다.','2025-04-17 19:52:26'),(4,4,'솜싹','솜싹','교보문고 부산점','010-2222-3344','qwdqwd@gmail.com','부산광역시 부산진구 중앙대로 658 교보생명빌딩 1층, 지하 1층','부산광역시-부산진구','11:00','21:00','연중 무휴','/static/shop/42b3384240364e40a2e9a1a01644780f_1.png','/static/shop/9a8fb6fa42554165bf13a57b362f6949_2.jpg','/static/shop/655c7610c2104d73b031a65dc091059b_3.jpg','안녕하세요. 부산 교보문고입니다.','2025-04-17 19:56:27'),(5,5,'마쿠아','사쿠아','영풍문고 부산점','010-7777-8888','saqdwd@naver.com','부산광역시 중구 중앙대로 2 아쿠아몰 5층','부산광역시-중구','오전 9시','오후 9시','첫 째 주, 셋 째 주 일요일 휴무','/static/shop/8a9ee76e59a14dd6bd50fc1209938efc_1.jpg','/static/shop/fef0473f297c45299e72e01b5369357a_2.jpg','/static/shop/38db3d4570914154aedebfac46bee16e_3.jpg','선착순 세 분께 쿠폰 드립니다.','2025-04-17 20:00:12'),(6,6,'알라딘','알라딘','알라딘 부산점','010-0000-0000','qwdasda@gmail.com','부산광역시 부산진구 중앙대로 709 금융프라자빌딩 지하 2층','부산광역시-부산진구','9','20','매주 화요일 휴무','/static/shop/4a6821bdbab84bd8945c64b58d64615e_1.jpg','/static/shop/b72e0958110f413abbca401ae9230b68_2.jpg','/static/shop/248c87e47cf14448b2281723054bad08_3.jpg','알라딘 부산점입니다.','2025-04-17 20:03:38');
/*!40000 ALTER TABLE `shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vaild4cfpw`
--

DROP TABLE IF EXISTS `vaild4cfpw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vaild4cfpw` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vaild4cfpw`
--

LOCK TABLES `vaild4cfpw` WRITE;
/*!40000 ALTER TABLE `vaild4cfpw` DISABLE KEYS */;
/*!40000 ALTER TABLE `vaild4cfpw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vaild4cjoin`
--

DROP TABLE IF EXISTS `vaild4cjoin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vaild4cjoin` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vaild4cjoin`
--

LOCK TABLES `vaild4cjoin` WRITE;
/*!40000 ALTER TABLE `vaild4cjoin` DISABLE KEYS */;
/*!40000 ALTER TABLE `vaild4cjoin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vaild4cur`
--

DROP TABLE IF EXISTS `vaild4cur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vaild4cur` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vaild4cur`
--

LOCK TABLES `vaild4cur` WRITE;
/*!40000 ALTER TABLE `vaild4cur` DISABLE KEYS */;
/*!40000 ALTER TABLE `vaild4cur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vaild4pfpw`
--

DROP TABLE IF EXISTS `vaild4pfpw`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vaild4pfpw` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vaild4pfpw`
--

LOCK TABLES `vaild4pfpw` WRITE;
/*!40000 ALTER TABLE `vaild4pfpw` DISABLE KEYS */;
/*!40000 ALTER TABLE `vaild4pfpw` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vaild4pjoin`
--

DROP TABLE IF EXISTS `vaild4pjoin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vaild4pjoin` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vaild4pjoin`
--

LOCK TABLES `vaild4pjoin` WRITE;
/*!40000 ALTER TABLE `vaild4pjoin` DISABLE KEYS */;
/*!40000 ALTER TABLE `vaild4pjoin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vaild4pur`
--

DROP TABLE IF EXISTS `vaild4pur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vaild4pur` (
  `idx` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `authCode` int NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vaild4pur`
--

LOCK TABLES `vaild4pur` WRITE;
/*!40000 ALTER TABLE `vaild4pur` DISABLE KEYS */;
/*!40000 ALTER TABLE `vaild4pur` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-18  7:26:16
