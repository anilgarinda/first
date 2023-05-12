import streamlit as st
st.title('My Web App')
st.header('Header')
st.subheader('Subheader')
st.write('Hello, World!')
if st.button('Click me'):
    st.write('Button clicked!')
if st.checkbox('Checkbox'):
    st.write('Checkbox checked!')
option = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])
st.write('You selected:', option)
value = st.slider('Slide me', 0, 10)
st.write('You selected:', value)
file = st.file_uploader('Upload file', type=['csv', 'txt','png'])
if file:
    st.write(file.read())
