[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Aplikacija za upravljanje teniskim terenima i rezervacijama. 
Omogućava kreiranje, pregled, ažuriranje i brisanje teniskih terena i rezervacija.

## Tim

- **Student A**: Dženan Čerkezović - resurs: `/tereni`
- **Student B**: Mahir Duraković - resurs: `/rezervacije`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi


### Resurs A: `/tereni`
| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/tereni` | Lista svih terena (filter po surface) |
| GET | `/tereni/{id}` | Dohvatanje terena po ID-u |
| POST | `/tereni` | Kreiranje novog terena |
| PUT | `/tereni/{id}` | Potpuna zamjena terena |
| PATCH | `/tereni/{id}` | Djelimično ažuriranje terena |
| DELETE | `/tereni/{id}` | Brisanje terena |

**Primjer zahtjeva:**
```bash
# Kreiranje novog terena
curl -X POST "http://localhost:8000/tereni" \
  -H "Content-Type: application/json" \
  -d '{"name": "Teren 1", "surface": "zemlja", "capacity": 2, "price_per_hour": 15.0, "is_covered": false, "available": true}'
```

### Resurs B: `/resursi_b`

| Metoda | Ruta                | Opis                                       |
| ------ | ------------------- | ------------------------------------------ |
| GET    | `/rezervacije`      | Lista svih rezervacija (filter po statusu) |
| GET    | `/rezervacije/{id}` | Dohvatanje rezervacije po ID-u             |
| POST   | `/rezervacije`      | Kreiranje nove rezervacije                 |
| PUT    | `/rezervacije/{id}` | Potpuna zamjena rezervacije                |
| PATCH  | `/rezervacije/{id}` | Djelimično ažuriranje rezervacije          |
| DELETE | `/rezervacije/{id}` | Brisanje rezervacije                       |

**Primjer zahtjeva:**
```bash
# Kreiranje nove rezervacije
curl -X POST "http://localhost:8000/rezervacije" \
  -H "Content-Type: application/json" \
  -d '{
    "user": "mahir",
    "date": "2026-05-12",
    "time_begin": "14:00:00",
    "duration_h": 2,
    "teren_id": 1
    "status": "pending"
  }'
```
## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** [GPT-4, Copilot model, ...]

**Primjer 1:**
- **Prompt:** [Npr. "Kreiraj SQLModel klasu za entitet Knjiga sa poljima naslov, autor, godina, isbn"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Da li ste morali prilagoditi generisani kod]

**Primjer 2:**
- **Prompt:** [Npr. "Implementiraj PATCH endpoint sa exclude_unset=True"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Opis]

## Napomene

[Dodatne napomene specifične za vašu implementaciju]