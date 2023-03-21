converter = int(input("Valor decimal: "))
print("Base desejada:\n1)binario\n2)octal\n3)hexadecimal\n")
base_final = int(input(" "))

if base_final == 2:
  octa = oct(converter)
  print(f'{converter} decimal = {octa} octal')

if base_final == 1:
  bina = bin(converter)
  print(f'{converter} decimal = {bina} binario')

if base_final == 3:
  hexa = hex(converter)
  print(f'{converter} decimal = {hexa} hexadecimal')
