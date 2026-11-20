# IL MIO CUCCIOLO — riassunto per continuare il lavoro (v1.5, 21/11/2026)

Versione a parte di "Cani ca Curri" (v0.1), ora chiamata "Il mio cucciolo", fatta per la sala giochi di Ale (il figlio di Alberto). NON è un gioco del Capone: niente Capone, niente siciliano, niente collegamento alla sala giochi del Capone.

## Cosa è cambiato rispetto a Cani ca Curri v0.1
- Nome: "Il mio cucciolo" (titolo, meta tag, impostazioni). Credits in basso: "Un gioco creato da Alberto e Alessandro Seminerio" con il link a albertoseminerio.com sulla parola Alberto (costante CREDITI in b_data.js e riga .cred in index.tpl.html).
- Salvataggio multiplo: fino a 10 cuccioli (MAXP in f_game.js), chiave localStorage ilmiocucciolo_v1 = {cur, pups[]}. Titolo: "I MIEI CUCCIOLI (n/10)" con elenco, gioca e cancella (con conferma); "NUOVO CUCCIOLO" bloccato a 10 finché non se ne cancella uno. Impostazioni: "Cambia cucciolo" e "Nuovo cucciolo".
- Tutti i testi (frasi del cucciolo, menu, messaggi) in italiano normale, niente dialetto.
- Razze: via Cirneco dell'Etna e Bastardino di Girgenti; entrano Beagle, Carlino, Dogue de Bordeaux, Golden Retriever, Corgi. Restano Bassotto, Barboncino, Bulldog inglese, Pastore tedesco, Dalmata, Chihuahua, Husky (12 in tutto). Razza di partenza: Beagle.
- Voci: "Il Capone" -> "Supereroe" (id eroe); "Rude e arrabbiata" -> "Brontolone".
- Accessori: Coppola -> Berretto, Baffi del Capone -> Baffoni, Cappello del Capone -> Cappello di feltro (id feltro).
- Valuta: "piccioli" -> "monete"; "La putìa" -> "Il negozio"; minigioco CURRI! -> CORRI!; cibi: Sasizza -> Salsiccia, Pasta e fasòla -> Pasta e fagioli.
- Tolti: logo/badge del Capone, pulsante "Prova anche gli altri giochi del Capone", crediti Il Capone Quiz. Il pulsante per la sala giochi di Ale c'è ma resta nascosto finché non si scrive l'indirizzo in SALA_URL (b_data.js).
- - Lo scenario (cortile con balcone, lucine, ficodindia, tempio sullo sfondo, nonna che lancia le ciabatte) è rimasto uguale.

## Novità v1.5 — Forme vere
- Nuovo file src/c2_creatures.js (in build.js dopo c_dog.js): SHAPES[nome](d,X) trasforma lo scheletro-cane dopo buildDog (campo B.shape): elefante, trex, tricera, giraffa, ippo, tigre, scimmia, unicorno, capibara, yeti. Helper colLegs (zampe a colonna).
- c_dog.js: B.pitch (corpo inclinato, zampe/collo compensati: d.pitch, d.liftY), B.mouthOpen, pattern 'giraffa'.
- Nuovi: giraffa, ippo, tricera (FANT_ORDER ora 11). Nuovi versi: giraffa, ippo (Snd.fant).
- Test: test/v16.js (ritratti di tutti i fantastici da 2 lati) + test/mont.py.

## Novità v1.4 — Fantastici + giochi
- b_data.js: 8 BREEDS con fan:true (unicorno, trex, capibara, alieno, tigre[cat:true], elefante, scimmia, yeti), FANT_ORDER, spOf(), NOMI_FANT, FRASI_FANT (file voce prefisso fant-), campo snd (kind sonoro).
- c_dog.js: orecchie 'tondo'/'elefante'/'nessuna', code dino/cavallo/scimmia/elefante, corno, criniera, proboscide (d.trunk), zanne, spine, dentini, antenne, occhi neri (eyeBlack).
- a_util.js: soundKind()/kindOf()/CATOVR (stringa), Snd.fant(kind,which) con i versi.
- g_ui.js: tre schede specie (Cani/Gatti/Fantastici) in crDraw.
- g2_garden.js: GAMES + GAME{corsa,rincorrella,calcio,tesoro,girotondo}; gameStart/gameStop/gameTick; stato d.g.st==='game' ferma l'IA libera; attrezzatura (porte, linee, arco, tesoro) in gBuild; #gGames, #gScore, sheetGames().
- Test: test/v14.js (creatore fantastici), test/v15.js (5 giochi, 10 animali).

## Novità v1.3 — Giardino
- Nuovo file src/g2_garden.js (in build.js tra g_ui e h_main). Schermata G.screen==='garden': prato costruito a x=GX=70 (fuori dal cortile), staccionata, laghetto, alberi, panchina, palla con fisica. Si spawnano dei dog (buildDog) per ogni cucciolo in root().pups (max 10), IA a stati: idle/wander/ball/greet/chase/flee (gDog), separazione tra cuccioli, cartellini DOM #gTags. Tap: gardenTap (coccola, lancia palla, chiama). Drag = ruota camera (GC.yaw). Ombre spostate con WORLD.shx.
- Pulsante #bGard (titolo, visibile da 2 cuccioli) e "🌳 Il giardino" nelle impostazioni; uscita #gExit -> exitGarden().
- isCat() ha l'override CATOVR per i versi dei gatti nel giardino.
- Test: sorgenti/test/v13.js (semina 10 cuccioli in localStorage).

## Novità v1.2
- Collina del tempio allargata + terrazza (cilindro) sotto il tempio (d_world.js).
- Gatti: BREEDS con cat:true (siamese, persiano, sphynx, soriano, maine, british), DOG_ORDER/CAT_ORDER/BREED_ORDER, selettore Cani/Gatti in crDraw (g_ui.js), baffi/guance/pupille a fessura in buildDog, coda 'gatto', NOMI_GATTI, FRASI_GATTO (file voce prefisso gatto-), suoni: Snd.mew/purr/shutter, bark/yip/whine/howl diventano versi da gatto (isCat()). Evento "gatto sul muretto" escluso per i gatti.
- Fotocamera: #bCam sempre visibile, snapshot() in g_ui.js (canvas + scritta, Web Share con file, altrimenti download).
- Carezze: petDog in f_game.js; gatto = fusa + cuori + vibrazione; cane = cuori e scamper() (corsetta con scia di cuori).
- Test: sorgenti/test/v12*.js. window.__freeCam=true blocca la camera (solo per prove).

## Cos'è
Cucciolo 3D da accudire nel cortile di una casa (balcone, lucine, ficodindia, limone, cuccia con targhetta, tempio sullo sfondo; cielo che segue l'ora vera).
- 12 cani + 6 gatti + 11 fantastici, pelo/secondo colore/disegno/occhi/collare/accessori/nome.
- 4 barre: fame, felicità, pulizia, energia (scendono anche a gioco chiuso, mai a zero). Mangiare (9 cibi con effetti), bagno strofinando, nanna con sogni, carezze, palla, frisbee, bolle.
- Minigioco CORRI!: la nonna butta il mangiare dal balcone, schivi ciabatte e vasi.
- 7 trucchi a livelli. Negozio accessori. Eventi strani: UFO, gatto sul muretto, ciabatta della nonna, scavo del tesoro, spine del ficodindia, coda, cacca (anche d'oro), gabbiano ladro.
- VOCI a scelta: Bimbo, Bimba, Supereroe, Dolce, Brontolone, Nonno saggio, Solo abbaio (voce sintetica del telefono; registrazioni predisposte in voci/<voce>/<chiave>-<n>.mp3, elenco VOCI_REGISTRATE in b_data.js, frasi in ELENCO-FRASI.txt).

## Come sono fatti i sorgenti
- sorgenti/src/*.js (a_util, b_data, c_dog, d_world, e_fx, f_game, g_ui, h_main) vengono uniti da build.js dentro index.tpl.html insieme a three.js r149 e al font Bungee.
- Per ricostruire:  cd sorgenti && npm i three@0.149.0 && mkdir -p dist && node build.js 1.5 bungee.woff2   -> dist/index.html
- Colori: con three r149 usare sempre l'helper col('#hex') / M('#hex').
- Porticina per le prove: window.__ccc (step(secondi) fa avanzare il gioco). Prove automatiche in sorgenti/test (Playwright): node run.js [title|breeds|more].
- I pannelli a scorrimento sopra il canvas vanno con opacity:.999.

## Cosa NON è stato verificato
- Mai provato su un telefono vero: fluidità, audio e comandi col dito da controllare lì.
- L'audio non è mai stato ascoltato (musica ed effetti sono generati dal gioco).
- Questo gioco non ha classifica.
