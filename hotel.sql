-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 13, 2024 at 04:50 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `guest`
--

CREATE TABLE `guest` (
  `guest_id` varchar(11) NOT NULL,
  `guest_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `guest_lastname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `guest_nationality` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--
-- Dumping data for table `guest`
--

INSERT INTO `guest` (`guest_id`, `guest_name`, `guest_lastname`, `guest_nationality`) VALUES
('[4569871236', '[sara]', '[mohammadi]', '[arab]'),
('12365478963', 'mohsen', 'rezaee', 'irani'),
('78965412314', 'mohsen', 'hosseini', 'irani');

-- --------------------------------------------------------

--
-- Table structure for table `guest_contactinfo`
--

CREATE TABLE `guest_contactinfo` (
  `guest_id` varchar(11) NOT NULL,
  `guest_phonenumber` varchar(11) NOT NULL,
  `guest_email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--

--
-- Table structure for table `offiice_personnel`
--

CREATE TABLE `offiice_personnel` (
  `personnel_id` varchar(11) NOT NULL,
  `reg_date` date NOT NULL,
  `reg_time` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--

--
-- Table structure for table `personnel`
--

CREATE TABLE `personnel` (
  `personnel_id` varchar(11) NOT NULL,
  `personnel_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `persnnel_lastname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `personnel_salary` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `personnel_workhour` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--

--
-- Table structure for table `personnel_contactinfo`
--

CREATE TABLE `personnel_contactinfo` (
  `personnel_id` varchar(11) NOT NULL,
  `personnel_phone` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--

--
-- Table structure for table `reservation`
--

CREATE TABLE `reservation` (
  `reservation_id` varchar(10) NOT NULL,
  `reservation_startday` varchar(10) NOT NULL,
  `reservation_endday` varchar(10) NOT NULL,
  `reservation_price` varchar(10) NOT NULL,
  `guest_id` varchar(11) NOT NULL,
  `personnel_id` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--
-- Triggers `reservation`
--
DELIMITER $$
CREATE TRIGGER `update_roomstatus_on_reservation_delete` AFTER DELETE ON `reservation` FOR EACH ROW BEGIN
    UPDATE room
    SET room_status = 'empty'
    WHERE reservation_id = OLD.reservation_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `room_id` varchar(10) NOT NULL,
  `room_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `room_status` varchar(10) NOT NULL,
  `personnel_id` varchar(11) DEFAULT NULL,
  `reservation_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`room_id`, `room_type`, `room_status`, `personnel_id`, `reservation_id`) VALUES
('4', 'single room', 'empty', NULL, NULL),
('5', 'double room', 'reserved', '74815926378', NULL),
('6', 'twin room', 'empty', '32615948732', NULL),
('7', 'double room', 'empty', '32615948732', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `service_personnel`
--

CREATE TABLE `service_personnel` (
  `personnel_id` varchar(11) NOT NULL,
  `service` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `service_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_persian_ci;

--

--
-- Indexes for table `guest`
--
ALTER TABLE `guest`
  ADD PRIMARY KEY (`guest_id`);

--
-- Indexes for table `guest_contactinfo`
--
ALTER TABLE `guest_contactinfo`
  ADD PRIMARY KEY (`guest_id`,`guest_phonenumber`,`guest_email`),
  ADD UNIQUE KEY `guest_phonenumber` (`guest_phonenumber`,`guest_email`);

--
-- Indexes for table `offiice_personnel`
--
ALTER TABLE `offiice_personnel`
  ADD PRIMARY KEY (`personnel_id`,`reg_date`,`reg_time`);

--
-- Indexes for table `personnel`
--
ALTER TABLE `personnel`
  ADD PRIMARY KEY (`personnel_id`);

--
-- Indexes for table `personnel_contactinfo`
--
ALTER TABLE `personnel_contactinfo`
  ADD PRIMARY KEY (`personnel_id`),
  ADD UNIQUE KEY `personnel_phone` (`personnel_phone`);

--
-- Indexes for table `reservation`
--
ALTER TABLE `reservation`
  ADD PRIMARY KEY (`reservation_id`),
  ADD KEY `fk_reserve_guest_id` (`guest_id`),
  ADD KEY `fk_reseve_personnel_id` (`personnel_id`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`room_id`),
  ADD KEY `fk_room_personnelid` (`personnel_id`),
  ADD KEY `fk_reserveid` (`reservation_id`);

--
-- Indexes for table `service_personnel`
--
ALTER TABLE `service_personnel`
  ADD PRIMARY KEY (`personnel_id`,`service`,`service_date`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `guest_contactinfo`
--
ALTER TABLE `guest_contactinfo`
  ADD CONSTRAINT `fk_guests` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`guest_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `offiice_personnel`
--
ALTER TABLE `offiice_personnel`
  ADD CONSTRAINT `fk_office_personnel` FOREIGN KEY (`personnel_id`) REFERENCES `personnel` (`personnel_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `personnel_contactinfo`
--
ALTER TABLE `personnel_contactinfo`
  ADD CONSTRAINT `fk_personnel` FOREIGN KEY (`personnel_id`) REFERENCES `personnel` (`personnel_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `fk_reserve_guest_id` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`guest_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_reseve_personnel_id` FOREIGN KEY (`personnel_id`) REFERENCES `personnel` (`personnel_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `fk_reserveid` FOREIGN KEY (`reservation_id`) REFERENCES `reservation` (`reservation_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_room_personnelid` FOREIGN KEY (`personnel_id`) REFERENCES `personnel` (`personnel_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `service_personnel`
--
ALTER TABLE `service_personnel`
  ADD CONSTRAINT `fk_service_personnel` FOREIGN KEY (`personnel_id`) REFERENCES `personnel` (`personnel_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
