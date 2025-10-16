##PDF Reader Multimodal RAG Application
This application enables you to take in data in the form of pdfs and prompt on the information contained therein. The RAG model doesn't only depend on gpt but passes additional data to the prompt from the ingested PDF to ensure relevance.The pdf can contain text, tables and images. The app uses powerful tools to process the data and provide a concise summary of the data.
Build with streamlit for an interactive user interface, the app provides a seamless experience for querying the pdfs. 

###Features
1. PDF ingest
   Takes in a pdf with images, texts or tables.
   From your queries it verifies the information and gives you output and associated sources
2. User-Friendly Interface:
   Built using streamlit with a visually appealing theme.
   simple input and output system for ease of use.
3. Database
   uses a vector databse to store information in the form the LLM can comprehend for quick search for simirality on queries 

##Installation
###Prerequisites
Python 3.8 and above
ensure you have a .env file containing the OPEN_AI_KEY for authenticating with OpenAi model.

###Install Dependencies

dependencies include:
Python: the coding environment
Streamlit: Frontend
qdrant: locally run vector database
inngest: for orchestration(manage and organize steps) and observability
LlamaIndex: ingesting PDFs i.e., load and parse PDFs
OpenAI: AI components

##How to Use
1. Prepare your environment
   Ensure the .env file with the OPENAI_API_KEY is set up correctly.
2. Run the application
   Execute the Python script
3. Interact with the App
   Drag and drop a pdf file in the provided section
   query the file and prompt for a response
   view the answer in the output section
