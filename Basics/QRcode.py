import turtle
import qrcode

# Get input from user
user_input = "Hi I am hariharan "

# Create QR code using qrcode library
qr = qrcode.QRCode(
    version=1,  # Adjust version for desired QR code size
    box_size=10,  # Adjust box size for visual clarity
    border=4  # Adjust border thickness
)
qr.add_data(user_input)
qr.make(fit=True)

# Get screen dimensions (not strictly necessary for this code, but included for demonstration)
screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()

# Set up Turtle screen based on QR code dimensions
screen.setup(width=qr.width * 10, height=qr.height * 10)

# Create turtle to draw QR code
t = turtle.Turtle()
t.speed(0)  # Set fastest drawing speed

# Drawing logic
module_size = 10  # Adjust for desired module size

for row in qr.modules:
    for col in row:
        if col:
            t.begin_fill()
            t.color("black")
        else:
            t.color("white")
        t.forward(module_size)
        t.right(90)
        t.forward(module_size)
        t.right(90)
        t.forward(module_size)
        t.right(90)
        t.forward(module_size)
        t.end_fill()
        # Move horizontally for spacing between modules
        if col < len(row) - 1:
            t.penup()
            t.forward(module_size)
            t.pendown()
    # Move down for next row
    t.penup()
    t.left(90)
    t.forward(module_size)
    t.right(90)
    t.pendown()

# Hide turtle and keep the window open
t.hideturtle()
turtle.done()
