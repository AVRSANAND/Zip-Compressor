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

# Files Upload Button

upload_files = st.button("Upload Files", key="files")

file_paths = []
if upload_files:
    filepaths = filedialog.askopenfilenames(master=root)
    for files in filepaths:
        file_paths.append(files)
    st.write(filepaths)

print(file_paths)

# Destination Folder button

st.write('Please select a destination folder:')
upload_folder = st.button('Folder Picker')

dest_folder = ''

if upload_folder:
    dirname = (filedialog.askdirectory(master=root))
    dest_folder = dirname


compress = st.button("Compress",on_click=functions.make_archive(file_paths, dest_folder))

st.write("Extract Zip Archives.")


upload_archive = st.button("Upload Archive", key="archive")
# archive = []

if upload_archive:
    archive = filedialog.askdirectory(master=root)
    st.write(archive)

upload_dest_folder = st.button('Folder Picker', key="dest_folder")

# extracted_dest_folder = []

if upload_dest_folder:
    dirname = (filedialog.askdirectory(master=root))
    # extracted_dest_folder = dirname
    st.write(dirname)
# extract = st.button("Extract", on_click=functions.extract_archive(archive, extracted_dest_folder))


# upload_file = st.file_uploader("Upload File", type=["zip"], accept_multiple_files=False, key="file")
# extract = st.button("Extract")

# print(upload_files, compress, upload_file, extract)
st.session_state
