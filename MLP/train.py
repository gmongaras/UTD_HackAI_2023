import torch
from torch import nn
from MLP import MLP, OutputHook
from torch.utils.data import DataLoader






def train():
    # Hyperparameters
    lr = 0.0001
    epochs = 100
    batchSize = 64
    testPer = 0.1
    device = torch.device("cuda:0")
    l1_lambda = 0.01
    
    
    
    # Load in the data
    data = torch.load("./data/data_tens.pt").to(torch.float32)
    
    # Split into train and test data
    train_data = data[int(len(data) * (testPer)):]
    test_data = data[:int(len(data) * (testPer))]
    
    train_dataloader = DataLoader(train_data, batch_size=batchSize, shuffle=True)
    test_dataloader = DataLoader(test_data, batch_size=batchSize, shuffle=True)
    
    
    
    
    # Create the model
    model = MLP().to(device)
    output_hook = OutputHook()
    
    # Create the optimizer
    optim = torch.optim.AdamW(model.parameters(), lr=lr)
    
    # Loss function
    lossFunct = nn.BCELoss(reduction="mean")
    
    
    
    def test_funct(model, device, test_dataloader):
        # Cumulative loss
        loss_cumulative = 0
        
        # Iterate over batches
        for batch in test_dataloader:
            # Split data into inputs and labels
            X = batch[:, :-1].clone().to(device)
            y = batch[:, -1].clone().to(device).unsqueeze(-1)
            
            # Feed data through MLP
            y_hat = model(X)
            
            # Loss calculation
            loss = lossFunct(y_hat, y)
            
            loss_cumulative += loss
        
        # Return the average loss
        return (loss_cumulative / test_data.shape[0]).detach().cpu().item()
    
    
    # Training loop
    for epoch in range(0, epochs):
        # Cumulative loss
        loss_cumulative = 0
        
        # Iterate over batches
        for batch in train_dataloader:
            # Split data into inputs and labels
            X = batch[:, :-1].clone().to(device)
            y = batch[:, -1].clone().to(device).unsqueeze(-1)
            
            # Feed data through MLP
            y_hat = model(X)
            
            # Compute the L1 penalty over the ReLU outputs captured by the hook.
            l1_penalty = 0
            for output in output_hook:
                l1_penalty += torch.norm(output, 1)
            l1_penalty *= l1_lambda
            
            # Loss calculation
            loss = lossFunct(y_hat, y) + l1_penalty
            
            # Backpropagation
            loss.backward()
            optim.step()
            optim.zero_grad()
            output_hook.clear()
            
            # Add to cumulative loss
            loss_cumulative += loss - l1_penalty
            
        print(test_funct(model, device, test_dataloader), (loss_cumulative/train_data.shape[0]).detach().cpu().item())
        
    torch.save(model.state_dict(), "MLP/model.pt")
    
    
    
    
    
    
if __name__ == "__main__":
    train()