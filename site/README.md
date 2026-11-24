# Story Dice (Kocky príbehov) – PWA

Statická offline PWA bez závislostí a bez externých požiadaviek.
Písma (Baloo 2, Nunito, licencia SIL OFL 1.1) sú vložené priamo v `index.html`.

## Súbory

| Súbor | Účel |
|---|---|
| `index.html` | celá aplikácia (HTML, CSS, JS, preklady, písma) |
| `manifest.webmanifest` | názov, ikony, farby, `display: standalone` |
| `sw.js` | service worker, pri prvej návšteve uloží všetky súbory do cache |
| `icons/` | ikony 192, 512, maskable 512, apple-touch 180, SVG favicon |

## Nasadenie

- Celý priečinok nahraj na web server. Môže byť aj v podadresári, cesty sú relatívne.
- Service worker funguje len cez **HTTPS** alebo na `localhost`.
- `sw.js` neposielaj s dlhou cache, aby sa aktualizácie dostali k používateľom:

```caddyfile
kocky.example.sk {
	root * /srv/kocky
	encode zstd gzip
	file_server
	@sw path /sw.js
	header @sw Cache-Control "no-cache"
}
```

## Aktualizácie

Verzia cache v `sw.js` je hash všetkých súborov aplikácie. Pri zmene súborov treba vygenerovať nový `sw.js`, inak klienti zostanú na starej verzii.
Nový service worker sa aktivuje okamžite. Nová verzia sa zobrazí pri ďalšom otvorení aplikácie.

## Lokálny test

```sh
python3 -m http.server 8000
# otvor http://localhost:8000, potom v DevTools zapni Offline a obnov stránku
```
