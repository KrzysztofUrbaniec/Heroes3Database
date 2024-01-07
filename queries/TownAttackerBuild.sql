/* Town attacker assumptions:
- attack is more important than defense
- flying units are obligatory
- ranged units are not a priority, but can serve as a support

In Heroes 3 towns are protected by walls, which can be crossed only be flying units. Other units can enter the interior of the town
only after the catapult breaks through its walls or the drawbridge. Also, only the drawbridge allows units to enter the town without stepping into the moat.

Ranged units are not of the greatest priority, because town's walls decrease the damage they deal by a half. There are some units, which
ignore this limitation though.
*/

/*
Which town has the highest number of flying units? 
(the number is doubled because flying units before and after an upgrade are counted separately)
*/
SELECT
	town,
    COUNT(unit_name) as `#units`
FROM 
	Heroes3DB.units
WHERE
	special_abilities LIKE "%Flying%"
GROUP BY 
	town
ORDER BY 
	`#units` DESC;
    
/* 
It seems, that attacking an enemy's town may be the easiest if player's primary town is either Dungeon or Necropolis, at least if 
the number of flying units is the only factor (both 3)
*/

/* Let's extract only flying units to a separate view */
CREATE VIEW flying_units_view AS
	SELECT *
	FROM
		Heroes3DB.units
	WHERE
		special_abilities LIKE "%Flying%";

/*
Which heroes specialize in offense (increases attack) or ballistics (allows to destroy town walls more efficiently)
or have them as one of initial skills? 
*/
CREATE VIEW heroes_with_offense_or_ballistics_view AS
	SELECT *
	FROM
		Heroes3DB.heroes
	WHERE
		specialty LIKE "%Offense%" OR
		specialty LIKE "%Ballistics%" OR  
		(skill1 LIKE "%Offense%" OR skill1 LIKE "%Ballistics%") OR
		(skill2 LIKE "%Offense%" OR skill2 LIKE "%Ballistics%");
        
/* Which artifacts increase hero's attack? */
CREATE VIEW artifacts_increasing_attack_view AS
	SELECT *
	FROM
		Heroes3DB.artifacts
	WHERE
		effect LIKE "%Attack%"
	
    










