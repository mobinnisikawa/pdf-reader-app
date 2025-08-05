import streamlit as st
import PyPDF2

st.title("📄 PDF 読解アプリ")

uploaded_file = st.file_uploader("PDFファイルをアップロードしてください", type="pdf")
if uploaded_file is not None:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    st.text_area("抽出されたテキスト", text, height=400)
