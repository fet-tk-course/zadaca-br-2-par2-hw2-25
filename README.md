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
**Model:** [ChatGPT baziran na GPT-5.5 modelu]

**Primjer 1:**
- **Prompt:** Kreiraj SQLModel klasu za entitet Rezervacija sa poljima user, date, time_begin, duration_h, teren_id i status.
- **Kako je pomoglo:** Pomoglo mi je da brzo definišem strukturu baze podataka
- **Prilagodbe:** Morao sam prilagoditi tipove podataka i nazive polja kako bi odgovarali ostatku projekta

**Primjer 2:**
- **Prompt:** "Napravi FastAPI CRUD za entitet Rezervacija (GET, POST, PUT, PATCH, DELETE) koristeći SQLModel, uključujući filter po statusu i 404 error handling."
- **Kako je pomoglo:** Pomoglo mi je da razumijem kako implementirati sve REST endpoint-e i kako koristiti Depends(get_session) za rad sa bazom. Također sam naučio kako pravilno implementirati PATCH sa exclude_unset=True.
- **Prilagodbe:** Morao sam prilagoditi importove i organizaciju fajlova jer moj projekat nije imao poseban schemas_b.py, pa sam modele za Create i Update prebacio u models_b.py

## Napomene

Endpointi su implementirani u skladu sa REST principima i zahtjevima zadatka, uključujući sve CRUD operacije.
Posebna pažnja je posvećena obradi grešaka, svi endpointi koji koriste ID vraćaju 404 status ukoliko resurs nije pronađen.
Implementiran je osnovni filter (status) u GET endpointu za dohvat liste resursa.


## Provjera Mahir Durakovic

Opis promjena dodanih u Z1 i Z2 :
1a) u models_b.py linija 17 -> class RezervacijaCreate(SQLModel): smo dodali validaciju/provjeru za users,duration_h i status.
Za users tj korisnika provjeravali smo da li ime počinje velikim slovom. 
Za duration_h provjeravali smo koliko dugo će trajati njihov boravak gdje smo odlučili da trajanje mora biti između 1-4
Za status radimo provjeru da li je status rezervacije pending , confirmed ili cancelled

1b) u routes_b.py linija 28 -> @router.post("/rezervacije", status_code=201)  dodali smo provjeru koja vraća HTTP 422. Provjerili smo ako rezervacija postoji onda će se korisniku vratiti "Rezervacija za ovaj teren u tom terminu već postoji"