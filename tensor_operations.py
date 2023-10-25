#!/usr/bin/env python
# coding: utf-8

# In[72]:


import torch


# In[84]:


class TensorCalculator():
    """ Class that makes calculations using tensors"""
    def __init__(self):
        return None
    
    def tensor_zeros(self, dim_x:int, dim_y:int):
        zeros = torch.zeros([dim_x, dim_y])
        return zeros
    
    def tensor_ones(self, dim_x:int, dim_y:int):
        ones = torch.ones([dim_x, dim_y])
        return ones
    
    def tensor_random(self, dim_x:int, dim_y:int):
        random = torch.rand([dim_x, dim_y])
        return random
    
    def tensor_sum(self, tensor1, tensor2):
        t_sum = tensor1 + tensor2
        return t_sum
    
    def tensor_mult(self, tensor1, tensor2):
        t_mult = torch.matmul(tensor1, tensor2)
        return t_mult
    
    def tensor_transpose(self, tensor1):
        transp = torch.transpose(tensor1, 0, 1)
        return transp
    
    def tensor_substraction(self, tensor1, tensor2):
        subs = tensor1 - tensor2
        return subs
    
    def tensor_equal(self, tensor1, tensor2):
        return torch.equal(tensor1, tensor2)
    
    def tensor_pow(self, tensor1, tensor2):
        t_pow = torch.pow(tensor1, tensor2)
        return t_pow
    

