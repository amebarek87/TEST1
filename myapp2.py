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
    data_file=st.sidebar.file_uploader("Sube tu fichero excel o csv", type=['csv','xlsx'])

    if choice == "Datos":
        st.subheader("Datos")
        if st.sidebar.button("Procesar datos"):
            if data_file is not None:
                file_details = {"Filename": data_file.name, "FileType": data_file.type, "FileSize": data_file.size}
                if data_file.type == "csv":
                    df = pd.read_csv(data_file)
                    st.dataframe(df)
                elif data_file.type=="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                    df=pd.read_excel(data_file)

                    columnas=list(df)
                    selected_sector = st.sidebar.multiselect('Variables', columnas, columnas)
                    #sector = df.groupby(columnas)
                    #sorted_sector_unique = sorted(df[columnas].nunique())
                    #selected_data = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)
                    #df_selected_sector = df[(df[columnas].isin(selected_data))]
                    st.dataframe(df)
                else:
                    st.write("file invalid")

    else:
        st.subheader("About")
        st.info("Built with Streamlit")
        st.info("Jesus Saves @JCharisTech")
        st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
    main()