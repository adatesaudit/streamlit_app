import streamlit as st
import datetime
from datetime import timedelta
import calendar
import os

import tkinter as tk
from tkinter import filedialog

# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.sidebar.title('A feldolgozandó fájlok helye')
st.sidebar.write('Válaszd ki a munkakönyvtárat:')
clicked = st.sidebar.button('Mappaválasztó')
if clicked:
    aaa = filedialog.askdirectory(master=root)
    # st.info(aaa)
    st.sidebar.text_input('kiválasztott könyvtár:', aaa)
    # st.success(aaa)
    os.chdir(aaa)

st.success("A munkamappa" + " --- " + os.getcwd())
#  dirname =


# Title
st.title("My first streamlit app")

# Header

st.header("Second line")
st.subheader("Second line")

# Markdown
st.markdown("### *Hi there!* *[Emy]*")
st.markdown("<https://index.hu>")
st.markdown("*I love supporting* **[Szandi](https://telex.hu)**")

# # Success text - green
st.success("Yeah, it was a success")
#
# # Error - red
st.error("Oops, something went wrong")
#
# # Warning - yellow
st.warning("May be good")
#
# # Info - blue
st.info("Something, you have to know")
#
# # Actual exception
# st.exception("Dummy error")
#
# # help - inbuilt documentation
st.help(type)
#
# # write
a = 10
st.write(a)
#
# # MEDIA
# # Images
# #path = "/streamlit/resources/taxer.JPG"
# #st.image(path)
#
# # Video
# # st.video("Demo.mkv")
#
# # Audio
# # st. audio("audio_sample.waw")
#
# # checkbox
if st.checkbox("1st check"):
    st.text("Checkbox has been selected")
#
# # Radio button
state = st.radio("My radio", ("Option A", "Option B "))
st.write(state)
#
# # Select boxes
selected_item = st.selectbox("Válassz", ["A", "B"])
st.write(selected_item)
#
# # slider
range_var = st.slider("Select range:", 1, 5)
st.write(range_var)
#
# # Buttons
st.button("Clicked!")
st.write("Clicked just now!")
#
# # Text input
info = st.text_input("Enter something", "megalumen sigvec")
info1 = st.text_input("Enter something", type="password")
#
# # Text area
area_info = st.text_area("My text area", height=350)
#
# # Datetime
currentDate = datetime.date.today()
today = st.date_input("Today: ", datetime.datetime.now())
tomorrow = st.date_input("Tomorrow: ", datetime.datetime.now() + timedelta(days=1))
firstDayOfMonth = st.sidebar.date_input("Hónap első napja", datetime.date(currentDate.year, currentDate.month, 1))
lastDayOfMonth = st.sidebar.date_input("Hónap utolsó napja", datetime.date(currentDate.year, currentDate.month,
                                                                           calendar.monthrange(currentDate.year,
                                                                                               currentDate.month)[1]))

# # Displaying json
# st.json({"name" : "Sha"})
#
# # Displaying code
# st.code("import streamlit")
#
# # spinner
# # from time import sleep
# # with st.spinner("please wait 2 secs..."):
# #     sleep(2)
#
# ballons
# st.balloons()
#
# # SIDEBAR
# st.sidebar.title("My sidebar")
#
# #st.sidebar.audio("audio_sample.waw")
#
# # expanders
with st.expander("Click to expand", expanded=False):
    st.code("import streamlit")
#
# st.write("")
# st.write("")
# st.write("")
# st.write("")
#
# # Uploading files
data = st.sidebar.file_uploader("Húzd ide vagy válaszd ki a szükséges fájlt", type=["jpg", "JPG", "pdf", "xls" , "xlsx"] , accept_multiple_files=True)
#
st.write(data)

