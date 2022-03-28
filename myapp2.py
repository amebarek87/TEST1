import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd





# import fitz  # this is pymupdf

# def read_pdf_with_fitz(file):
# 	with fitz.open(file) as doc:
# 		text = ""
# 		for page in doc:
# 			text += page.getText()
# 		return text

# Fxn



def main():
    st.title("TABLERO")

    menu =["Datos"]
    choice = st.sidebar.selectbox("Menu", menu)
   


if __name__ == '__main__':
    main()
