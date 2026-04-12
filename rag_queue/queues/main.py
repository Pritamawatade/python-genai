import sys
from pathlib import Path

# Project root on path: `server` imports `rag_queue.*`, which needs the parent of `rag_queue/`.
_root = Path(__file__).resolve().parents[2]
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from server import app
import uvicorn
from dotenv import load_dotenv
load_dotenv()
def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# if __name__ == "__main__":
#     main()
main()