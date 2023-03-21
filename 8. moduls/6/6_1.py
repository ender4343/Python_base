try:
    f = open("abc.txt",encoding='utf-8')
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")