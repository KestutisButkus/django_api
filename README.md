# Muzikos Projekto API

Tai yra Django projektas, kuris teikia RESTful API sąsają valdyti grupėms, albumams, dainoms, albumų apžvalgoms ir susijusiems subjektams. Projektas sukurtas naudojant Django ir Django REST Framework.

## Funkcijos

- Grupės, albumų, dainų, albumų apžvalgų, apžvalgų komentarų ir patiktukų valdymas.
- RESTful API galiniai taškai CRUD operacijoms.
- Vartotojų autentifikacija ir autorizacija.
- Patogi naudoti Django administravimo sąsaja.

## Modeliai

Projektas apima šiuos modelius:

### Grupė (Band)
- `name`: CharField

### Albumas (Album)
- `name`: CharField
- `band`: ForeignKey į Grupę

### Daina (Song)
- `name`: CharField
- `duration`: DurationField
- `album`: ForeignKey į Albumą

### Albumo apžvalga (AlbumReview)
- `user`: ForeignKey į Vartotoją (User)
- `album`: ForeignKey į Albumą
- `content`: TextField
- `score`: IntegerField (pvz., 8/10)

### Albumo apžvalgos komentaras (AlbumReviewComment)
- `user`: ForeignKey į Vartotoją
- `album_review`: ForeignKey į Albumo apžvalgą
- `content`: TextField

### Albumo apžvalgos patiktukas (AlbumReviewLike)
- `user`: ForeignKey į Vartotoją
- `album_review`: ForeignKey į Albumo apžvalgą

## Diegimas

1. **Klonuokite saugyklą**:
   ```sh
   git clone <repository_url>
   cd music_project

2. **Sukurkite virtualią aplinką ir aktyvuokite ją**:
    ```she
    python -m venv venv
    source venv/bin/activate  # Windows sistemoje: venv\Scripts\activate
   
3. **Įdiekite priklausomybes**:
    ```she
    pip install -r requirements.txt

4. **Pritaikykite migracijas**:
    ```she
    python manage.py makemigrations
    python manage.py migrate


5. **Sukurkite supervartotoją**:
    ```she
    python manage.py createsuperuser

6. **Paleiskite vystymo serverį**:
    ```she
    python manage.py runserver