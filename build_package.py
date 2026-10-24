"""Neon Pulse Icons: .evoxpack paketleyicisi ve evoX yerel kurulumu. Calistir: python build_package.py"""
import datetime, glob, json, os, shutil, zipfile

PACK_NAME = "Neon Pulse Icons"
VERSION = "1.0.0"
DESCRIPTION = "evoX ve Stream Deck cihazlari icin 100 adet ozenle hazirlanmis, yuksek kaliteli hareketli neon GIF ikon paketi (Acik/Kapali durumlari, Medya, OBS yayin, Sistem ve Sosyal kontroller)."
AUTHOR = {"id": "desktop-local-user", "name": "Yerel Kullanici"}


def friendly_name(fname):
    base = os.path.splitext(fname)[0]
    is_on = base.endswith("_on")
    is_off = base.endswith("_off")
    core = base.replace("_on", "").replace("_off", "")
    words = core.replace("_", " ").title().split()
    name = " ".join(words)
    if is_on:
        return f"{name} (Açık)"
    elif is_off:
        return f"{name} (Kapalı)"
    return name


def build():
    src_icons = sorted(glob.glob("icons/*.gif"))
    print(f"Toplam paketlenecek ikon: {len(src_icons)}")

    icon_assets = []
    for f in src_icons:
        fname = os.path.basename(f)
        slug = "neon-pulse-" + os.path.splitext(fname)[0].replace("_", "-")
        icon_assets.append({
            "id": slug,
            "name": friendly_name(fname),
            "path": f"assets/icons/{fname}"
        })

    manifest = {
        "name": PACK_NAME,
        "version": VERSION,
        "packageType": "icon_pack",
        "description": DESCRIPTION,
        "author": AUTHOR,
        "assets": {
            "icons": icon_assets
        }
    }

    # 1. .evoxpack ZIP paketini olustur
    pack_filename = f"{PACK_NAME}.evoxpack"
    with zipfile.ZipFile(pack_filename, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
        for f in src_icons:
            fname = os.path.basename(f)
            z.write(f, f"assets/icons/{fname}")

    print(f"Paket olusturuldu: {pack_filename} ({os.path.getsize(pack_filename) // 1024} KB)")

    # Kullanicinin Websites kok klasorune de kopyalayalim
    websites_dest = os.path.join(r"c:\Users\hfati\Desktop\Websites", pack_filename)
    if os.path.abspath(pack_filename) != os.path.abspath(websites_dest):
        shutil.copy2(pack_filename, websites_dest)
        print(f"Websites altina kopyalandi: {websites_dest}")

    # 2. evoX calisma dizinine de dogrudan kur
    appdata_icons = os.path.expandvars(r"%APPDATA%\evoX\icons")
    if os.path.exists(appdata_icons):
        target_dir = os.path.join(appdata_icons, PACK_NAME)
        os.makedirs(target_dir, exist_ok=True)
        for f in src_icons:
            shutil.copy2(f, target_dir)

        evoxpack_info = {
            "name": PACK_NAME,
            "version": VERSION,
            "packageType": "icon_pack",
            "installedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        with open(os.path.join(target_dir, "evoxpack-info.json"), "w", encoding="utf-8") as fp:
            json.dump(evoxpack_info, fp, indent=2, ensure_ascii=False)

        print(f"evoX uygulamasina kuruldu: {target_dir}")


if __name__ == "__main__":
    build()
