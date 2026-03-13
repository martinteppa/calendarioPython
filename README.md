# calendarioPython

A Python script with two programs:

1. **Available time slots** — given the schedules of two workers, calculates all time windows where both are free to meet. This is a classic Google interview problem.
2. **Pokédex lookup** — queries the [PokéAPI](https://pokeapi.co/) REST API to fetch a Pokémon by ID.

---

## Run with Docker

```bash
docker pull martinteppa/calendariopython

docker create -it --name calendariopy martinteppa/calendariopython

docker start calendariopy

docker exec -it calendariopy bash
```

Then inside the container:

```bash
python3 calendario.py
```

## Run locally

Requires Python 3 and the `requests` library:

```bash
pip install requests
python3 calendario.py
```

---

## Program 1 — Available Time Slots

Enter each person's busy schedule and working hours slot as Python lists.

**Example input:**

```
Person 1 schedule : [['9:00', '13:30'], ['14:30', '15:30']]
Person 1 slot     : ['8:00', '17:30']

Person 2 schedule : [['10:00', '13:30'], ['16:00', '16:30']]
Person 2 slot     : ['10:00', '18:40']
```

**Example output:**

```
Available meeting times for both: [['13:30', '14:30'], ['15:30', '16:00'], ['16:30', '18:40']]
```

## Program 2 — Pokédex Lookup

Enter a Pokémon ID (1–898) to fetch its name from the PokéAPI. Press Enter with no input to quit.

---

## Author

[Martin Teppa](https://github.com/martinteppa) — https://github.com/martinteppa/calendarioPython
