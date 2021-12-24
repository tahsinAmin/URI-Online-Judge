Hello solvers ,

today I tried to solve #2988 SQL problem this is my code and I have submited with PostgreSQL 9.5 my output is correspond to the problem output I don't understand why I got this wrong answer.

select teams.name , count(teams.id) as matches,

count( CASE 
         WHEN (team_1_goals > team_2_goals and teams.id = team_1) or (team_2_goals > team_1_goals and teams.id = team_2)  then 1 end ) as victories ,

count( case when (team_1_goals < team_2_goals and teams.id = team_1)  or   (team_2_goals < team_1_goals and teams.id = team_2) then 1 end ) as defeats ,

count( case when team_1_goals = team_2_goals then 1 end) as draws,

count( CASE WHEN (team_1_goals > team_2_goals and teams.id = team_1)  or   (team_2_goals > team_1_goals and teams.id = team_2)  then 1 end )* 3 +
count( case when (team_1_goals < team_2_goals and teams.id = team_1)  or   (team_2_goals < team_1_goals and teams.id = team_2) then 1 end ) * 0 +

count( case when team_1_goals = team_2_goals then 1 end) * 1 as score from teams

join matches ON teams.id = matches.team_1 or teams.id = matches.team_2

group by teams.id 

order by score DESC ;

Thanks in advanced , 


the number of matches is not the sum of the numbers of teams.id.you will have the sum of matches made by each team (use a COUNT to count by checking all the matches that a team has won, lost or drawn).

