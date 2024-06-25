import streamlit as st
st.title('Title-> Streamlit')
st.header('Header-> Streamlit')
st.subheader('Subheader-> Streamlit')
st.text('text-> Streamlit')
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.success('Success!')
st.info('Info')
st.warning('Warning!')
st.error('Error!')
exp = ZeroDivisionError('Division is not possible with 0')
st.exception(exp)
st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))
st.write(1+2+3)
st.write('1+2+3')
st.subheader('Code')
st.code('x = 10\n'                                      
        'for i in range(x):\n'
        '\tprint(i)')

st.subheader('Checkbox')
st.checkbox('Male')
st.checkbox('Female')
if(st.checkbox('Adult')):
    st.write("You're an adult")
st.subheader('Radio Button')
radiobutton = st.radio('Select : ', ('Male','Female'))
if(radiobutton == 'Male'):
    st.write("You're a male")
elif(radiobutton == 'Female'):
    st.write("You're a Female")

st.subheader('Select Box')
selectbox = st.selectbox("Data Science : ", ['Data Analysis', 'Web Scraping', 'Deep Learning', 'Natural Learning Processing', 'Machine Learning',
                                            'Computer Vision', 'Image Processing'])
st.write('You have selected :', selectbox)

st.subheader('MultiSelect Box')
multiselect_box = st.multiselect("Data Science : ", ['Data Analysis', 'Web Scraping', 'Deep Learning', 'Natural Learning Processing', 'Machine Learning',
                                            'Computer Vision', 'Image Processing'])
st.write('You have selected :', len(multiselect_box), multiselect_box)

st.subheader("Button")
if(st.button('Click Me')):
    st.write("Thanks for clicking me.")

st.subheader("Slider")
vol = st.slider('Select the volume:',0,100,step = 1)
st.write('Volume is : ',vol)

st.subheader("Text Input")
username = st.text_input("Username :")
password = st.text_input("Password :", type = 'password')

st.subheader("Text Area")
st.text_area('Write something interesting about yourself')

st.subheader("Input Number")
st.number_input('Select your age',18,110)

st.subheader('Input Date')
st.date_input('Date')

st.subheader("Input Time")
st.time_input('Time')