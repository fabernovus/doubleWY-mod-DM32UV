# doubleWY Mod per Baofeng DM32UV — v1.0.0

La **doubleWY Mod** nasce da **IU1WWY**, radioamatore appassionato di
informatica, per migliorare il firmware originale del Baofeng DM32UV
(`DM32.NRF.01.049`) e aggiungere nuove funzioni nel tempo.

The **doubleWY Mod** was created by **IU1WWY**, a radio amateur with a passion
for computing, to improve the Baofeng DM32UV original firmware
(`DM32.NRF.01.049`) and add new features over time.

> ☕ **Supporta il progetto / Support the project**
>
> [![Supporta su Ko-fi / Support me on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/doublewy)
>
> La mod è gratuita e sviluppata nel tempo libero. Se ti è utile, puoi
> offrirmi un caffè: **[ko-fi.com/doublewy](https://ko-fi.com/doublewy)**.
>
> The mod is free and built in spare time. If you find it useful, you can buy
> me a coffee: **[ko-fi.com/doublewy](https://ko-fi.com/doublewy)**.

| File | Uso / Purpose |
| --- | --- |
| [doublewy_patcher.py](doublewy_patcher.py) | Genera il firmware della mod / Builds the mod firmware |
| [GUIDE.it.md](GUIDE.it.md) | Guida completa in italiano |
| [GUIDE.en.md](GUIDE.en.md) | Complete English guide |
| [CHANGELOG.md](CHANGELOG.md) | Modifiche per versione / Changes by version |
| [LICENSE](LICENSE), [LICENSE-docs.md](LICENSE-docs.md) | Licenze / Licenses |

Firmware generato / Generated firmware: `doubleWY-mod-DM32UV-v1.0.0.bin`,
**999680 byte**, SHA-256:

```text
66fcfe2558d2c2e025472c26ee119c1aa01f5e45e290de121968487d7b587dc4
```

## TL;DR

### 🇮🇹 Funzioni

**📻 Uso quotidiano**
- **Menu in italiano** — menu, impostazioni e messaggi OEM tradotti.
- **Avvio rapido + splash** — accensione più veloce e logo doubleWY.
- **Tasti in ricezione** — i tasti rispondono anche mentre la radio riceve.
- **Luce in Scan** — la retroilluminazione si spegne anche durante la scansione.

**🖥️ Schermo**
- **Schermata A/B ridisegnata** — cosa ascolti al centro, l'altro lato in una scheda.
- **S-meter S0–S9/9+** — barra e valore S compatti.
- **Pagina QSO DMR** — nominativo e nome grandi, ID, destinazione, paese.

**🎛️ Controlli rapidi**
- **Editor con P2 lunga** — contatto DMR, tono TX, CC, TS e frequenza TX al volo.
- **Tasto `*`** — passa da analogico a digitale.
- **Monitor DMR** — ascolta tutto il traffico senza filtri CC/TS.
- **Squelch rapido** — SK1 + Su/Giù.

**🔎 Scansione e spettro**
- **Zone unite e All Zones** — navigazione e Scan su più zone o su tutte.
- **Scan migliorato** — più chiaro, Nuisance Delete, rispetto del tono RX.
- **Panorama** — analizzatore di spettro sul VFO, ricerca e ascolto FM/DMR.
- **Calibra SQL1** — taratura dello squelch ascoltando, salvata per banda.

**🛰️ GPS e info**
- **GPS Info con locator** — locator Maidenhead a 6 caratteri.
- **GPS Debug** — satelliti, C/N0, elevazione e azimut.
- **Mod Info** — versione installata e autore.

### 🇬🇧 Features

- **📻 Everyday use** — Italian menus · fast boot + splash · keys during receive · backlight timeout in Scan
- **🖥️ Screen** — redesigned A/B screen · S0–S9/9+ meter · DMR QSO page with large callsign and name
- **🎛️ Quick controls** — long-P2 editor (DMR contact, TX tone, CC, TS, TX frequency) · `*` analog/digital · DMR Monitor · SK1 + Up/Down squelch
- **🔎 Scan and spectrum** — merged zones and All Zones · better Scan · Panorama spectrum view · Calibrate SQL1 by ear
- **🛰️ GPS and info** — Maidenhead locator · GPS Debug · Mod Info

Dettagli e schermate / Details and screenshots: [italiano](GUIDE.it.md) · [English](GUIDE.en.md).

## Installazione / Installation

Questo repository **non contiene il firmware Baofeng**: lo script legge il
firmware originale **della tua radio** (`DM32.NRF.01.049`), crea la mod e la
installa, guidandoti passo passo con barre di avanzamento.

1. Installa **Python 3.8+** e **pyserial** (`pip install pyserial`).
2. Collega il cavo di programmazione e chiudi CPS e browser che lo usano.
3. Lancia `python3 doublewy_patcher.py` (su Windows `py doublewy_patcher.py`)
   e segui le istruzioni: lettura della radio (circa 2 min), creazione della
   mod, installazione in modalità aggiornamento SK1 + PTT (circa 2 min).
4. **Conserva il backup** `DM32UV-program-memory-….bin`: è il firmware
   originale della tua radio.

Istruzioni dettagliate per **Windows, macOS e Linux** (driver, porte,
permessi, aggiornamenti, ritorno all'originale): [guida, capitolo 13](GUIDE.it.md#13-installazione-e-aggiornamento).

This repository **does not contain Baofeng firmware**: the script reads **your
radio's** original firmware (`DM32.NRF.01.049`), builds the mod and installs it,
step by step with progress bars.

1. Install **Python 3.8+** and **pyserial** (`pip install pyserial`).
2. Connect the programming cable and close CPS/browser using it.
3. Run `python3 doublewy_patcher.py` (Windows: `py doublewy_patcher.py`) and
   follow the steps: read the radio (~2 min), build, install in SK1 + PTT
   update mode (~2 min).
4. **Keep the backup** `DM32UV-program-memory-….bin`: your radio's original
   firmware.

Detailed **Windows, macOS and Linux** instructions: [guide, chapter 13](GUIDE.en.md#13-installing-and-updating).

## Licenze / Licenses

Patcher e modifiche: **PolyForm Noncommercial 1.0.0** ([LICENSE](LICENSE)).
Guide, changelog e immagini: **CC BY-NC-SA 4.0** ([LICENSE-docs.md](LICENSE-docs.md)).
Uso e modifiche consentiti, uso commerciale no. / Use and modification
allowed, no commercial use.

## Avvertenze / Disclaimer

Progetto amatoriale **non affiliato né approvato da Baofeng**; Baofeng e
DM32UV sono marchi dei rispettivi proprietari. Uso a proprio
rischio. Le prestazioni RF (sensibilità, potenza, tempi) non sono state
misurate in laboratorio. Il repository non contiene firmware, sorgenti OEM, codeplug, contatti o dati
del dispositivo.

Hobby project, **not affiliated with or endorsed by Baofeng**; Baofeng and
DM32UV are trademarks of their owners. Use at your own risk. RF
performance (sensitivity, power, timing) has not been lab-measured. The
repository contains no firmware, OEM source code, codeplug, contacts or device
data.
