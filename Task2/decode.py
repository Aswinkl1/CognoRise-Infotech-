import cv2

def decode_qr(file_name):
    """
    Decodes a qr code and Return the decoded data
 
    Args:
        file_name (String): The filename of the QR code . 
 
    Returns:
        string : The decoded data
    """
    try:
        detector = cv2.QRCodeDetector()
        revel, point, s_qr = detector.detectAndDecode(cv2.imread(file_name))
        return revel
    except Exception as e:
        print(e)