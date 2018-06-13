-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-06-2018 a las 18:39:32
-- Versión del servidor: 10.1.31-MariaDB
-- Versión de PHP: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `examenredes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tweet`
--

CREATE TABLE `tweet` (
  `id` varchar(196) NOT NULL,
  `text` text NOT NULL,
  `user` varchar(196) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tweet`
--

INSERT INTO `tweet` (`id`, `text`, `user`, `date`) VALUES
('1006796816132734978', 'De nuevo #intentadoSalvarElSemestreConRojo', 'JaneRojasR', '0000-00-00'),
('1006813418471460864', 'RT @JaneRojasR: Y aquí sigo #intentadoSalvarElSemestreConRojo', 'leiver_jimenez', '0000-00-00'),
('1006814940919975936', '12 horas después seguimos #intentadoSalvarElSemestreConRojo', 'JaneRojasR', '0000-00-00'),
('1006818947856064515', 'Y eso que estaba estimado para 9 horas ????\n#intentadoSalvarElSemestreConRojo https://t.co/tBEUSp2V0F', 'leiver_jimenez', '0000-00-00'),
('1006872145627172867', '@JaneRojasR #intentadoSalvarElSemestreConRojo Muy bien parece que funciona ahora queda ver los correos', 'rgonzalez_tec', '0000-00-00'),
('1006872321347420160', '@MauroLopezJ #intentadoSalvarElSemestreConRojo Bueno hora dedesayunear para terminar el Semestre', 'rgonzalez_tec', '0000-00-00'),
('1006872622615924736', '@ale_npz @MauroLopezJ #intentadoSalvarElSemestreConRojo El modo Chill para estudiantes del TEC es luego de entrega… https://t.co/T3P9eJmlGq', 'rgonzalez_tec', '0000-00-00'),
('1006872913226723328', '@valeviquez @MiguelMendezRo1 @leiver_jimenez #intentadoSalvarElSemestreConRojo Solo es la última cuesta para la rec… https://t.co/Ewnz1SMTBI', 'rgonzalez_tec', '0000-00-00'),
('1006873330027302912', '@leiver_jimenez @JaneRojasR #intentadoSalvarElSemestreConRojo Esta fácil no se enreden ustedes saben analizar y abs… https://t.co/CvRNhKRMw2', 'rgonzalez_tec', '0000-00-00'),
('1006873624354189312', '@Adrian_H_S6 #intentadoSalvarElSemestreConRojo Todavía nadie a muerto y ahora son mejores desarrolladores de software. Si se puede', 'rgonzalez_tec', '0000-00-00'),
('1006883259765149696', '@MauroLopezJ #intentadoSalvarElSemestreConRojo Suele pasar al final del Semestre', 'rgonzalez_tec', '0000-00-00'),
('1006885468519256064', '@rgonzalez_tec @MauroLopezJ Y debido a eso, por la excelente disciplina y conducta de @MauroLopezJ ya no está… https://t.co/t9F8lsKk91', 'ale_npz', '0000-00-00'),
('1006891563081916416', '@Freddy13180577 #intentadoSalvarElSemestreConRojo Así es Freddy es una tradición despedir a los estudiantes que van… https://t.co/FepKCwEMdC', 'rgonzalez_tec', '0000-00-00'),
('1006898777624436736', '#intentadoSalvarElSemestreConRojo', 'FelipeMartnezB1', '0000-00-00'),
('1006900594940960768', '@rgonzalez_tec El problema es que mi persona no va para practica Jajajaja.\n#intentadoSalvarElSemestreConRojo', 'Freddy13180577', '0000-00-00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tweet`
--
ALTER TABLE `tweet`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
