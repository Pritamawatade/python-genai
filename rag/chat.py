from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
load_dotenv()

openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="nodejs",
    embedding=embedding_model,
)

user_query = input("Ask something : ")


# return relevent chunks from the DB
search_result = vector_db.similarity_search(query=user_query)

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


response = openai_client.chat.completions.create(model="gpt-4o",
                                                 messages=[
                                                     {"role": "system", "content":SYSTEM_PROMPT},
                                                     {"role":"user", "content":user_query}
                                                 ])

print(f"🤖: {response.choices[0].message.content}")

