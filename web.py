import streamlit as st
import tkinter as tk
from tkinter import filedialog
import functions

st.title("Streamlit Web App")
st.write("Convert Files to Zip Archives OR Extract Zip Archives.")


root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# upload_files = st.file_uploader("Upload Files", accept_multiple_files=True, key="files")
upload_files = st.button("Upload Files")

if upload_files:
    filepaths = filedialog.askopenfilenames(master=root)
    st.write(filepaths)
# Folder picker button
st.write('Please select a destination folder:')
clicked = st.button('Folder Picker')

if clicked:
    dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))

compress = st.button("Compress")

upload_file = st.file_uploader("Upload File", type=["zip"], accept_multiple_files=False, key="file")
extract = st.button("Extract")

# print(upload_files, compress, upload_file, extract)
st.session_state
