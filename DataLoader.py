import torch
from torch.utils.data import Dataset, DataLoader

class GPTDataset(Dataset):
    def __init__(self, tokens, context_size):
        self.tokens = torch.tensor(tokens)
        self.context_size = context_size

    def __len__(self):
        return len(self.tokens) - self.context_size

    def __getitem__(self, index):
        x = self.tokens[index:index + self.context_size]
        y = self.tokens[index + 1:index + self.context_size + 1]
        return x, y

tokens = [10, 20, 30, 40, 50, 60, 70, 80]

dataset = GPTDataset(tokens, context_size=3)

dataloader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=False
)

for inputs, targets in dataloader:
    print("Inputs:")
    print(inputs)

    print("Targets:")
    print(targets)
    print("----------------")
