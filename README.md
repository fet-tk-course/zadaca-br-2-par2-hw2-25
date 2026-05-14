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

[Analogno kao za Resurs A]

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





Provjera2

U Z1 a) je provjera da li je naziv terena u create shemi prazan string. Ukoliko jeste baci se iznimka
uz odgovarajucu poruku.
Z1 b) U zadatku dva dohvata se lista svih terena i vrsim provjeru da li u toj listi postoji teren
sa istim nazivom kao teren koji se zeli dodati u listu preko POST metoda. Ukoliko postoji potrebno je baciti iznimku 
u formatu statusni kod (409) plus odgovarajuca poruka.


Z2)
U endpointima se traze dostupni tereni (get_dostupni) i veliki tereni (get_veliki_tereni).
Ukoliko isti postoje trebao bi se vratiti 200 ok statusni kod sa listom svih terena u odgovoru.
U slucaju ako ne postoje mogao bi se dodati 404 status kod i bacanje iznimke.
Naredni endpoint predstavlja (get_nedostupni) dohvat nedostupnih terena predstavlja listu svih onih koji nisu dostupni u datom trenutku i koji se mogu izbrisati iz liste. Ponovno u slucaju uspjesnog GET zahtjeva se vraca lista svih nedostupnih
u bodyju plus 200 OK statusni kod.

Promjene modela 1: Dodavanje validatora, polja nisu mijenjana.