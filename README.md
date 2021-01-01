# Regression Analysis on Through Balls and Presses in Football
This program was created to analyse the relationship between how high an opponent team attempts to press the target team and how many through balls the target team completes.

This is done to see whether pressing high against a certain team will put a team at risk of through balls being completed against them.

## Run your own analysis

To run your own analysis using the program you'll have to place a .xslx file for each team within the /teams/ directory with the file bearing the name of the team. This file should contain five columns:
- Name of opponent
- Presses from the opponent in their defensive third
- Presses from the opponent in the middle third
- Presses from the opponent in their attacking third
- Through balls completed by the target team
The project contains files for each of the premier league teams in the 2020/21 season, correct as of 31/12/2020. This should give an idea of how the files need to be structured.

The data in the example files has been sourced from https://fbref.com/

## Improvements

Due to the limitations of the data its only possible to estimate the average position that a team presses based on which third of the pitch the press occurred in.

In the future this should be improved when access to more exact data is made available.

## Output

The program outputs a scatter plot graph with the following features:
- X-Axis : The average position of the press from the opponent team as a proportion of the pitch
- Y-Axis : The average amount of through balls completed by the target team.
- Colour of Point: The R^2 value calculated across all the games of the target team.

Here is an example of the graph with an added table to show the R^2 values.

![Example graph](https://github.com/greggblenkinsop/football-press-throughball-RA/blob/main/premierleague20-21analysis.png?raw=true)
