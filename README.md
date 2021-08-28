[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c88747bbd6434dfea8e41b21ebc2c82b)](https://www.codacy.com/gh/TheoXiong7/nba_sim/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=TheoXiong7/nba_sim&amp;utm_campaign=Badge_Grade)

# nba_sim
 
## About
This program simulates basketball using statistics.

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
