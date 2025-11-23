# Cse-Project-Vityarthi
A simple Python-based shopping cart system with item management, bulk removal, frequency table billing, and automatic receipt generation.

# 🛒 Shopping Cart System (Python)

A simple command-line based shopping cart and billing system written in Python.
It allows users to:

* Added up to 30 items into a store dictionary
* Add items to the cart
* Remove multiple items at once
* View a frequency table of purchased items
* Auto-generate an Order ID
* Estimate delivery date
* Save a receipt file
* Fully interactive checkout system

## 📌 Features

### ✅ Add Store Items

* The program lets you input 30 items with prices.
* All items stored in a Python dictionary.

### ✅ Add Items to Cart

* User can add any available store item.
* Cart supports duplicate entries.

### ✅ Remove Items in Bulk

* User inputs how many items to remove at once.
* Removes them cleanly from the cart.

### ✅ Auto Frequency Count

At checkout, you get a clean table:

Item        | Quantity | Price per unit | Subtotal
--------------------------------------------------
Jam         |    10    |      75        |   750
Pen         |    50    |      10        |   500
Pencil      |    10    |       5        |    50


### ✅ Order Summary

Includes:

* Username
* Order ID
* Delivery Address
* Estimated Delivery Date
* Item Frequency Table
* Final Payable Amount

### ✅ Receipt Generation

The program creates `receipt.txt` containing the full summary.


## 📁 Project Structure

project/
│── project.py
│── receipt.txt  (auto-generated on checkout)
│── README.md


## 🚀 How to Run

1. Install Python 3.10+
2. To run the script: python project.py


3. Follow the on-screen instructions
4. At checkout, a `receipt.txt` will be generated in the same folder


## 🔧 Technologies Used

* Python 3
* Built-in dictionary, loops, and file I/O
* No external libraries used

## 📜 Future Improvements

* Add GUI (Tkinter / PyQt)
* Add SQL database for inventory
* Add discount / coupon system
* Create a web version (Flask or Django)

## 📄 License

This project is free to use and modify for educational purposes.

