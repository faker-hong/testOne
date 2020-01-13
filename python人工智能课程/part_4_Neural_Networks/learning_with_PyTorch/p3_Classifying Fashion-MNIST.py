from collections import OrderedDict

import matplotlib.pyplot as plt
import numpy as np
import time

import torch
import torchvision
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms
import python人工智能课程.part4_Neural_Networks.learning_with_PyTorch.helper as helper


# Define a transform to normalize the data
# transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), ])
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

# TODO: Define your network architecture here
model = nn.Sequential(OrderedDict([
                      ('fc1', nn.Linear(784, 128)),
                      ('relu1', nn.ReLU()),
                      ('fc2', nn.Linear(128, 64)),
                      ('relu2', nn.ReLU()),
                      ('logits', nn.Linear(64, 10))]))

# TODO: Create the network, define the criterion and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.003)

# TODO: Train the network here
epochs = 3
print_every = 40
steps = 0
for e in range(epochs):
    running_loss = 0
    for images, labels in iter(train_loader):
        steps += 1
        # Flatten MNIST images into a 784 long vector
        images.resize_(images.size()[0], 784)

        optimizer.zero_grad()

        # Forward and backward passes
        output = model.forward(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        if steps % print_every == 0:
            print("Epoch: {}/{}... ".format(e + 1, epochs),
                  "Loss: {:.4f}".format(running_loss / print_every))

            running_loss = 0

# Test out your network!

dataiter = iter(test_loader)
images, labels = dataiter.next()
img = images[0]
# Convert 2D image to 1D vector
img = img.resize_(1, 784)

# TODO: Calculate the class probabilities (softmax) for img
ps = F.softmax(model.forward(img), dim=1)

# Plot the image and probabilities
helper.view_classify(img.resize_(1, 28, 28), ps)
plt.show()
