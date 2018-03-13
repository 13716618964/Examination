-- MySQL dump 10.13  Distrib 5.5.40, for Win64 (x86)
--
-- Host: 192.168.1.98    Database: Examination_system
-- ------------------------------------------------------
-- Server version	5.7.19-log

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
-- Table structure for table `Examination_subjects`
--

DROP TABLE IF EXISTS `Examination_subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Examination_subjects` (
  `class` varchar(10) NOT NULL COMMENT '班级',
  `subjects` varchar(100) NOT NULL COMMENT '考试科目'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Examination_subjects`
--

LOCK TABLES `Examination_subjects` WRITE;
/*!40000 ALTER TABLE `Examination_subjects` DISABLE KEYS */;
INSERT INTO `Examination_subjects` VALUES ('111','英语,体育,思想道德修养与法律基础,机械制图,线性代数,计算机基础,高等数学'),('成人教育','运维基础,随机字符');
/*!40000 ALTER TABLE `Examination_subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Historical_achievement`
--

DROP TABLE IF EXISTS `Historical_achievement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Historical_achievement` (
  `userID` int(11) NOT NULL,
  `achievement` varchar(5) NOT NULL,
  `date` datetime DEFAULT NULL,
  `subject` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Historical_achievement`
--

LOCK TABLES `Historical_achievement` WRITE;
/*!40000 ALTER TABLE `Historical_achievement` DISABLE KEYS */;
INSERT INTO `Historical_achievement` VALUES (1153,'50','2018-03-08 16:17:05','高等数学'),(1153,'100','2018-03-08 16:25:35','高等数学'),(1153,'0','2018-03-09 10:03:13','高等数学'),(1153,'0','2018-03-09 11:55:50','高等数学'),(1153,'50','2018-03-09 11:59:03','高等数学');
/*!40000 ALTER TABLE `Historical_achievement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Questions`
--

DROP TABLE IF EXISTS `Questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Questions` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `subject` text NOT NULL,
  `question` text NOT NULL COMMENT '题目',
  `answer1` text NOT NULL,
  `answer2` text NOT NULL,
  `answer3` text NOT NULL,
  `answer4` text NOT NULL,
  `Right_Answer` text NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Questions`
--

LOCK TABLES `Questions` WRITE;
/*!40000 ALTER TABLE `Questions` DISABLE KEYS */;
INSERT INTO `Questions` VALUES (1,'高等数学','1+1','1','2','3','4','2'),(2,'高等数学','1+9','8','9','10','11','10'),(3,'随机字符','yBrfsiVWlgTgsx','NeGhl','GxJImMRf','PvsUvG','nALdVA','NeGhl'),(4,'随机字符','xrmsvPKxRjwZO','gvcNo','tAhEKeubGt','VGYwOyWn','hgUlMO','tAhEKeubGt'),(5,'随机字符','SzACbEJIUEXIi','pbUaTg','CaWWDoBvj','MmJZEEtelp','cLRukoftXv','pbUaTg'),(6,'随机字符','XQxRcR','gEjwVYir','rvdwd','vtelbGBt','fMEvbBDL','gEjwVYir'),(7,'随机字符','zlNvFabRZbrStpWaKti','xxrtA','uNGov','vQgjO','NfDWtwboj','vQgjO'),(8,'随机字符','fhRjdjoCTUYRyDKLinO','rFrTiDvUH','UzrmKfU','mmcec','GmrPNxun','GmrPNxun'),(9,'随机字符','HQXZQtTOObmmJcwDp','lZbrfwlt','wGNLokNLY','jNaUE','uTUBsq','wGNLokNLY'),(10,'随机字符','LZpjfstR','kTLtz','uhdmaAC','CwHiFYoV','rEvRHb','CwHiFYoV'),(11,'随机字符','MBBWDMYnvCTqsZjhvq','XEWTcNaQJ','DHRBZ','rEWIDRirdM','CPJxiPoFRw','rEWIDRirdM'),(12,'随机字符','VarWpPBN','JUmkz','rNijA','XJlTf','HsncmjScCK','JUmkz'),(13,'随机字符','kjMFvYYTOQ','eBjUMb','JoqDxaVKe','BFNrsBlZC','tsaMJX','JoqDxaVKe'),(14,'随机字符','kFhwugkfGZBOIW','zgyJs','CdnReh','zBtnjK','ROLwro','ROLwro'),(15,'随机字符','lCDoQCVsBRMgJOOcZHXM','VcItM','uPtTBDAE','GRskL','SDSoMF','uPtTBDAE'),(16,'随机字符','LddXwhyiyagpPVld','AEaZBo','grafbWUe','cvcLXERtPs','ONkAKoTNgC','grafbWUe'),(17,'随机字符','oHyILBfZ','AvKiWhxzu','AQeQYZxDTP','IFWcv','plaPRyP','IFWcv'),(18,'随机字符','HsuDoNij','MOFGjSbc','xTlCAsAAeE','FingSJZ','ZwRoLe','ZwRoLe'),(19,'随机字符','euJXvQIBjCgPmgVr','sYtsoIu','KdtSMAlds','OYJflPbE','PUOxBbxd','sYtsoIu'),(20,'随机字符','TvxTgcoPjKOTHmYh','RIMbZYbC','MZuKBBweQc','sjtOiebzZU','ssBgs','sjtOiebzZU'),(21,'随机字符','GWKOiTXHVHN','EUrRIn','mtrdiwio','lHEsOsS','rsoDsqQrKT','rsoDsqQrKT'),(22,'随机字符','gHsxZiF','lMukRd','zKYZyjJ','XrxMQXtYIn','AsYjqlQ','lMukRd'),(23,'随机字符','LflNhNyha','TzEhcTTtqE','Hklxp','GWrIcWyeaK','YBUxLDMyz','TzEhcTTtqE'),(24,'随机字符','dOTrMmBP','ABiTX','CsiqhyTA','uwzdOwFpXz','bfJGZacUK','bfJGZacUK'),(25,'随机字符','PXWirCmyIeTYrXPS','VcchMkUJdO','ayDBQrC','asFojVM','VYGPFyH','ayDBQrC'),(26,'随机字符','oadydpoGg','FIawg','nwipa','sBkgieJkfk','BxRMJ','FIawg'),(27,'随机字符','rimOGMdGShgGb','ZiHBr','zydbVosF','mjRNOfLLR','syDoKW','mjRNOfLLR'),(28,'随机字符','hUZSjIqnTh','OWWSZffYPw','hWiiP','uFAmYeltxL','rDuUBIQUo','OWWSZffYPw'),(29,'随机字符','RRRPFyQAG','RpUHJC','mCAHaD','BbMwPEd','HCydRLv','mCAHaD');
/*!40000 ALTER TABLE `Questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL COMMENT '学生姓名',
  `student_ID` varchar(13) NOT NULL COMMENT '学号',
  `class` varchar(10) NOT NULL COMMENT '班级',
  `password` varchar(35) NOT NULL,
  `Enrollment` date DEFAULT NULL COMMENT '入学年份',
  `Graduation` date DEFAULT NULL COMMENT '毕业年份',
  PRIMARY KEY (`userID`),
  UNIQUE KEY `student_ID` (`student_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1155 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1152,'王小明','1121111','电子1211','e10adc3949ba59abbe56e057f20f883e','2016-09-01','2019-07-01'),(1153,'aaa','111','111','e10adc3949ba59abbe56e057f20f883e','2015-09-01','2018-07-01'),(1154,'刘博文','13716618964','成人教育','e10adc3949ba59abbe56e057f20f883e','2011-09-01','2014-07-01');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-12 17:35:18
