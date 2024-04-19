import qrcode

def create_qr(data,name):
    """
    creates a qr code and return the filename
 
    Args:
        data (String): The data to store in qrcode
        name (String): The filename where the QR code will be saved. 
 
    Returns:
        string : The filename
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        file_name = name +".png"
        img.save(file_name)
        return file_name
    except Exception as e:
        print("error")
        print(e)


create_qr("atw","w")