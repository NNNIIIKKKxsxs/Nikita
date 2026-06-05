Library Management System
Functional Requirements
| ID | Requirement |
|----|------------|
| FR-01 | User can view books |
| FR-02 | User can search books |
| FR-03 | User can view book details |
| FR-04 | User can borrow books |
| FR-05 | Admin can add books |
| FR-06 | Admin can edit books |
| FR-07 | Admin can delete books |

Use Case Diagram

+----------------------+
          |      Бібліотека      |
          +----------------------+

Користувач
   |
   +---- Переглянути книги
   |
   +---- Шукати книгу
   |
   +---- Переглянути інформацію
   |
   +---- Взяти книгу

Адміністратор
   |
   +---- Додати книгу
   |
   +---- Редагувати книгу
   |
   +---- Видалити книгу

Class Diagram
User
----------------
id : int
name : string
+ SearchBook()
+ BorrowBook()

Admin : User
----------------
+ AddBook()
+ EditBook()
+ DeleteBook()

Book
----------------
id : int
title : string
author : string
available : bool

Library
----------------
books : List<Book>
+ FindBook()
+ AddBook()

Loan
----------------
loanId : int
date : Date
+ CreateLoan()
Admin ----|> User
Library o---- Book
User ----- Loan
Loan ----- Book

Sequence Diagram
Користувач -> Система : Запит книги
Система -> Бібліотека : Перевірити наявність
Бібліотека -> Книга : Отримати статус
Книга -> Бібліотека : Доступна
Бібліотека -> Система : Підтвердження
Система -> Користувач : Книгу видано

Матриця трасовності

| Вимога | Прецедент              | Класи            |
| ------ | ---------------------- | ---------------- |
| FR-01  | Переглянути книги      | Book, Library    |
| FR-02  | Шукати книгу           | Book, Library    |
| FR-03  | Переглянути інформацію | Book             |
| FR-04  | Взяти книгу            | User, Loan, Book |
| FR-05  | Додати книгу           | Admin, Book      |
| FR-06  | Редагувати книгу       | Admin, Book      |
| FR-07  | Видалити книгу         | Admin, Book      |
