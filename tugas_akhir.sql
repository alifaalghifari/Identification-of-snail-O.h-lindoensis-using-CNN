-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2024 at 02:16 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugas_akhir`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbl_gambar`
--

CREATE TABLE `tbl_gambar` (
  `id_gambar` varchar(10) NOT NULL,
  `nama_gambar` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_kepadatan_keong`
--

CREATE TABLE `tbl_kepadatan_keong` (
  `id` int(10) NOT NULL,
  `desa` varchar(50) NOT NULL,
  `jml_keong` int(100) NOT NULL DEFAULT 0,
  `jml_orang` int(100) NOT NULL DEFAULT 0,
  `jml_titik` int(100) NOT NULL DEFAULT 0,
  `hasil` float NOT NULL DEFAULT 0,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_kepadatan_keong`
--

INSERT INTO `tbl_kepadatan_keong` (`id`, `desa`, `jml_keong`, `jml_orang`, `jml_titik`, `hasil`, `tanggal`) VALUES
(1, 'Anca', 10, 7, 5, 0.29, '2023-09-30'),
(2, 'Tomado', 7, 6, 4, 0.29, '2023-09-30'),
(3, 'Wuasa', 23, 13, 11, 0.16, '2023-09-30'),
(56, 'Tomado', 15, 10, 4, 0.38, '2023-10-07'),
(57, 'Wuasa', 0, 12, 0, 0, '2023-10-07'),
(58, 'Tomado_1', 0, 10, 0, 0, '2023-10-07'),
(59, 'Wuasa_2', 0, 12, 0, 0, '2023-10-07'),
(60, 'Wuasa_2', 0, 12, 0, 0, '2023-10-07'),
(61, 'Wanga_3', 0, 12, 0, 0, '2023-10-09');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `id_user` int(11) NOT NULL,
  `nama` text NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_gambar` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`id_user`, `nama`, `password`, `id_gambar`) VALUES
(1, 'Muh Alif Alghifari', 'sha256$K7RwbcoPsDZM2sft$9e80c4f2bb070ddf4e4b5968ece7adc9c62dc01933f15ec83ddda7f630e84bc0', 'Muh Alif A'),
(2, 'Kopi Kopte Tarik', 'sha256$feGuJMRSA6COHmYK$f92f540c53bc38a503894ef6d728d20b578ee9915f27380c93ee7fdc5c1a84a4', 'Kopi Kopte'),
(3, 'Muh Alif Alghifari', 'sha256$ZsqRAv5cUAKW9EJs$b12f5bb375f0bed870af4df6bcc0f897775dd7446f7ac243e4397fd6489234b2', 'Muh Alif A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbl_gambar`
--
ALTER TABLE `tbl_gambar`
  ADD PRIMARY KEY (`id_gambar`);

--
-- Indexes for table `tbl_kepadatan_keong`
--
ALTER TABLE `tbl_kepadatan_keong`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_kepadatan_keong`
--
ALTER TABLE `tbl_kepadatan_keong`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
