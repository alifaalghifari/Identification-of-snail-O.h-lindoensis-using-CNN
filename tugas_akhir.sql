-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 25, 2024 at 04:10 AM
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
  `id_gambar` int(10) NOT NULL,
  `user` varchar(20) NOT NULL,
  `nama_gambar` varchar(50) NOT NULL,
  `nama_kelas` varchar(50) NOT NULL,
  `skor_akurasi` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_gambar`
--

INSERT INTO `tbl_gambar` (`id_gambar`, `user`, `nama_gambar`, `nama_kelas`, `skor_akurasi`) VALUES
(4, 'user', 'IMG20171107233323.jpg', 'Data 3 Thiara sp', 99.9976),
(5, 'user', 'IMG20230921112433.jpg', 'Sulawesidrobia', 82.0241),
(9, 'user', 'IMG20230921115904.jpg', 'O.H. lindoensis', 56.8135),
(14, 'admin', 'IMG20171107233315.jpg', 'Data 3 Thiara sp', 99.9802),
(15, 'user3', 'IMG20171107233337.jpg', 'Data 3 Thiara sp', 99.9929);

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
(1, 'Anca', 12, 7, 5, 0.34, '2023-09-30'),
(2, 'Tomado', 7, 6, 4, 0.29, '2023-09-30'),
(3, 'Wuasa', 23, 13, 11, 0.16, '2023-09-30'),
(56, 'Tomado', 15, 9, 4, 0.42, '2023-10-07'),
(57, 'Wuasa', 0, 12, 0, 0, '2023-10-07'),
(58, 'Tomado_1', 0, 10, 0, 0, '2023-10-07'),
(59, 'Wuasa_2', 0, 12, 0, 0, '2023-10-07'),
(60, 'Wuasa_2', 0, 12, 0, 0, '2023-10-07'),
(61, 'Wanga_3', 0, 12, 0, 0, '2023-10-09'),
(62, 'Wanga', 0, 5, 0, 0, '2024-03-25');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `id_user` int(11) NOT NULL,
  `nama` text NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `is_admin` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`id_user`, `nama`, `password`, `email`, `is_admin`) VALUES
(4, 'admin', 'sha256$JZ6kLht34mQp5hjo$26c941b1bdeda48984fb4d2daaf15802911569aa831bbc48fe9bf1c3e13c9e61', 'muh.alif.alghifari@gmail.com', 1),
(7, 'user', 'sha256$b9HjLSAAE3QEy3XN$01b5f06b9be69a493021dad7958fd608ce5a5bf0fa950c492bbdaacdd01ce166', 'user@gmail.com', 0),
(9, 'user2', 'sha256$YdmheFzyZHR7IetR$7e8667edd317250cbc31b1c0429b63b2d555b885d7d47e0e0fd40037e8f40ce7', 'user2@gmail.com', 0),
(10, 'user3', 'sha256$CHUzNjF8u0w58NaZ$323046713939e1379d2b225b86ccc2491b69af17489486709e8fde69137162b4', 'user3@gmail.com', 0);

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
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `unique_email` (`nama`) USING HASH;

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_gambar`
--
ALTER TABLE `tbl_gambar`
  MODIFY `id_gambar` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `tbl_kepadatan_keong`
--
ALTER TABLE `tbl_kepadatan_keong`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
