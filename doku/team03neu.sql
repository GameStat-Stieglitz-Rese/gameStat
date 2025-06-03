-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 03. Jun 2025 um 23:01
-- Server-Version: 10.4.32-MariaDB
-- PHP-Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `team03`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `benutzer`
--

CREATE TABLE `benutzer` (
  `ID` int(11) NOT NULL,
  `Vorname` varchar(255) DEFAULT NULL,
  `Benutzername` varchar(255) DEFAULT NULL,
  `Passwort` varchar(255) DEFAULT NULL,
  `E_Mail` varchar(255) DEFAULT NULL,
  `Geschlecht_ID` int(11) DEFAULT NULL,
  `Land_ID` int(11) DEFAULT NULL,
  `Sprache` int(11) DEFAULT NULL,
  `Geburtsdatum` date DEFAULT NULL,
  `Bildnummer` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `benutzer`
--

INSERT INTO `benutzer` (`ID`, `Vorname`, `Benutzername`, `Passwort`, `E_Mail`, `Geschlecht_ID`, `Land_ID`, `Sprache`, `Geburtsdatum`, `Bildnummer`) VALUES
(4, 'Marc', 'marcstieglitz', '25687893d97c0bf572cf9ac0fe37df99c5558b38fe672c8d4bef7352a1eb6215', 'marc.stieglitz@rdf.nuernberg.de', 1, 1, 1, '2000-12-25', 1),
(5, 'Max', 'max', '1d137c711daf45aa5ee1300108f836844b13f73efd48c746dbfed9f23b3bffb4', 'maxi@maxman.de', 1, 4, 3, '2000-12-25', 1),
(6, 'Max', 'mustermann', '49245585662d83f4731d95a9c243c2fd29000246fd999c1a8c7df11f03cb528c', 'maxmuster@onlinemail.de', 1, 1, 1, '1995-12-12', 1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `geschlecht`
--

CREATE TABLE `geschlecht` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `geschlecht`
--

INSERT INTO `geschlecht` (`ID`, `Name`) VALUES
(1, 'Männlich'),
(2, 'Weiblich');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `herausgeber`
--

CREATE TABLE `herausgeber` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `herausgeber`
--

INSERT INTO `herausgeber` (`ID`, `Name`) VALUES
(1, 'Rockstar Games'),
(2, 'EA Games'),
(3, 'Ubisoft'),
(4, 'Valve Games'),
(5, 'Microsoft'),
(6, 'Sony'),
(7, 'Activison Blizzard'),
(8, 'Epic Games'),
(9, 'CD Projekt'),
(10, 'SEGA'),
(11, 'BANDAI Namco'),
(12, 'Sonstiges');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `land`
--

CREATE TABLE `land` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `land`
--

INSERT INTO `land` (`ID`, `Name`) VALUES
(1, 'Deutschland'),
(2, 'England'),
(3, 'USA'),
(4, 'Russland'),
(5, 'Frankreich'),
(6, 'Spanien'),
(7, 'Polen'),
(8, 'Niederlande');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `platform`
--

CREATE TABLE `platform` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `platform`
--

INSERT INTO `platform` (`ID`, `Name`) VALUES
(1, 'Playstation 3'),
(2, 'Xbox 360'),
(3, 'PC'),
(4, 'Playstation 4'),
(5, 'Playstation 5'),
(6, 'Xbox One'),
(7, 'Xbox Serie S'),
(8, 'Xbox Serie X');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `spieldaten`
--

CREATE TABLE `spieldaten` (
  `ID` int(11) NOT NULL,
  `Spiel_ID` int(11) NOT NULL,
  `Benutzer_ID` int(11) NOT NULL,
  `Platform_ID` int(11) NOT NULL,
  `Level` int(11) DEFAULT NULL,
  `Spielzeit` int(11) DEFAULT NULL,
  `Eigenbewertung` int(11) DEFAULT NULL,
  `Startdatum` date DEFAULT NULL,
  `Durchgespielt` int(11) DEFAULT NULL,
  `Empfohlen` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `spieldaten`
--

INSERT INTO `spieldaten` (`ID`, `Spiel_ID`, `Benutzer_ID`, `Platform_ID`, `Level`, `Spielzeit`, `Eigenbewertung`, `Startdatum`, `Durchgespielt`, `Empfohlen`) VALUES
(1, 4, 4, 3, 12, 14, 1, '2025-11-11', 3, 3),
(2, 4, 4, 2, 199, 199, 10, '2222-12-22', 1, 1),
(3, 4, 5, 2, 12, 12, 1, NULL, 2, 3),
(4, 7, 4, 3, 23, 1000, 8, '2020-02-24', 2, 2),
(5, 8, 4, 3, 123, 1000, 9, NULL, 1, 1),
(6, 15, 6, 3, NULL, 50, 10, '2025-01-02', 2, 1),
(7, 7, 6, 6, 50, 520, 7, '2020-11-11', 2, 2),
(8, 9, 6, 3, NULL, 500, 10, NULL, 2, 1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `spiele`
--

CREATE TABLE `spiele` (
  `ID` int(11) NOT NULL,
  `Spielname` varchar(255) DEFAULT NULL,
  `Herausgeber_ID` int(11) DEFAULT NULL,
  `Kategorie_ID` int(11) DEFAULT NULL,
  `max_Level` int(11) DEFAULT NULL,
  `Onlinefunktion` tinyint(1) NOT NULL,
  `Erscheinungsjahr` year(4) DEFAULT NULL,
  `Altersfreigabe` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `spiele`
--

INSERT INTO `spiele` (`ID`, `Spielname`, `Herausgeber_ID`, `Kategorie_ID`, `max_Level`, `Onlinefunktion`, `Erscheinungsjahr`, `Altersfreigabe`) VALUES
(1, 'Counter Strike 2', 4, 10, NULL, 0, '2023', 18),
(2, 'Call of Duty: Black Ops 6', 7, 10, NULL, 0, '2024', 18),
(3, 'Need for Speed: Heat', 2, 6, NULL, 0, '2019', 6),
(4, 'GTA IV', 1, 9, NULL, 0, '2008', 18),
(5, 'Red Dead Redemption 2', 1, 9, NULL, 0, '2018', 18),
(6, 'Bully', 1, 9, NULL, 1, '2006', 18),
(7, 'GTA V', 1, 9, NULL, 0, '2013', 18),
(8, 'Cyberpunk 2077', 2, 9, NULL, 0, '2020', 18),
(9, 'Gran Turismo 7', 6, 6, NULL, 0, '2022', 6),
(10, 'Gran Turismo Sport', 6, 6, NULL, 0, '2017', 6),
(11, 'Gran Turismo 6', 6, 6, NULL, 0, '2013', 6),
(12, 'Forza Horizon 5', 5, 6, NULL, 0, '2021', 6),
(13, 'TETRIS', 12, 8, NULL, 1, '1984', 0),
(14, 'Portal 2', 4, 8, NULL, 0, '2011', 12),
(15, 'Minecraft', 12, 9, NULL, 0, '2009', 6);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `spielkategorie`
--

CREATE TABLE `spielkategorie` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `spielkategorie`
--

INSERT INTO `spielkategorie` (`ID`, `Name`) VALUES
(1, 'Action'),
(2, 'Adventure'),
(3, 'Rollenspiel (RPG)'),
(4, 'Strategie'),
(5, 'Simulation'),
(6, 'Rennspiel'),
(7, 'Sport'),
(8, 'Denkspiel'),
(9, 'Open-World'),
(10, 'Shooter');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `sprache`
--

CREATE TABLE `sprache` (
  `ID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Daten für Tabelle `sprache`
--

INSERT INTO `sprache` (`ID`, `Name`) VALUES
(1, 'deutsch'),
(2, 'englisch'),
(3, 'russisch'),
(4, 'französisch'),
(5, 'spanisch'),
(6, 'polnisch'),
(7, 'niederländisch');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `benutzer`
--
ALTER TABLE `benutzer`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Geschlecht_ID` (`Geschlecht_ID`),
  ADD KEY `Land_ID` (`Land_ID`),
  ADD KEY `Sprache` (`Sprache`);

--
-- Indizes für die Tabelle `geschlecht`
--
ALTER TABLE `geschlecht`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `herausgeber`
--
ALTER TABLE `herausgeber`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `land`
--
ALTER TABLE `land`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `platform`
--
ALTER TABLE `platform`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `spieldaten`
--
ALTER TABLE `spieldaten`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Spiel_ID` (`Spiel_ID`,`Benutzer_ID`,`Platform_ID`) USING BTREE,
  ADD KEY `Benutzer_ID` (`Benutzer_ID`),
  ADD KEY `Platform_ID` (`Platform_ID`);

--
-- Indizes für die Tabelle `spiele`
--
ALTER TABLE `spiele`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Herausgeber_ID` (`Herausgeber_ID`),
  ADD KEY `Kategorie_ID` (`Kategorie_ID`);

--
-- Indizes für die Tabelle `spielkategorie`
--
ALTER TABLE `spielkategorie`
  ADD PRIMARY KEY (`ID`);

--
-- Indizes für die Tabelle `sprache`
--
ALTER TABLE `sprache`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `benutzer`
--
ALTER TABLE `benutzer`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT für Tabelle `geschlecht`
--
ALTER TABLE `geschlecht`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT für Tabelle `herausgeber`
--
ALTER TABLE `herausgeber`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT für Tabelle `land`
--
ALTER TABLE `land`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT für Tabelle `platform`
--
ALTER TABLE `platform`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT für Tabelle `spieldaten`
--
ALTER TABLE `spieldaten`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT für Tabelle `spiele`
--
ALTER TABLE `spiele`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT für Tabelle `spielkategorie`
--
ALTER TABLE `spielkategorie`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT für Tabelle `sprache`
--
ALTER TABLE `sprache`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `benutzer`
--
ALTER TABLE `benutzer`
  ADD CONSTRAINT `benutzer_ibfk_1` FOREIGN KEY (`Geschlecht_ID`) REFERENCES `geschlecht` (`ID`),
  ADD CONSTRAINT `benutzer_ibfk_2` FOREIGN KEY (`Land_ID`) REFERENCES `land` (`ID`),
  ADD CONSTRAINT `benutzer_ibfk_3` FOREIGN KEY (`Sprache`) REFERENCES `sprache` (`ID`);

--
-- Constraints der Tabelle `spieldaten`
--
ALTER TABLE `spieldaten`
  ADD CONSTRAINT `spieldaten_ibfk_1` FOREIGN KEY (`Spiel_ID`) REFERENCES `spiele` (`ID`),
  ADD CONSTRAINT `spieldaten_ibfk_2` FOREIGN KEY (`Benutzer_ID`) REFERENCES `benutzer` (`ID`),
  ADD CONSTRAINT `spieldaten_ibfk_3` FOREIGN KEY (`Platform_ID`) REFERENCES `platform` (`ID`);

--
-- Constraints der Tabelle `spiele`
--
ALTER TABLE `spiele`
  ADD CONSTRAINT `spiele_ibfk_1` FOREIGN KEY (`Herausgeber_ID`) REFERENCES `herausgeber` (`ID`),
  ADD CONSTRAINT `spiele_ibfk_2` FOREIGN KEY (`Kategorie_ID`) REFERENCES `spielkategorie` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
