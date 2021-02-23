import torch
import torch.nn as nn
import time
import math
from data.data_utils import ExampleForGeneration

def train(model, category_tensor, input_line_tensor, target_line_tensor,criterion,learning_rate):      
    target_line_tensor.unsqueeze_(-1)
    hidden = model.initHidden()
    model.zero_grad()

    loss = 0

    for i in range(input_line_tensor.size(0)):   # complete the forward process of conditional rnn
        ... , ... = model(... , ... ,  ...)
        l = criterion(...  , ... )
        loss += l

    loss.backward()

    for p in model.parameters():
        p.data.add_(p.grad.data, alpha=-learning_rate)

    return output, loss.item() / input_line_tensor.size(0)


def generate_from_category(model,all_categories,category,chars,max_length,start_letter='A'):
     
     n_letters = len(chars) + 1
     category_tensor, input_line_tensor = ExampleForGeneration(all_categories,category,chars,start_letter)

     with torch.no_grad():  # Question 3 : why do we need this ? 
        hidden = model.initHidden()
        output_name = start_letter

        for i in range(max_length):
            ... , ... = model(... , ... , ...)  # complete ! 
            topv, topi = output.topk(1)
            topi = topi[0][0]
            if topi == n_letters - 1:
                break
            else:
                letter = chars[topi]
                output_name += letter
            category_tensor, input_line_tensor = ExampleForGeneration(all_categories,category,chars, ...) # complete ! 

        return output_name


def timeSince(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)