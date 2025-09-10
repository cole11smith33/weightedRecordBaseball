# weightedRecordBaseball
<div>

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=flat&logo=microsoft-excel&logoColor=white)
![JavaScript](https://img.shields.io/badge/JAVASCRIPT-323330.svg?&style=flat&logo=javascript&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?&style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-%231572B6.svg?&style=flat&logo=css3&logoColor=white)
</div>


The weighted record is a new baseball statistic, that I am developing to give a clearer picture of a team's skill. Due to the greater level of inter-division and interleague play present in the MLB (52 games against inter-division teams - 13 games per team, 62 games against inter-league teams, 6 games against 8 inter-league opponents and 7 games against 2 inter-league opponents, 48 games against opposing league teams - 3 games against 14 opposing league teams, 6 games against 1 opposing league team).

This means that because nearly a third of all games a team plays in a season is within the same division, that teams in easier divisions have therefore an easier schedule and by extension an easier time making it to the post-season. For example in the 2023 season (which had a slightly different version schedule format), the Minnesota Twins came first in their division with an 87-75 season, meanwhile their wildcard round opponent the Toronto Blue Jays had an 89-73 record came third in there division.

This suggests a large skill gap between these two divisions, a divide between the teams that would be even greater if inter-division play wasn't so prominent. This is because the Jays were in one of the hardest divisions in the league, where all inter-divisional play is more difficult, e.g. harder to get wins because you are playing better teams. Whereas the Twins had one of the easiest divisions in the MLB, playing against easier teams more means more wins.

This would mean, functionally and statistically the game is skill between these two teams would be much larger than the seasonal record of wins and loses should suggest. We need a method for assigning weighting to the value of a team's wins and loses. Sidenote, the Twins swept the Blue Jays in 2 games, so really anything can happen is baseball.

The first step to see if this is a valid measurement and if this is a statistic that we should put any stake within, is to find which divisions are the strongest. A quick and dirty way to do this is to observe the record for each team in the division for the 110 games they play outside there division. Then sum the records for each team in the division. Finally, we compare the records for each division to each other to find the best and the worst.
