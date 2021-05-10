import bball

def main():
	t1 = bball.Team('lakers')
	t2 = bball.Team('celtics')
	"""
	t1.players[2].identifier = 'Lebron'
	t1.players[2].body = {
		'height': 205,
		'weight': 110,
		'strength': 95,
		'speed': 90,
		'vertical': 90
	}
	t1.players[2].attributes = {
		'shot-mid': 80,
		'shot-three': 75,
		'freethrow': 95,
		'finishing': 95,
		'passing': 95,
		'ball-handling': 95,
		'perimeter-defense': 80,
		'interior-defense': 80,
		'block': 90,
		'steal': 65,
	}
	t1.players[2].set_ovr()

	t2.players[2].identifier = 'PG13'
	t2.players[2].body = {
		'height': 205,
		'weight': 100,
		'strength': 70,
		'speed': 90,
		'vertical': 90
	}
	t2.players[2].attributes = {
		'shot-mid': 90,
		'shot-three': 95,
		'freethrow': 95,
		'finishing': 95,
		'passing': 95,
		'ball-handling': 95,
		'perimeter-defense': 90,
		'interior-defense': 80,
		'block': 70,
		'steal': 75,
	}
	t2.players[2].set_ovr()
	"""
	
	t1.detailed_players_info()
	t2.detailed_players_info()
	g = bball.Game(t1, t2)
	g.start_game()

if __name__ == '__main__':
	main()