import snake as s
import scoreboard
import turtle as t
import food as f
import mine as m
import alt_snake as alt_s
import potion as p
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

user_selection = screen.textinput("Welcome", "Control your snake with the Up, Down, Left, Right keys.\n"
                                             "Make sure not to hit the wall or yourself.\n"
                                  "Enter '1' for NORMAL mode, '2' for HARD mode or '3' for WEIRD mode:\n")

if user_selection != '1' and user_selection != '2' and user_selection != '3':
    user_selection = screen.textinput("Welcome", "That was not a valid selection\n"
                                      "Enter '1' for NORMAL mode, '2' for HARD mode or '3' for WEIRD mode:\n")
if user_selection == '1':
    GROWTH = 2
    snake = s.Snake()
elif user_selection == '2':
    GROWTH = 4
    snake = s.Snake()
elif user_selection == '3':
    screen.textinput("Info", "Stay away from the red mines! Eat blue food to shrink yourself. Click any key to continue.")
    GROWTH = 3
    snake = alt_s.AltSnake()
    mine = m.Mine()

food = f.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_potion = False
game_is_live = True
while game_is_live:
    screen.update()
    time.sleep(0.15)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow_snake(GROWTH)
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    if not is_potion and scoreboard.score == 8 or scoreboard.score == 20:
        potion = p.Potion()
        is_potion = True
    if is_potion and snake.head.distance(potion) < 15:
        snake.shrink()
        potion.ht()
        is_potion = False

    if snake.wall_collision() or snake.tail_collision():
        game_is_live = False
        scoreboard.game_over()

    if user_selection == '3':
        for square in snake.squares[:10]:
            if mine.distance(square) < 16:
                mine.clear()
                mine.color("pink")
                mine.write("BOOOOOOM!", move=False, font=("Courier", 20, "bold"))
                game_is_live = False
                scoreboard.game_over()

screen.exitonclick()

