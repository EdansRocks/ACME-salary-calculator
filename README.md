<h1 align="center">  ACME Salary Calculator </h1>

![python-badge](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

## Table of Contents
- [Exercise Description](#exercise-description)
- [Solution](#solution)
- [Architecture](#architecture)
- [Aproach and Methodology](#aproach-and-methodology)
	- [Analysis](#analysis)
	- [Design](#design)
	- [Development](#development)
	- [Testing](#testing)
- [How to Run](#how-to-run)
	- [Requirements](#requirements)
	- [Download and Run](#download-and-run)
- [Comment](#comment)

## Exercise Description
The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:
```
Monday - Friday					        Saturday and Sunday
00:01 - 09:00 -> 25 USD					00:01 - 09:00 -> 30 USD
09:01 - 18:00 -> 15 USD					09:01 - 18:00 -> 20 USD
18:01 - 00:00 -> 20 USD					18:01 - 00:00 -> 25 USD
```

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

```
MO: Monday					      FR: Friday
TU: Tuesday					      SA: Saturday
WE: Wednesday					      SU: Sunday
TH: Thursday
```

## Solution
In order to solve the problem it was decided to implement a software that allows to use a .txt file with the information of the employees and the days they have worked, which will automatically calculate the salary to be paid for each of the employees.

The following technologies were used to solve this problem:
- [Python](https://www.python.org) as a programming language.
- [Command](https://en.wikipedia.org/wiki/Command_pattern) design pattern.
- [Unittest](https://docs.python.org/3/library/unittest.html) for testing.
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) Style guide.

## Architecture
The software architecture is defined according to the following diagram:

![Architecture](https://github.com/EdansRocks/ACME-salary-calculator/blob/main/public/Images/Architecture.png?raw=true)

The diagram shows the communication between the different components of the software, taking into consideration the command design pattern in which different actors are involved such as the receiver, the invoker, the existing commands and the client.

## Aproach and Methodology
A series of activities were followed for the development as detailed below:

### Analysis
The features that the software should meet were analyzed and the elements involved in the description of the exercise to define a set of technologies such as the programming language to be used, as well as its framework for testing, programming style and design patterns.

### Design
After the analysis, the architecture that would support the software was designed taking into consideration the command design pattern and the elements involved in the solution. Also, different factors such as simplicity or scalability of the software were taken into consideration.

### Development
Once the architecture and programming language were defined, the software development stage began in an organized manner, developing each of the components respecting the established coding style and coding standards.

### Testing
Finally, a set of tests was established to verify the correct functioning of all the developed code using the Unittest library..

## How to Run
In order to run the software you need the following:

### Requirements
- [Python](https://www.python.org/downloads/) `>= v3.1.x`

### Download and Run
Clone the project:
```
git clone https://github.com/EdansRocks/ACME-salary-calculator.git
cd ACME-salary-calculator
```
To run the project:
```
python3 main.py
```
To run tests:
```
python3 tests.py
```
Example:

![Example](https://github.com/EdansRocks/ACME-salary-calculator/blob/main/public/Images/Example.png?raw=true)

### Comment
This exercise was a good practice to improve my skills with the Python programming language, and also to improve my ability to find solutions to problems in an organized way from software analysis, architecture design, software development and finally testing, all this using design patterns, style guides and good programming practices.

Remember to drink water! :)

