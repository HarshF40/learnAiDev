file = input("File Name: ")
str_len = len(file)

dot_pos = file.rfind(".") #this will return the position of the dot in the text file

file_ext = file[dot_pos+1:] #this will return the string from the dot pos to the end of the string

if file_ext in {"jpg","jpeg","png","gif"}:
    print(f"image/{file_ext}")
elif file_ext == "pdf":
    print(f"document/{file_ext}")
elif file_ext == "txt":
    print(f"text/{file_ext}")
elif file_ext == "zip":
    print(f"compressed_file/{file_ext}")
else:
    print(f"application/octet-stream")