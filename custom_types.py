import pydantic

# reps the results after chunking pdf 
class RAGChunksAndSrc(pydantic.BaseModel):
    chunks: list[str]
    source_id: str=None

# reps items ingested
class RAGUpsertResult(pydantic.BaseModel):
    ingested:int

# reps the searches
class RAGSearchResult(pydantic.BaseModel):
    contexts: list[str]
    sources: list[str]

# reps query from user
class RAQQueryResult(pydantic.BaseModel):
    answer: str
    sources:list[str]
    num_contexts:int