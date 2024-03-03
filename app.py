import streamlit as st
from document_reader_v5 import read_text_from_docx, biography
from docx import Document
import io

# This must be the first Streamlit command used.
st.set_page_config(page_title="German Biography Generator", layout="wide")

# Custom header with HTML and CSS
header_html = """
    <div style="background-color:#618264; padding:10px; border-radius:10px">
    <h1 style="color:white; text-align:center;">German Biography Generator</h1>
    <p style="color:white; text-align:center;">We generate short biographies in German language using interview text of any length. Please upload the interview text in Word format to generate biography of the interviewee.</p>
    </div>
    """
st.markdown(header_html, unsafe_allow_html=True)

# Inject CSS for "Generate new biography" button color
st.markdown("""
<style>
.stButton>button {
    border: 1px solid #4CAF50;
    border-radius: 4px; /* Match Streamlit's default button radius */
    color: black; /* Match Streamlit's default button text color */
    background-color: #D0E7D2; /* Custom button color */
    font-size: 16px; /* Adjust to match Streamlit's default button size, if needed */
}
</style>
""", unsafe_allow_html=True)

def create_word_document(biography_text):
    doc = Document()
    doc.add_paragraph(biography_text)
    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

if 'biography_generated' not in st.session_state:
    st.session_state.biography_generated = False

if not st.session_state.biography_generated:
    uploaded_file = st.file_uploader("Choose a Word file", type=['docx'], key="file_uploader")
    if uploaded_file is not None:
        with st.spinner('Processing the document and generating biography...'):
            document_text = read_text_from_docx(uploaded_file)
            biography_text = biography(document_text)
            st.session_state.biography_text = biography_text  # Store biography text in session state
            st.session_state.biography_generated = True
            st.experimental_rerun()
else:
    st.success("Biography generated successfully.")
    
    # Add a heading for the biography preview
    st.markdown("""
        <h2 style='text-align: left; margin-top: 20px;'>Biography</h2>
        """, unsafe_allow_html=True)
    
    st.write(st.session_state.biography_text)
    doc_io = create_word_document(st.session_state.biography_text)
    st.download_button(label="Download Biography in Word Format",
                       data=doc_io,
                       file_name="biography.docx",
                       mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    if st.button("Generate new biography"):
        st.session_state.biography_generated = False
        st.session_state.biography_text = ""
        st.experimental_rerun()
