# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:56:49 2020

Reference: https://www.geeksforgeeks.org/python-loan-calculator-using-tkinter/?ref=rp
"""
# Import tkinter 
from functools import total_ordering
from tkinter import *
class LoanCalculator: 

	def __init__(self): 

		window = Tk() # Create a window 
		window.title("Loan Calculator") # Set title 
		# create the input boxes. 
		Label(window, text = "Annual %Interest Rate").grid(row = 1, column = 1, sticky = W) 
		Label(window, text = "Number of Years").grid(row = 2, column = 1, sticky = W) 
		Label(window, text = "Loan Amount").grid(row = 3, column = 1, sticky = W) 
		Label(window, text = "Monthly Payment").grid(row = 4, column = 1, sticky = W) 
		Label(window, text = "Total Payment").grid(row = 5, column = 1, sticky = W) 
		Label(window, text = "Total Interest").grid(row = 6, column = 1, sticky = W) 

		# for taking inputs 
		self.annualInterestRateVar = StringVar() 
		Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2) 
		self.numberOfYearsVar = StringVar() 

		Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2) 
		self.loanAmountVar = StringVar() 

		Entry(window, textvariable = self.loanAmountVar, justify = RIGHT).grid(row = 3, column = 2) 
		self.monthlyPaymentVar = StringVar() 
		lblMonthlyPayment = Label(window, textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E) 
        
		self.totalPaymentVar = StringVar() 
		lblTotalPayment = Label(window, textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E) 
		
		#Updated output for total interest
		self.totalInterestPaymentVar = StringVar() 
		lblTotalInterestPayment = Label(window, textvariable = self.totalInterestPaymentVar).grid(row = 6, column = 2, sticky = E) 

		# create the button 
		btComputePayment = Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 7, column = 2, sticky = E) 
		window.mainloop() # Create an event loop 

	# compute the total payment. 
	def computePayment(self): 
				
		monthlyPayment = self.getMonthlyPayment( 
		float(self.loanAmountVar.get()), 
		float(self.annualInterestRateVar.get()) / 1200, 
		int(self.numberOfYearsVar.get()) * 12) 
		
		self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f')) # Outputs for monthly
		totalPayment = float(self.monthlyPaymentVar.get()) * 12 *int(self.numberOfYearsVar.get()) 

		totalInterestPayment = float(totalPayment) - float(self.loanAmountVar.get()) # Total Interest formula

		self.totalPaymentVar.set(format(totalPayment, '10.2f')) #Total payment
		self.totalInterestPaymentVar.set(format(totalInterestPayment, '10.2f'))  # And total interest

	def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears): 
		# compute the monthly payment. 
		#monthlyPayment = loanAmount * monthlyInterestRate / (1
		#- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))

		#Updated formula
		monthlyPayment = loanAmount * ((monthlyInterestRate) *
		(1 + monthlyInterestRate)**numberOfYears) / (
		((1 + monthlyInterestRate)**numberOfYears) - 1) 
		return monthlyPayment; 
		root = Tk() # create the widget


# call the class to run the program. 
LoanCalculator() 
