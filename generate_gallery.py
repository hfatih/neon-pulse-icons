"""neon_gallery.html uretici betik. Calistir: python generate_gallery.py"""
import glob, json, os

ICONS_DIR = r"c:\Users\hfati\Desktop\Websites\evox-neon-pack\icons"
OUTPUT_HTML = r"c:\Users\hfati\Desktop\Websites\neon_gallery.html"

CATEGORIES = {
    "toggle": "Açık / Kapalı Durumları",
    "media": "Medya & Ses",
    "stream": "Yayın & OBS",
    "system": "Sistem & Araçlar",
    "game": "Oyun & Eğlence",
    "brand": "Markalar & Platformlar"
}

ICON_CATEGORY_MAP = {
    # Toggles
    "airplane": "toggle", "bell": "toggle", "bluetooth": "toggle", "bulb": "toggle",
    "camera": "stream", "chat": "toggle", "eye": "toggle", "headphones": "stream",
    "heart": "toggle", "live": "stream", "lock": "toggle", "mic": "stream",
    "monitor": "stream", "moon": "toggle", "power": "toggle", "record": "stream",
    "repeat": "media", "shuffle": "media", "star": "toggle", "sun": "toggle",
    "volume": "media", "wifi": "toggle",
    
    # Media
    "equalizer": "media", "music": "media", "next": "media", "pause": "media",
    "play": "media", "prev": "media", "volume_down": "media", "volume_up": "media",
    
    # Stream
    "clapper": "stream", "screenshot": "stream",
    
    # System
    "battery": "system", "bookmark": "system", "calendar": "system", "clock": "system",
    "cloud": "system", "code": "system", "copy": "system", "download": "system",
    "folder": "system", "globe": "system", "grid": "system", "home": "system",
    "hourglass": "system", "key": "system", "keyboard": "system", "link": "system",
    "mail": "system", "refresh": "system", "search": "system", "shield": "system",
    "terminal": "system", "trash": "system", "upload": "system",
    
    # Game / Fun
    "bolt": "game", "chart": "system", "coin": "game", "crown": "game",
    "diamond": "game", "fire": "game", "gamepad": "game", "ghost": "game",
    "pin": "system", "rain": "game", "rocket": "game", "smile": "game",
    "snowflake": "game", "target": "game", "trophy": "game", "wand": "game",
    
    # Brand
    "discord": "brand", "instagram": "brand", "spotify": "brand",
    "twitch": "brand", "x": "brand", "youtube": "brand"
}

def build_gallery():
    files = sorted(glob.glob(os.path.join(ICONS_DIR, "*.gif")))
    icons_data = []

    for f in files:
        fname = os.path.basename(f)
        base = os.path.splitext(fname)[0]
        is_on = base.endswith("_on")
        is_off = base.endswith("_off")
        core = base.replace("_on", "").replace("_off", "")
        
        cat = ICON_CATEGORY_MAP.get(core, "system")
        if (is_on or is_off) and cat not in ("stream", "media"):
            cat = "toggle"

        title_parts = core.replace("_", " ").title().split()
        title = " ".join(title_parts)
        state_tag = "AÇIK" if is_on else ("KAPALI" if is_off else "DÖNGÜ")
        state_class = "state-on" if is_on else ("state-off" if is_off else "state-loop")

        icons_data.append({
            "filename": fname,
            "base": base,
            "core": core,
            "title": title,
            "category": cat,
            "is_on": is_on,
            "is_off": is_off,
            "state_tag": state_tag,
            "state_class": state_class,
            "rel_path": f"evox-neon-pack/icons/{fname}"
        })

    json_data = json.dumps(icons_data, ensure_ascii=False, indent=2)

    html_content = f"""<!DOCTYPE html>
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
    --border: #1f2538;
    --border-glow: rgba(0, 229, 255, 0.3);
    --cyan: #00e5ff;
    --pink: #ff3cc8;
    --gold: #ffcd05;
    --green: #3cff8c;
    --orange: #ff8c1e;
    --violet: #aa6eff;
    --red: #ff4664;
    --text: #f8fafc;
    --muted: #8b95a8;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    padding: 32px 20px 100px;
    background-image: 
      radial-gradient(circle at 15% 15%, rgba(0, 229, 255, 0.08) 0%, transparent 40%),
      radial-gradient(circle at 85% 25%, rgba(255, 60, 200, 0.07) 0%, transparent 45%),
      radial-gradient(circle at 50% 85%, rgba(60, 255, 140, 0.05) 0%, transparent 50%);
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
    gap: 10px;
    margin-bottom: 16px;
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
    box-shadow: 0 0 16px rgba(0, 229, 255, 0.2);
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
    max-width: 720px;
    margin: 0 auto 28px;
    line-height: 1.6;
  }}

  /* Interactive Stream Deck Simulator */
  .deck-simulator {{
    background: linear-gradient(160deg, #131724 0%, #0a0c14 100%);
    border: 1px solid #232a3f;
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 40px;
    box-shadow: 0 20px 48px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.08);
    position: relative;
    overflow: hidden;
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
    gap: 12px;
  }}
  .deck-title h2 {{
    font-size: 20px;
    font-weight: 700;
    color: #fff;
  }}
  .deck-hint {{
    font-size: 13px;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .deck-controls {{
    display: flex;
    gap: 10px;
  }}
  .btn-deck {{
    background: #1b2133;
    border: 1px solid #2f3954;
    color: #cbd5e1;
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
  }}
  .btn-deck:hover {{
    background: #252d45;
    color: #fff;
    border-color: var(--cyan);
  }}

  /* Deck Device Frame */
  .device-chassis {{
    background: radial-gradient(circle at 50% 20%, #171c2c 0%, #080a11 100%);
    border: 2px solid #242c44;
    border-radius: 20px;
    padding: 24px;
    display: inline-block;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.8), inset 0 2px 4px rgba(255, 255, 255, 0.1);
    max-width: 100%;
    overflow-x: auto;
  }}
  .deck-grid {{
    display: grid;
    grid-template-columns: repeat(6, 92px);
    gap: 14px;
  }}
  @media (max-width: 768px) {{
    .deck-grid {{ grid-template-columns: repeat(3, 86px); }}
  }}
  .deck-key {{
    width: 92px;
    height: 92px;
    background: #090b10;
    border: 2px solid #1a2030;
    border-radius: 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    cursor: pointer;
    overflow: hidden;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: inset 0 0 12px rgba(0,0,0,0.8), 0 4px 10px rgba(0,0,0,0.5);
  }}
  .deck-key:hover {{
    border-color: var(--cyan);
    box-shadow: 0 0 20px rgba(0, 229, 255, 0.3), inset 0 0 8px rgba(0, 229, 255, 0.2);
    transform: translateY(-2px);
  }}
  .deck-key.active {{
    border-color: var(--pink);
    box-shadow: 0 0 24px rgba(255, 60, 200, 0.4);
  }}
  .deck-key img {{
    width: 60px;
    height: 60px;
    object-fit: contain;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.6));
  }}
  .deck-key-label {{
    position: absolute;
    bottom: 4px;
    font-size: 9px;
    font-weight: 700;
    color: rgba(255,255,255,0.7);
    text-shadow: 0 1px 2px #000;
    letter-spacing: 0.3px;
    text-transform: uppercase;
    max-width: 84px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }}

  /* Filter & Search Bar */
  .filter-section {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 20px 24px;
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
    background: #151a28;
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
    font-weight: 600;
    cursor: pointer;
    transition: all 0.15s;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }}
  .tab-btn:hover {{
    background: var(--surface-hover);
    color: #fff;
    border-color: #2e3752;
  }}
  .tab-btn.active {{
    background: rgba(0, 229, 255, 0.15);
    color: var(--cyan);
    border-color: var(--cyan);
    box-shadow: 0 0 16px rgba(0, 229, 255, 0.2);
  }}

  /* Main Grid */
  .gallery-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(132px, 1fr));
    gap: 14px;
  }}
  .icon-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 16px 10px 12px;
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
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 229, 255, 0.2);
  }}
  .icon-card.highlight {{
    border-color: var(--pink);
    box-shadow: 0 0 24px rgba(255, 60, 200, 0.4);
  }}
  .img-wrapper {{
    width: 84px;
    height: 84px;
    background: #080a11;
    border: 1px solid #1a2030;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
    box-shadow: inset 0 0 12px rgba(0, 0, 0, 0.8);
    position: relative;
    overflow: hidden;
  }}
  .img-wrapper img {{
    width: 72px;
    height: 72px;
    object-fit: contain;
    filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.5));
  }}
  .icon-title {{
    font-size: 12px;
    font-weight: 700;
    color: #e2e8f0;
    text-align: center;
    line-height: 1.3;
    margin-bottom: 6px;
    max-width: 100%;
    word-break: break-word;
  }}
  .state-pill {{
    font-size: 9px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 6px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
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
  .card-action-hint {{
    font-size: 10px;
    color: var(--muted);
    margin-top: 6px;
    opacity: 0;
    transition: opacity 0.15s;
  }}
  .icon-card:hover .card-action-hint {{ opacity: 1; }}

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
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.8), 0 0 24px rgba(0, 229, 255, 0.3);
    display: none;
    align-items: center;
    gap: 10px;
    z-index: 9999;
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
  <header>
    <div class="badge-row">
      <span class="badge badge-neon">⚡ evoX & Stream Deck Suite</span>
      <span class="badge badge-green">● 100 Canlı GIF İkonu</span>
      <span class="badge badge-pink">★ Pürüzsüz Sonsuz Döngü</span>
    </div>
    <h1>Neon Pulse Canlı GIF Galerisi</h1>
    <p class="subtitle">
      evoX cihazı ve uygulaması için özel olarak tasarlanan 100 adet hareketli neon GIF ikonunu canlı olarak inceleyin. 
      Aşağıdaki <strong>Stream Deck Simülatörü</strong>'ne tıklayarak gerçek cihaz tuşundaki görünümünü hemen test edebilirsiniz!
    </p>
  </header>

  <!-- Interactive Stream Deck Simulator -->
  <section class="deck-simulator">
    <div class="deck-header">
      <div class="deck-title">
        <span style="font-size: 24px;">🎮</span>
        <div>
          <h2>Canlı evoX / Stream Deck Simülatörü</h2>
          <span class="deck-hint">Aşağıdaki galeriden herhangi bir ikona tıklayın &bull; Seçili tuş yuvasına anında canlı yerleşsin</span>
        </div>
      </div>
      <div class="deck-controls">
        <button class="btn-deck" onclick="resetDeckPreset('streamer')">🎙️ Yayıncı Seti</button>
        <button class="btn-deck" onclick="resetDeckPreset('gaming')">⚡ Oyun Seti</button>
        <button class="btn-deck" onclick="resetDeckPreset('media')">🎵 Medya Seti</button>
        <button class="btn-deck" onclick="clearDeck()">Temizle</button>
      </div>
    </div>

    <div style="text-align: center;">
      <div class="device-chassis">
        <div class="deck-grid" id="deckGrid">
          <!-- 12 Key slots generated by JS -->
        </div>
      </div>
    </div>
  </section>

  <!-- Filters & Search -->
  <section class="filter-section">
    <div class="filter-top">
      <div class="search-wrapper">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="İkon ara (örn: mic, live, play, volume, discord, camera, battery)..." oninput="filterGallery()">
      </div>
      <div class="counter-pill">
        Gösterilen: <strong id="visibleCount">100</strong> / 100 İkon
      </div>
    </div>

    <div class="tabs-row" id="categoryTabs">
      <button class="tab-btn active" onclick="setCategory('all', this)">Tümü (100)</button>
      <button class="tab-btn" onclick="setCategory('toggle', this)">🔄 Açık / Kapalı Çiftleri</button>
      <button class="tab-btn" onclick="setCategory('stream', this)">🎙️ Yayın & OBS</button>
      <button class="tab-btn" onclick="setCategory('media', this)">🎵 Medya & Ses</button>
      <button class="tab-btn" onclick="setCategory('system', this)">⚙️ Sistem & Araçlar</button>
      <button class="tab-btn" onclick="setCategory('game', this)">🎮 Oyun & Eğlence</button>
      <button class="tab-btn" onclick="setCategory('brand', this)">🌐 Markalar</button>
    </div>
  </section>

  <!-- Main Grid -->
  <main class="gallery-grid" id="galleryGrid">
    <!-- Populated by JavaScript -->
  </main>
</div>

<!-- Toast Notification -->
<div class="toast" id="toastBox">
  <span id="toastIcon">✨</span>
  <span id="toastMsg">İkon adı kopyalandı!</span>
</div>

<script>
  const ICONS = {json_data};

  let activeCategory = 'all';
  let searchQuery = '';
  let selectedDeckSlot = 0;

  // Deck slots state
  const deckSlots = [
    {{ id: 'mic_on', name: 'Mic On', file: 'mic_on.gif' }},
    {{ id: 'headphones_on', name: 'Headphones', file: 'headphones_on.gif' }},
    {{ id: 'live_on', name: 'Live', file: 'live_on.gif' }},
    {{ id: 'camera_on', name: 'Camera', file: 'camera_on.gif' }},
    {{ id: 'discord', name: 'Discord', file: 'discord.gif' }},
    {{ id: 'youtube', name: 'YouTube', file: 'youtube.gif' }},
    {{ id: 'volume_up', name: 'Vol Up', file: 'volume_up.gif' }},
    {{ id: 'volume_down', name: 'Vol Down', file: 'volume_down.gif' }},
    {{ id: 'play', name: 'Play', file: 'play.gif' }},
    {{ id: 'next', name: 'Next', file: 'next.gif' }},
    {{ id: 'equalizer', name: 'Equalizer', file: 'equalizer.gif' }},
    {{ id: 'power_on', name: 'Power', file: 'power_on.gif' }}
  ];

  function renderDeck() {{
    const grid = document.getElementById('deckGrid');
    grid.innerHTML = '';
    deckSlots.forEach((slot, index) => {{
      const keyEl = document.createElement('div');
      keyEl.className = 'deck-key' + (index === selectedDeckSlot ? ' active' : '');
      keyEl.onclick = () => selectDeckSlot(index);
      
      if (slot && slot.file) {{
        keyEl.innerHTML = `
          <img src="evox-neon-pack/icons/${{slot.file}}" alt="${{slot.name}}">
          <span class="deck-key-label">${{slot.name}}</span>
        `;
      }} else {{
        keyEl.innerHTML = `
          <span style="font-size:20px; color:#334155;">+</span>
          <span class="deck-key-label" style="color:#475569;">BOŞ #${{index+1}}</span>
        `;
      }}
      grid.appendChild(keyEl);
    }});
  }}

  function selectDeckSlot(index) {{
    selectedDeckSlot = index;
    renderDeck();
    showToast('🎮', `Simülatör Yuvası #${{index + 1}} seçildi. Galeriden bir ikona tıklayın!`);
  }}

  function assignToDeck(icon) {{
    deckSlots[selectedDeckSlot] = {{
      id: icon.base,
      name: icon.title,
      file: icon.filename
    }};
    renderDeck();
    showToast('🚀', `"${{icon.title}}" simülatör yuvası #${{selectedDeckSlot + 1}}'e atandı!`);
    
    // Auto advance to next slot
    selectedDeckSlot = (selectedDeckSlot + 1) % deckSlots.length;
    renderDeck();
  }}

  function resetDeckPreset(type) {{
    const presets = {{
      streamer: ['mic_on', 'headphones_on', 'live_on', 'camera_on', 'discord', 'twitch', 'clapper', 'volume_up', 'volume_down', 'screenshot', 'chat_on', 'bell_on'],
      gaming: ['gamepad', 'trophy', 'target', 'discord', 'fire', 'bolt', 'crown', 'diamond', 'spotify', 'volume_up', 'volume_down', 'power_on'],
      media: ['play', 'pause', 'next', 'prev', 'equalizer', 'music', 'volume_up', 'volume_down', 'shuffle_on', 'repeat_on', 'headphones_on', 'spotify']
    }};
    const list = presets[type] || [];
    list.forEach((id, i) => {{
      if (i < deckSlots.length) {{
        const ic = ICONS.find(x => x.base === id) || {{ title: id, filename: id + '.gif' }};
        deckSlots[i] = {{ id: id, name: ic.title, file: ic.filename }};
      }}
    }});
    renderDeck();
    showToast('⚡', `${{type.toUpperCase()}} hazır seti simülatöre yüklendi!`);
  }}

  function clearDeck() {{
    for (let i = 0; i < deckSlots.length; i++) deckSlots[i] = null;
    renderDeck();
    showToast('🗑️', 'Simülatör tuşları temizlendi.');
  }}

  function renderGallery() {{
    const grid = document.getElementById('galleryGrid');
    grid.innerHTML = '';
    
    const query = searchQuery.toLowerCase().trim();
    const filtered = ICONS.filter(item => {{
      const matchCat = (activeCategory === 'all') || (item.category === activeCategory) || 
                       (activeCategory === 'toggle' && (item.is_on || item.is_off));
      const matchSearch = !query || 
                          item.title.toLowerCase().includes(query) || 
                          item.filename.toLowerCase().includes(query) ||
                          item.core.toLowerCase().includes(query);
      return matchCat && matchSearch;
    }});

    document.getElementById('visibleCount').textContent = filtered.length;

    filtered.forEach(icon => {{
      const card = document.createElement('div');
      card.className = 'icon-card';
      card.onclick = () => assignToDeck(icon);
      card.innerHTML = `
        <div class="img-wrapper">
          <img src="${{icon.rel_path}}" alt="${{icon.title}}" loading="lazy">
        </div>
        <div class="icon-title">${{icon.title}}</div>
        <span class="state-pill ${{icon.state_class}}">${{icon.state_tag}}</span>
        <span class="card-action-hint">Tuşa Ata ➔</span>
      `;
      grid.appendChild(card);
    }});
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

  let toastTimer = null;
  function showToast(icon, msg) {{
    const toast = document.getElementById('toastBox');
    document.getElementById('toastIcon').textContent = icon;
    document.getElementById('toastMsg').textContent = msg;
    toast.style.display = 'flex';
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {{
      toast.style.display = 'none';
    }}, 2600);
  }}

  // Init
  renderDeck();
  renderGallery();
</script>

</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Galeri başarıyla oluşturuldu: {OUTPUT_HTML} ({len(icons_data)} ikon)")

if __name__ == "__main__":
    build_gallery()
