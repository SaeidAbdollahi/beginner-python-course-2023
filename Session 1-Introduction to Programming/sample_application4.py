import turtle
import math

# Function to draw a Spirograph
def draw_spirograph(R, r, d):
    turtle.speed(0)  # Set the drawing speed (0 = fastest)

    # Calculate the GCD of r and R using Euclidean algorithm
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_value = gcd(r, R)
    lcm_value = r * R // gcd_value

    # Calculate the number of rotations needed to complete the Spirograph
    rotations = R / gcd_value

    # Set the initial position
    turtle.penup()
    x = (R - r) * math.cos(0) + d * math.cos(0 * (R - r) / r)
    y = (R - r) * math.sin(0) - d * math.sin(0 * (R - r) / r)
    turtle.goto(x, y)
    turtle.pendown()

    # Draw the Spirograph
    for i in range(int(360 * rotations)):
        t = math.radians(i)
        x = (R - r) * math.cos(t) + d * math.cos(i * (R - r) / r)
        y = (R - r) * math.sin(t) - d * math.sin(i * (R - r) / r)
        turtle.goto(x, y)

    turtle.hideturtle()
    turtle.done()

# Main function
if __name__ == "__main__":
    R = int(input("Enter the value of R (outer radius): "))
    r = int(input("Enter the value of r (inner radius): "))
    d = int(input("Enter the value of d (distance from the center): "))

    draw_spirograph(R, r, d)
