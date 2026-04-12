import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client.http.exceptions import ResponseHandlingException
import warnings
warnings.filterwarnings(
    "ignore",
    message=r"Core Pydantic V1 functionality isn't compatible with Python 3\.14 or greater\.",
)
warnings.filterwarnings(
    "ignore",
    message=r"Qdrant client version .* is incompatible with server version .*",
)

def main() -> None:
    load_dotenv(Path(__file__).parent / ".env")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing in rag/.env")

    pdf_path = Path(__file__).parent / "nodejs.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)
    chunks = text_splitter.split_documents(documents=docs)

    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    try:
        QdrantVectorStore.from_documents(
            documents=chunks,
            embedding=embedding_model,
            url="http://localhost:6333",
            collection_name="nodejs",
        )
    except ResponseHandlingException as exc:
        print(
            "Cannot connect to Qdrant at http://localhost:6333.\n"
            "Start it with: cd rag && docker compose up -d"
        )
        print(f"Details: {exc}")
        return

    # print(chunks[0].page_content[:400])

    


if __name__ == "__main__":
    main()