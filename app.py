import streamlit as st

def calculator():
    st.title("Simple Calculator")
    
    # Initialize session state
    if 'result' not in st.session_state:
        st.session_state.result = 0
        st.session_state.first_number = 0
    
    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        first_number = st.number_input("First number", value=st.session_state.first_number)
    with col2:
        operation = st.selectbox("Operation", ['+', '-', '*', '/'])
    with col3:
        second_number = st.number_input("Second number", value=0.0)
    
    # Calculate button
    if st.button("Calculate"):
        if operation == '+':
            st.session_state.result = first_number + second_number
        elif operation == '-':
            st.session_state.result = first_number - second_number
        elif operation == '*':
            st.session_state.result = first_number * second_number
        elif operation == '/':
            if second_number == 0:
                st.error("Division by zero not allowed")
                return
            st.session_state.result = first_number / second_number
        
        # Update first_number for next calculation
        st.session_state.first_number = st.session_state.result
    
    # Display result
    st.write(f"Result: {first_number} {operation} {second_number} = {st.session_state.result}")
    
    # Reset button
    if st.button("Reset"):
        st.session_state.result = 0
        st.session_state.first_number = 0

if __name__ == "__main__":
    calculator()
