"""Génère un QR code PNG par slug défini dans redirects.json."""
import json
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_H

BASE_URL = "https://hebus.github.io/qr-redirect/"
ROOT = Path(__file__).parent
OUT_DIR = ROOT / "qrcodes"


def main() -> None:
    redirects = json.loads((ROOT / "redirects.json").read_text(encoding="utf-8"))
    OUT_DIR.mkdir(exist_ok=True)
    for slug in redirects:
        qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=20, border=4)
        qr.add_data(f"{BASE_URL}?r={slug}")
        qr.make(fit=True)
        path = OUT_DIR / f"{slug}.png"
        qr.make_image(fill_color="black", back_color="white").save(path)
        print(f"{slug} -> {path}")


if __name__ == "__main__":
    main()
