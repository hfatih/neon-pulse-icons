r"""Yeni duzenlenen ve eklenen ikonlari tek bir yuksek kaliteli tanitim gorselinde birlestiren betik.
Cikti: c:\Users\hfati\Desktop\Websites\yeni_duzenlenen_ikonlar.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

ICONS_DIR = r"c:\Users\hfati\Desktop\Websites\evox-neon-pack\icons"
OUTPUT_PNG = r"c:\Users\hfati\Desktop\Websites\yeni_duzenlenen_ikonlar.png"
OUTPUT_LOCAL = r"c:\Users\hfati\Desktop\Websites\evox-neon-pack\yeni_duzenlenen_ikonlar.png"

FONT_BOLD_PATH = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_REG_PATH = r"C:\Windows\Fonts\segoeui.ttf"

def load_font(size, bold=False):
    path = FONT_BOLD_PATH if bold else FONT_REG_PATH
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

SECTIONS = [
    {
        "title": "1. GERİ BİLDİRİMLERLE DÜZELTİLEN & İYİLEŞTİRİLENLER",
        "tag": "BUG FIX & REFINEMENT",
        "tag_color": (60, 255, 140), # Neon Green
        "icons": [
            ("live_on.gif", "live_on", "Sadece Beyaz Nokta", "Dağılma kaldırıldı, nokta nabız atar", (60, 255, 140)),
            ("live_off.gif", "live_off", "Canlı Kapalı", "Karanlık çerçeve, kapalı rozet", (255, 70, 100)),
            ("mic_on.gif", "mic_on", "Halkasız Sade Yeşil", "Dağılan ses halkaları kaldırıldı", (60, 255, 140)),
            ("mic_off.gif", "mic_off", "Mikrofon Kapalı", "Kırmızı neon üzeri net kesme", (255, 70, 100)),
            ("star_on.gif", "star_on", "Uçları Düzeltildi", "Köşe ve çentik kırpılması giderildi", (255, 205, 5)),
            ("star_off.gif", "star_off", "Yıldız Kapalı", "Köşe vertex düzeltmeli kapalı mod", (255, 70, 100)),
            ("play.gif", "play", "Üçgen Köşe Düzeltildi", "Tepe ve köşe kırpılması onarıldı", (0, 229, 255)),
            ("next.gif", "next", "Çift Üçgen Düzeltildi", "İleri ok köşe uçları pürüzsüz", (0, 229, 255)),
            ("prev.gif", "prev", "Geri Ok Düzeltildi", "Geri ok köşe uçları pürüzsüz", (0, 229, 255)),
            ("battery.gif", "battery", "Dikişsiz Döngü Fix", "Pil dolumunda sıçrama kaldırıldı", (60, 255, 140)),
            ("hourglass.gif", "hourglass", "Kum Akışı Döngü Fix", "Kum saati akıcı sonsuz döngü", (0, 229, 255)),
            ("bell_on.gif", "bell_on", "Zil Sallanma Fix", "Zil sallanma döngüsü pürüzsüz", (255, 205, 5)),
        ]
    },
    {
        "title": "2. YENİ STREAM DECK & YAYIN KONTROL İKONLARI",
        "tag": "STREAM DECK ESSENTIALS",
        "tag_color": (0, 229, 255), # Neon Cyan
        "icons": [
            ("camera_on.gif", "camera_on", "Kamera Açık", "Canlı yeşil webcam lensi", (60, 255, 140)),
            ("camera_off.gif", "camera_off", "Kamera Kapalı", "Kırmızı neon kesmeli kamera", (255, 70, 100)),
            ("record_on.gif", "record_on", "Kayıt Açık (REC)", "Pulsing kırmızı kayıt rozeti", (255, 70, 100)),
            ("record_off.gif", "record_off", "Kayıt Kapalı", "Kapalı stand-by kayıt çerçevesi", (140, 150, 170)),
            ("clapper.gif", "clapper", "Yayın Klaketi", "Animasyonlu klaket vuruşu", (0, 229, 255)),
            ("screenshot.gif", "screenshot", "Ekran Görüntüsü", "Vizör ve parlama deklanşör", (0, 229, 255)),
            ("volume_up.gif", "volume_up", "Ses Aç (+)", "Dalga yayan ses açma ikonu", (0, 229, 255)),
            ("volume_down.gif", "volume_down", "Ses Kıs (-)", "Düşük seviye ses ikonu", (0, 229, 255)),
            ("equalizer.gif", "equalizer", "Ses Ekolayzerı", "Canlı zıplayan frekans çubukları", (255, 60, 200)),
            ("music.gif", "music", "Müzik Notası", "Ritimle salınan neon nota", (255, 60, 200)),
            ("headphones_on.gif", "headphones_on", "Kulaklık Açık", "Canlı neon dinleme modu", (60, 255, 140)),
            ("headphones_off.gif", "headphones_off", "Kulaklık Kapalı", "Kırmızı kesmeli kulaklık", (255, 70, 100)),
        ]
    },
    {
        "title": "3. YENİ POPÜLER MARKA & PLATFORM LOGOLARI",
        "tag": "NEON BRAND ICONS",
        "tag_color": (255, 60, 200), # Neon Pink
        "icons": [
            ("discord.gif", "discord", "Discord", "Gözleri kırpan neon Clyde maskotu", (170, 110, 255)),
            ("spotify.gif", "spotify", "Spotify", "Dalgası atan neon yeşil Spotify", (60, 255, 140)),
            ("twitch.gif", "twitch", "Twitch", "Piksel göz kırpan mor Twitch", (170, 110, 255)),
            ("youtube.gif", "youtube", "YouTube", "Oynatma üçgeni nabız atan YT", (255, 70, 100)),
            ("instagram.gif", "instagram", "Instagram", "Neon gradyan parlayan IG kamera", (255, 60, 200)),
            ("x.gif", "x", "X (Twitter)", "Parıldayan neon geometrik X", (0, 229, 255)),
        ]
    },
    {
        "title": "4. YENİ OYUN, ESPOR & SİSTEM ARAÇLARI",
        "tag": "GAMING & SYSTEM SUITE",
        "tag_color": (255, 205, 5), # Neon Gold
        "icons": [
            ("gamepad.gif", "gamepad", "Oyun Kolu", "Neon kontrolcü tuş parlaması", (170, 110, 255)),
            ("trophy.gif", "trophy", "Şampiyon Kupası", "Işıldayan altın şampiyonluk kupası", (255, 205, 5)),
            ("target.gif", "target", "FPS Nişangah", "Hedefe kilitlenen neon crosshair", (255, 70, 100)),
            ("crown.gif", "crown", "Kral Tacı (VIP)", "Mücevherleri parlayan altın taç", (255, 205, 5)),
            ("diamond.gif", "diamond", "Elmas Mücevher", "Faset parlamalı elmas ikon", (0, 229, 255)),
            ("fire.gif", "fire", "Ateş Kombo", "Dalgalanan alev animasyonu", (255, 140, 30)),
            ("bolt.gif", "bolt", "Yıldırım Turbo", "Çakan yüksek enerji şimşeği", (255, 205, 5)),
            ("coin.gif", "coin", "Altın Coin", "Dönen/parlayan altın jeton", (255, 205, 5)),
            ("chart.gif", "chart", "İstatistik Grafiği", "Yükselen neon trend barları", (60, 255, 140)),
            ("rocket.gif", "rocket", "Hızlı Roket", "Ateş püskürten uzay roketi", (255, 60, 200)),
            ("keyboard.gif", "keyboard", "Mekanik Klavye", "Tuşları parlayan oyuncu klavyesi", (0, 229, 255)),
            ("terminal.gif", "terminal", "Kod Konsolu", "Yanıp sönen imleçli terminal", (60, 255, 140)),
        ]
    }
]

def create_showcase_image():
    W = 1860
    COLS = 6
    CARD_W = 280
    CARD_H = 220
    GAP_X = 20
    GAP_Y = 20
    
    HEADER_H = 220
    SECTION_HEADER_H = 70
    FOOTER_H = 120
    PAD_X = 40
    PAD_Y = 40
    
    # Calculate total height
    total_h = PAD_Y + HEADER_H
    for sec in SECTIONS:
        num_icons = len(sec["icons"])
        rows = (num_icons + COLS - 1) // COLS
        sec_h = SECTION_HEADER_H + rows * (CARD_H + GAP_Y) + 20
        total_h += sec_h
    total_h += FOOTER_H + PAD_Y

    # Base Canvas
    im = Image.new("RGB", (W, total_h), (8, 10, 16))
    draw = ImageDraw.Draw(im)

    # Gradient background mesh (subtle dark cyberpunk tones)
    for y in range(total_h):
        # subtle vertical gradient
        r = int(8 + (y / total_h) * 6)
        g = int(10 + (y / total_h) * 6)
        b = int(17 + (y / total_h) * 12)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Ambient glow blobs
    # (Top left cyan, top right pink, bottom center green)
    glow_overlay = Image.new("RGBA", (W, total_h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_overlay)
    
    # Top left cyan glow
    for rad in range(350, 0, -20):
        alpha = int((1 - rad / 350) * 22)
        glow_draw.ellipse([(-100 - rad, -50 - rad), (400 + rad, 450 + rad)], fill=(0, 229, 255, alpha))
    # Top right pink glow
    for rad in range(350, 0, -20):
        alpha = int((1 - rad / 350) * 18)
        glow_draw.ellipse([(W - 400 - rad, -50 - rad), (W + 100 + rad, 450 + rad)], fill=(255, 60, 200, alpha))
        
    im.paste(Image.alpha_composite(im.convert("RGBA"), glow_overlay).convert("RGB"), (0, 0))
    draw = ImageDraw.Draw(im)

    # Fonts
    f_badge = load_font(12, bold=True)
    f_title = load_font(38, bold=True)
    f_sub = load_font(16, bold=False)
    
    f_sec_title = load_font(18, bold=True)
    f_sec_tag = load_font(11, bold=True)
    
    f_card_title = load_font(15, bold=True)
    f_card_sub = load_font(12, bold=True)
    f_card_desc = load_font(11, bold=False)
    f_footer = load_font(14, bold=False)

    # 1. HEADER SECTION
    curr_y = PAD_Y
    
    # Header box frame
    hdr_box = [PAD_X, curr_y, W - PAD_X, curr_y + HEADER_H - 30]
    draw.rounded_rectangle(hdr_box, radius=20, fill=(15, 19, 30), outline=(35, 45, 68), width=2)
    
    # Top Badge (Left)
    badge_text = "evoX NEON PULSE • V4.0 GÜNCELLEMESİ"
    badge_w = int(draw.textlength(badge_text, font=f_badge)) + 28
    draw.rounded_rectangle([PAD_X + 24, curr_y + 24, PAD_X + 24 + badge_w, curr_y + 54], radius=999, fill=(12, 36, 50), outline=(0, 229, 255), width=1)
    draw.text((PAD_X + 38, curr_y + 32), badge_text, font=f_badge, fill=(0, 229, 255))
    
    # 100 İkon Sayacı Rozeti (Right)
    counter_text = "● TOPLAM 100 CANLI GIF İKON"
    counter_w = int(draw.textlength(counter_text, font=f_badge)) + 28
    draw.rounded_rectangle([W - PAD_X - counter_w - 24, curr_y + 24, W - PAD_X - 24, curr_y + 54], radius=999, fill=(14, 42, 28), outline=(60, 255, 140), width=1)
    draw.text((W - PAD_X - counter_w - 10, curr_y + 32), counter_text, font=f_badge, fill=(60, 255, 140))

    # Main Title
    draw.text((PAD_X + 24, curr_y + 68), "YENİ DÜZENLENEN & EKLENEN İKONLAR", font=f_title, fill=(255, 255, 255))
    
    # Subtitle
    sub_desc = "Geri bildirimler doğrultusunda düzeltilen köşe/uç çizimleri, basitleştirilen Live & Mikrofon efektleri ve eklenen Stream Deck & Marka ikonları."
    draw.text((PAD_X + 26, curr_y + 126), sub_desc, font=f_sub, fill=(148, 163, 184))
    
    curr_y += HEADER_H

    # 2. SECTIONS
    for sec in SECTIONS:
        sec_title = sec["title"]
        sec_tag = sec["tag"]
        tag_col = sec["tag_color"]
        icons = sec["icons"]
        
        # Section Header Row
        draw.rounded_rectangle([PAD_X, curr_y + 6, PAD_X + 6, curr_y + 36], radius=3, fill=tag_col)
        draw.text((PAD_X + 18, curr_y + 8), sec_title, font=f_sec_title, fill=(245, 247, 250))
        
        # Tag pill
        tag_w = int(draw.textlength(sec_tag, font=f_sec_tag)) + 20
        tag_x = W - PAD_X - tag_w
        draw.rounded_rectangle([tag_x, curr_y + 6, tag_x + tag_w, curr_y + 32], radius=6, fill=(20, 26, 42), outline=tag_col, width=1)
        draw.text((tag_x + 10, curr_y + 11), sec_tag, font=f_sec_tag, fill=tag_col)

        curr_y += SECTION_HEADER_H - 15

        # Render Icon Cards in Grid
        for i, item in enumerate(icons):
            fname, code_name, title, desc, col_accent = item
            
            row = i // COLS
            col = i % COLS
            
            cx = PAD_X + col * (CARD_W + GAP_X)
            cy = curr_y + row * (CARD_H + GAP_Y)
            
            # Card Base
            draw.rounded_rectangle([cx, cy, cx + CARD_W, cy + CARD_H], radius=16, fill=(13, 17, 26), outline=(32, 42, 64), width=1)
            
            # Image Stage
            stage_size = 96
            stage_x = cx + 14
            stage_y = cy + 14
            draw.rounded_rectangle([stage_x, stage_y, stage_x + stage_size, stage_y + stage_size], radius=12, fill=(6, 8, 12), outline=(22, 28, 42), width=1)
            
            # Load and paste GIF frame
            gif_path = os.path.join(ICONS_DIR, fname)
            if os.path.exists(gif_path):
                try:
                    with Image.open(gif_path) as gif:
                        # Pick optimal representative frame
                        target_frame = min(12, gif.n_frames - 1)
                        if "live" in fname:
                            target_frame = 10
                        elif "battery" in fname:
                            target_frame = 14
                        gif.seek(target_frame)
                        frame_rgba = gif.convert("RGBA")
                        frame_thumb = frame_rgba.resize((stage_size - 10, stage_size - 10), Image.LANCZOS)
                        im.paste(frame_thumb, (stage_x + 5, stage_y + 5), frame_thumb)
                except Exception as e:
                    pass

            # Card Text Info (Right side of stage)
            tx = stage_x + stage_size + 14
            draw.text((tx, cy + 18), code_name, font=f_card_title, fill=(255, 255, 255))
            
            # Pill indicator
            draw.rounded_rectangle([tx, cy + 42, cx + CARD_W - 12, cy + 64], radius=6, fill=(20, 26, 40))
            draw.text((tx + 6, cy + 45), title, font=f_card_sub, fill=col_accent)

            # File Badge
            draw.text((tx, cy + 72), f"256x256 • {fname}", font=f_card_desc, fill=(100, 116, 139))
            
            # Card Description Line (Bottom)
            draw.line([(cx + 14, cy + 120), (cx + CARD_W - 14, cy + 120)], fill=(22, 28, 42), width=1)
            
            # Word wrap description
            desc_y = cy + 130
            words = desc.split()
            lines = []
            curr_line = []
            for w in words:
                curr_line.append(w)
                if draw.textlength(" ".join(curr_line), font=f_card_desc) > (CARD_W - 28):
                    curr_line.pop()
                    lines.append(" ".join(curr_line))
                    curr_line = [w]
            if curr_line:
                lines.append(" ".join(curr_line))
            
            for l in lines[:3]:
                draw.text((cx + 14, desc_y), l, font=f_card_desc, fill=(148, 163, 184))
                desc_y += 18
                
        num_icons = len(icons)
        rows = (num_icons + COLS - 1) // COLS
        curr_y += rows * (CARD_H + GAP_Y) + 30

    # 3. FOOTER
    footer_box = [PAD_X, curr_y, W - PAD_X, curr_y + 80]
    draw.rounded_rectangle(footer_box, radius=16, fill=(13, 17, 26), outline=(30, 40, 60), width=1)
    
    draw.text((PAD_X + 24, curr_y + 30), "● evoX & Stream Deck Entegrasyonu • 100 İkonluk Tam Paket • .evoxpack & Web Galerisi Hazır", font=f_footer, fill=(203, 213, 225))
    draw.text((W - PAD_X - 320, curr_y + 30), "Canlı Galeri: neon_gallery.html", font=f_footer, fill=(0, 229, 255))

    # Save
    im.save(OUTPUT_PNG, "PNG", optimize=True)
    im.save(OUTPUT_LOCAL, "PNG", optimize=True)
    print(f"Showcase görseli başarıyla oluşturuldu: {OUTPUT_PNG} ({im.size})")

if __name__ == "__main__":
    create_showcase_image()
