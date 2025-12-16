import streamlit as st
import pandas as pd

st.header("Knowledge Transfer")
st.write("Upload and manage files for your agents to use as a knowledge base.")

if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []

uploaded_file = st.file_uploader("Upload a file", type=['txt', 'pdf', 'md', 'csv', 'json'])

if uploaded_file is not None:
    # Avoid adding the same file multiple times
    if not any(f['name'] == uploaded_file.name for f in st.session_state.uploaded_files):
        file_details = {"name": uploaded_file.name, "type": uploaded_file.type, "size": uploaded_file.size}
        st.session_state.uploaded_files.append(file_details)
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

st.subheader("Uploaded Files")

if not st.session_state.uploaded_files:
    st.info("No files uploaded yet.")
else:
    # Create a DataFrame for better display
    df = pd.DataFrame(st.session_state.uploaded_files)
    df['size (KB)'] = df['size'].apply(lambda x: f"{x/1024:.2f}")

    st.dataframe(df[['name', 'type', 'size (KB)']], use_container_width=True)

    selected_file_name = st.selectbox("Select a file to manage", [f['name'] for f in st.session_state.uploaded_files])

    if selected_file_name:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("View Content", key="view_content", use_container_width=True)
        with col2:
            if st.button("Delete File", key="delete_file", use_container_width=True):
                st.session_state.uploaded_files = [f for f in st.session_state.uploaded_files if f['name'] != selected_file_name]
                st.experimental_rerun()
        with col3:
            st.button("Update File", key="update_file", use_container_width=True)
