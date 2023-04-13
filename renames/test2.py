import os
path = r"C:\Users\pwnag\OneDrive\Desktop\Python by example\8. tuples_lists_dicts"
count = 1
num = int(input("Insira o valor atual do primeiro challenge da pasta a ser mudado: "))
num2 = int(input("Insira o novo valor que substituirá o antigo informado anteriormente: "))

while count <= 11:

    file_name = f"challenge_{str(num).zfill(2)}.py"
    old_path = os.path.join(path, file_name)

    
    
    if os.path.isfile(old_path):
        num += 1
        num2 += 1
        new_file = f"challenge_{str(num2-1).zfill(2)}.py"
        new_path = os.path.join(path, new_file)
        os.rename(old_path, new_path)
        count = count + 1

    else:
        count = count + 1


