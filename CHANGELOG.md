# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-24

### Added

- Fullscreen play mode: an optional setting that switches the dice tray to fullscreen on the first roll, plus a manual fullscreen button on the tray. Uses the Fullscreen API with a CSS overlay fallback.

## [1.0.0] - 2026-11-24

### Added

- Storytelling dice game as an installable, offline-first PWA.
- Four picture sets (classic, universal, travel, household) with 54 pictures each.
- Game modes: classic, relay (2–9 players), theme and surprise.
- 3, 6 or 9 dice, re-rolling of a single die and optional picture names.
- Optional timer (60, 120, 180 seconds) with an audible alert.
- User interface in Slovak, English, German, Hungarian, Czech, Spanish and French.
- Light and dark theme, keyboard support and reduced-motion support.
- Service worker with offline-first caching and a content-hash cache version.
- Web app manifest and icons (192, 512, maskable 512, Apple touch icon, SVG favicon).
- Embedded Baloo 2 and Nunito fonts, so the app makes no external requests.
- Dockerfile, nginx configuration and a Docker Compose file for caddy-docker-proxy.

[Unreleased]: https://github.com/kozliatko/storydice/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/kozliatko/storydice/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/kozliatko/storydice/releases/tag/v1.0.0
