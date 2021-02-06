# Overview

This program is a simple storefront backend, allowing customers to view products and add them to a cart and managers to add products. This program was a learning experience for cloud databases.

To use this program, simply run `main.py`. A command line interface guides the user through the workings of the program.

I wanted to learn to use cloud databases to store data not only after the termination of a program, but across systems.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

In this project I am using a free version of [Google's Firebase](firebase.google.com)

The structure is relativly simple, with two collections: products and orders. Products contains auto-ID documents that contain product information like name, price, and avaliable quantity.

# Development Environment

This project was written entirely in Visual Studio Code and managed with git. GitHub is the chosen sharing platform.

Written 100% in Python 3.8.1, this project uses only one external library - `firebase-admin` - which can be pip installed. I've split this project into several files for easy readibility.

## Getting started

To get this program working on your own machine, you will need to provide your own credentials to your cloud database. Save the JSON credentials file downloaded from your Firebase database as `creds.json` in the same directory as `main.py`.

# Useful Websites

* [Firebase Docs](https://firebase.google.com/docs/guides)
* [Python 3 Docs](https://docs.python.org/3/)

# Future Work

* Add nesting products capability. Already have fields to support parent products, just need to implement nesting.
* Improve error handling. Little to no error handling allows significant changes to the database to be made.
* Add a front end web page. Firebase offers some hosting capabilities, so serving up HTML pages should be possible.