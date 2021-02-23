from data.data_preprocess import load_data
from data.data_utils import randomTrainingExample
from utils import train,timeSince,generate_from_category
from model import RNN
import unicodedata
import string
import numpy as np
import torch
import torch.nn as nn
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker




'''

Instructions : 
1) read the model.py file, and fill in the right dimensions
2) complete the train function in utils.py
3) fill in the right parameters for main.py
4) train and test your model
5) look at the loss curve and generation results
6) finetune parameters 
7) Answer 3 questions in your report (can be found CTRL+F Question)

'''

# define some parameters     

all_letters = string.ascii_letters + " .,;'-"
n_letters = len(all_letters) + 1 # Question 2 : Plus EOS marker , Why ?
max_len = 15  
path = '.......'   # write the directory to your training data
n_iters = ......   #recommend >10000
print_every = ......
plot_every = ......
hidden_size = ......  #recommend >50

# load data and model 
category_lines , all_categories, n_categories = load_data(path)

learning_rate = 0.0005  # need to tune
criterion = ....... # loss criterion
model = RNN(.......) # define the model 


# start training !
all_losses = []
total_loss = 0 # Reset every plot_every iters
start = time.time()

for iter in range(1, n_iters + 1):
    category, input,output = randomTrainingExample(all_categories,category_lines,all_letters)
    output, loss = train(model,category, input,output,criterion,learning_rate)
    total_loss += loss

    if iter % print_every == 0:
        print('%s (%d %d%%) %.4f' % (timeSince(start), iter, iter / n_iters * 100, loss))

    if iter % plot_every == 0:
        all_losses.append(total_loss / plot_every)
        total_loss = 0

# finish training 
# visualize result
plt.figure()
plt.plot(all_losses)


# perform generation
def samples(category, start_letters='ABC'):
    print("Country:", category)
    for start_letter in start_letters:
        print(generate_from_category(model,all_categories,category,all_letters,max_len,start_letter))

samples('Russian','RUS')
samples('German', 'GER')
samples('Spanish', 'SPA')
samples('Chinese', 'CHI')
