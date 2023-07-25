create table games_NBA( 
id int not null primary key,
foreign key(home_team_id) references home_teams_nba(id), 
foreign key(visitor_team_id) references visitors_teams_nba(id),
date TIMESTAMPTZ null, 
home_team_score int null,
visitor_team_score int null,
season int null,
periodo int null,
status char(10) null,
timer time null,
postseason char(10) null,
home_team_id int not null, 
visitor_team_id int not null);

create table home_teams_nba( 
id int not null primary key,
abbreviation char(5),
city char(20),
conference char(8),
division char(15),
full_Name char(30),
short_name char(20));

create table visitors_teams_nba( 
id int not null primary key,
abbreviation char(5),
city char(20),
conference char(8),
division char(15),
full_Name char(30),
short_name char(20));