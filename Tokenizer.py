# Read the file
with open("training_data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Count total characters
total_chars = len(text)
print(f"Total characters: {total_chars}")

# 2. Split text into tokens
tokens = text.split()
print(f"Total tokens: {len(tokens)}")

# 3. Print all tokens
print("\nAll tokens:")
for i, token in enumerate(tokens, start=1):
    print(f"{i:3d}: {token}")



import re

# Step 1: Read dataset
with open("training_data.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Step 2: Split text into tokens
result = re.split(r'([,.!?]|\s)', text)

tokens = [item for item in result if item.strip()]

# Step 3: Generate vocabulary
vocabulary = sorted(set(tokens))

# Step 4: Print vocabulary
print("Total tokens:", len(tokens))
print("Total unique tokens:", len(vocabulary))

print("\nVocabulary:")

for index, token in enumerate(vocabulary):
    print(f"{index}: {token}")




import re

# Original dataset
text = "I love Python. I love programming."

# Step 1: Tokenization
tokens = re.split(r'([,.!?]|\s)', text)
tokens = [token for token in tokens if token.strip()]

# Step 2: Vocabulary
vocabulary = sorted(set(tokens))

# Step 3: Token to ID mapping
token_to_id = {
    token: index
    for index, token in enumerate(vocabulary)
}

# Step 4: Encode
token_ids = [
    token_to_id[token]
    for token in tokens
]

# Step 5: Reverse vocabulary
id_to_token = {
    index: token
    for token, index in token_to_id.items()
}

# Step 6: Decode
decoded_text = " ".join(
    id_to_token[token_id]
    for token_id in token_ids
)

print("Original text:", text)
print("Tokens:", tokens)
print("Vocabulary:", vocabulary)
print("Token IDs:", token_ids)
print("Decoded text:", decoded_text)







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
        tokens = re.split(r'([,.!?]|\s)', text)

        tokens = [
            token for token in tokens
            if token.strip()
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


# Dataset
text = "I love Python. I love programming."

# Create vocabulary
tokens = re.split(r'([,.!?]|\s)', text)
tokens = [token for token in tokens if token.strip()]

vocabulary = sorted(set(tokens))

# Create tokenizer
tokenizer = SimpleTokenizer(vocabulary)

# Encoding
ids = tokenizer.encode(text)

# Decoding
decoded_text = tokenizer.decode(ids)

print("Vocabulary:", vocabulary)
print("Token IDs:", ids)
print("Decoded text:", decoded_text)



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
