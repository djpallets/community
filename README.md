<div align="center">

  <img width="100" height="100" alt="18132" src="https://github.com/user-attachments/assets/41fb641c-4ef4-465e-9335-c3ec83c05956" />


  # Pallets Community Edition
  _Django Admin, Made Better_
</div>

---

## Cos'è Pallets

Pallets è un Admin Site alternativo a quello di Django Base. Di differenze, ha un'interfaccia più moderna ed è più semplice da gestire.

---

##  Quick Setup

### 1. Clona il codice

```bash
git clone https://github.com/djpallets/community.git pallets
```

### 2. Aggiungi alle apps

```python
INSTALLED_APPS = [
  'pallets'
  'my_app'
  'django.contrib.admin'
  --snip--
]
```

### 3. Aggiungi agli urls del progetto il necessario

```python
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Admin predefinito (Puoi toglierlo sostituendolo con pallets)
    path('admin/', admin.site.urls),

    # Pallets
    path('pallets/', include('pallets.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # Poi le tue
]
```

---

## Contribuire

Se vuoi contribuire, leggi il file:

👉 `CONTRIBUTING.md`

---

## Obiettivo del progetto

Pallets vuole diventare un admin panel:

- più moderno di default
- più facile da estendere
- più piacevole da usare

---

## Note importanti

- Django è un marchio registrato di Django Software Foundation.
