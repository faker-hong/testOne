import matplotlib.pyplot as plt

import torch
import torchvision
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms

import python人工智能课程.part4_Neural_Networks.learning_with_PyTorch.helper as helper
import python人工智能课程.part4_Neural_Networks.learning_with_PyTorch.fc_model as fc_model


# Define a transform to normalize the data
# transform = transforms.Compose([
#      transforms.ToTensor(),
#      transforms.Lambda(lambda x: x.repeat(3, 1, 1)),
#      transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
#  ])
# Download and load the training data
train_set = datasets.MNIST('MNIST_data/', download=True, train=True, transform=torchvision.transforms.ToTensor())
# batch_size 每批图片的数量， shuffle 每个epoch之后是否重新洗牌
train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

# Download and load the test data
test_set = datasets.MNIST('MNIST_data/', download=True, train=False, transform=torchvision.transforms.ToTensor())
test_loader = torch.utils.data.DataLoader(test_set, batch_size=64, shuffle=True)


# Train a network
model = fc_model.Network(784, 10, [512, 256, 128])
criterion = nn.NLLLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

fc_model.train(model, train_loader, test_loader, criterion, optimizer, epochs=2)

# Saving and loading networks
print("Our model: \n\n", model, '\n')
print("The state dict keys: \n\n", model.state_dict().keys())


torch.save(model.state_dict(), 'checkpoint.pth')

state_dict = torch.load('checkpoint.pth')
print(state_dict.keys())
model.load_state_dict(state_dict)


# write a function to load checkpoints.
# def load_checkpoint(filepath):
#     checkpoint = torch.load(filepath)
#     model = fc_model.Network(checkpoint['input_size'],
#                              checkpoint['output_size'],
#                              checkpoint['hidden_layers'])
#     model.load_state_dict(checkpoint['state_dict'])
#
#     return model
#
# model = load_checkpoint('checkpoint.pth')
# print(model)