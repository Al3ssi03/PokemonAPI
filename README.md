# PokemonAPI Project

Questo progetto estrae i dati sui Pokémon dalla PokéAPI, li elabora, li memorizza in un database SQLite e permette di eseguire analisi tramite SQL. L'obiettivo è costruire una pipeline di dati che integri Pokémon, tipi, abilità e danni correlati in un sistema relazionale.

## Struttura del Progetto

Il progetto è diviso in più componenti principali:
- **Estrazione dei Dati**: I dati sui Pokémon vengono estratti da PokéAPI utilizzando endpoint RESTful. Le informazioni raccolte includono dettagli sui Pokémon, i loro tipi, abilità e le relazioni di danno tra i vari tipi.
- **Trasformazione e Pulizia dei Dati**: I dati vengono elaborati per rimuovere duplicati, gestire dati mancanti e normalizzare le informazioni per l'inserimento nel database.
- **Caricamento nel Database**: I dati vengono inseriti in un database SQLite utilizzando tabelle relazionali.
- **Analisi dei Dati**: Una volta che i dati sono stati caricati nel database, vengono effettuate analisi tramite query SQL.

## Endpoints Usati
- **/pokemon/{id}**: Estrae informazioni su un Pokémon, come nome, altezza, peso, esperienza base, tipi e abilità.
- **/type**: Estrae informazioni sui tipi di Pokémon, comprese le relazioni di danno.
- **/ability**: Fornisce dettagli sulle abilità dei Pokémon.

## Installazione

1. **Clona il Repository**
   ```bash
   git clone https://github.com/Al3ssi03/PokemonAPI.git

2. **Avvia il progetto Esegui lo script Python per estrarre i dati e popolare il database SQLite:**
    python main.py

## Schema del Database

Le seguenti tabelle vengono create nel database SQLite:

- **pokemon**: Contiene le informazioni di base dei Pokémon (id, nome, altezza, peso, esperienza).
- **types**: Contiene i tipi di Pokémon (id, nome, relazioni di danno).
- **abilities**: Contiene le abilità dei Pokémon.
- **pokemon_types**: Relazione molti-a-molti tra Pokémon e tipi.
- **pokemon_abilities**: Relazione molti-a-molti tra Pokémon e abilità.
- **type_damage_relations**: Relazione di danno tra i vari tipi di Pokémon.

## Funzionalità

- **Estrazione Dati**: I dati vengono estratti tramite richieste API REST a PokéAPI.
- **Database SQLite**: I dati estratti vengono memorizzati in un database SQLite in tabelle relazionali.
- **SQL Queries**: Una volta che i dati sono nel database, puoi eseguire analisi come:
   - Query per trovare Pokémon di un certo tipo.
   - Verifica delle relazioni di danno tra tipi.
   - Dettagli delle abilità di un Pokémon.

