# Security policy

## Supported versions

Only the latest release receives security fixes.

## Reporting a vulnerability

Please do not open a public issue for security problems. Use GitHub's private vulnerability reporting instead: open the **Security** tab of this repository and choose **Report a vulnerability**.

Include a description of the problem, steps to reproduce and the potential impact. You can expect an initial response within a few days.

## Scope

Story Dice is a static, client-side application. It has no backend, accounts or telemetry and makes no external requests. It stores only a language preference (cookie and `localStorage`) and game settings (`localStorage`) in the user's browser. Relevant reports include, for example, cross-site scripting, service worker cache poisoning or problems in the provided Docker and nginx configuration.
