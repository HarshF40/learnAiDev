file = input("File Name: ")
str_len = len(file)

i = 0
flag = True

while file[i]!="." and i<str_len-1:
        i+=1

if flag:
    file_ext = file[i+1:str_len] #this will the other part... i+1-str_len chracters from i+1
    if file_ext == "jpeg" or file_ext == "jpg" or file_ext == "gif" or file_ext == "png":
        print(f"image/{file_ext}")
    elif file_ext == "pdf":
        print(f"document/{file_ext}")
    elif file_ext == "txt":
        print(f"text/{file_ext}")
    elif file_ext == "zip":
        print(f"compressed_file/{file_ext}")
    else:
         print(f"application/octet-stream")