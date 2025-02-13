import torch
import torch.nn as nn # contains layers, loss functions
import torch.optim as optim # contains optimizers (adam, sgd)
from torch.utils.data import DataLoader, Dataset # allows for storing data and batching

import numpy as np
import pandas as pd

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

class Net(nn.Module): # define model
    def __init__(self):
        super(Net, self).__init__()

        # Creates two connected linear layers; can also be:
        #     2D Convolutional layers, Conv2d(in channels, output channels, kernel size, stride/step, padding)
        #     1D Convolution layers, Conv1D(in channels, output channels, kernel size)
        #     Max Pooling layer, MaxPool2D(kernel size, stride/step, padding)
        #     Average Pooling layer, AvgPool2d(kernel size, stride/step, padding)
        #     Activation Functions (ReLU, LeakyReLU, Sigmoid, Tanh, Softmax, GELU)
        #     Recurrent layers
        #     Batch normalization layers
        #     Dropout layers
        self.fc1 = nn.Linear(10, 5) # layer with 10 input, 2 outputs
        self.fc2 = nn.Linear(5, 2) # layer with 5 input, 2 outputs

    # Tack on an activation function
    # We could also use nn.Sequential to define both the layer and activation at once
    def forward(self, x):
        x = torch.relu(self.fx1(x)) # apply activation function to layer
        x = self.fx2(x)
        return x

### Synthetic Data

### Instatiation
# Instantiate model defined earlier
model = Net()

# Instatiate loss function
# Other types of loss functions:
#
criterion = nn.CrossEntropyLoss()

# Instantiate optimizer
# Other types of optimizers
#
optimizer = optim.Adam(model.parameters(), lr=0.001)

### Training
epochs = 10 # iterations; number of times to go through dataset

for epoch in range(epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad() # clears gradient, as acucmulates gradients default

        outputs = model(inputs) # forward pass; passes input batch
        loss = criterion(outputs, labels) # calculate loss between outputs and labels

        loss.backward() # backward pass; computes gradient of loss
        optimizer.step() # optimization; updates model parameters using optimizer

    print(f"epoch {epoch+1}; loss: {loss.item():.4f}"")
