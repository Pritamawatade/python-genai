import tiktoken
def tokenise(text: str, model: str = "gpt-3.5-turbo") -> list[int]:
    """Tokenise a string using the tiktoken library."""
    enc = tiktoken.encoding_for_model(model)
    print(enc.decode(enc.encode(text)))
    return enc.encode(text)
if __name__ == "__main__":
    text = "Hello, how are you?"
    tokens = tokenise(text)
    print()
    print(tokens)