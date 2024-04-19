import encode
import decode
print("QrCode Encoder and Decoder ")
print(" ---------------------")
user_input =  input("Enter d for decode or e for encode: ").lower()

if user_input == 'd':
    file_name =  input("Enter the file name: ")
    message = decode.decode_qr(file_name)
    print(message)
elif user_input == 'e':
    data = input("Enter the data: ")
    file_name =  input("Enter the file name: ")
    encode.create_qr(data=data,name=file_name)
else:
    print("invalid input")
