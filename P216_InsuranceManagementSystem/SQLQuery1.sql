
create database InsuranceManagement

use InsuranceManagement

CREATE DATABASE InsuranceManagementDB;
USE InsuranceManagementDB;

-- Create Users table
CREATE TABLE Users (
    userId INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) NOT NULL,
    password NVARCHAR(50) NOT NULL,
    role NVARCHAR(50) NOT NULL
);

-- Create Clients table
CREATE TABLE Clients (
    clientId INT PRIMARY KEY IDENTITY(1,1),
    clientName NVARCHAR(100) NOT NULL,
    contactInfo NVARCHAR(100) NOT NULL,
    policy NVARCHAR(100) NOT NULL
);

-- Create Policies table
CREATE TABLE Policies (
    policyId INT PRIMARY KEY IDENTITY(1,1),
    policyName NVARCHAR(100) NOT NULL,
    policyDescription NVARCHAR(255) NOT NULL
);

-- Create Claims table
CREATE TABLE Claims (
    claimId INT PRIMARY KEY IDENTITY(1,1),
    claimNumber NVARCHAR(100) NOT NULL,
    dateFiled DATE NOT NULL,
    claimAmount DECIMAL(10, 2) NOT NULL,
    status NVARCHAR(50) NOT NULL,
    clientId INT,
    policy NVARCHAR(100),
    FOREIGN KEY (clientId) REFERENCES Clients(clientId)
);

-- Create Payments table
CREATE TABLE Payments (
    paymentId INT PRIMARY KEY IDENTITY(1,1),
    paymentDate DATE NOT NULL,
    paymentAmount DECIMAL(10, 2) NOT NULL,
    clientId INT,
    FOREIGN KEY (clientId) REFERENCES Clients(clientId)
);

-- Insert sample policies into Policies
INSERT INTO Policies (policyName, policyDescription)
VALUES ('Health Insurance', 'Covers medical expenses including hospital stays and treatments'),
       ('Life Insurance', 'Provides financial security to your family in case of your death'),
       ('Auto Insurance', 'Covers damages to your car and third-party liability'),
       ('Home Insurance', 'Covers damages to your home and belongings');

SELECT * FROM Clients;
SELECT * FROM Users;
SELECT * FROM Claims;
SELECT * FROM Payments;
SELECT * FROM Policies;