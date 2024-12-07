SELECT types.type_name , pokemon.name, pokemon.weight
FROM pokemon
JOIN pokemon_types_relations ptr ON p.id = ptr.pokemon_id
JOIN types ON ptr.type_id = types.id
WHERE pokemon.weight IS NOT NULL
ORDER BY types.type_name , pokemon.weight DESC
LIMIT 5