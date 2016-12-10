import base, random

class Snake:
	def __init__(self):
		self.headx = 0
		self.heady = 0
		self.body = [(self.headx, self.heady)]
		self.length = 1
		self.color = (255, 0, 0)
		self.tilesize = 10
		self.direction = 1 # ^0 >1 v2 <3

	def step(self):
		if self.direction == 0:
			self.heady -= 1
		if self.direction == 1:
			self.headx += 1
		if self.direction == 2:
			self.heady += 1
		if self.direction == 3:
			self.headx -= 1
		self.body.append((self.headx, self.heady))
		self.body = self.body[-self.length:]

	def is_dead(self):
		dead = False
		for point in self.body:
			ti = 0
			for check in self.body:
				if check == point:
					ti += 1
			if ti > 1:
				dead = True

		if not self.headx in xrange(50) or not self.heady in xrange(50):
			dead = True

		return dead

	def draw(self, pygame, screen):
		for point in self.body:
			X = point[0] * self.tilesize
			Y = point[1] * self.tilesize
			pygame.draw.rect(screen, self.color, [X, Y, self.tilesize, self.tilesize])

class Game(base.Game):
	def __init__(self):
		base.Game.__init__(self)
		self.title = "Snake"
		self.show_fps = False
		self.tilesize = 10
		self.rate = 7
		self.snake = Snake()
		self.snake.tilesize = self.tilesize
		self.food = [random.randint(0, 49), random.randint(0, 49)]

	def logic(self):
		self.snake.step()
		if self.snake.is_dead():
			self.running = False
			print "You died!"

		if self.snake.headx == self.food[0] and self.snake.heady == self.food[1]:
			self.food = [random.randint(0, 49), random.randint(0, 49)]
			self.snake.length += 1

	def control(self, keys, mouse):
		if keys[self.pygame.K_UP]:
			self.snake.direction = 0
		if keys[self.pygame.K_RIGHT]:
			self.snake.direction = 1
		if keys[self.pygame.K_DOWN]:
			self.snake.direction = 2
		if keys[self.pygame.K_LEFT]:
			self.snake.direction = 3

	def draw(self):
		self.snake.draw(self.pygame, self.screen)

		X = self.food[0] * self.tilesize
		Y = self.food[1] * self.tilesize
		self.pygame.draw.rect(self.screen, (0, 0, 255), [X, Y, self.tilesize, self.tilesize])

game = Game()
game.start()