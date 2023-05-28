import streamlit as st
from PyPDF4 import PdfReader

def extract_page_content(pdf_file, page_number):
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        page = reader.pages[page_number]
        return page.extract_text()

# Streamlit app
def main():
    st.title("PDF Page Content Extractor")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        # Read uploaded file
        file_contents = uploaded_file.read()
        st.write("File uploaded successfully!")
        
        # Display uploaded file
        st.subheader("Uploaded PDF file")
        st.write(uploaded_file)
        
        # Select page to extract content
        page_number = st.number_input("Enter the page number to extract content", min_value=0)
        
        if st.button("Extract Content"):
            try:
                # Create a temporary file to store the uploaded PDF
                with st.spinner("Extracting content..."):
                    with open("temp.pdf", "wb") as temp_file:
                        temp_file.write(file_contents)
                    
                    # Extract content from the selected page
                    extracted_content = extract_page_content("temp.pdf", page_number)
                    
                    # Display extracted content
                    st.subheader("Extracted Content")
                    st.write(extracted_content)
                    
            except Exception as e:
                st.error(f"Error occurred: {e}")
                
    else:
        st.info("Please upload a PDF file.")

if __name__ == "__main__":
    main()
