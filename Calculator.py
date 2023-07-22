import streamlit as st
import pandas as pd
import numpy as np

def add(a, b):
	sum = a+b
	st.write("The sum for the 2 numbers is: ", sum)
def subtract(a, b):
	diff = a-b
	st.write("The difference for the 2 numbers is: ", diff)
def multiply(a, b):
	product = a*b
	st.write("The sum for the 2 numbers is: ", product)
def divide(a, b):
	quotient = a/b
	st.write("The quotient for the 2 numbers is: ", quotient)
a = st.slider("Choose first number", 1, 2000)
b = st.slider("Choose second number", 1, 2000)
if st.button("Add"):
	add(a, b)
if st.button("Subtract"):
	subtract(a, b)
if st.button("Multiply"):
	multiply(a, b)
if st.button("Divide"):
	divide(a, b)