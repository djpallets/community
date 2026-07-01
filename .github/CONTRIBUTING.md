# Contribuire a Pallets

Grazie per il tuo interesse nel contribuire a **Pallets**! ❤️

Ogni contributo è il benvenuto, che si tratti di correggere un bug, migliorare la documentazione, proporre una nuova funzionalità o inviare una pull request.

## Prima di iniziare

Prima di aprire una pull request, ti chiediamo di:

- Controllare se esiste già una issue o una pull request simile.
- Assicurarti che la tua proposta sia coerente con gli obiettivi del progetto.
- Mantenere sempre un comportamento rispettoso e collaborativo.

## Segnalazione di bug

Se trovi un bug, apri una nuova issue includendo:

- Una descrizione chiara del problema.
- I passaggi per riprodurlo.
- Il comportamento previsto.
- Il comportamento effettivo.
- La versione di Python e Django utilizzata.
- Eventuali messaggi di errore o screenshot.

## Proporre nuove funzionalità

Le nuove idee sono sempre benvenute.

Quando proponi una funzionalità, cerca di spiegare:

- Quale problema risolve.
- Come dovrebbe funzionare.
- Perché potrebbe essere utile al progetto.

## Configurazione dell'ambiente di sviluppo

1. Clona il codice sorgente

```bash
git clone https://github.com/djpallets/community.git pallets
cd pallets
```

2. Crea un ambiente virtuale.

```bash
python -m venv .venv
```

3. Attivalo.

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

4. Installa Django e crea un progetto con il database.

```bash
pip install django
django-admin startproject pallets_project .
python manage.py migrate
```

5. Configura le app e gli URL come indicato nel README.
  
6. Esegui i test e avvia il server di sviluppo per verificare le modifiche.

```bash
python manage.py test
python manage.py runserver
```

## Linee guida per il codice

Quando contribuisci:

- Scrivi codice pulito e leggibile.
- Segui lo stile già presente nel progetto.
- Aggiungi o aggiorna i test quando necessario.
- Aggiorna la documentazione se le modifiche influiscono sugli utenti.
- Mantieni le modifiche il più possibile semplici e mirate.

## Messaggi di commit

Scrivi messaggi di commit chiari e descrittivi.

Esempi:

```text
feat: aggiunge il supporto al tema scuro
fix: corregge un errore nella barra laterale
docs: migliora la guida all'installazione
refactor: semplifica il sistema di navigazione
```

## Pull Request

Prima di inviare una pull request, verifica che:

- Il codice funzioni correttamente.
- Eventuali test siano superati.
- La documentazione sia stata aggiornata, se necessario.
- La descrizione della pull request spieghi chiaramente cosa è stato modificato e perché.

## Codice di condotta

Ci aspettiamo che tutti i contributori mantengano un comportamento rispettoso, educato e collaborativo.

Non saranno tollerati comportamenti offensivi, discriminatori o molesti.

## Hai domande?

Se hai dubbi o domande, puoi aprire una issue o una discussione nel repository.

---

Grazie per il tuo contributo!

Ogni miglioramento, grande o piccolo, aiuta a rendere **Pallets** un progetto sempre migliore. 🚀
