<h1> PDF Reader Multimodal RAG Application </h1>

<br>
<div>
This application enables you to take in data in the form of pdfs and prompt on the information contained therein. The RAG model doesn't only depend on gpt but passes additional data to the prompt from the ingested PDF to ensure relevance.The pdf can contain text, tables and images. The app uses powerful tools to process the data and provide a concise summary of the data.
Build with streamlit for an interactive user interface, the app provides a seamless experience for querying the pdfs. 
</div>
<hr>

<h2> Features </h2>

1. PDF ingest
   <ul> 
   <li>Takes in a pdf with images, texts or tables. </li>
   <li>From your queries it verifies the information and gives you output and associated sources</li>
   </ul>
2. User-Friendly Interface:
   <ul>
   <li>Built using streamlit with a visually appealing theme.</li>
   <li>Simple input and output system for ease of use.</li>
   </ul>
3. Database
   <ul>
   <li>uses a vector databse to store information in the form the LLM can comprehend for quick search for simirality on queries </li>
   </ul>
<hr>

<h2>Installation </h2>
<h3>Prerequisites</h3>
<ul>
<li> Python 3.8 and above </li>
<li> Ensure you have a .env file containing the OPEN_AI_KEY for authenticating with OpenAi model.</li>
</ul>

<h3>Install Dependencies</h3> 

Dependencies include:
<ul> 
<li><strong>Python: </strong> the coding environment </li> 
<li><strong>Streamlit:</strong>strong> Frontend </li>
<li><strong>qdrant:</strong> locally run vector database
</li>
<li><strong>inngest:</strong> for orchestration(manage and organize steps) and observability
</li>
<li><strong>LlamaIndex:</strong> ingesting PDFs i.e., load and parse PDFs
</li>
<li><strong>OpenAI: </strong> AI components
</li>
</ul>
<hr>

<h2>How to Use</h2>
1.<strong>Prepare your environment </strong> 
<ul>   <li>Ensure the .env file with the OPENAI_API_KEY is set up correctly.</li>
 </ul>
2. <strong>Run the application </strong>
<ul> <li> Execute the Python script
</li></ul>
3. <strong>Interact with the App </strong>
<ul> 
<li> Drag and drop a pdf file in the provided section
</li>   
<li> Query the file and prompt for a response</li>
<li> View the answer in the output section
</li> 

</ul>
<hr>
<p2>License</p2>
This project is licensed under the MIT License.See the LICENSE file for more details.




