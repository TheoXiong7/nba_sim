import bball

def main():
	team1 = bball.Team('lakers')
	team2 = bball.Team('celtics')
	team1.detailed_players_info()
	team2.detailed_players_info()
	game = bball.Game(team1, team2)
	game.start()
	game.save_stats()

if __name__ == '__main__':
	main()


#> Think Code