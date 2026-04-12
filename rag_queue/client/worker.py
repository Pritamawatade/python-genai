from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings

def process_query(query: str):
    client = OpenAI()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="nodejs",
    embedding=embeddings,
    )
    
    search_result = vector_db.similarity_search(query=query)
    
    context = "\n\n\n".join(
        [
            f"Page content : {result.page_content}\n Page Number : {result.metadata['page_label']}\n file location: {result.metadata['source']}"
            for result in search_result
        ]
    )
    
    SYSTEM_PROMPT = f"""
    You are a helpfull assistant who answers users query based on the available context retried from the pdf file along with page content and page number.

    you should only answer the user based on the following context and naviagate user to the correct page number. 

    Context: {context}
    """
    
    response = client.chat.completions.create(model="gpt-4o",
                                              messages=[
                                                  {"role": "system", "content":SYSTEM_PROMPT},
                                                  {"role":"user", "content":query}
                                              ])
    print(f"🤖: {response.choices[0].message.content}")
    return response.choices[0].message.content
    

    