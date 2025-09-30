from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

# turn data into vectors
class QdrantStorage:
    def __init__(self, url="http://localhost:6333", collection="docs", dim=3072):
        self.client = QdrantClient(url=url, timeout=30)
        self.collection = collection
        if not self.client.collection_exists(self.collection):
            self.client.create_collection(
                collectiom_name=self.collection,
                vectors_config= VectorParams(size=dim, distance=Distance.COSINE), #calc distance between points
            )
    # get the associate vectors(dims), ids and payloads(data)
    def upsert(self, ids, vectors, payloads):
        points= [PointStruct(id=ids[i], vector=vectors[i], payload=payloads[i]) for i in range(len(ids))]
        self.client.upsert(self.collection, points=points)

    # search database and get relevant results
    def search(self, query_vector, top_k: int=5):
        results = self.client.search(
            collection_name=self.collection,
            query_vector=query_vector,
            with_payload=True,
            limits=top_k #look for results in database
        )


        contexts= [] #store context
        sources = set() #store the sources

        # gets the context
        for r in results:
            payload= getattr(r, "payload", None) or {}
            text=payload.get("text", "")
            source = payload.get("source", "")
            if text:
                contexts.append(text)
                sources.add(source)
        
        return{"contexts": contexts, "sources": list(sources)}


