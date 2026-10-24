"""neon_gallery.html olusturucu betik.
evoX Neon Pulse 100 Hareketli GIF Ikon Paketi icin interaktif Stream Deck simülatörlü galeri web sitesi üretir.
"""
import glob, json, os

ICONS_DIR = r"c:\Users\hfati\Desktop\Websites\evox-neon-pack\icons"
OUTPUT_HTML = r"c:\Users\hfati\Desktop\Websites\neon_gallery.html"

KEYWORDS_MAP = {
    "airplane": "ucak airplane mode seyahat flight ucus",
    "bell": "zil bell bildirim notification alert alarm uyar",
    "bluetooth": "bluetooth bt kablosuz wireless baglanti eslesme",
    "bulb": "ampul bulb isik lamba light fikir idea aydinlatma",
    "camera": "kamera camera webcam goruntu video yayin obs",
    "chat": "sohbet chat mesaj message discord twitch yorum chatbox",
    "eye": "goz eye gorunum gizlilik privacy izle bak",
    "headphones": "kulaklik headphones headset ses music dinle kulak",
    "heart": "kalp heart begeni like favori can hp canlilik",
    "live": "canli live yayin stream on air yayinda yayinci kirmizi",
    "lock": "kilit lock guvenlik security kilitli sifre gizli",
    "mic": "mikrofon mic ses voice konusma mute sustur sesli",
    "monitor": "monitor ekran screen display masaustu goruntu pencere",
    "moon": "ay moon gece night karanlik dark uyku rahatsiz etme",
    "power": "guc power ac kapat acma kapatma switch tus baslat",
    "record": "kayit record rec video kayit obs baslat rec button",
    "repeat": "tekrar repeat loop dongu sarki tekrar replay",
    "shuffle": "karistir shuffle rastgele random mix sarki karisik",
    "star": "yildiz star favori favorite puan rating favorilere ekle",
    "sun": "gunes sun parlaklik brightness gunduz light aydinlik",
    "volume": "ses volume audio hoparlor speaker duzey ses seviyesi",
    "wifi": "wifi kablosuz internet ag network baglanti modem",
    "equalizer": "ekolayzer equalizer eq ses frekans muzik ritim dalga",
    "music": "muzik music nota sarki ses track melodi",
    "next": "sonraki next ileri forward sarki parca atla",
    "prev": "onceki prev previous geri sarki basa sar",
    "play": "oynat play baslat cal resume video sarki",
    "pause": "duraklat pause beklet durdur mola",
    "volume_up": "ses arttir volume up ses ac yuksek vol+",
    "volume_down": "ses azalt volume down ses kis alcak vol-",
    "clapper": "klaket clapper sahne film yayin cut video klip",
    "screenshot": "ekran goruntusu screenshot ss yakala capture foto",
    "battery": "pil battery batarya sarj guc enerji seviye",
    "bookmark": "yer imi bookmark kaydet favori isaret",
    "calendar": "takvim calendar tarih date gun ajanda etkinlik",
    "clock": "saat clock zaman time kronometre sure vakit",
    "cloud": "bulut cloud senkron depolama sync drive yedek",
    "code": "kod code yazilim dev programlama script html css js",
    "copy": "kopyala copy kopyalama panoya aktar duplicate",
    "download": "indir download yukleme kaydet al diske kaydet",
    "upload": "yukle upload gonder buluta yukle gonderim",
    "folder": "klasor folder dosya dizin arsiv belge",
    "globe": "dunya globe web internet tarayici site browser ag",
    "grid": "izgara grid menu duzen butonlar uygulamalar dashboard",
    "home": "ev home anasayfa baslangic giris kok dizin",
    "hourglass": "kum saati hourglass bekle wait sure geri sayim zaman",
    "key": "anahtar key sifre erisim password kilit yetki",
    "keyboard": "klavye keyboard tus yazi typing gaming mekanik",
    "link": "baglanti link url kopyala web hiperlink",
    "mail": "e-posta mail posta inbox gelen kutusu mesaj mektup",
    "refresh": "yenile refresh reload guncelle tekrar yukle f5",
    "search": "ara search arama bul mercek find query buyutec",
    "shield": "kalkan shield guvenlik koruma anti-virus guard savunma",
    "terminal": "terminal konsol console bash komut cmd shell powershell",
    "trash": "cop trash sil delete kaldir kutusu kutu copluk",
    "bolt": "yildirim bolt simsek elektrik enerji flash turbo yildiz",
    "chart": "grafik chart istatistik borsa analiz stats yukselis trend",
    "coin": "madeni para coin altin para bakiye crypto btc coin",
    "crown": "tac crown kral vip sampiyon lider bir numara gold",
    "diamond": "elmas diamond cevher nadir premium pirlanta gem",
    "fire": "ates fire alev hot populer trend combo yangin kombo",
    "gamepad": "oyun kolu gamepad joystick oyun gaming controller steam",
    "ghost": "hayalet ghost gizli gorunmez stealth pacman hortlak",
    "pin": "sabitle pin raptiye onemli tuttur pinle pano",
    "rain": "yagmur rain hava weather bulut damla su firtina",
    "rocket": "roket rocket firlat hizli boost launch uzay baslat",
    "smile": "gulumse smile emoji ifade mutlu happy neseli gulucuk",
    "snowflake": "kar tanesi snowflake soguk kis donma buz cool freeze",
    "target": "hedef target nisan aim fps crosshair atis nisan al",
    "trophy": "kupa trophy odul basari kazanan winner win sampiyonluk",
    "wand": "sihirli degnek wand efekt buyu sihir sihirbaz wizard parlama",
    "discord": "discord dc chat sunucu sesli sohbet ses kanali topluluk",
    "instagram": "instagram ig reels hikaye story sosyal medya post foto",
    "spotify": "spotify muzik sarki podcast playlist calma listesi sarki",
    "twitch": "twitch canli yayin yayinci stream kanal chat sub abone",
    "x": "x twitter tweet sosyal medya paylas gonderi post",
    "youtube": "youtube yt video abone izle kanal shorts yayin video"
}

CATEGORY_MAP = {
    # Stream & Broadcast
    "camera": "stream", "live": "stream", "mic": "stream", "headphones": "stream",
    "clapper": "stream", "screenshot": "stream", "record": "stream", "chat": "stream",
    
    # Media & Music
    "equalizer": "media", "music": "media", "next": "media", "pause": "media",
    "play": "media", "prev": "media", "volume_down": "media", "volume_up": "media",
    "repeat": "media", "shuffle": "media", "volume": "media",
    
    # Brands
    "discord": "brand", "instagram": "brand", "spotify": "brand",
    "twitch": "brand", "x": "brand", "youtube": "brand",
    
    # Gaming & Fun
    "bolt": "game", "coin": "game", "crown": "game", "diamond": "game",
    "fire": "game", "gamepad": "game", "ghost": "game", "rain": "game",
    "rocket": "game", "smile": "game", "snowflake": "game", "target": "game",
    "trophy": "game", "wand": "game",
    
    # System & Tools
    "battery": "system", "bookmark": "system", "calendar": "system", "clock": "system",
    "cloud": "system", "code": "system", "copy": "system", "download": "system",
    "folder": "system", "globe": "system", "grid": "system", "home": "system",
    "hourglass": "system", "key": "system", "keyboard": "system", "link": "system",
    "mail": "system", "refresh": "system", "search": "system", "shield": "system",
    "terminal": "system", "trash": "system", "upload": "system", "chart": "system", "pin": "system",
    
    # General Toggles
    "airplane": "toggle", "bell": "toggle", "bluetooth": "toggle", "bulb": "toggle",
    "eye": "toggle", "heart": "toggle", "lock": "toggle", "monitor": "system",
    "moon": "toggle", "power": "toggle", "star": "toggle", "sun": "toggle",
    "wifi": "toggle"
}

TITLE_TR = {
    "airplane": "Uçak Modu", "bell": "Bildirim Zili", "bluetooth": "Bluetooth",
    "bulb": "Işık / Ampul", "camera": "Webcam Kamera", "chat": "Yayın Sohbeti",
    "eye": "Görünürlük", "headphones": "Kulaklık", "heart": "Beğeni / Kalp",
    "live": "Canlı Yayın Rozeti", "lock": "Kilit Güvenlik", "mic": "Mikrofon",
    "monitor": "Monitör Ekranı", "moon": "Gece Modu", "power": "Güç Aç / Kapat",
    "record": "Kayıt (REC)", "repeat": "Şarkı Tekrarı", "shuffle": "Karışık Çal",
    "star": "Yıldız Favori", "sun": "Gündüz / Parlaklık", "volume": "Ses Açık / Kapalı",
    "wifi": "Wi-Fi Kablosuz", "equalizer": "Ekolayzer Spektrumu", "music": "Müzik Notası",
    "next": "Sonraki Şarkı", "pause": "Duraklat", "play": "Oynat / Başlat",
    "prev": "Önceki Şarkı", "volume_down": "Ses Kıs", "volume_up": "Ses Aç",
    "clapper": "Yayın Klaketi", "screenshot": "Ekran Görüntüsü", "battery": "Pil Durumu",
    "bookmark": "Yer İmi", "calendar": "Takvim", "clock": "Canlı Saat",
    "cloud": "Bulut Depolama", "code": "Kod Editörü", "copy": "Panoya Kopyala",
    "download": "Dosya İndir", "upload": "Dosya Yükle", "folder": "Klasör",
    "globe": "İnternet Tarayıcısı", "grid": "Uygulama Tablosu", "home": "Ana Sayfa",
    "hourglass": "Kum Saati Geri Sayım", "key": "Erişim Anahtarı", "keyboard": "Klavye",
    "link": "Web Bağlantısı", "mail": "Gelen Kutusu", "refresh": "Sayfayı Yenile",
    "search": "Hızlı Arama", "shield": "Güvenlik Kalkanı", "terminal": "Terminal Konsolu",
    "trash": "Çöp Kutusu", "bolt": "Yıldırım Turbo", "chart": "İstatistik Grafiği",
    "coin": "Altın Coin", "crown": "Kral Tacı", "diamond": "Elmas Mücevher",
    "fire": "Ateş Kombo", "gamepad": "Oyun Kolu Gamepad", "ghost": "Gizli Hayalet",
    "pin": "Raptiye İğnesi", "rain": "Yağmur Bulutu", "rocket": "Hızlı Roket",
    "smile": "Gülen Yüz", "snowflake": "Kar Tanesi", "target": "Hedef Nişangahı",
    "trophy": "Şampiyonluk Kupası", "wand": "Sihirli Değnek", "discord": "Discord",
    "instagram": "Instagram", "spotify": "Spotify", "twitch": "Twitch",
    "x": "X (Twitter)", "youtube": "YouTube"
}

def generate_gallery():
    files = sorted(glob.glob(os.path.join(ICONS_DIR, "*.gif")))
    all_icons = []
    
    # Identify pairs
    all_bases = set(os.path.splitext(os.path.basename(f))[0] for f in files)
    
    for f in files:
        fname = os.path.basename(f)
        base = os.path.splitext(fname)[0]
        size_kb = round(os.path.getsize(f) / 1024, 1)
        
        is_on = base.endswith("_on")
        is_off = base.endswith("_off")
        is_toggle = is_on or is_off
        core = base.replace("_on", "").replace("_off", "")
        
        # Twin finding
        twin_base = ""
        twin_file = ""
        if is_on:
            cand = f"{core}_off"
            if cand in all_bases:
                twin_base = cand
                twin_file = f"{cand}.gif"
        elif is_off:
            cand = f"{core}_on"
            if cand in all_bases:
                twin_base = cand
                twin_file = f"{cand}.gif"
                
        category = CATEGORY_MAP.get(core, "system")
        if is_toggle and category not in ("stream", "media"):
            category = "toggle"
            
        title_base = TITLE_TR.get(core, core.replace("_", " ").title())
        if is_on:
            display_title = f"{title_base} (Açık)"
            state_tag = "AÇIK"
            state_class = "state-on"
        elif is_off:
            display_title = f"{title_base} (Kapalı)"
            state_tag = "KAPALI"
            state_class = "state-off"
        else:
            display_title = title_base
            state_tag = "DÖNGÜ"
            state_class = "state-loop"
            
        kw = KEYWORDS_MAP.get(core, "") + f" {core} {base} {display_title.lower()}"
        
        all_icons.append({
            "id": base,
            "filename": fname,
            "core": core,
            "title": display_title,
            "title_base": title_base,
            "category": category,
            "is_on": is_on,
            "is_off": is_off,
            "is_toggle": is_toggle,
            "twin_base": twin_base,
            "twin_file": twin_file,
            "state_tag": state_tag,
            "state_class": state_class,
            "size_kb": size_kb,
            "rel_path": f"evox-neon-pack/icons/{fname}",
            "keywords": kw
        })
        
    icons_json = json.dumps(all_icons, ensure_ascii=False, indent=2)
    
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Neon Pulse - evoX Canlı GIF İkon Galerisi (100 Hareketli İkon)</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #07090e;
    --surface: #0f121c;
    --surface-hover: #161b2a;
    --surface-active: #1e2438;
    --border: #1f2538;
    --border-hover: #2e3752;
    --border-glow: rgba(0, 229, 255, 0.4);
    --cyan: #00e5ff;
    --cyan-glow: rgba(0, 229, 255, 0.25);
    --pink: #ff3cc8;
    --pink-glow: rgba(255, 60, 200, 0.25);
    --gold: #ffcd05;
    --green: #3cff8c;
    --green-glow: rgba(60, 255, 140, 0.25);
    --red: #ff4664;
    --red-glow: rgba(255, 70, 100, 0.25);
    --violet: #aa6eff;
    --text: #f8fafc;
    --text-dim: #cbd5e1;
    --muted: #8490a6;
  }}
  
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  
  body {{
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    padding: 32px 24px 120px;
    background-image: 
      radial-gradient(circle at 10% 10%, rgba(0, 229, 255, 0.08) 0%, transparent 45%),
      radial-gradient(circle at 90% 20%, rgba(255, 60, 200, 0.07) 0%, transparent 45%),
      radial-gradient(circle at 50% 80%, rgba(60, 255, 140, 0.05) 0%, transparent 50%);
    background-attachment: fixed;
    -webkit-font-smoothing: antialiased;
  }}
  
  .container {{ max-width: 1480px; margin: 0 auto; }}

  /* Top Bar & Header */
  header {{
    text-align: center;
    margin-bottom: 36px;
    position: relative;
  }}
  
  .badge-row {{
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-bottom: 18px;
    flex-wrap: wrap;
  }}
  
  .badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}
  
  .badge-neon {{
    background: rgba(0, 229, 255, 0.12);
    border: 1px solid rgba(0, 229, 255, 0.4);
    color: var(--cyan);
    box-shadow: 0 0 16px var(--cyan-glow);
  }}
  
  .badge-green {{
    background: rgba(60, 255, 140, 0.12);
    border: 1px solid rgba(60, 255, 140, 0.4);
    color: var(--green);
  }}
  
  .badge-pink {{
    background: rgba(255, 60, 200, 0.12);
    border: 1px solid rgba(255, 60, 200, 0.4);
    color: var(--pink);
  }}
  
  h1 {{
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 12px;
    background: linear-gradient(135deg, #ffffff 30%, var(--cyan) 75%, var(--pink) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  
  .subtitle {{
    color: var(--muted);
    font-size: 16px;
    max-width: 780px;
    margin: 0 auto 24px;
    line-height: 1.6;
  }}
  
  .top-actions {{
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 10px;
  }}
  
  .btn-top {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #121624;
    border: 1px solid #28324a;
    color: var(--text-dim);
    padding: 10px 20px;
    border-radius: 12px;
    font-size: 13px;
    font-weight: 700;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.2s;
  }}
  
  .btn-top:hover {{
    background: #1b2136;
    color: #fff;
    border-color: var(--cyan);
    box-shadow: 0 0 18px var(--cyan-glow);
    transform: translateY(-2px);
  }}
  
  .btn-top-accent {{
    background: linear-gradient(135deg, rgba(0, 229, 255, 0.2), rgba(255, 60, 200, 0.2));
    border-color: rgba(0, 229, 255, 0.5);
    color: #fff;
  }}

  /* Interactive Stream Deck Simulator */
  .deck-section {{
    background: linear-gradient(160deg, #131724 0%, #0a0c14 100%);
    border: 1px solid #232a3f;
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 40px;
    box-shadow: 0 20px 48px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.08);
  }}
  
  .deck-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
    flex-wrap: wrap;
    gap: 16px;
  }}
  
  .deck-title {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  
  .deck-title h2 {{
    font-size: 22px;
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.3px;
  }}
  
  .deck-hint {{
    font-size: 13px;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 2px;
  }}
  
  .deck-presets {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }}
  
  .btn-preset {{
    background: #161c2d;
    border: 1px solid #2a344d;
    color: #cbd5e1;
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }}
  
  .btn-preset:hover {{
    background: #202840;
    color: #fff;
    border-color: var(--cyan);
  }}
  
  /* Deck Chassis */
  .deck-center {{
    display: flex;
    justify-content: center;
    margin: 10px 0;
  }}
  
  .device-chassis {{
    background: radial-gradient(circle at 50% 15%, #181d2e 0%, #080a10 100%);
    border: 2px solid #28324a;
    border-radius: 24px;
    padding: 24px 28px;
    box-shadow: 0 24px 50px rgba(0, 0, 0, 0.8), inset 0 2px 4px rgba(255, 255, 255, 0.1);
    max-width: 100%;
    overflow-x: auto;
  }}
  
  .deck-grid {{
    display: grid;
    grid-template-columns: repeat(6, 96px);
    grid-template-rows: repeat(2, 96px);
    gap: 16px;
  }}
  
  @media (max-width: 768px) {{
    .deck-grid {{
      grid-template-columns: repeat(3, 88px);
      grid-template-rows: repeat(4, 88px);
    }}
  }}
  
  .deck-key {{
    width: 96px;
    height: 96px;
    background: #080a11;
    border: 2px solid #1a2030;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    cursor: pointer;
    overflow: hidden;
    user-select: none;
    transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: inset 0 0 14px rgba(0,0,0,0.85), 0 4px 12px rgba(0,0,0,0.5);
  }}
  
  @media (max-width: 768px) {{
    .deck-key {{ width: 88px; height: 88px; }}
  }}
  
  .deck-key:hover {{
    border-color: var(--cyan);
    box-shadow: 0 0 22px var(--cyan-glow), inset 0 0 10px rgba(0, 229, 255, 0.2);
    transform: translateY(-2px);
  }}
  
  .deck-key:active, .deck-key.pressing {{
    transform: scale(0.94);
    border-color: var(--pink);
    box-shadow: 0 0 24px var(--pink-glow);
  }}
  
  .deck-key.selected {{
    border-color: var(--cyan);
    box-shadow: 0 0 20px var(--cyan-glow);
  }}
  
  .deck-key img {{
    width: 62px;
    height: 62px;
    object-fit: contain;
    filter: drop-shadow(0 2px 10px rgba(0,0,0,0.7));
    pointer-events: none;
  }}
  
  .deck-key-label {{
    position: absolute;
    bottom: 5px;
    font-size: 9px;
    font-weight: 700;
    color: rgba(255,255,255,0.75);
    text-shadow: 0 1px 3px #000;
    letter-spacing: 0.3px;
    text-transform: uppercase;
    max-width: 86px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    pointer-events: none;
  }}
  
  .deck-key-toggle-badge {{
    position: absolute;
    top: 5px;
    right: 5px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    pointer-events: none;
  }}
  .badge-on {{ background: var(--green); box-shadow: 0 0 8px var(--green); }}
  .badge-off {{ background: var(--red); box-shadow: 0 0 8px var(--red); }}

  /* Filter & Search Bar */
  .filter-section {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 22px 26px;
    margin-bottom: 32px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }}
  
  .filter-top {{
    display: flex;
    gap: 16px;
    align-items: center;
    flex-wrap: wrap;
  }}
  
  .search-wrapper {{
    flex: 1;
    min-width: 280px;
    position: relative;
  }}
  
  .search-input {{
    width: 100%;
    padding: 14px 20px 14px 48px;
    border-radius: 12px;
    border: 1px solid var(--border);
    background: #090c14;
    color: #fff;
    font-size: 15px;
    outline: none;
    transition: all 0.2s;
  }}
  
  .search-input:focus {{
    border-color: var(--cyan);
    box-shadow: 0 0 0 3px rgba(0, 229, 255, 0.15);
  }}
  
  .search-icon {{
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--muted);
    font-size: 18px;
    pointer-events: none;
  }}
  
  .counter-pill {{
    font-size: 13px;
    color: var(--muted);
    font-weight: 600;
    background: #141926;
    padding: 10px 18px;
    border-radius: 12px;
    border: 1px solid var(--border);
    white-space: nowrap;
  }}
  .counter-pill strong {{ color: var(--cyan); }}
  
  /* Filter Tabs */
  .tabs-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }}
  
  .tab-btn {{
    padding: 8px 18px;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: #0d101a;
    color: var(--muted);
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.15s;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }}
  
  .tab-btn:hover {{
    background: var(--surface-hover);
    color: #fff;
    border-color: var(--border-hover);
  }}
  
  .tab-btn.active {{
    background: rgba(0, 229, 255, 0.15);
    color: var(--cyan);
    border-color: var(--cyan);
    box-shadow: 0 0 16px var(--cyan-glow);
  }}

  /* Quick Suggestion Chips */
  .chips-row {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    color: var(--muted);
  }}
  
  .chip {{
    padding: 4px 10px;
    background: #131724;
    border: 1px solid #22293d;
    border-radius: 6px;
    color: var(--text-dim);
    cursor: pointer;
    transition: all 0.15s;
  }}
  .chip:hover {{
    background: #1d2338;
    color: var(--cyan);
    border-color: var(--cyan);
  }}

  /* Main Gallery Grid */
  .gallery-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(136px, 1fr));
    gap: 16px;
  }}
  
  .icon-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 14px 10px 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    overflow: hidden;
  }}
  
  .icon-card:hover {{
    transform: translateY(-4px);
    background: var(--surface-hover);
    border-color: rgba(0, 229, 255, 0.5);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.5), 0 0 20px var(--cyan-glow);
  }}
  
  .img-wrapper {{
    width: 86px;
    height: 86px;
    background: #080a11;
    border: 1px solid #1a2030;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
    box-shadow: inset 0 0 14px rgba(0, 0, 0, 0.85);
    position: relative;
    overflow: hidden;
  }}
  
  .img-wrapper img {{
    width: 72px;
    height: 72px;
    object-fit: contain;
    filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.6));
  }}
  
  .icon-title {{
    font-size: 11px;
    font-weight: 700;
    color: #e2e8f0;
    text-align: center;
    line-height: 1.3;
    margin-bottom: 6px;
    max-width: 100%;
    word-break: break-word;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  
  .state-pill {{
    font-size: 9px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 6px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}
  
  .state-on {{
    background: rgba(60, 255, 140, 0.15);
    color: var(--green);
    border: 1px solid rgba(60, 255, 140, 0.4);
  }}
  
  .state-off {{
    background: rgba(255, 70, 100, 0.15);
    color: var(--red);
    border: 1px solid rgba(255, 70, 100, 0.4);
  }}
  
  .state-loop {{
    background: rgba(0, 229, 255, 0.15);
    color: var(--cyan);
    border: 1px solid rgba(0, 229, 255, 0.4);
  }}
  
  /* Card Overlay Actions */
  .card-actions {{
    display: flex;
    gap: 4px;
    margin-top: 8px;
    opacity: 0;
    transition: opacity 0.15s;
    width: 100%;
    justify-content: center;
  }}
  
  .icon-card:hover .card-actions {{
    opacity: 1;
  }}
  
  .btn-card-act {{
    background: #141926;
    border: 1px solid #28334d;
    color: var(--text-dim);
    padding: 4px 6px;
    border-radius: 6px;
    font-size: 10px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.15s;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }}
  
  .btn-card-act:hover {{
    background: #1e263a;
    color: #fff;
    border-color: var(--cyan);
  }}
  
  .btn-card-toggle {{
    background: rgba(0, 229, 255, 0.12);
    border-color: rgba(0, 229, 255, 0.4);
    color: var(--cyan);
  }}

  /* Modal Preview */
  .modal-overlay {{
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.85);
    backdrop-filter: blur(8px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    padding: 20px;
  }}
  
  .modal-box {{
    background: #0f121d;
    border: 1px solid #28334d;
    border-radius: 24px;
    max-width: 500px;
    width: 100%;
    padding: 28px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.9), 0 0 30px var(--cyan-glow);
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
  }}
  
  .modal-close {{
    position: absolute;
    top: 20px;
    right: 20px;
    background: #161b2a;
    border: 1px solid #28334d;
    color: var(--muted);
    width: 32px;
    height: 32px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.15s;
  }}
  .modal-close:hover {{ background: #242c44; color: #fff; }}
  
  .modal-preview-stage {{
    width: 256px;
    height: 256px;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 16px 0 20px;
    border: 2px solid #242c44;
    background: #000;
    transition: background 0.2s;
    box-shadow: inset 0 0 24px rgba(0,0,0,0.9), 0 10px 30px rgba(0,0,0,0.5);
  }}
  
  .modal-preview-stage img {{
    width: 200px;
    height: 200px;
    object-fit: contain;
  }}
  
  .bg-switcher {{
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
  }}
  
  .bg-dot {{
    width: 26px;
    height: 26px;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid #334155;
    transition: all 0.15s;
  }}
  .bg-dot.active {{ border-color: var(--cyan); transform: scale(1.15); }}
  
  .modal-info {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--muted);
    background: #080a10;
    padding: 10px 16px;
    border-radius: 10px;
    border: 1px solid #1a2030;
    width: 100%;
    margin-bottom: 20px;
    text-align: center;
  }}

  /* Guide Section */
  .guide-card {{
    background: linear-gradient(145deg, #121624, #0b0d14);
    border: 1px solid #232a3f;
    border-radius: 20px;
    padding: 28px;
    margin-top: 48px;
  }}
  
  .guide-title {{
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    color: #fff;
  }}
  
  .guide-steps {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
  }}
  
  .guide-step {{
    background: #090c14;
    border: 1px solid #1b2133;
    border-radius: 14px;
    padding: 18px;
  }}
  
  .guide-step-num {{
    font-size: 12px;
    font-weight: 800;
    color: var(--cyan);
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  
  .guide-step-text {{
    font-size: 13px;
    color: var(--text-dim);
    line-height: 1.5;
  }}

  /* Toast Notification */
  .toast {{
    position: fixed;
    bottom: 28px;
    right: 28px;
    background: #141926;
    border: 1px solid var(--cyan);
    color: #fff;
    padding: 14px 24px;
    border-radius: 14px;
    font-size: 14px;
    font-weight: 600;
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.8), 0 0 24px var(--cyan-glow);
    display: none;
    align-items: center;
    gap: 10px;
    z-index: 99999;
    animation: toastPop 0.25s ease-out;
  }}
  
  @keyframes toastPop {{
    from {{ opacity: 0; transform: translateY(20px) scale(0.95); }}
    to {{ opacity: 1; transform: translateY(0) scale(1); }}
  }}
</style>
</head>
<body>

<div class="container">
  <!-- Header -->
  <header>
    <div class="badge-row">
      <span class="badge badge-neon">⚡ evoX &amp; Stream Deck Suite</span>
      <span class="badge badge-green">● 100 Canlı GIF İkonu</span>
      <span class="badge badge-pink">★ Pürüzsüz Sonsuz Döngü</span>
    </div>
    <h1>Neon Pulse Canlı GIF Galerisi</h1>
    <p class="subtitle">
      evoX cihazı ve uygulaması için özel olarak tasarlanan 100 adet hareketli neon GIF ikonunu canlı olarak inceleyin. 
      Aşağıdaki <strong>Stream Deck Simülatörü</strong>'ne tıklayarak gerçek cihaz tuşundaki görünümünü ve Açık/Kapalı geçişlerini hemen test edebilirsiniz!
    </p>

    <div class="top-actions">
      <a href="Neon Pulse Icons.evoxpack" download class="btn-top btn-top-accent">
        <span>📦</span> evoX Paketini İndir (.evoxpack)
      </a>
      <a href="evox-neon-pack/icons_sheet.png" target="_blank" class="btn-top">
        <span>🖼️</span> 10x10 Tam Tabloyu Gör (PNG)
      </a>
      <button class="btn-top" onclick="copyEvoxPath()">
        <span>📋</span> evoX Klasör Yolunu Kopyala
      </button>
    </div>
  </header>

  <!-- Stream Deck Interactive Simulator -->
  <section class="deck-section">
    <div class="deck-header">
      <div class="deck-title">
        <span style="font-size: 28px;">🎮</span>
        <div>
          <h2>Canlı evoX / Stream Deck Simülatörü</h2>
          <span class="deck-hint">
            💡 Galeriden bir ikona tıklayarak tuşa atayın &bull; Atanmış Açık/Kapalı tuşuna basarak canlı durumu (ON ↔ OFF) değiştirin!
          </span>
        </div>
      </div>
      <div class="deck-presets">
        <button class="btn-preset" onclick="resetDeckPreset('streamer')">🎙️ Yayıncı Seti</button>
        <button class="btn-preset" onclick="resetDeckPreset('gaming')">⚡ Oyun &amp; Espor</button>
        <button class="btn-preset" onclick="resetDeckPreset('media')">🎵 Medya Seti</button>
        <button class="btn-preset" onclick="resetDeckPreset('system')">⚙️ Sistem Seti</button>
        <button class="btn-preset" onclick="clearDeck()">🗑️ Temizle</button>
      </div>
    </div>

    <div class="deck-center">
      <div class="device-chassis">
        <div class="deck-grid" id="deckGrid">
          <!-- 12 Keys generated by JavaScript -->
        </div>
      </div>
    </div>
  </section>

  <!-- Filter & Search Bar -->
  <section class="filter-section">
    <div class="filter-top">
      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="İkon ara (örn: mic, ses, canlı yayın, discord, wifi, kamera, pil)..." oninput="filterGallery()">
      </div>
      <div class="counter-pill">
        Gösterilen: <strong id="visibleCount">100</strong> / 100 İkon
      </div>
    </div>

    <div class="tabs-row" id="categoryTabs">
      <button class="tab-btn active" onclick="setCategory('all', this)">Tümü (100)</button>
      <button class="tab-btn" onclick="setCategory('toggle', this)">🔄 Açık / Kapalı Çiftleri (44)</button>
      <button class="tab-btn" onclick="setCategory('stream', this)">🎙️ Yayın &amp; OBS</button>
      <button class="tab-btn" onclick="setCategory('media', this)">🎵 Medya &amp; Ses</button>
      <button class="tab-btn" onclick="setCategory('system', this)">⚙️ Sistem &amp; Araçlar</button>
      <button class="tab-btn" onclick="setCategory('game', this)">🎮 Oyun &amp; Eğlence</button>
      <button class="tab-btn" onclick="setCategory('brand', this)">🌐 Markalar</button>
    </div>

    <div class="chips-row">
      <span style="font-weight: 700; color: #fff;">Hızlı Ara:</span>
      <span class="chip" onclick="quickSearch('mic')">🎙️ mic</span>
      <span class="chip" onclick="quickSearch('live')">🔴 live</span>
      <span class="chip" onclick="quickSearch('camera')">📹 camera</span>
      <span class="chip" onclick="quickSearch('volume')">🔊 volume</span>
      <span class="chip" onclick="quickSearch('discord')">💬 discord</span>
      <span class="chip" onclick="quickSearch('twitch')">🟣 twitch</span>
      <span class="chip" onclick="quickSearch('gamepad')">🎮 gamepad</span>
      <span class="chip" onclick="quickSearch('battery')">🔋 battery</span>
      <span class="chip" onclick="quickSearch('wifi')">📶 wifi</span>
      <span class="chip" onclick="quickSearch('lock')">🔒 lock</span>
      <span class="chip" onclick="quickSearch('')">✖ Temizle</span>
    </div>
  </section>

  <!-- Main Grid -->
  <main class="gallery-grid" id="galleryGrid">
    <!-- Populated by JavaScript -->
  </main>

  <!-- Guide / How to use with evoX -->
  <section class="guide-card">
    <div class="guide-title">
      <span>🚀</span> evoX Masaüstü Uygulaması ile Kullanım Rehberi
    </div>
    <div class="guide-steps">
      <div class="guide-step">
        <div class="guide-step-num">1. Paket Dosyasını Edinin</div>
        <div class="guide-step-text">
          Yukarıdaki <strong>"evoX Paketini İndir"</strong> butonuna tıklayarak <code>Neon Pulse Icons.evoxpack</code> arşivini bilgisayarınıza kaydedin.
        </div>
      </div>
      <div class="guide-step">
        <div class="guide-step-num">2. evoX Uygulamasına Tanıtın</div>
        <div class="guide-step-text">
          evoX uygulamasında <strong>Icon Library ➔ Import Pack</strong> diyerek paketi seçin ya da doğrudan <code>%APPDATA%\evoX\icons</code> dizinine çıkartın.
        </div>
      </div>
      <div class="guide-step">
        <div class="guide-step-num">3. Tuşlara Atayın &amp; Keyfini Çıkarın</div>
        <div class="guide-step-text">
          evoX arayüzünde "Neon Pulse Icons" sekmesinden istediğiniz ikonu cihazınızın tuşlarına sürükleyip bırakın. Açık ve Kapalı durumlarını kolayca eşleyin!
        </div>
      </div>
    </div>
  </section>
</div>

<!-- Modal Detail Inspector -->
<div class="modal-overlay" id="modalOverlay" onclick="closeModal(event)">
  <div class="modal-box" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal()">&times;</button>
    <h3 id="modalTitle" style="font-size: 20px; font-weight: 800; color: #fff; margin-bottom: 4px;">İkon Adı</h3>
    <span id="modalCategory" class="state-pill state-loop" style="margin-bottom: 12px;">DÖNGÜ</span>

    <div class="modal-preview-stage" id="modalStage">
      <img id="modalImg" src="" alt="Preview">
    </div>

    <div class="bg-switcher">
      <div class="bg-dot active" style="background: #000000;" onclick="changeModalBg('#000000', this)" title="OLED Siyah"></div>
      <div class="bg-dot" style="background: #0f121d;" onclick="changeModalBg('#0f121d', this)" title="Koyu Lacivert"></div>
      <div class="bg-dot" style="background: #1e2438;" onclick="changeModalBg('#1e2438', this)" title="Stream Deck Gri"></div>
      <div class="bg-dot" style="background: #f1f5f9;" onclick="changeModalBg('#f1f5f9', this)" title="Açık Mod"></div>
    </div>

    <div class="modal-info" id="modalInfo">
      256x256 px &bull; 36 Kare @ 40ms &bull; Kusursuz Döngü
    </div>

    <div style="display: flex; gap: 10px; width: 100%;">
      <button class="btn-top btn-top-accent" style="flex: 1; justify-content: center;" id="modalDownloadBtn">
        💾 GIF İndir
      </button>
      <button class="btn-top" style="flex: 1; justify-content: center;" id="modalAssignBtn">
        🎮 Simülatöre Ata
      </button>
    </div>
  </div>
</div>

<!-- Toast Box -->
<div class="toast" id="toastBox">
  <span id="toastIcon">✨</span>
  <span id="toastMsg">İşlem yapıldı!</span>
</div>

<script>
  // Icon Database
  const ICONS = {icons_json};

  // Audio Synth for mechanical switch sound
  let audioCtx = null;
  function playClickSound(freq = 600, duration = 0.04) {{
    try {{
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(120, audioCtx.currentTime + duration);
      gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start();
      osc.stop(audioCtx.currentTime + duration);
    }} catch(e) {{}}
  }}

  // Deck State (12 Slots)
  let deckSlots = new Array(12).fill(null);
  let selectedDeckSlot = 0;
  let activeCategory = 'all';
  let searchQuery = '';

  // Initial preset
  const PRESETS = {{
    streamer: ['mic_on', 'headphones_on', 'live_on', 'camera_on', 'discord', 'twitch', 'clapper', 'volume_up', 'volume_down', 'screenshot', 'chat_on', 'bell_on'],
    gaming: ['gamepad', 'trophy', 'target', 'discord', 'fire', 'bolt', 'crown', 'diamond', 'spotify', 'volume_up', 'volume_down', 'power_on'],
    media: ['play', 'pause', 'next', 'prev', 'equalizer', 'music', 'volume_up', 'volume_down', 'shuffle_on', 'repeat_on', 'headphones_on', 'spotify'],
    system: ['battery', 'clock', 'calendar', 'wifi_on', 'bluetooth_on', 'lock_on', 'terminal', 'search', 'folder', 'copy', 'download', 'trash']
  }};

  function initDeck() {{
    const list = PRESETS.streamer;
    list.forEach((id, i) => {{
      const ic = ICONS.find(x => x.id === id);
      if (ic) deckSlots[i] = {{ ...ic }};
    }});
    renderDeck();
  }}

  function renderDeck() {{
    const grid = document.getElementById('deckGrid');
    grid.innerHTML = '';

    deckSlots.forEach((slot, index) => {{
      const keyEl = document.createElement('div');
      keyEl.className = 'deck-key' + (index === selectedDeckSlot ? ' selected' : '');
      
      if (slot) {{
        const isToggle = slot.is_toggle;
        const toggleBadge = slot.is_on ? '<span class="deck-key-toggle-badge badge-on"></span>' :
                            (slot.is_off ? '<span class="deck-key-toggle-badge badge-off"></span>' : '');

        keyEl.innerHTML = `
          <img src="${{slot.rel_path}}" alt="${{slot.title}}">
          <span class="deck-key-label">${{slot.title_base || slot.title}}</span>
          ${{toggleBadge}}
        `;
        keyEl.onclick = (e) => onDeckKeyClick(index, e);
      }} else {{
        keyEl.innerHTML = `
          <span style="font-size:22px; color:#28334d;">+</span>
          <span class="deck-key-label" style="color:#475569;">#${{index + 1}} BOŞ</span>
        `;
        keyEl.onclick = () => selectDeckSlot(index);
      }}

      grid.appendChild(keyEl);
    }});
  }}

  function selectDeckSlot(index) {{
    selectedDeckSlot = index;
    playClickSound(450, 0.03);
    renderDeck();
    showToast('🎮', `Simülatör Yuvası #${{index + 1}} seçildi. Galeriden bir ikona tıklayın.`);
  }}

  function onDeckKeyClick(index, e) {{
    const slot = deckSlots[index];
    if (!slot) return;

    // Trigger visual press effect
    const keys = document.querySelectorAll('.deck-key');
    if (keys[index]) {{
      keys[index].classList.add('pressing');
      setTimeout(() => keys[index].classList.remove('pressing'), 150);
    }}

    // Check if slot has twin toggle state
    if (slot.is_toggle && slot.twin_base) {{
      const twin = ICONS.find(x => x.id === slot.twin_base);
      if (twin) {{
        deckSlots[index] = {{ ...twin }};
        playClickSound(slot.is_on ? 320 : 750, 0.05); // low freq when turning off, high when turning on
        renderDeck();
        showToast(twin.is_on ? '🟢' : '🔴', `${{twin.title_base}}: ${{twin.state_tag}} durumuna geçti!`);
        return;
      }}
    }}

    // If single state or clicked again, play tap sound & select slot
    playClickSound(520, 0.03);
    selectedDeckSlot = index;
    renderDeck();
    showToast('⚡', `"${{slot.title}}" tetiklendi.`);
  }}

  function assignToDeck(icon) {{
    deckSlots[selectedDeckSlot] = {{ ...icon }};
    playClickSound(800, 0.04);
    renderDeck();
    showToast('🚀', `"${{icon.title}}" #${{selectedDeckSlot + 1}} numaralı tuşa yerleştirildi!`);
    
    // Auto advance to next slot
    selectedDeckSlot = (selectedDeckSlot + 1) % deckSlots.length;
    renderDeck();
  }}

  function resetDeckPreset(type) {{
    const list = PRESETS[type] || [];
    deckSlots = new Array(12).fill(null);
    list.forEach((id, i) => {{
      const ic = ICONS.find(x => x.id === id);
      if (ic && i < 12) deckSlots[i] = {{ ...ic }};
    }});
    playClickSound(650, 0.05);
    renderDeck();
    showToast('⚡', `${{type.toUpperCase()}} hazır seti simülatöre yüklendi!`);
  }}

  function clearDeck() {{
    deckSlots = new Array(12).fill(null);
    playClickSound(300, 0.05);
    renderDeck();
    showToast('🗑️', 'Tüm simülatör tuşları temizlendi.');
  }}

  // Gallery Rendering
  function renderGallery() {{
    const grid = document.getElementById('galleryGrid');
    grid.innerHTML = '';

    const q = searchQuery.toLowerCase().trim();
    const filtered = ICONS.filter(item => {{
      const matchCat = (activeCategory === 'all') || 
                       (activeCategory === 'toggle' && item.is_toggle) ||
                       (item.category === activeCategory);

      const matchSearch = !q || item.keywords.toLowerCase().includes(q);
      return matchCat && matchSearch;
    }});

    document.getElementById('visibleCount').textContent = filtered.length;

    filtered.forEach(icon => {{
      const card = document.createElement('div');
      card.className = 'icon-card';
      
      let toggleBtnHtml = '';
      if (icon.is_toggle && icon.twin_base) {{
        toggleBtnHtml = `
          <button class="btn-card-act btn-card-toggle" onclick="swapCardState('${{icon.id}}', event)" title="Açık/Kapalı Durumunu Çevir">
            ⇄ Çevir
          </button>
        `;
      }}

      card.innerHTML = `
        <div class="img-wrapper" onclick="assignToDeck(ICONS.find(x => x.id === '${{icon.id}}'))">
          <img src="${{icon.rel_path}}" alt="${{icon.title}}" loading="lazy" id="img_${{icon.id}}">
        </div>
        <div class="icon-title">${{icon.title}}</div>
        <span class="state-pill ${{icon.state_class}}">${{icon.state_tag}}</span>
        <div class="card-actions">
          ${{toggleBtnHtml}}
          <button class="btn-card-act" onclick="openModal('${{icon.id}}', event)" title="Büyüt & İncele">🔍</button>
          <button class="btn-card-act" onclick="copyFilename('${{icon.filename}}', event)" title="Dosya Adını Kopyala">📋</button>
          <button class="btn-card-act" onclick="downloadIcon('${{icon.rel_path}}', '${{icon.filename}}', event)" title="GIF İndir">💾</button>
        </div>
      `;

      card.onclick = (e) => {{
        if (!e.target.closest('button')) {{
          assignToDeck(icon);
        }}
      }};

      grid.appendChild(card);
    }});
  }}

  function swapCardState(iconId, e) {{
    if (e) e.stopPropagation();
    const cur = ICONS.find(x => x.id === iconId);
    if (!cur || !cur.twin_base) return;
    const twin = ICONS.find(x => x.id === cur.twin_base);
    if (!twin) return;

    playClickSound(twin.is_on ? 700 : 350, 0.04);
    
    // Quick in-place update if visible
    const imgEl = document.getElementById('img_' + iconId);
    if (imgEl) {{
      imgEl.src = twin.rel_path;
      imgEl.id = 'img_' + twin.id;
    }}
    showToast(twin.is_on ? '🟢' : '🔴', `${{twin.title}}: Canlı geçiş yapıldı!`);
  }}

  function filterGallery() {{
    searchQuery = document.getElementById('searchInput').value;
    renderGallery();
  }}

  function setCategory(cat, btn) {{
    activeCategory = cat;
    document.querySelectorAll('#categoryTabs .tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderGallery();
  }}

  function quickSearch(word) {{
    document.getElementById('searchInput').value = word;
    searchQuery = word;
    renderGallery();
  }}

  function copyFilename(fn, e) {{
    if (e) e.stopPropagation();
    navigator.clipboard.writeText(fn).then(() => {{
      showToast('📋', `"${{fn}}" panoya kopyalandı!`);
    }}).catch(() => {{
      showToast('📄', fn);
    }});
  }}

  function copyEvoxPath() {{
    const p = `%APPDATA%\\\\evoX\\\\icons\\\\Neon Pulse Icons`;
    navigator.clipboard.writeText(p).then(() => {{
      showToast('📁', `evoX klasör yolu panoya kopyalandı!`);
    }});
  }}

  function downloadIcon(path, fn, e) {{
    if (e) e.stopPropagation();
    const a = document.createElement('a');
    a.href = path;
    a.download = fn;
    a.click();
    showToast('💾', `"${{fn}}" indiriliyor...`);
  }}

  // Modal Inspector
  let currentModalIcon = null;
  function openModal(iconId, e) {{
    if (e) e.stopPropagation();
    const ic = ICONS.find(x => x.id === iconId);
    if (!ic) return;
    currentModalIcon = ic;

    document.getElementById('modalTitle').textContent = ic.title;
    const catBadge = document.getElementById('modalCategory');
    catBadge.textContent = ic.state_tag;
    catBadge.className = 'state-pill ' + ic.state_class;
    
    document.getElementById('modalImg').src = ic.rel_path;
    document.getElementById('modalInfo').textContent = `${{ic.filename}} &bull; 256x256 px &bull; ${{ic.size_kb}} KB &bull; 36 Kare @ 40ms`;

    document.getElementById('modalDownloadBtn').onclick = () => downloadIcon(ic.rel_path, ic.filename);
    document.getElementById('modalAssignBtn').onclick = () => {{
      assignToDeck(ic);
      closeModal();
    }};

    document.getElementById('modalOverlay').style.display = 'flex';
  }}

  function closeModal(e) {{
    if (e && e.target !== e.currentTarget && !e.target.classList.contains('modal-close')) return;
    document.getElementById('modalOverlay').style.display = 'none';
  }}

  function changeModalBg(color, dot) {{
    document.getElementById('modalStage').style.background = color;
    document.querySelectorAll('.bg-dot').forEach(d => d.classList.remove('active'));
    if (dot) dot.classList.add('active');
  }}

  // Toast Box
  let toastTimer = null;
  function showToast(icon, msg) {{
    const toast = document.getElementById('toastBox');
    document.getElementById('toastIcon').textContent = icon;
    document.getElementById('toastMsg').textContent = msg;
    toast.style.display = 'flex';
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {{
      toast.style.display = 'none';
    }}, 2800);
  }}

  // Keyboard shortcut (Escape closes modal)
  window.addEventListener('keydown', (e) => {{
    if (e.key === 'Escape') closeModal();
  }});

  // Init on load
  window.addEventListener('DOMContentLoaded', () => {{
    initDeck();
    renderGallery();
  }});
</script>

</body>
</html>
"""
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Başarıyla güncellendi: {OUTPUT_HTML} ({len(all_icons)} ikon)")

if __name__ == "__main__":
    generate_gallery()
