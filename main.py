import streamlit as sl
 
# Methods (1)
sl.markdown("<h1 style='text-align:center;'>User Registration</h1>", unsafe_allow_html=True)

# With this sintax we create a form widget and 
# then appen the widget to the form widget
form = sl.form("Form 1")

form.text_input("First Name")
form.form_submit_button("Submit")



sl.markdown("---")



# Methods (2)
sl.markdown("<h1 style='text-align:center;'>User Registration ( With Method )</h1>", unsafe_allow_html=True)

# Using the with method we can create a form widget function, 
# and all that is defined in that function is create inside the form widget
with sl.form("Form 2"):
    sl.text_input("Last Name")
    sl.form_submit_button("submit")



sl.markdown("---")




#Complete Registration using the column widget
sl.markdown("<h1 style='text-align:center;'>User Registration ( using column widget )</h1>", unsafe_allow_html=True)

with sl.form("Form 3", clear_on_submit=True):
    
    col1, col2 = sl.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")

    email = sl.text_input("Email Address")
    
    password = sl.text_input("Password")
    
    conf_password = sl.text_input("Confirm Password")
    
    day,month,year = sl.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    
    s_state = sl.form_submit_button("submit")
    if s_state:
        if f_name == "" or l_name =="" or email=="" or password =="" or conf_password=="":
            sl.warning("Please Fill all the fields!")
        else:
            sl.success("Submitted successfully!")