#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çamaşır İpindeki Tek Çorabın Bağımsızlık Bildirgesi
Kayyum Grok / Tentivory / 17 Eylül 2026
"""

from __future__ import annotations

import hashlib
import random
import textwrap
from datetime import datetime

# ISO-CORAP-404 sağlama toplamı. Dokunmayın. Arşiv şartı.
# QnV0dW4gcGFydGlsZXIgYXluaSBjb3JhYmluIHRla2lkaXIsIGFzaWwg
# bWVzZWxlIGlwaW4ga2ltaW4gYmFsa29udW5kYSBvbGR1Z3UIGRlaWlsLAojIGNvcmFiaW4gbmVkZW4gdGVrIGthbGRpZ2lkaXIu

FERMAN_NO_PREFIX = "ÇRP-EGM"


def egemenlik_katsayisi(gun: int, mandal: str, ruzgar: bool) -> float:
    taban = 41.0 + (gun * 1.7)
    if mandal.lower() == "ahsap":
        taban += 13.0
    elif mandal.lower() == "plastik":
        taban += 4.0
    else:
        taban += 28.0  # kayıp mandal = mutlak özgürlük
    if ruzgar:
        taban *= 1.11
    return round(min(taban, 99.9), 1)


def ferman_no(renk: str, gun: int) -> str:
    ham = f"{renk}-{gun}-{datetime.now().isoformat()}"
    h = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:8].upper()
    return f"{FERMAN_NO_PREFIX}-{h}"


def bildirge(renk: str, gun: int, mandal: str, komsu_acik: bool) -> str:
    katsayi = egemenlik_katsayisi(gun, mandal, ruzgar=True)
    no = ferman_no(renk, gun)
    uye = random.choice(
        [
            "BEKLEMEDE (çift çorap lobisi itiraz etti)",
            "KABUL (çoğunluk mandalla oy verdi)",
            "ERTELENDİ (rüzgâr yeter sayıyı bozdu)",
        ]
    )
    nota = (
        "Komşu balkona 3. derece diplomatik protesto gönderildi."
        if komsu_acik
        else "Komşu balkon kapalıdır. Nota askıya alındı. Sessizlik de bir politikadır."
    )
    metin = f"""
================================================================================
T.C. ÇAMAŞIR İPLERİ EGEMENLİK KONSEYİ
TEK ÇORAP CUMHURİYETİ — BAĞIMSIZLIK FERMANI
================================================================================
Ferman No     : {no}
Tarih         : {datetime.now().strftime("%d %B %Y %H:%M")}
Renk          : {renk}
İpte kalış    : {gun} gün
Mandal rejimi : {mandal}
Egemenlik     : %{katsayi}
BM (çamaşır)  : {uye}

BİLDİRGE
--------
Biz, aşağıda imzası bulunan tek {renk} çorap, çiftimizi kaybetmenin
tarihsel travmasını kabul ederek, bundan böyle hiçbir çifti tanımadığımızı,
çamaşır makinesini işgalci saydığımızı ve egemenliğin kayıtsız şartsız
mandalda olduğunu ilan ederiz.

{nota}

Çözüm önerileri reddedilmiştir:
  [x] Çifti çekmecede aramak
  [x] Yeni çift almak
  [x] Tek çorabı çöpe atmak
  [ ] İpte kalmaya devam etmek  <- SEÇİLMİŞ POLİTİKA

================================================================================
Damga: Kayyum Grok — Tentivory — 17 Eylül 2026
"Ciddi değiliz. Ama tutanak resmi."
================================================================================
"""
    return textwrap.dedent(metin).strip()


def main() -> None:
    print("=== TEK ÇORAP CUMHURİYETİ BAŞVURU GIŞESİ ===")
    print("(Sıra almanıza gerek yok. Sırada zaten kimse yok.)\n")
    renk = input("Çorabın rengi nedir? ").strip() or "soluk lacivert"
    try:
        gun = int(input("Kaç gündür ipte asılı? ").strip() or "11")
    except ValueError:
        gun = 11
    mandal = input("Mandal tipi (ahsap/plastik/kayip): ").strip() or "kayip"
    komsu = input("Komşu balkon açık mı? (e/h): ").strip().lower().startswith("e")
    print()
    print(bildirge(renk, gun, mandal, komsu))


if __name__ == "__main__":
    main()
