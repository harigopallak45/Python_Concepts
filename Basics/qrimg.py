import qrcode

# Text to encode in the QR code
text_to_encode = input("Enter Ur Text: ")

# Create a QRCode object with desired settings
qr = qrcode.QRCode(
    version=3.0,  # Adjust version for more data (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Width of the QR code border
)

# Add the text to the QR code
qr.add_data(text_to_encode)
qr.make(fit=True)  # Ensure optimal QR code size

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image as a PNG file
img.save(text_to_encode+".jpg")
