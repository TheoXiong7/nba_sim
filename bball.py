import random
import time
import sys

sys.setrecursionlimit(1500)


ID_LIST = []

class Team():

	players = []
	team_name = ''

	def __init__(self, name):

		self.team_name = name
		self.players = []
		self.players.append(PointGuard(self))
		self.players.append(ShootingGuard(self))
		self.players.append(SmallForward(self))
		self.players.append(PowerForward(self))
		self.players.append(Center(self))

		self.players.sort(key=lambda x: x.get('height'), reverse=True)


	def team_info(self):
		print(self.team_name)
		for p in self.players:
			print('ID: {}\tPosition: {}\tOverall: {}'.format(p.identifier, p.pos, p.overall))
		print('\n\n')

	def detailed_players_info(self):
		print(self.team_name)
		for p in self.players:
			p.player_info()
		print('\n\n')

	def random_player(self):
		return random.choice(self.players)

class Player():

	# basic info
	fname = ""
	lname = ""
	age = 0
	identifier = 0

	# cm, kg
	body = {}
	attributes = {}

	matchup = None
	team = None
	pos = ''
	overall = 0

	def __init__(self, team):
		pass

	def player_info(self):
		print('----------------------------------------------------------------------------------------------------')
		print('ID: {}\tPosition: {}\tOverall: {}'.format(self.identifier, self.pos, self.overall))
		print(self.body)
		print(self.attributes)
		#print('----------------------------------------------------------------------------------------------------')

	def get(self, att):
		if att in self.attributes:
			return self.attributes[att]
		elif att in self.body:
			return self.body[att]

	def set_matchup(self, matchup):
		self.matchup = matchup
		
	def shoot_ball(self, matchup, game):
		matchup_defense = matchup.get('perimeter-defense')

		chance = (self.get('height') - matchup.get('height')) + (self.get('speed') - matchup.get('speed'))
		chance += self.get('shot-three') - matchup_defense
		chance += random.randint(0, 30)
		#print(chance)
		if chance < 30:
			chance = 30
		elif chance > 70:
			chance = 70

		if random.randint(0, 100) <= chance:
			if game.team1 == self.team:
				game.score[0] += 3
				print('{}\t{} Made 3pt shot'.format(game.score, self.identifier))
				game.team1_stats[self.identifier]['3pa'] += 1
				game.team1_stats[self.identifier]['3pm'] += 1
				game.team1_stats[self.identifier]['fga'] += 1
				game.team1_stats[self.identifier]['fgm'] += 1
				game.team1_stats[self.identifier]['pts'] += 3
				game.team2.random_player().possesion(game)
			elif game.team2 == self.team:
				game.score[1] += 3
				print('{}\t{} Made 3pt shot'.format(game.score, self.identifier))
				game.team2_stats[self.identifier]['3pa'] += 1
				game.team2_stats[self.identifier]['3pm'] += 1
				game.team2_stats[self.identifier]['fga'] += 1
				game.team2_stats[self.identifier]['fgm'] += 1
				game.team2_stats[self.identifier]['pts'] += 3
				game.team1.random_player().possesion(game)
		else:
			if game.team1 == self.team:
				print('{}\t{} Missed 3pt shot'.format(game.score, self.identifier))
				game.team1_stats[self.identifier]['fga'] += 1
				game.team1_stats[self.identifier]['3pa'] += 1
				game.team2.random_player().possesion(game)
			else:
				print('{}\t{} Missed 3pt shot'.format(game.score, self.identifier))
				game.team2_stats[self.identifier]['fga'] += 1
				game.team2_stats[self.identifier]['3pa'] += 1
				game.team1.random_player().possesion(game)

	def pass_ball(self, recipient, game):
		recipient.possesion(game)

	def drive_basket(self, matchup, game):
		# possible steal
		"""
		if random.random() <= 0.2:
			steal_chance = matchup.get('steal') - self.get('ball-handling') 
			if steal_chance > 10:
				if random.random() <= 0.6:
					matchup.possesion()
			else:
				if random.random() <= 0.2:
					matchup.possesion()
		# possible block
		if random.random() <= 0.2:
			block_chance = matchup.get('block') - self.get('finishing') 
			if block_chance > 10:
				if random.random() <= 0.6:
					matchup.possesion()
			else:
				if random.random() <= 0.2:
					matchup.possesion()
		"""
		matchup_defense = (matchup.get('interior-defense') + matchup.get('perimeter-defense')) / 2

		chance = (self.get('height') - matchup.get('height')) + (self.get('speed') - matchup.get('speed'))
		chance += self.get('finishing') - matchup_defense
		chance += random.randint(0, 30)
		#print(chance)
		if chance < 40:
			chance = 40
		elif chance > 90:
			chance = 90

		if random.randint(0, 100) <= chance:
			if game.team1 == self.team:
				game.score[0] += 2
				print('{}\t{} Made driving layup'.format(game.score, self.identifier))
				game.team1_stats[self.identifier]['fga'] += 1
				game.team1_stats[self.identifier]['fgm'] += 1
				game.team1_stats[self.identifier]['pts'] += 2
				game.team2.random_player().possesion(game)
			elif game.team2 == self.team:
				game.score[1] += 2
				print('{}\t{} Made driving layup'.format(game.score, self.identifier))
				game.team2_stats[self.identifier]['fga'] += 1
				game.team2_stats[self.identifier]['fgm'] += 1
				game.team2_stats[self.identifier]['pts'] += 2
				game.team1.random_player().possesion(game)
		else:
			if game.team1 == self.team:
				print('{}\t{} Missed driving layup'.format(game.score, self.identifier))
				game.team1_stats[self.identifier]['fga'] += 1
				game.team2.random_player().possesion(game)
			else:
				print('{}\t{} Missed driving layup'.format(game.score, self.identifier))
				game.team2_stats[self.identifier]['fga'] += 1
				game.team1.random_player().possesion(game)


		#print("height: {}\tspeed: {}\tfinishing: {}".format(self.get('height'), self.get('speed'), self.get('finishing')))
		#print("height: {}\tspeed: {}\tdefense: {}".format(matchup.get('height'), matchup.get('speed'), matchup_defense))
		#print(chance)

	def possesion(self, game):
		# print(game.score)
		
		if game.possesions <= 0:
			game.end()
		else:
			if random.random() <= 0.4:
				game.possesions -= 1
				if random.random() <= 0.5:
					self.drive_basket(self.matchup, game)
				else:
					self.shoot_ball(self.matchup, game)
			else:
				self.pass_ball(self.random_teammate(), game)

	def random_teammate(self):
		return random.choice(self.team.players)

	def set_ovr(self):
		self.overall = int((sum(self.attributes.values()) - self.attributes['block'] - self.attributes['steal']) /  (len(self.attributes) - 2)) + 5


class PointGuard(Player):

	def __init__(self, team):
		while True:
			rand_id = random.randint(100000, 999999)
			if rand_id not in ID_LIST:
				self.identifier = rand_id
				ID_LIST.append(rand_id)
				break
		self.age = random.randint(18, 37)
		self.team = team
		self.pos = 'PG'

		self.body = {
			'height': 190 + random.randint(-15, 15),
			'weight': 90 + random.randint(-20, 20),
			'strength': 60 + random.randint(-25, 25),
			'speed': 80 + random.randint(-15, 15),
			'vertical': 75 + random.randint(-20, 20)
		}

		self.attributes = {
			'shot-mid': random.randint(55, 95),
			'shot-three': random.randint(50, 95),
			'freethrow': random.randint(65, 95),
			'finishing': random.randint(45, 95),
			'passing': random.randint(65, 95),
			'ball-handling': random.randint(65, 95),
			'perimeter-defense': random.randint(45, 95),
			'interior-defense': random.randint(25, 85),
			'block': random.randint(30, 85),
			'steal': random.randint(45, 95),
		}

		self.overall = int((sum(self.attributes.values()) - self.attributes['block'] - self.attributes['steal']) /  (len(self.attributes) - 2)) + 5

class ShootingGuard(Player):

	def __init__(self, team):
		while True:
			rand_id = random.randint(100000, 999999)
			if rand_id not in ID_LIST:
				self.identifier = rand_id
				ID_LIST.append(rand_id)
				break
		self.age = random.randint(18, 37)
		self.team = team
		self.pos = 'SG'

		self.body = {
			'height': 195 + random.randint(-10, 10),
			'weight': 92 + random.randint(-20, 20),
			'strength': 65 + random.randint(-25, 25),
			'speed': 80 + random.randint(-15, 15),
			'vertical': 75 + random.randint(-20, 20)
		}

		self.attributes = {
			'shot-mid': random.randint(60, 95),
			'shot-three': random.randint(60, 95),
			'freethrow': random.randint(65, 95),
			'finishing': random.randint(50, 95),
			'passing': random.randint(35, 85),
			'ball-handling': random.randint(45, 90),
			'perimeter-defense': random.randint(50, 95),
			'interior-defense': random.randint(35, 85),
			'block': random.randint(35, 85),
			'steal': random.randint(45, 95),
		}

		self.overall = int((sum(self.attributes.values()) - self.attributes['block'] - self.attributes['steal']) /  (len(self.attributes) - 2)) + 5

class SmallForward(Player):

	def __init__(self, team):
		while True:
			rand_id = random.randint(100000, 999999)
			if rand_id not in ID_LIST:
				self.identifier = rand_id
				ID_LIST.append(rand_id)
				break
		self.age = random.randint(18, 37)
		self.team = team
		self.pos = 'SF'

		self.body = {
			'height': 200 + random.randint(-5, 10),
			'weight': 97 + random.randint(-20, 20),
			'strength': 65 + random.randint(-25, 25),
			'speed': 70 + random.randint(-15, 15),
			'vertical': 65 + random.randint(-20, 20)
		}

		self.attributes = {
			'shot-mid': random.randint(35, 95),
			'shot-three': random.randint(35, 95),
			'freethrow': random.randint(35, 95),
			'finishing': random.randint(55, 95),
			'passing': random.randint(45, 85),
			'ball-handling': random.randint(45, 90),
			'perimeter-defense': random.randint(50, 95),
			'interior-defense': random.randint(35, 85),
			'block': random.randint(45, 90),
			'steal': random.randint(45, 90),
		}

		self.overall = int((sum(self.attributes.values()) - self.attributes['block'] - self.attributes['steal']) /  (len(self.attributes) - 2)) + 5

class PowerForward(Player):

	def __init__(self, team):
		while True:
			rand_id = random.randint(100000, 999999)
			if rand_id not in ID_LIST:
				self.identifier = rand_id
				ID_LIST.append(rand_id)
				break
		self.age = random.randint(18, 37)
		self.team = team
		self.pos = 'PF'

		self.body = {
			'height': 205 + random.randint(-10, 10),
			'weight': 105 + random.randint(-15, 15),
			'strength': 70 + random.randint(-20, 25),
			'speed': 65 + random.randint(-20, 20),
			'vertical': 65 + random.randint(-20, 20)
		}

		self.attributes = {
			'shot-mid': random.randint(30, 95),
			'shot-three': random.randint(30, 95),
			'freethrow': random.randint(35, 95),
			'finishing': random.randint(55, 95),
			'passing': random.randint(35, 85),
			'ball-handling': random.randint(35, 85),
			'perimeter-defense': random.randint(20, 95),
			'interior-defense': random.randint(45, 95),
			'block': random.randint(45, 95),
			'steal': random.randint(25, 85),
		}

		self.overall = int((sum(self.attributes.values()) - self.attributes['block'] - self.attributes['steal']) /  (len(self.attributes) - 2)) + 5

class Center(Player):

	def __init__(self, team):
		while True:
			rand_id = random.randint(100000, 999999)
			if rand_id not in ID_LIST:
				self.identifier = rand_id
				ID_LIST.append(rand_id)
				break
		self.age = random.randint(18, 37)
		self.team = team
		self.pos = 'C'

		self.body = {
			'height': 208 + random.randint(-7, 10),
			'weight': 115 + random.randint(-15, 25),
			'strength': 70 + random.randint(-20, 25),
			'speed': 65 + random.randint(-15, 15),
			'vertical': 45 + random.randint(-20, 30)
		}

		self.attributes = {
			'shot-mid': random.randint(35, 95),
			'shot-three': random.randint(35, 95),
			'freethrow': random.randint(35, 95),
			'finishing': random.randint(55, 95),
			'passing': random.randint(40, 85),
			'ball-handling': random.randint(35, 90),
			'perimeter-defense': random.randint(15, 95),
			'interior-defense': random.randint(50, 95),
			'block': random.randint(50, 95),
			'steal': random.randint(25, 85),
		}

		self.overall = int((sum(self.attributes.values()) - self.attributes['block'] - self.attributes['steal']) /  (len(self.attributes) - 2)) + 5

class Game():

	score = []
	team1 = None
	team2 = None
	possesions = 0
	team1_stats = {}
	team2_stats = {}

	def __init__(self, team1, team2, pace = 200):
		self.possesions = pace
		self.team1 = team1
		self.team2 = team2
		self.score = [0, 0]
		self.team1_stats = {
			team1.players[0].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team1.players[1].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team1.players[2].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team1.players[3].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team1.players[4].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0}
		}
		self.team2_stats = {
			team2.players[0].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team2.players[1].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team2.players[2].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team2.players[3].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0},
			team2.players[4].identifier: {'pts': 0, 'fga': 0, 'fgm': 0, '3pa': 0, '3pm': 0}
		}
		#self.start_game()

	def start_game(self):
		
		# set matchups
		for i in range(len(self.team1.players)):
			self.team1.players[i].matchup = self.team2.players[i]
			self.team2.players[i].matchup = self.team1.players[i]

		# start game
		random.choice(self.team1.players).possesion(self)

	def end(self):
		
		t1_name = self.team1.team_name
		t2_name = self.team2.team_name
		print('\n')
		if self.score[0] > self.score[1]:
			print('{} Won\n'.format(t1_name))
		elif self.score[0] < self.score[1]:
			print('{} Won\n'.format(t2_name))
		else:
			print('Draw')

		print('Final Score: {}\n'.format(self.score))
		print('{} Stats:'.format(t1_name))
		for s in self.team1_stats:
			print('Player: {}\t\tStats: {}'.format(s, self.team1_stats[s]))
		print('\n')
		print('{} Stats:'.format(t2_name))
		for s in self.team2_stats:
			print('Player: {}\t\tStats: {}'.format(s, self.team2_stats[s]))

		self.save_stats()

	def save_stats(self):
		t1_name = self.team1.team_name
		t2_name = self.team2.team_name

		save_dir = t1_name + '_' + t2_name + '.txt'
		f = open(save_dir, "w")
		f.write('{}\n\n\n\n{} vs {}\n'.format(time.time(), t1_name, t2_name))
		f.write('Final Score: {}\n'.format(self.score))
		f.write('\n\n{} Stats:'.format(t1_name))
		for s in self.team1_stats:
			f.write('\nPlayer: {}\t\tPoints: {}'.format(s, self.team1_stats[s]))
		f.write('\n\n\n{} Stats:'.format(t2_name))
		for s in self.team2_stats:
			f.write('\nPlayer: {}\t\tPoints: {}'.format(s, self.team2_stats[s]))
		f.close()

	def scored(self, player, pts):
		if team == self.team1:
			self.score[0] += pts
		elif team == self.team2:
			self.score[1] += pts



