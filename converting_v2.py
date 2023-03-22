#!/usr/bin/env python
# coding: utf-8

# In[11]:


converter = input("Valor inicial: ")
base_atual = int(input("Base atual:\n1)binario\n2)octal\n3)decimal\n4)hexadecimal\n\n"))
base_final = int(input("Base final:\n1)binario\n2)octal\n3)decimal\n4)hexadecimal\n\n"))


if base_atual == 2:
    novo_converter = int(converter, base=8)
    if base_final == 1:
        bina = bin(novo_converter)
        print(f'{converter} octal = {bina} binario')
    
    elif base_final == 3:
        print(f'{converter} octal = {novo_converter} decimal')

    elif base_final == 4:
        hexa = hex(novo_converter)
        print(f'{converter} octal = {hexa} hexadecimal')

        
if base_atual == 3:
    novo_converter = int(converter)
    if base_final == 1:
        bina = bin(novo_converter)
        print(f'{novo_converter} decimal = {bina} binario')
    
    elif base_final == 2:
        octa = oct(novo_converter)
        print(f'{novo_converter} decimal = {octa} octal')

    elif base_final == 4:
        hexa = hex(novo_converter)
        print(f'{novo_converter} decimal = {hexa} hexadecimal')
        
        
if base_atual == 4:
    novo_converter = int(converter, base=16)
    if base_final == 1:
        bina = bin(novo_converter)
        print(f'{converter} hexadecimal = {bina} binario')
        
    elif base_final == 2:
        octa = oct(novo_converter)
        print(f'{converter} hexadecimal = {octa} octal')
        
    elif base_final == 3:
        print(f'{converter} hexadecimal = {novo_converter} decimal')

