import re

class SimpleTokenizer:

    def __init__(self, vocabulary):
        self.str_to_int = {
            token: index
            for index, token in enumerate(vocabulary)
        }

        self.int_to_str = {
            index: token
            for token, index in self.str_to_int.items()
        }

    def encode(self, text):
        print(self.int_to_str)
        print(self.str_to_int)

        tokens = re.split(r'([,.!?]|\s)', text)

        tokens = [
            token for token in tokens
            if token.strip()
        ]

        # Replace unknown tokens
        tokens = [
            token if token in self.str_to_int
            else "<|unk|>"
            for token in tokens
        ]

        token_ids = [
            self.str_to_int[token]
            for token in tokens
        ]

        return token_ids

    def decode(self, token_ids):

        tokens = [
            self.int_to_str[token_id]
            for token_id in token_ids
        ]

        return " ".join(tokens)


# Example dataset
text = "I love Python. I love programming."

# Create vocabulary
tokens = re.split(r'([,.!?]|\s)', text)
tokens = [token for token in tokens if token.strip()]

vocabulary = sorted(set(tokens))

# Add special tokens
vocabulary.extend(["<|unk|>", "<|endoftext|>"])

# Create tokenizer
tokenizer = SimpleTokenizer(vocabulary)

# Test unknown word
test_text = "I love JavaScript."

encoded = tokenizer.encode(test_text)

print("Encoded:", encoded)
print("Decoded:", tokenizer.decode(encoded))
