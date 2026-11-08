# Changelog — doubleWY Mod

## v1.0.0 — Prima versione stabile / First stable release

Base: firmware OEM Baofeng DM32UV `DM32.NRF.01.049`.

### Novità / New features

- **Installazione guidata** (`doublewy_patcher.py`): sceglie lingua e porta,
  legge il firmware dalla radio con un lettore doubleWY, salva il backup,
  riconosce la versione, crea la mod e la installa, con barre di avanzamento.
  Nessun firmware Baofeng nel repository. / Guided installer: reads the radio,
  backs up, detects the version, builds and installs the mod with progress bars.
- **Menu in italiano** al posto della lingua cinese OEM; voce Italiano/English
  nel menu lingua. / Italian menus replacing the OEM Chinese language.
- **Schermata A/B** ridisegnata: identità al centro, scheda dell'altro lato,
  avviso RX sull'altro lato, S-meter S0–S9/9+. / Redesigned A/B screen.
- **Pagina QSO DMR**: nominativo e nome grandi dal database DMR, Talker Alias
  come ripiego, regione/paese in basso. / DMR QSO page with callsign and name.
- **Editor rapido** (P2 lunga): contatto DMR, tono TX analogico, CC, TS e
  frequenza TX; scelte temporanee sulle memorie. / Quick editor.
- **Tasto `*`**: Analogico/Digitale sul lato selezionato. / Analog/Digital toggle.
- **Monitor DMR** dal campo CC e automatico sui VFO digitali. / DMR Monitor.
- **Zone unite** (Zona1, Zona2…) e **All Zones** per navigazione e Scan.
  / Merged zones and All Zones.
- **Panorama**: analizzatore di spettro su VFO con ricerca, soglia, pagine,
  ascolto FM/DMR; visibile nel menu solo in VFO, con icona propria.
  / Panorama spectrum view.
- **Squelch rapido** SK1 + Su/Giù e **Calibra SQL1** con ascolto live e
  profili salvati, con icona propria. / Quick squelch and Calibrate SQL1.
- **GPS**: locator Maidenhead in GPS Info e pagina **GPS Debug** con
  satelliti, C/N0, elevazione e azimut. / GPS locator and debug page.
- **Schermata di avvio** con il logo doubleWY (1,5 s). / Boot splash with the doubleWY logo.
- **Mod Info** nel menu: autore e versione installata. / Mod Info menu entry.
- Bande RX 136–174 e 400–480 MHz, AM 108–136 MHz; TX 136–174 e 400–480 MHz.

### Miglioramenti / Improvements

- **Avvio più rapido**: ~0,35 s di attese prima dello schermo invece di ~2 s.
- Scan VFO con frequenza aggiornata e ascolto dell'altro lato sospeso;
  All Zones più efficiente; Nuisance Delete con ripristino immediato.
- Aggiornamenti dello schermo solo dei campi che cambiano.
- Etichette inglesi con lingua English.

### Correzioni / Fixes

- Tasti ignorati durante la ricezione.
- Retroilluminazione sempre accesa durante Scan.
- Nome canale assente durante la ricezione DMR.
- Canale iniziale a 0 MHz fino al primo scatto della manopola.
- Tono RX CTCSS/DCS ignorato durante lo Scan delle memorie.
- Ridisegni identici dello S-meter (possibile ticchettio).
