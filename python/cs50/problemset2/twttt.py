text = input("Input : ")

i=0
while i < len(text):
    if text[i] in {'a','e','i','o','u','A','E','I','O','U'}:
        text = text[:i] + text[i+1:]
    i+=1

print(text)
