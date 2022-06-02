import data_preprocess
from DCGAN import dcgan

import torch
import numpy as np
import time
import random

gen_model = "DCGAN"

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmarks = True

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

seed_n = np.random.randint(500)
print(seed_n)

random.seed(seed_n)
np.random.seed(seed_n)
torch.manual_seed(seed_n)

gen_time = 0
for nclass in range(0, 3):

    if nclass == 0:
        data_train = data_perprocess.data_class0
        label_train = Data_prep.label_class0
    elif nclass == 1:
        data_train = data_perprocess.data_class1
        label_train = Data_prep.label_class1
    elif nclass == 2:
        data_train = data_perprocess.data_class2
        label_train = Data_prep.label_class2
    
    data_train = data_train.sqapaxes(1,2)

    # generative model
    print("TRAINING GENERATIVE MODEL")
    start = time.time()
    
    print(gen_model)
    gen_data = dcgan(data_train, label_train, seed_n)

    gen_time = gen_time + (time.time() - start)

    if nclass == 0:
        fake_data0 = gen_data
    if nclass == 1:
        fake_data1 = gen_data
    if nclass == 2:
        fake_data2 = gen_data
print("Time for generative model: %f"  % gen_time)