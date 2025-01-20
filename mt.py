import streamlit as st
import numpy as np

# Title and Intro
st.title('12th Class Math Problem Solver')
st.write("Solve different types of 12th class math problems chapter-wise.")

# Sidebar for chapter selection
chapters = [
    "Relations and Functions",
    "Inverse Trigonometric Functions",
    "Matrices",
    "Determinants",
    "Continuity and Differentiability",
    "Application of Derivatives",
    "Integrals",
    "Application of Integrals",
    "Differential Equations",
    "Vector Algebra",
    "Three-dimensional Geometry",
    "Linear Programming",
    "Probability"
]

chapter = st.sidebar.selectbox("Select Chapter", chapters)

# Function to solve Relation and Functions problems
def solve_relations_and_functions():
    st.subheader("Relations and Functions Problem Solver")
    # Example: Find domain and range of a function
    st.write("This feature will help you find domain and range of a function.")
    function = st.text_input("Enter your function (e.g., sqrt(x), 1/(x-2))")
    
    # Simulating a solution for demonstration
    if function:
        st.write(f"The domain of the function {function} is ...")
        st.write(f"The range of the function {function} is ...")

# Function to solve Matrix problems
def solve_matrices():
    st.subheader("Matrices Problem Solver")
    # Example: Matrix addition
    st.write("This feature helps in solving matrix-related problems (addition, multiplication, etc.)")
    
    rows = st.number_input("Enter number of rows in matrix", min_value=1, max_value=5, value=2)
    cols = st.number_input("Enter number of columns in matrix", min_value=1, max_value=5, value=2)
    
    st.write("Enter elements of Matrix A:")
    matrix_a = np.array([[st.number_input(f'A[{i},{j}]') for j in range(cols)] for i in range(rows)])
    
    st.write("Enter elements of Matrix B:")
    matrix_b = np.array([[st.number_input(f'B[{i},{j}]') for j in range(cols)] for i in range(rows)])
    
    if st.button("Solve Matrix Addition"):
        result = matrix_a + matrix_b
        st.write("Matrix A + Matrix B = ")
        st.write(result)

# Function to solve Integration problems
def solve_integrals():
    st.subheader("Integral Problem Solver")
    # Example: Basic integration
    st.write("Solve basic integration problems here.")
    function = st.text_input("Enter the function to integrate (e.g., x^2, sin(x))")
    lower_limit = st.number_input("Enter the lower limit of integration")
    upper_limit = st.number_input("Enter the upper limit of integration")
    
    if st.button("Solve Integral"):
        # Here we would use sympy or numpy for actual integration, but we'll simulate for now.
        st.write(f"The integral of {function} from {lower_limit} to {upper_limit} is ...")

# Main functionality
if chapter == "Relations and Functions":
    solve_relations_and_functions()

elif chapter == "Matrices":
    solve_matrices()

elif chapter == "Integrals":
    solve_integrals()

# Add similar functions for other chapters

# Closing remarks
st.write("More chapters and features coming soon! Stay tuned.")
