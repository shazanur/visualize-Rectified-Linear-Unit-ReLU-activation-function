#SD23001 LAB 4
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

x = np.linspace(-5, 5, 200)
relu = np.maximum(0, x)

plt.figure()
plt.plot(x, relu)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("ReLU Function")
plt.grid(True)

st.pyplot(plt)
