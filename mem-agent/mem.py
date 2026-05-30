from mem0 import Memory
import os 
from dotenv import load_dotenv  
from openai import OpenAI
import json


load_dotenv()  # Load environment variables from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO_CONNECTION_URI = os.getenv("NEO_CONNECTION_URI")
NEO_USERNAME = os.getenv("NEO_USERNAME")
NEO_PASS = os.getenv("NEO_PASS")

config = {
    "version": "v1.1",
    "embedder":{
        "provider": "openai",
        "config": { "api_key": OPENAI_API_KEY, "model": "text-embedding-3-small" }
    },
    "llm":{
    "provider": "openai",
        "config": { "api_key": OPENAI_API_KEY, "model": "gpt-4.1" }
        
    },
    "graph_store":{
        "provider":"neo4j",
        "config":{
            "url": NEO_CONNECTION_URI,
            "username": NEO_USERNAME,
            "password": NEO_PASS
        }
    },
    "vector_store":{
        "provider":"qdrant",
        "config":{
            "host": "localhost",
            "port": 6333
        }
    }
}


client = OpenAI()

mem_client = Memory.from_config(config)

while True:
        
    user_query = input("> ")
    
    search_memory = mem_client.search(query=user_query, filters={"user_id": "user_123"})

    memories = [
        f"Id: {mem.get("id")}\n memory:{mem.get("memory")}" for mem in search_memory.get("results")
    ]
    
    print("Relevant Memories:", memories)

    SYSTEM_PROMPT = f"""
    Here is the context about user
    
    {json.dumps(memories)}
    """
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content

    print("AI Response:", ai_response)

    mem_client.add(
        user_id="user_123",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

    print("Memory stored successfully!")