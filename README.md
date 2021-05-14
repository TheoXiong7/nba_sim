# nba_sim
 
## About
This project is currently still under development. I initially made it as a fun way of seeing simulated basketball, but I've decided to try and incorporate real statistics of players in order to generate more accurate results. I'm working on it to be at least a somewhat accurate prediction for nba games.

## Note
- The program uses a bunch of recursion
- Feel free to contact me about this project if you would like to know more/help.

## Usage
```python
import bball

# initiate teams
team1 = bball.Team('lakers')
team2 = bball.Team('celtics')

# print player details
team1.detailed_players_info()
team2.detailed_players_info()

# initiate and start game
game = bball.Game(team1, team2)
game.start()
```
