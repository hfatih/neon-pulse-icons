"""Neon Pulse v2: animasyonlu GIF ikonlar + acik/kapali (_on/_off) halleri. Calistir: python make_icons.py -> icons/*.gif
Her kare 1024px cizilip 256px'e kucultulur (kenar yumusatma); ikon basina tek global palet = titreme yok."""
import math, os, shutil
from PIL import Image, ImageDraw, ImageFilter, ImageFont

S, OUT, N, MS = 1024, 256, 36, 40
W = 56  # cizgi kalinligi
TAU = 2 * math.pi
C = {"cyan": (0, 229, 255), "pink": (255, 60, 200), "gold": (255, 205, 5), "green": (60, 255, 140),
     "orange": (255, 140, 30), "violet": (170, 110, 255), "red": (255, 70, 100)}
OFFC, SLASHC = (105, 112, 132), (235, 70, 85)
CLEAR = (0, 0, 0, 0)


def dim(c, b):
    return tuple(int(x * b) for x in c)


def cap(d, p, c, r=W // 2):
    d.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill=c)


def line(d, a, b, c, w=W):
    d.line([a, b], fill=c, width=w)
    cap(d, a, c, w // 2), cap(d, b, c, w // 2)


def arc(d, cx, cy, r, a0, a1, c):
    """r = dis yaricap; PIL cizgiyi iceri dogru cizer, kapaklar orta cizgide (r - W/2)."""
    d.arc((cx - r, cy - r, cx + r, cy + r), a0, a1, fill=c, width=W)
    m = r - W / 2
    for a in (a0, a1):
        cap(d, (cx + m * math.cos(math.radians(a)), cy + m * math.sin(math.radians(a))), c)


def heart_pts(s):
    pts = []
    for i in range(240):
        a = TAU * i / 240
        pts.append((512 + 16 * math.sin(a) ** 3 * s * 1.5,
                    500 - (13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a)) * s * 1.5))
    return pts


def power(d, t, c, on):
    arc(d, 512, 540, 300, -55, 235, c)
    line(d, (512, 220), (512, 520), c)
    return 0.6 + 0.6 * (0.5 + 0.5 * math.sin(TAU * t))


def heart(d, t, c, on):
    if on:
        d.polygon(heart_pts(14 * (1 + 0.13 * max(0, math.sin(2 * TAU * t)) ** 2)), fill=c)
    else:
        p = heart_pts(14)
        d.line(p + p[:2], fill=c, width=40, joint="curve")
    return 0.6 + 0.8 * max(0, math.sin(2 * TAU * t)) ** 2


def bolt(d, t, c, on):
    pts = [(590, 130), (300, 570), (490, 570), (420, 900), (730, 440), (540, 440)]
    d.polygon(pts, fill=c)
    d.line(pts + pts[:2], fill=c, width=24, joint="curve")
    return 0.4 + 0.9 * max(0, math.sin(TAU * t)) ** 4


def volume(d, t, c, on):
    d.polygon([(200, 400), (350, 400), (520, 250), (520, 774), (350, 624), (200, 624)], fill=c)
    if on:
        for i, r in enumerate((150, 250, 350)):
            arc(d, 560, 512, r, -42, 42, dim(c, 0.25 + 0.75 * max(0, math.sin(TAU * (t - i / 6) + math.pi / 2)) ** 2))
    return 0.9


def mic(d, t, c, on):
    d.rounded_rectangle((392, 160, 632, 560), 120, fill=c)
    arc(d, 512, 480, 270, 5, 175, c)
    line(d, (512, 700), (512, 850), c)
    line(d, (390, 850), (634, 850), c)
    return 0.9


def play(d, t, c, on):
    for k in range(9, -1, -1):  # kuyruktan basa: parlak uc en ustte
        a = t * 360 - k * 12
        arc(d, 512, 512, 430, a - 10, a, dim(c, 1 - k / 10))
    pts = [(390, 300), (390, 724), (740, 512)]
    d.polygon(pts, fill=c)
    d.line(pts + pts[:2], fill=c, width=40, joint="curve")
    return 0.8


def pause(d, t, c, on):
    s = 50 * math.sin(TAU * t)
    d.rounded_rectangle((290, 270 + s, 450, 754), 60, fill=c)
    d.rounded_rectangle((574, 270 - s, 734, 754), 60, fill=c)
    return 0.8


def bell(d, t, c, on):
    d.ellipse((322, 230, 702, 640), fill=c)
    d.polygon([(322, 440), (702, 440), (790, 720), (234, 720)], fill=c)
    d.ellipse((234, 680, 790, 760), fill=c)
    cap(d, (512, 200), c, 40)
    cap(d, (512, 820), c, 60)
    return 0.9


def wifi(d, t, c, on):
    cap(d, (512, 780), c, 56)
    fade = 1 if not on else max(0.0, min(1.0, (1 - t) / 0.15))
    for i, r in enumerate((190, 330, 470)):
        b = 1 if not on else min(1, max(0.2, (t * 4.5 - i) * 2)) * fade
        arc(d, 512, 780, r, 228, 312, dim(c, max(b, 0.2)))
    return 0.9


def gear(d, t, c, on):
    for k in range(8):
        a = math.radians(t * 45 + k * 45)
        ux, uy, vx, vy = math.cos(a), math.sin(a), -math.sin(a), math.cos(a)
        r0, r1, hw = 250, 400, 62
        d.polygon([(512 + ux * r0 + vx * hw, 512 + uy * r0 + vy * hw), (512 + ux * r1 + vx * hw * .75, 512 + uy * r1 + vy * hw * .75),
                   (512 + ux * r1 - vx * hw * .75, 512 + uy * r1 - vy * hw * .75), (512 + ux * r0 - vx * hw, 512 + uy * r0 - vy * hw)], fill=c)
    d.ellipse((212, 212, 812, 812), fill=c)
    d.ellipse((392, 392, 632, 632), fill=CLEAR)
    return 0.8


def eq(d, t, c, on):
    for i in range(5):
        h = 130 + 400 * (0.5 + 0.5 * math.sin(TAU * (t + i * 0.2)))
        x = 512 + (i - 2) * 150
        d.rounded_rectangle((x - 50, 790 - h, x + 50, 790), 50, fill=dim(c, 0.55 + 0.45 * h / 530))
    return 0.9


def record(d, t, c, on):
    d.ellipse((122, 122, 902, 902), outline=c if on else c, width=44)
    if on:
        u = t
        r = 240 + 110 * u
        d.ellipse((512 - r, 512 - r, 512 + r, 512 + r), outline=dim(c, 0.8 * (1 - u)), width=22)
        r = 230 * (1 + 0.06 * math.sin(TAU * t))
        d.ellipse((512 - r, 512 - r, 512 + r, 512 + r), fill=c)
    else:
        d.rounded_rectangle((352, 352, 672, 672), 60, fill=c)
    return 0.4 + 0.7 * (0.5 + 0.5 * math.sin(TAU * t))


def camera(d, t, c, on):
    d.polygon([(370, 250), (654, 250), (700, 330), (324, 330)], fill=c)
    d.rounded_rectangle((130, 300, 894, 800), 100, fill=c)
    d.ellipse((512 - 190, 550 - 190, 512 + 190, 550 + 190), fill=CLEAR)
    d.ellipse((512 - 130, 550 - 130, 512 + 130, 550 + 130), fill=dim(c, 0.55 + 0.45 * math.sin(TAU * t) ** 2) if on else c)
    if on and (0.1 < t < 0.3):  # flas
        d.ellipse((772 - 34, 400 - 34, 772 + 34, 400 + 34), fill=(255, 255, 255))
        return 1.6
    return 0.7


def bulb(d, t, c, on):
    d.ellipse((282, 200, 742, 660), fill=c)
    d.polygon([(400, 600), (624, 600), (590, 730), (434, 730)], fill=c)
    d.rounded_rectangle((420, 740, 604, 800), 30, fill=c)
    d.rounded_rectangle((452, 812, 572, 872), 30, fill=c)
    if on:
        for k in range(7):
            a = math.radians(-180 + 30 * k)
            b = 0.35 + 0.65 * max(0, math.sin(TAU * (t - k / 7) + math.pi / 2)) ** 2
            p0 = (512 + 300 * math.cos(a), 430 + 300 * math.sin(a))
            p1 = (512 + 370 * math.cos(a), 430 + 370 * math.sin(a))
            line(d, p0, p1, dim(c, b), 40)
    return 0.7 + 0.5 * (0.5 + 0.5 * math.sin(TAU * t))


def lock(d, t, c, on):
    d.rounded_rectangle((252, 470, 772, 890), 70, fill=c)
    if on:  # kilitli
        arc(d, 512, 480, 190 + W // 2, 180, 360, c)
        line(d, (512 - 190, 480), (512 - 190, 500), c)
        line(d, (512 + 190, 480), (512 + 190, 500), c)
    else:  # acik: sag bacak havada
        arc(d, 512, 360, 190 + W // 2, 180, 360, c)
        line(d, (512 - 190, 360), (512 - 190, 480), c)
        line(d, (512 + 190, 360), (512 + 190, 400), c)
    d.ellipse((462, 600, 562, 700), fill=CLEAR)
    d.rectangle((492, 660, 532, 780), fill=CLEAR)
    return 0.6 + 0.5 * (0.5 + 0.5 * math.sin(TAU * t))


def screenshot(d, t, c, on):
    i = 120 + 50 * math.sin(TAU * t) ** 2
    for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        x, y = (i if sx > 0 else S - i), (i if sy > 0 else S - i)
        line(d, (x, y + sy * 190), (x, y), c)
        line(d, (x, y), (x + sx * 190, y), c)
    r = 90 * (1 + 0.15 * math.sin(TAU * t))
    d.ellipse((512 - r, 512 - r, 512 + r, 512 + r), fill=c)
    return 0.9


def star4(d, x, y, r, c):
    d.polygon([(x + (r if i % 2 == 0 else r * .28) * math.cos(math.radians(i * 45 - 90)),
                y + (r if i % 2 == 0 else r * .28) * math.sin(math.radians(i * 45 - 90))) for i in range(8)], fill=c)


def poly(d, pts, c, w=36):
    d.polygon(pts, fill=c)
    d.line(pts + pts[:2], fill=c, width=w, joint="curve")


def rotp(pts, deg, cx=512, cy=512):
    a = math.radians(deg)
    return [(cx + (x - cx) * math.cos(a) - (y - cy) * math.sin(a), cy + (x - cx) * math.sin(a) + (y - cy) * math.cos(a)) for x, y in pts]


def bluetooth(d, t, c, on):
    if on:
        for k in range(2):
            u = (t + k / 2) % 1
            r = 300 + 200 * u
            d.ellipse((512 - r, 512 - r, 512 + r, 512 + r), outline=dim(c, 0.6 * (1 - u)), width=12)
    p = [(330, 330), (694, 694), (512, 876), (512, 148), (694, 330), (330, 694)]
    for a, b in zip(p, p[1:]):
        line(d, a, b, c)
    return 0.6 + 0.6 * (0.5 + 0.5 * math.sin(TAU * t))


def moon(d, t, c, on):
    d.ellipse((182, 182, 842, 842), fill=c)
    d.ellipse((380, 100, 980, 700), fill=CLEAR)
    if on:
        for k, (x, y, r0) in enumerate(((650, 320, 90), (800, 520, 60), (610, 580, 50))):
            star4(d, x, y, r0 * (0.3 + 0.7 * math.sin(math.pi * ((t + k / 3) % 1))), (255, 240, 180))
    return 0.7


def airplane(d, t, c, on):
    dy = 30 * math.sin(TAU * t) if on else 0
    base = [(512, 120), (560, 300), (560, 420), (860, 600), (860, 670), (560, 610), (560, 760), (650, 830), (650, 880),
            (512, 850), (374, 880), (374, 830), (464, 760), (464, 610), (164, 670), (164, 600), (464, 420), (464, 300)]
    poly(d, rotp([(x, y + dy) for x, y in base], 45), c, 24)
    if on:  # arkada kayan cizgiler
        for k in range(3):
            u = (t + k / 3) % 1
            o = (k - 1) * 90
            f = lambda s: (512 - s * .707 + o * .707, 512 + s * .707 + o * .707)
            line(d, f(450 + 130 * u), f(500 + 130 * u), dim(c, 1 - u), 30)
    return 0.8


FONT = ImageFont.truetype("arialbd.ttf", 210)


def live(d, t, c, on):
    if on:
        d.rounded_rectangle((92, 300, 932, 724), 130, fill=c)
        r = 40 + 14 * (0.5 + 0.5 * math.sin(TAU * t))
        d.ellipse((250 - r, 512 - r, 250 + r, 512 + r), fill=(255, 235, 235))
        d.text((350, 520), "LIVE", font=FONT, fill=CLEAR, anchor="lm")
    else:
        d.rounded_rectangle((92, 300, 932, 724), 130, outline=c, width=36)
        d.ellipse((195, 457, 305, 567), outline=c, width=22)
        d.text((350, 520), "LIVE", font=FONT, fill=c, anchor="lm")
    return 0.8


def chat(d, t, c, on):
    d.rounded_rectangle((100, 170, 924, 720), 160, fill=c)
    d.polygon([(240, 680), (240, 890), (470, 700)], fill=c)
    for k in range(3):
        dy = -50 * max(0, math.sin(TAU * (t - k / 6))) if on else 0
        d.ellipse((342 + 170 * k - 55, 445 + dy - 55, 342 + 170 * k + 55, 445 + dy + 55), fill=CLEAR)
    return 0.8


def star(d, t, c, on):
    s = 1 + 0.1 * math.sin(TAU * t) if on else 1
    pts = [(512 + (410 if i % 2 == 0 else 170) * s * math.cos(math.radians(-90 + 36 * i)),
            560 + (410 if i % 2 == 0 else 170) * s * math.sin(math.radians(-90 + 36 * i))) for i in range(10)]
    if on:
        poly(d, pts, c, 30)
        for k, (x, y) in enumerate(((820, 190), (200, 300), (850, 660))):
            star4(d, x, y, 80 * math.sin(math.pi * ((t + k / 3) % 1)), (255, 255, 255))
    else:
        d.line(pts + pts[:2], fill=c, width=40, joint="curve")
    return 0.8 + 0.4 * math.sin(TAU * t)


def repeat(d, t, c, on):
    a = t * 360 if on else -90
    for k in range(6):
        arc(d, 512, 512, 380, a + 45 * k, a + 45 * (k + 1) + 1, dim(c, 0.35 + 0.65 * k / 5))
    e = math.radians(a + 270)
    ex, ey = 512 + 352 * math.cos(e), 512 + 352 * math.sin(e)
    tx, ty, nx, ny = -math.sin(e), math.cos(e), math.cos(e), math.sin(e)
    d.polygon([(ex + tx * 130, ey + ty * 130), (ex + nx * 100, ey + ny * 100), (ex - nx * 100, ey - ny * 100)], fill=c)
    return 0.8


def battery(d, t, c, on):
    d.rounded_rectangle((130, 300, 830, 724), 90, outline=c, width=44)
    d.rounded_rectangle((850, 410, 920, 614), 30, fill=c)
    lvl = min(1, t * 1.25)
    if lvl > 0.08:
        d.rounded_rectangle((204, 364, 204 + 560 * lvl, 660), 50, fill=dim(c, min(1, (1 - t) / .2)))
    d.polygon([(540, 330), (430, 540), (500, 540), (470, 700), (610, 470), (530, 470)], fill=(255, 255, 255))
    return 0.5 + 0.5 * lvl


def _skip(d, t, c, flip):
    X = (lambda x: S - x) if flip else (lambda x: x)
    sh = 30 * math.sin(TAU * t)
    for i, x0 in enumerate((170, 440)):
        poly(d, [(X(x0 + sh), 270), (X(x0 + sh), 754), (X(x0 + 300 + sh), 512)], dim(c, 0.55 + 0.45 * max(0, math.sin(TAU * (t - i / 4)))), 40)
    x0, x1 = sorted((X(790), X(850)))
    d.rounded_rectangle((x0, 260, x1, 764), 30, fill=c)
    return 0.8


def next_(d, t, c, on):
    return _skip(d, t, c, False)


def prev_(d, t, c, on):
    return _skip(d, t, c, True)


def fire(d, t, c, on):
    def flame(sc, cy, col, h, sw):
        pts = []
        for i in range(120):
            u = TAU * i / 120
            y = cy - h * math.cos(u)
            pts.append((512 + 380 * sc * math.sin(u) * (1 - math.cos(u)) / 2 + 70 * sw * max(0, (cy - y) / h) ** 2, y))
        d.polygon(pts, fill=col)
    fl = 400 + 30 * math.sin(2 * TAU * t + 1)
    flame(1, 540, c, fl, math.sin(TAU * t))
    flame(.55, 700, (255, 235, 130), fl * .55, math.sin(TAU * t + .8))
    for k in range(3):
        u = (t + k / 3) % 1
        x, y, r = 512 + (k - 1) * 150 + 25 * math.sin(TAU * (t * 2 + k)), 260 - 200 * u, 18 * (1 - u) + 4
        d.ellipse((x - r, y - r, x + r, y + r), fill=dim(c, 1 - u))
    return 0.9


def download(d, t, c, on):
    dy = 40 * math.sin(TAU * t)
    line(d, (512, 180 + dy), (512, 560 + dy), c)
    poly(d, [(290, 500 + dy), (734, 500 + dy), (512, 760 + dy)], c, 40)
    line(d, (200, 880), (824, 880), c)
    return 0.8


def pin(d, t, c, on):
    r = 100 + 220 * t
    d.ellipse((512 - r, 930 - r * .3, 512 + r, 930 + r * .3), outline=dim(c, .8 * (1 - t)), width=14)
    dy = -80 * max(0, math.sin(TAU * t))
    d.ellipse((252, 150 + dy, 772, 670 + dy), fill=c)
    d.polygon([(268, 540 + dy), (756, 540 + dy), (512, 900 + dy)], fill=c)
    d.ellipse((412, 310 + dy, 612, 510 + dy), fill=CLEAR)
    return 0.8


# fonksiyon: (aci(t), donus merkezi)
ROT = {bell: (lambda t: 22 * math.sin(2 * TAU * t) * max(0, 1 - t / 0.7), (512, 200)),
       lock: (lambda t: 6 * math.sin(4 * TAU * t) * max(0, 1 - t / 0.3), (512, 880))}

# (dosya adi, fn, renk, kapali modu: "slash" | "plain" | None -> tek hal)
ICONS = [("power", power, "red", "plain"), ("heart", heart, "pink", "plain"), ("volume", volume, "cyan", "slash"),
         ("mic", mic, "green", "slash"), ("wifi", wifi, "cyan", "slash"), ("bell", bell, "orange", "slash"),
         ("record", record, "red", "plain"), ("camera", camera, "violet", "slash"), ("bulb", bulb, "gold", "plain"),
         ("lock", lock, "green", "plain"),
         ("play", play, "violet", None), ("pause", pause, "cyan", None), ("bolt", bolt, "gold", None),
         ("gear", gear, "gold", None), ("equalizer", eq, "pink", None), ("screenshot", screenshot, "cyan", None),
         ("bluetooth", bluetooth, "cyan", "slash"), ("moon", moon, "violet", "plain"), ("airplane", airplane, "cyan", "slash"),
         ("live", live, "red", "plain"), ("chat", chat, "pink", "slash"), ("star", star, "gold", "plain"),
         ("repeat", repeat, "green", "plain"),
         ("battery", battery, "green", None), ("next", next_, "orange", None), ("prev", prev_, "orange", None),
         ("fire", fire, "orange", None), ("download", download, "cyan", None), ("pin", pin, "red", None)]


def background(c):
    bg = Image.new("RGB", (S, S), (12, 13, 20))
    tint = Image.new("L", (S, S), 0)
    ImageDraw.Draw(tint).ellipse((212, 212, 812, 812), fill=60)
    return Image.composite(Image.new("RGB", (S, S), dim(c, 0.5)), bg, tint.filter(ImageFilter.GaussianBlur(160)))


def frames(fn, c, on, slash=False):
    bg, out = background(c), []
    n = N if on else 1
    for f in range(n):
        t = f / N if on else 0.8  # kapali hal: tek kare (wifi tum cubuklar yanik)
        layer = Image.new("RGBA", (S, S), CLEAR)
        d = ImageDraw.Draw(layer)
        gs = fn(d, t, c if on else OFFC, on) if on else 0.15
        if not on:
            fn(d, t, OFFC, on)
        if slash:
            d.line([(190, 190), (834, 834)], fill=CLEAR, width=130)
            line(d, (190, 190), (834, 834), SLASHC)
        if fn in ROT:
            ang, ctr = ROT[fn]
            layer = layer.rotate(ang(t) if on else 0, center=ctr, resample=Image.BICUBIC)
        glow = layer.filter(ImageFilter.GaussianBlur(34))
        glow.putalpha(glow.getchannel("A").point(lambda v: min(255, int(v * gs * 1.6))))
        img = Image.alpha_composite(Image.alpha_composite(bg.convert("RGBA"), glow), layer)
        out.append(img.convert("RGB").resize((OUT, OUT), Image.LANCZOS))
    return out


def save(name, fr):
    montage = Image.new("RGB", (OUT, OUT * len(fr)))
    for i, f in enumerate(fr):
        montage.paste(f, (0, i * OUT))
    pal = montage.quantize(256, method=Image.Quantize.FASTOCTREE)
    q = [f.quantize(palette=pal, dither=Image.Dither.FLOYDSTEINBERG) for f in fr]
    q[0].save(f"icons/{name}.gif", save_all=True, append_images=q[1:], duration=MS, loop=0, disposal=1)
    print(name, os.path.getsize(f"icons/{name}.gif") // 1024, "KB")


if __name__ == "__main__":
    shutil.rmtree("icons", ignore_errors=True)
    os.makedirs("icons")
    for name, fn, col, off in ICONS:
        c = C[col]
        if off is None:
            save(name, frames(fn, c, True))
        else:
            save(f"{name}_on", frames(fn, c, True))
            save(f"{name}_off", frames(fn, c, False, off == "slash"))
