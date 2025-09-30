from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# chunk pdfs to process big pdfs
EMBED_MODEL = "text-embedding-3-large"
EMBED_DIM = 3072 #should match in vector database

splitter= SentenceSplitter(chunk_size=1000, chunk_overlap=200)

def load_chunk_pdf(path:str):
    docs= PDFReader().load_data(file=path)
    texts = [d.texts for d in docs if getattr(d, "text", None)]
    chunks = []

    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

# convert to vector
def embed_texts(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create( #goes through results
        model= EMBED_MODEL,
        input=texts,
    )
    return[item.embedding for item in response.data]