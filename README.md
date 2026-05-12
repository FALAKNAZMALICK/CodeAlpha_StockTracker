# CodeAlpha_StockTracker
A Python-based portfolio tracker that manages stock investments using dictionaries and basic arithmetic to calculate total value. It allows users to input quantities for predefined stocks and provides an option to export the final investment report to a text file.

# Overview
This is a simple Python program that helps you track your stock portfolio.
You enter the stock names and the number of shares you own, and the program calculates your total portfolio value.

# How It Works
A small dictionary stores fixed prices for stocks (AAPL, TSLA, GOOG, AMZN, META).

You type the stock symbol (like AAPL) and how many shares you own.

The program multiplies shares × price to calculate cost.

It shows a portfolio report with each stock and the total value.

Optionally, you can save the report to a text file (portfolio_report.txt).

# Key Concepts
Dictionary → stores stock prices

Loop → keeps asking until user types done

If-elif → checks valid stock names

Input/Output → user interaction

File Handling → saves report to .txt
