
import turtle
import math

def draw_pythagoras_tree(t, branch_length, level, angle):
    if level == 0:
        return
    
    t.forward(branch_length)
    
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)
    
    t.right(2 * angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1, angle)
    
    t.left(angle)
    
    t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    
    level = int(screen.textinput("Рівень рекурсії", "Введіть рівень рекурсії:"))
    
    draw_pythagoras_tree(t, 100, level, 45)
    
    turtle.done()

if __name__ == "__main__":
    main()
