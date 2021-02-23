import random
import torch


def randomChoice(l):
    return l[random.randint(0, len(l) - 1)]

# generate training example

def randomTrainingExample(all_categories,category_lines,chars):   
    category = randomChoice(all_categories)
    line = randomChoice(category_lines[category])

    category_tensor = torch.zeros(1, len(all_categories))
    category_tensor[0][all_categories.index(category)] = 1

    num_char = len(chars)+1

    input_line_tensor  = torch.zeros(len(line), 1, num_char)
    for li in range(len(line)):
        letter = line[li]
        input_line_tensor[li][0][chars.find(letter)] = 1
    

    target_letter_indexes = [chars.find(line[li]) for li in range(1, len(line))]
    target_letter_indexes.append(num_char - 1) # EOS
    target_line_tensor = torch.LongTensor(target_letter_indexes)


    return category_tensor, input_line_tensor, target_line_tensor


# produce input for generation network

def ExampleForGeneration (all_categories,category,chars,letter='A'):
    
    line = letter

    category_tensor = torch.zeros(1, len(all_categories))
    category_tensor[0][all_categories.index(category)] = 1

    num_char = len(chars)+1

    input_line_tensor = tensor = torch.zeros( 1, num_char)
    input_line_tensor[0][chars.find(letter)] = 1

    return category_tensor, input_line_tensor
