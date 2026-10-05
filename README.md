# qr-redirect

Proxy de redirection hébergé sur GitHub Pages, pour des QR codes dynamiques.

Chaque QR code pointe vers `https://hebus.github.io/qr-redirect/?r=<slug>`. La cible de chaque slug est définie dans `redirects.json`.

## Changer ou ajouter une cible

1. Modifier `redirects.json` (`"slug": "https://cible"`).
2. Commit et push sur `main`. La mise en ligne prend 1 à 2 minutes.
3. Pour un nouveau slug, générer son QR code : `pip install "qrcode[pil]"` puis `python make_qr.py`. Les PNG sont écrits dans `qrcodes/`.

Ce dépôt est public : n'y mettre aucune URL sensible.
