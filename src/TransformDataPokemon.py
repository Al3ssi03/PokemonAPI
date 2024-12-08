import pandas as panda

def GetCleanData(PokeDataList):
    PokeData = panda.DataFrame(PokeDataList)
    PokeDataWithoutDuplicates= PokeData.drop_duplicates(subset=["name"])
    PokeDataNoData = PokeDataWithoutDuplicates.fillna({"name":"Unknown","types": "Unknown","height":0,"weight":0,"base_experience":0, "abilities":"Unknown", "double_damage_to":0 ,"double_damage_from": 0 ,"ability_name": "Unknown", "effect":"Unknown"})
    return PokeDataNoData

def CleanDF(DataFrame):
    # Specifica le colonne da considerare per i duplicati
    columns_to_check = [col for col in DataFrame.columns if not DataFrame[col].apply(lambda x: isinstance(x, list)).any()]
    DataFrameNoDuplicates = DataFrame.drop_duplicates(subset=columns_to_check)

    return DataFrameNoDuplicates
