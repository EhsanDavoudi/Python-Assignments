import turtle

poly = turtle.Turtle()
sides = int(input('Enter the number of sides: '))
while True:
    color = input('Enter the color(red, blue, green, yello): ')  
    if color == 'red' or color == 'blue' or color == 'green' or color == 'yellow':
        poly.color(color)
        break
    else:
        print('you have to choose between "red", "blue", "green" or "yello"')
        continue
for i in range(sides):
    poly.forward(100)
    poly.right(360 / sides)
turtle.done()