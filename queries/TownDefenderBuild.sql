/*
Castle defender setup assumptions:
- unit speed is not a priority
- unit defense preferred over attack
- hero's defense more important than attack

High defense makes the units withstand longer, which is especially beneficial if the town's castle was upgraded to contain towers,
which deal additional damage to enemys' units each turn.
*/

/* Which units have above average defense per town type? */
CREATE VIEW above_average_defense_units AS
	SELECT 
		u.*
	FROM 
		Heroes3DB.units u
	WHERE u.defense > (
		SELECT 
			AVG(u2.defense)
		FROM 
			Heroes3DB.units u2
		WHERE 
			u2.town = u.town
	);

/* Which artefacts increase defense of the hero? */
CREATE VIEW artifacts_increasing_defense AS
	SELECT *
	FROM 
		Heroes3DB.artifacts
	WHERE 
		effect LIKE "%Defense%";

/* Which of them can be placed in "Shield" slot too? */
SELECT *
FROM 
	Heroes3DB.artifacts
WHERE 
	effect LIKE "%Defense%" AND 
    slot LIKE "Shield";

/* 
For a defender, the "Armorer" is a quite useful skill. Although skills in Heroes 3 can be developed during the game, heroes also have 
specializations, which increase the benefits of corresponding skills. Which heroes possess "Armorer" specialization and which ones
only start with it as one of their skills? 
*/

CREATE VIEW heroes_with_armorer_specialty AS
	SELECT *
	FROM 
		Heroes3DB.heroes
	WHERE 
		specialty LIKE "Armorer";

CREATE VIEW heroes_starting_with_armorer_skill AS
	SELECT *
	FROM 
		Heroes3DB.heroes
	WHERE 
		skill1 LIKE "%Armorer%" OR 
        skill2 LIKE "%Armorer%";
