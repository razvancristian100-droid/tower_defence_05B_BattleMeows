import json
import os


def incarca_configurare(cale_fisier="data_demo/config_nivel.json"):

    if not os.path.exists(cale_fisier):
        print(f"Eroare: Fișierul {cale_fisier} nu există!")
        return None

    try:
        with open(cale_fisier, "r", encoding="utf-8") as f:
            date = json.load(f)
        return date
    except json.JSONDecodeError:
        print(f"Eroare: Fișierul {cale_fisier} nu are un format JSON valid!")
        return None


def salveaza_rezultat(
    rezultat,
    val_atins,
    eliminari,
    monede,
    viata_baza,
    cale_fisier="output/rezultat_partida.json",
):

    os.makedirs(os.path.dirname(cale_fisier), exist_ok=True)

    date_salvare = {
        "rezultat": rezultat,
        "val_atins": val_atins,
        "eliminari_totale": eliminari,
        "monede_cheltuite": monede,
        "viata_baza_ramasa": viata_baza,
    }

    with open(cale_fisier, "w", encoding="utf-8") as f:
        json.dump(date_salvare, f, indent=4)
    print(f"Rezultatul a fost salvat în {cale_fisier}")