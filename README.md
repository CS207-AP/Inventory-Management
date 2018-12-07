# Pharmacy Management Software

## GitHub Repository
* https://github.com/CS207-AP/Inventory-Management

## Table of Contents

* [Aim](#aim)
* [Our Approach to the Solution](#our-approach-to-the-solution)
* [Technology Utilised](#technology-utilised)
* [Issues Faced](#issues-faced)
* [Scope of improvement](#scope-of-improvement)
* [Contributors](#contributors)
* [License](#license)

## Aim 
To create an inventory management software that deals with the day-to-day workings of a pharmacy store, thereby improving its efficiency and productivity. 

## Our Approach to the Solution
Once the aim was established, we ideated to develop a program by which a pharmacy can deal with the following tasks:
* Customer Database Management
* Supplier Database Management
* Inventory Database Management
* Invoicing (To manage bill generation.)
* Reports (To maintain the record of medicines sold and bought on a daily/monthly/yearly basis.)

We worked upon a basic structure of what we wanted to achieve, and we started working on it in C language. However, once we were almost halfway done, we realised that managing multiple databses in the said language was neither easy, nor efficient. Additionally, working on a GUI in C was challenging as most of its GUI libraries like 'graphics.h' were outdated and out of active support. 

Due to the continued problems that the C language posed us with, we decided to move our whole code to the Python language - a language that none of us group members were earlier familiar with - by learning it from scratch. We decided on this switch given Python's extensive support of libraries, efficient database management, and active support availability. 

We read the python documentation, and began our work. We used '.csv' files to maintain our databse records, which helped us manage our data in a relatively efficient manner as compared to the '.txt' files that we had been using in the C langauge.

## Technology Utilised 
* Python - https://docs.python.org/3/
* CSV files for Database Management - https://docs.python.org/3/library/csv.html
* Git & GitHub for Version Control- https://www.github.com

## Issues Faced

* Lack of modern libraries and complexity of C langauge for database management made us transistion to a programming language that we had never worked upon before.
* Implementation of a GUI was challenging as the C language's 'graphics.h' and 'windows.h' libraries were very outdated and most other libraries lacked enough documentation for beginners to understand.
* Switching to Python, an entirely new language, posed a set of different problems.
* While selecting a database, we tried the following:
    * .txt files 
    * MySql & MongoDB 
    * .csv files 
* After writing our code for all the features of our program, we went on to make the GUI. While researching about the same we came across the following modules to make the GUI, and we worked with all of them -
    * Tkinter
    * EasyGUI
    * PyQT5 
* One might say that we got a little too ambitious as we weren't aware about the challenges learning a completely new programming language would pose. After spending 2 days working with above mentioned modules to implement and make the GUI work, we had to leave it incomplete given our limited time.

## Scope of improvement
* GUI
* A more efficient database management 
* Login Page

## Contributors

### Shivam Sharda
* Github
* Customer Menu & Functions:
   * Add Customer
   * Update Customer
   * Search Customer
* Debugging 
* Report
* Designing 
* GUI attempt
### Vir Jhangiani
* Github
* Medicine Menu & Functions:
   * Add Medicine
   * Search Medicine
   * Update Medicine
   * Medicine to be purchased
* Invoicing Menu & Functions:
   * Supplier Invoice
   * Customer Invoice
* Designing
* Debugging
* Compilation
### Harpreet Virk
* Github
* Supplier Menu & Functions: 
   * Add Supplier
   * Update Supplier
   * Search Supplier
* Report Menu & Functions:
   * Day Sale
   * Month Sale
   * Day Purchase
   * Month Purchase
   * Profit Report
* Designing
* GUI attempt
* Report 
* Compilation
* Debugging 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
