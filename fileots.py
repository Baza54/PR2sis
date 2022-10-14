while True:
    try:
        line :str= input("Введите строку: ")
        if len(line) <= 3:
            print("Введите больше 3-ёх букв")
            continue
        if not line.isalpha():
            print("Строка должна быть без цифр и символов")
            continue
        with open(r"G:\files\filep.txt", "w") as fo:
            fo.write(line)
        
    except Exception as e:
         print(e)
