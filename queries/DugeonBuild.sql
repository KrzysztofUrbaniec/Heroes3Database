/*
Build for town defender, attacker and a scout based on query results from TownDefenderBuild.sql, ScoutBuild.sql, TownAttackerBuild.sql
under assumption, that player's primary town is Dungeon.
*/

/* Scout */
/* Which units should be avioded to maximize hero's movement points? */
SELECT *
FROM
	slowest_units_view
WHERE
	town = "Dungeon";
    
/* Troglodytes are the slowest units. They are level 1 creatures and are also quite weak. What about fastest creatures below level 5? */
SELECT *
FROM 
	fastest_units_view
WHERE
	town = "Dungeon";

/* Harpy Hag is an upgraded equivalent of a regular Harpy. They are level 2 creatures and can be readily obtained even in first phases
of the game. Their speed is high, they are able to fly (can omit obstacles) and prevent enemy's retaliation, which makes them a good choice for
a long-distance scout. */

/* What units below level 5 remain if we exclude both Troglodytes and Harpies? */
SELECT *
FROM
	Heroes3DB.units
WHERE
	town = 'Dungeon' AND level BETWEEN 3 AND 4;
    
/* Both Beholders and Medusas and their upgraded versions are ranged units. Upgraded version of Beholders (Evil Eyes) are characterized
by speed equal to 7, which is 2 less than Harpy Hag. They can also be quite easily recruited in the early phase of the game, which makes
them a good choice for a support in scout's army. */

/* Does Dungeon have any heroes, which could serve as scouts in early game? */
SELECT *
FROM heroes_with_scouting_skills_view;

/* 
Gunnar, Lorelei and Deemer are Dungeon heroes and possess one of the following skills when recruited: Logistics or Scouting.
Gunnar starts  with Logistics, which is more benefitial, because it directly increases number of hero's movement points 
*/

/* Artifact further increasing units speed or hero's movement points: */
SELECT *
FROM artifacts_increasing_movement_view;

/* 
One of the buildings available in Dungeon is an Artifact Merchans, which allows to purchase artifacts for quite considerable amounts of gold.
This might be a convenient way to get some items, but rather inaccesible in early phases of the game (Merchant itself costs 10k gold +
artifact price).
*/

/* Town Defender Build */
/* Are there any "Dungeon" heroes with "Armorer" specialization? */
SELECT * 
FROM heroes_with_armorer_specialty;

/* Unfortunately not. How about those, who have it as a starting skill? */
SELECT *
FROM heroes_starting_with_armorer_skill;

/* No heroes from the Dungeon again, that's a pity. Skills can be learned throughout the game, though. */

/* Town Attacker Build */
/* Flying units are the priority. What flying creatures does the Dungeon have? */
SELECT *
FROM 
	flying_units_view
WHERE 
	town = "Dungeon";
    
/* Harpy Hag are quite inexpensive level 2 units, which additionally doesn't allow enemy units to retaliate. There are
also Manticores and Dragon, but both of them accessible in later phases of the game due to elevated recruitment costs. 
This gives Dungeon a total of 3 flying units, providing a significant advantage during town sieges. */




