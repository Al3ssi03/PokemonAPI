SELECT types.type_name, AVG(pokemon.base_experience) as avg_base_experience
FROM pokemon
JOIN pokemon_types_relations ON pokemon.id = pokemon_types_relations.pokemon_id
JOIN types ON pokemon_types_relations.type_id = types.type_id
GROUP BY types.type_name
ORDER BY avg_base_experience DESC
