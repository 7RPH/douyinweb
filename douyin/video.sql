-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-06-07 21:30:11
-- 服务器版本： 5.7.26
-- PHP 版本： 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `douyin`
--

-- --------------------------------------------------------

--
-- 表的结构 `video`
--

CREATE TABLE `video` (
  `vpath` text COLLATE utf8_unicode_ci NOT NULL,
  `vsize` varchar(512) COLLATE utf8_unicode_ci NOT NULL,
  `vsummary` text COLLATE utf8_unicode_ci NOT NULL,
  `putdate` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `uname` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `likenum` int(64) NOT NULL,
  `comnum` int(64) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `video`
--

INSERT INTO `video` (`vpath`, `vsize`, `vsummary`, `putdate`, `uname`, `likenum`, `comnum`) VALUES
('./videos/第45届世界技能大赛网络安全项目湖北选拔赛，选手不仅要防守的自己服务器，还要攻破对方主机！.mp4', '4.22MB', ' 2019年网络安全主题手抄报教程，双击收藏吧', '2019-09-21 09:37:51', '曲洲老师画卡通', 17792, 865);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
