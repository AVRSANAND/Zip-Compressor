import streamlit as st
import functions

st.title("Streamlit Web App")
st.write("Convert Files to Zip Archives OR Extract Zip Archives.")

upload_files = st.file_uploader("Upload Files", accept_multiple_files=True, key="files")
dest_folder = st
compress = st.button("Compress")

upload_file = st.file_uploader("Upload File", type=["zip"], accept_multiple_files=False, key="file")
extract = st.button("Extract")

# print(upload_files, compress, upload_file, extract)
st.session_state
