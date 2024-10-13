import torch
import torch.nn as nn
import torch.optim as optim

# Check if a GPU is available and set the device accordingly
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define a basic transformer model
class BasicTransformerModel(nn.Module):
    def __init__(self, vocab_size, embed_size, num_heads, hidden_dim, num_layers, max_seq_length):
        super(BasicTransformerModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.positional_encoding = nn.Parameter(torch.zeros(1, max_seq_length, embed_size))
        self.transformer = nn.Transformer(
            d_model=embed_size, 
            nhead=num_heads, 
            num_encoder_layers=num_layers, 
            dim_feedforward=hidden_dim
        )
        self.fc_out = nn.Linear(embed_size, vocab_size)
        self.max_seq_length = max_seq_length

    def forward(self, src, tgt):
        # Move inputs to the device (GPU or CPU)
        src_embed = self.embedding(src) + self.positional_encoding[:, :src.size(1), :]
        tgt_embed = self.embedding(tgt) + self.positional_encoding[:, :tgt.size(1), :]

        # Transformer forward pass
        transformer_out = self.transformer(src_embed, tgt_embed)

        # Final linear layer to predict next word probabilities
        output = self.fc_out(transformer_out)
        return output

# Hyperparameters
vocab_size = 10000  # Adjust as per your dataset
embed_size = 256
num_heads = 8
hidden_dim = 512
num_layers = 2
max_seq_length = 50

# Initialize the model and move it to the device
model = BasicTransformerModel(vocab_size, embed_size, num_heads, hidden_dim, num_layers, max_seq_length).to(device)

# Example input (random data for illustration purposes) - Move tensors to device
src = torch.randint(0, vocab_size, (10, max_seq_length)).to(device)  # Batch of 10 sequences
tgt = torch.randint(0, vocab_size, (10, max_seq_length)).to(device)

# Forward pass
output = model(src, tgt)
print(output.shape)  # Output shape would be [10, max_seq_length, vocab_size]

# Define a tagging system for "Cats" and "cat"
tagging_system = {
    "Cats": {"Animal": 5, "Domestic": 3, "Feline": 2},
    "cat": {"Animal": 5, "Domestic": 3, "Feline": 2}
}

# Example user input for predictions with a tagging system
def predict_next_word(model, sentence, tags, vocab_size):
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():  # Disable gradient calculation for inference
        # Tokenize and encode the sentence
        tokens = sentence.split()
        token_indices = torch.randint(0, vocab_size, (1, len(tokens))).to(device)  # Randomly generate indices for tokens
        
        # Print out the tags for debugging
        for token in tokens:
            if token in tags:
                print(f"Tags for '{token}': {tags[token]}")

        # Assuming the last token is to be predicted
        src = token_indices
        tgt = token_indices  # Here, you would typically use the input sequence as the target as well for next token prediction

        output = model(src, tgt)
        predicted_index = output.argmax(dim=-1)[:, -1]  # Get the index of the predicted next word
        return f"The predicted next word is: word{predicted_index.item()}"

# Example usage with user input
user_input = input("Enter a sentence: ")
print(predict_next_word(model, user_input, tagging_system, vocab_size))
