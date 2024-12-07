SELECT p.name, COUNT(par.ability_id) AS abilities_count
FROM pokemon p
JOIN pokemon_abilities_relations par ON p.id = par.pokemon_id
GROUP BY p.id
ORDER BY abilities_count DESC
LIMIT 1;