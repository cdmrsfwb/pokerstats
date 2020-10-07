# pokerstats
A python script for keeping track of poker stats and calculating rankings


The script takes data for poker games from two text files and displays rankings based on performace over time, as well as stats for all games played. The average (starting) ranking is 1500


The data needs to be entered in text files called "players.txt" and "games.txt". The python file is then executed to provide a visual output consisting of a players table and a games table, both of which can be sorted according to your needs by clicking on the headers.

Players who have a € in front of their name in "players.txt" or who have not played at least five games will be exluded from the main tables. You can see all players by selecting "All Players" and entering the password "password".


Sample data is provided to give a better idea of how to write down game results.

First, "players.txt" should be filled with players with one on each line in the format: ID (space) nickname (space) full name

In "games.txt", each game should be separated from the next with a newline in between (see sample file). The format of a game is as follows:

  In case of a new date, it should be specified on the first line in the format $YYYY-MM-DD
  
  On the next line should be the name of the game. If you want to use unconventional scoring (more on that later) use the suffix "unc". The suffix will not be displayed in the games table.
  
  On the next line should be the type of the game, eg "Tourney" or "Cash Game"
  
  On the final line, in case of a regular tourney with placements, you can simply write the IDs of players in order (separated by spaces), starting from the winner. In case of a Cash Game or any other game with unconventional scoring you need to add a coefficent after each ID showing how much they won or lost. In my games, I have used being up 100BB as equivalent to winning a tourney (coefficent 1) and losing 100BB as equivalent to coming in last (coefficent -1) and typically rounded the coefficents to one or two decimal places. So, +42BB would give a coefficent of 0.42.
