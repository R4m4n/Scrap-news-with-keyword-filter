-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 04, 2020 at 03:16 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.3.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `newsparser`
--

-- --------------------------------------------------------

--
-- Table structure for table `rss_source_link`
--

CREATE TABLE `rss_source_link` (
  `id` int(10) UNSIGNED NOT NULL,
  `source_id` int(10) UNSIGNED DEFAULT NULL,
  `rss_id` int(10) UNSIGNED DEFAULT NULL,
  `topic_id` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `rss_table`
--

CREATE TABLE `rss_table` (
  `id` int(10) UNSIGNED NOT NULL,
  `title` text DEFAULT NULL,
  `source_link` varchar(500) DEFAULT '-',
  `date_created` datetime NOT NULL,
  `processed` tinyint(4) UNSIGNED NOT NULL DEFAULT 0,
  `topic_id` int(10) UNSIGNED NOT NULL DEFAULT 405,
  `date_create_unix` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sources`
--

CREATE TABLE `sources` (
  `id` int(10) UNSIGNED NOT NULL,
  `source_name` varchar(100) NOT NULL,
  `source_type` varchar(100) DEFAULT NULL,
  `selected` tinyint(2) UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sources`
--

INSERT INTO `sources` (`id`, `source_name`, `source_type`, `selected`) VALUES
(1, 'facebook', 'social media', 1),
(2, 'reddit', 'social media', 1),
(3, 'twitter', 'social media', 1),
(4, 'linkedin', 'social media', 1),
(5, 'instagram', 'social media', 1),
(6, 'channel news asia', 'news', 1),
(8, 'straits times', 'news', 1),
(9, 'the guardian', 'news', 1),
(10, 'south china morning post', 'news', 1),
(11, 'the new york times', 'news', 1),
(12, 'mothership', 'news', 1),
(13, 'the online citizen', 'news', 1),
(14, 'today', 'news', 1),
(15, 'the independent singapore', 'news', 1),
(16, 'Newyork Health', 'news', 1),
(17, 'SCMPFeedHealthMedicine', 'news', 0),
(18, 'SCMPFeedHealthBeauty', 'news', 0);

-- --------------------------------------------------------

--
-- Table structure for table `topics`
--

CREATE TABLE `topics` (
  `id` int(11) UNSIGNED NOT NULL,
  `description` varchar(300) DEFAULT '',
  `exclude_keywords` varchar(300) DEFAULT NULL,
  `last_modified` datetime DEFAULT NULL,
  `status` tinyint(2) NOT NULL DEFAULT 0 COMMENT '1 represents true, 0 otherwise',
  `keywords` varchar(300) NOT NULL DEFAULT '',
  `page_id` int(11) NOT NULL DEFAULT 1,
  `topic_name` varchar(100) NOT NULL DEFAULT '',
  `processed_before` tinyint(2) UNSIGNED NOT NULL DEFAULT 0,
  `parent_topic_id` int(11) DEFAULT NULL,
  `keywords_for_crawling_parent_topic` varchar(300) DEFAULT NULL,
  `earliest_crawl_date_in_utc` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `topics`
--

INSERT INTO `topics` (`id`, `description`, `exclude_keywords`, `last_modified`, `status`, `keywords`, `page_id`, `topic_name`, `processed_before`, `parent_topic_id`, `keywords_for_crawling_parent_topic`, `earliest_crawl_date_in_utc`) VALUES
(406, 'This topic is a subset of COVID-19 (Worldwide), where data is based on Reddit API (r/singapore) and Twitter API (geocode = sg).', '', '2020-08-28 00:03:37', 1, '2019-nCoV,nCoV,coronavirus,Wuhan Virus,novel coronavirus,covid', 1, 'Covid-19 (Singapore)', 0, NULL, NULL, NULL),
(407, 'Test', '', '2020-08-28 00:03:37', 1, 'bus,mrt,public transport council,PTC,SBS transit', 1, 'test', 0, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rss_source_link`
--
ALTER TABLE `rss_source_link`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`),
  ADD KEY `rss_id_idx` (`rss_id`),
  ADD KEY `source_id_idx` (`source_id`);

--
-- Indexes for table `rss_table`
--
ALTER TABLE `rss_table`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`);

--
-- Indexes for table `sources`
--
ALTER TABLE `sources`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`);

--
-- Indexes for table `topics`
--
ALTER TABLE `topics`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rss_source_link`
--
ALTER TABLE `rss_source_link`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `rss_table`
--
ALTER TABLE `rss_table`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sources`
--
ALTER TABLE `sources`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `topics`
--
ALTER TABLE `topics`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=477;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `rss_source_link`
--
ALTER TABLE `rss_source_link`
  ADD CONSTRAINT `rss_id` FOREIGN KEY (`rss_id`) REFERENCES `rss_table` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `source_id` FOREIGN KEY (`source_id`) REFERENCES `sources` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
