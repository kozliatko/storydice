# Contributing

Thanks for your interest in improving Story Dice! Bug reports, ideas, translations and pull requests are all welcome.

## Reporting bugs and requesting features

Open an issue using one of the templates. For bugs, please include your browser and operating system, whether the app was installed as a PWA, and steps to reproduce. Security problems must not be reported in public issues, see [SECURITY.md](SECURITY.md).

## Development setup

The app is a static site without a build step or dependencies.

```sh
cd site
python3 -m http.server 8000
```

Open <http://localhost:8000>. To test the service worker, use `localhost` or HTTPS and the *Application* tab in your browser's DevTools (tick *Update on reload* while developing).

To test the Docker image:

```sh
docker build -t story-dice .
docker run --rm -p 8080:80 story-dice
```

## Project conventions

- Keep the app dependency-free and free of external requests (no CDNs, analytics or remote fonts). It has to work fully offline.
- All user-visible strings live in the `I18N` object in `site/index.html`. When adding or changing a string, update every language so that all languages keep the same keys.
- Keep the interface accessible: visible focus states, sufficient contrast, 44 px minimum touch targets, keyboard operation and `prefers-reduced-motion` support.
- Use relative paths so the app works from a sub-directory.
- Use [EditorConfig](https://editorconfig.org/) settings from `.editorconfig`.

## Service worker version

`VERSION` in `site/sw.js` is a hash of the app files and is used as the cache name. When you change any file in `site/`, run the bundled script, otherwise returning users keep the previously cached version:

```sh
cd site
python3 update-sw.py          # rewrites VERSION and ASSETS in sw.js
python3 update-sw.py --check  # verifies that sw.js is up to date
```

The script also keeps the `ASSETS` list in sync with the files in `site/`.

## Pull requests

1. Fork the repository and create a topic branch from `main`.
2. Keep each pull request focused on one change.
3. Test in at least one Chromium-based browser and one other browser, including offline mode after the first load.
4. Add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).
5. Fill in the pull request template.

## Commit messages

Write short, imperative commit messages, for example `Add French translation` or `Fix timer not stopping after re-roll`.

## Licence

By contributing you agree that your contributions are licensed under the [MIT License](LICENSE).
