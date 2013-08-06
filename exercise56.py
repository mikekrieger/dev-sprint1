#exercise 5.6

world.clear()
bob = Turtle()

def koch(t, n):
	if n < 3:
		fd(t, n)
		return
	m = n/3.0
	koch(t, m)
	lt(t, 60)
	koch(t, m)
	rt(t, 120)
	koch(t, m)
	lt(t, 60)
	koch(t, m)

def snowflake(t, n):
	for i in range(3):
		koch(t, n)
		rt(t, 120)(t, 120)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -150
bob.y = 90
bob.redraw()

snowflake(bob, 300)

world.mainloop()