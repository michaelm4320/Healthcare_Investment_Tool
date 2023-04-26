CREATE TABLE `Credentials` (
  `email` varchar(45) NOT NULL,
  `password` varchar(103) NOT NULL,
  `title` varchar(45) NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `usertype` varchar(45) NOT NULL,
  `organization name` varchar(45) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Patient` (
  `Id` varchar(45) NOT NULL,
  `BirthDate` varchar(45) NOT NULL,
  `FirstName` varchar(45) NOT NULL,
  `LastName` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Race` varchar(45) NOT NULL,
  `Age` varchar(3) NOT NULL,
  `Insurance` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
