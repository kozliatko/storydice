# Story Dice – app folder

This folder contains the complete Story Dice application: a static, offline-first PWA with no dependencies and no external requests. Fonts (Baloo 2 and Nunito, SIL OFL 1.1) are embedded directly in `index.html`.

For the project overview, features and Docker setup, see the [main README](../README.md).

## Files

| File | Purpose |
|---|---|
| `index.html` | The whole app: HTML, CSS, JavaScript, translations and fonts |
| `manifest.webmanifest` | App name, icons, colours, `display: standalone` |
| `sw.js` | Service worker, caches all app files on the first visit |
| `update-sw.py` | Regenerates the cache version and file list in `sw.js` |
| `icons/` | Icons: 192, 512, maskable 512, Apple touch 180 and SVG favicon |

## Running locally

```sh
python3 -m http.server 8000
# open http://localhost:8000, then enable Offline in DevTools and reload the page
```

## Deployment

- Upload the whole folder to a web server. It can live in a sub-directory, all paths are relative.
- The service worker works only over **HTTPS** or on `localhost`.
- Do not send `sw.js` with a long cache lifetime, otherwise updates will not reach users. Example Caddyfile:

```caddyfile
dice.example.com {
	root * /srv/story-dice
	encode zstd gzip
	file_server
	@sw path /sw.js
	header @sw Cache-Control "no-cache"
}
```

`update-sw.py` is a development tool and does not need to be deployed.

## Updating

The cache version in `sw.js` is a hash of all app files. After changing any file in this folder, regenerate it, otherwise returning visitors stay on the old cached version:

```sh
python3 update-sw.py          # update VERSION and ASSETS in sw.js
python3 update-sw.py --check  # only report whether sw.js is up to date (exit code 1 if not)
```

The version is the first 10 hex characters of a SHA-256 hash over `index.html`, `manifest.webmanifest` and all other app files sorted by path. `sw.js`, `README.md`, the script itself and hidden files are not part of the hash.

A new service worker activates immediately. Users see the new version the next time they open the app.
