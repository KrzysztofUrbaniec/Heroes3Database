/*
Scout setup assumptions:
- important in the first phase of the game for quick exploration of the map and resource gathering
- should move fast and be able to defeat low and medium-level neutral creatures guarding resource sources
- due to lack of resources in the first phase, can most likely purchase only low- and medium-level (<5) creatures (depends on initial conditions of the game)
*/

/*
Mobility of a hero is highly influenced by the speed of the units he leads. Slow units work like a bottleneck greatly reducing the number of
movement points the hero has. Let's identify the slowest/fastest units below level 5 in particular towns:
*/

-- Slowest (matches all creatures with speed equal to min_speed, but we have to again filter out these above level 4)
CREATE VIEW slowest_units_view AS
	SELECT
		u.*
	FROM (
		SELECT 
			town,
			MIN(speed) AS min_speed
		FROM Heroes3DB.units
		WHERE level < 5
		GROUP BY town
	) sub
	INNER JOIN 
		Heroes3DB.units u 
	ON 
		u.town = sub.town AND u.speed = sub.min_speed
	WHERE
		level < 5;

-- Fastest
CREATE VIEW fastest_units_view AS
	SELECT
		u1.*
	FROM (
		SELECT 
			town,
			MAX(speed) AS max_speed
		FROM Heroes3DB.units
		WHERE level < 5
		GROUP BY town
		) sub
	INNER JOIN 
		Heroes3DB.units u1 
	ON 
		u1.town = sub.town AND u1.speed = sub.max_speed
	WHERE
		level < 5;
		
/* 
The fastest units are preferred due to their large number of movement points, but may need support of other units (e.g. ranged ones)
if the scout is meant to engage in battles with neutral guarding creatures
*/

/* What creatures below level 5 remain if we exclude the slowest ones? */
SELECT * 
FROM Heroes3DB.units
WHERE unit_name NOT IN (SELECT unit_name FROM slowest_units_view) AND town NOT LIKE "Neutral" AND level < 5;
    
/* 
In Heroes 3 there are 2 skills, which facilitate movement of the hero greatly (logistics & pathfinding) and 1, which is helpful, but 
rather only during exploration phase (scouting). Which heroes have those abilities on start?
*/

CREATE VIEW heroes_with_scouting_skills_view AS
	SELECT
		hero_name,
		skill1,
		skill2
	FROM
		Heroes3DB.heroes
	WHERE
		(skill1 LIKE "%logistics%" OR skill2 LIKE "%logistics%") OR
		(skill1 LIKE "%pathfinding%" OR skill2 LIKE "%pathfinding%") OR
		(skill1 LIKE "%scouting%" OR skill2 LIKE "%scouting%");
    
/* 
Finally, are there any artifacts, that could increase the speed even more?
*/

CREATE VIEW artifacts_increasing_movement_view AS
	SELECT
		*
	FROM Heroes3DB.artifacts
	WHERE
		effect LIKE "%speed%" OR effect like "%movement%";
    
/* 
There are 2 artifacts, which affect hero's movement directly and 3 ones, which increase creatures' speed and therefore hero's movement indirectly.
It would be advantegous to find/get them in the early game.
*/
