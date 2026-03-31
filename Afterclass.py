ruler = "".join(chr(i) for i in range(128))
user_text = input("Enter as many characters to find out its ASCII value: ")
for letter in user_text:
    ascii_value = ruler.find(letter)
    print("The value of", letter ,"is", ascii_value)
