SELECT types.type_name , COUNT(tdr.relation_type_id) as strong_relations
FROM types
JOIN types_damage_relations tdr ON types.type_id = tdr.type_id
WHERE tdr.damage_relation = 'double_damage_to'
GROUP BY types.type_id
ORDER BY strong_relations DESC
LIMIT 1
