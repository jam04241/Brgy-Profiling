-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 08, 2024 at 12:53 PM
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
-- Database: `db_brgyprofilling`
--

-- --------------------------------------------------------

--
-- Table structure for table `pendingcase`
--

CREATE TABLE `pendingcase` (
  `case_no` int(11) NOT NULL,
  `admin_id` int(11) NOT NULL,
  `brgy_id` int(11) NOT NULL,
  `incident` varchar(50) NOT NULL,
  `loc_incident` varchar(50) NOT NULL,
  `date_incident` date NOT NULL,
  `date_reported` date NOT NULL,
  `person_incharge` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `residents`
--

CREATE TABLE `residents` (
  `brgy_id` int(11) NOT NULL,
  `admin_id` int(50) NOT NULL,
  `Fname` varchar(50) DEFAULT NULL,
  `Lname` varchar(50) NOT NULL,
  `mid_ini` char(1) NOT NULL,
  `Age` int(3) NOT NULL,
  `sex` set('Male','Female') NOT NULL,
  `PWD` set('yes','no') NOT NULL,
  `birthplace` varchar(50) NOT NULL,
  `Birth_date` date NOT NULL,
  `blood_type` varchar(3) NOT NULL,
  `Civil_status` set('Single','Married','Divorced','Separated','Windowed') NOT NULL,
  `contact_no` int(14) NOT NULL,
  `email` varchar(50) NOT NULL,
  `isactive` set('yes','no') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_adminlogin`
--

CREATE TABLE `tbl_adminlogin` (
  `admin_id` int(11) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `username` varchar(12) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_adminlogin`
--

INSERT INTO `tbl_adminlogin` (`admin_id`, `fullname`, `username`, `password`) VALUES
(544056, 'Vincent Pautog', 'admin1', 'password1'),
(544057, 'Kerby Navallo', 'tite', 'asshole'),
(544058, 'Benz Carl Vale', 'walangkwenta', 'putapepe'),
(544059, 'Python Connected', 'Jam04241', 'wowex1234'),
(544060, 'Rameses Bernabe', 'Rampinakagwa', '123456789'),
(544061, 'rameses bernabe', 'rams123', 'ramsbernabe19'),
(544062, 'John Carl', 'Hayssst123', 'joshgwapo'),
(544063, 'sample', 'admin89', 'wewz1234'),
(544064, 'Jorge Maccabenta', 'Jorge123', '123456789'),
(544065, 'qwe', 'qwe', '123456789'),
(544066, 'gggg', 'wewe', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_officials`
--

CREATE TABLE `tbl_officials` (
  `official_id` int(11) NOT NULL,
  `admin_id` int(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `mid_ini` char(1) NOT NULL,
  `age` int(3) NOT NULL,
  `sex` set('Male','Female') NOT NULL,
  `date_of_birth` date NOT NULL DEFAULT '1970-01-01',
  `Position` set('Captain','Secretary','Treasurer','Councelor','Kagawad','SK Kagawad','Tanod') NOT NULL,
  `status` set('Married','Single','widow') NOT NULL,
  `term_start` varchar(50) NOT NULL,
  `term_end` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `isactive` set('yes','no') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_officials`
--

INSERT INTO `tbl_officials` (`official_id`, `admin_id`, `fname`, `lname`, `mid_ini`, `age`, `sex`, `date_of_birth`, `Position`, `status`, `term_start`, `term_end`, `email`, `isactive`) VALUES
(1, 0, 'asdasd', 'dasdas', '', 23, 'Male', '1970-01-01', 'Captain', 'Married', '2002-01-01', '2002-01-01', '', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pendingcase`
--
ALTER TABLE `pendingcase`
  ADD PRIMARY KEY (`case_no`);

--
-- Indexes for table `residents`
--
ALTER TABLE `residents`
  ADD PRIMARY KEY (`brgy_id`);

--
-- Indexes for table `tbl_adminlogin`
--
ALTER TABLE `tbl_adminlogin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `tbl_officials`
--
ALTER TABLE `tbl_officials`
  ADD PRIMARY KEY (`official_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pendingcase`
--
ALTER TABLE `pendingcase`
  MODIFY `case_no` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `residents`
--
ALTER TABLE `residents`
  MODIFY `brgy_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_adminlogin`
--
ALTER TABLE `tbl_adminlogin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=544067;

--
-- AUTO_INCREMENT for table `tbl_officials`
--
ALTER TABLE `tbl_officials`
  MODIFY `official_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
