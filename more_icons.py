"""Stream Deck tarzi ek ikonlar. Calistir: python more_icons.py  (icons/ klasorune ekler, mevcutlari silmez)
Ayrica icons_sheet.png: tum GIF'lerin ortadan bir karesiyle onizleme tablosu."""
from make_icons import *  # noqa: yardimcilar (arc, line, poly, frames, save...) ve sabitler


def mix(a, b, u):
    return tuple(int(a[i] * (1 - u) + b[i] * u) for i in range(3))


def polypos(P, u):
    segs = [(a, b, math.dist(a, b)) for a, b in zip(P, P[1:])]
    k = u * sum(s[2] for s in segs)
    for a, b, L in segs:
        if k <= L:
            return a[0] + (b[0] - a[0]) * k / L, a[1] + (b[1] - a[1]) * k / L
        k -= L
    return P[-1]


def _vol(d, t, c, plus):
    d.polygon([(110, 400), (260, 400), (430, 250), (430, 774), (260, 624), (110, 624)], fill=c)
    arc(d, 470, 512, 200, -40, 40, dim(c, .4 + .6 * max(0, math.sin(TAU * t + math.pi / 2)) ** 2))
    s = 70 * (1 + .15 * math.sin(TAU * t))
    line(d, (790 - s, 512), (790 + s, 512), c)
    if plus:
        line(d, (790, 512 - s), (790, 512 + s), c)
    return .8


def volume_up(d, t, c, on): return _vol(d, t, c, True)
def volume_down(d, t, c, on): return _vol(d, t, c, False)


def home(d, t, c, on):
    d.rectangle((690, 190, 780, 380), fill=c)
    poly(d, [(512, 140), (100, 510), (924, 510)], c, 40)
    d.rectangle((240, 480, 784, 870), fill=c)
    d.rectangle((432, 630, 592, 870), fill=dim((255, 225, 150), .55 + .45 * math.sin(TAU * t) ** 2))
    for k in range(3):
        u = (t + k / 3) % 1
        x, y, r = 735 + 30 * math.sin(TAU * (u + k / 3)), 160 - 140 * u, 22 + 20 * u
        d.ellipse((x - r, y - r, x + r, y + r), fill=dim((210, 210, 230), 1 - u))
    return .8


def folder(d, t, c, on):
    o = .5 + .5 * math.sin(TAU * t)
    d.rounded_rectangle((100, 230, 924, 850), 70, fill=dim(c, .55))
    d.rounded_rectangle((100, 170, 430, 320), 50, fill=dim(c, .55))
    d.rounded_rectangle((220, 360 - 110 * o, 804, 700), 40, fill=(240, 240, 250))
    d.rounded_rectangle((100, 430 - 50 * o, 924, 850), 70, fill=c)
    return .8


def globe(d, t, c, on):
    d.ellipse((132, 132, 892, 892), outline=c, width=44)
    for k in range(2):
        w = max(1, 380 * abs(math.cos(math.pi * t + k * math.pi / 2)))
        d.ellipse((512 - w, 132, 512 + w, 892), outline=c, width=36)
    for y, h in ((330, 333), (512, 380), (694, 333)):
        line(d, (512 - h, y), (512 + h, y), c, 36)
    return .8


def clock(d, t, c, on):
    d.ellipse((132, 132, 892, 892), outline=c, width=44)
    for k in range(12):
        a = math.radians(k * 30)
        line(d, (512 + 300 * math.cos(a), 512 + 300 * math.sin(a)), (512 + 340 * math.cos(a), 512 + 340 * math.sin(a)), c, 30)
    a = math.radians(-90 + t * 360)
    line(d, (512, 512), (512 + 270 * math.cos(a), 512 + 270 * math.sin(a)), c, 44)
    a = math.radians(-50)
    line(d, (512, 512), (512 + 170 * math.cos(a), 512 + 170 * math.sin(a)), c, 56)
    d.ellipse((472, 472, 552, 552), fill=c)
    return .8


def monitor(d, t, c, on):
    d.rounded_rectangle((110, 170, 914, 700), 50, outline=c, width=44)
    if on:
        d.rounded_rectangle((154, 214, 870, 656), 20, fill=dim(c, .22))
        y = 214 + 372 * (.5 + .5 * math.sin(TAU * t - math.pi / 2))
        d.rounded_rectangle((154, y, 870, y + 70), 20, fill=dim(c, .7))
    line(d, (512, 700), (512, 820), c)
    line(d, (330, 850), (694, 850), c)
    return .8


def headphones(d, t, c, on):
    arc(d, 512, 560, 372, 180, 360, c)
    b = lambda ph: .65 + .35 * max(0, math.sin(TAU * t + ph)) if on else 1
    d.rounded_rectangle((88, 520, 248, 830), 60, fill=dim(c, b(0)))
    d.rounded_rectangle((776, 520, 936, 830), 60, fill=dim(c, b(math.pi)))
    return .8


def keyboard(d, t, c, on):
    d.rounded_rectangle((80, 260, 944, 780), 90, outline=c, width=40)
    for row, y in enumerate((350, 470)):
        for i in range(6):
            x = 168 + 120 * i
            d.rounded_rectangle((x, y, x + 84, y + 84), 22, fill=dim(c, .35 + .65 * max(0, math.sin(TAU * (t - (i + row * 2) / 14))) ** 2))
    d.rounded_rectangle((300, 600, 724, 684), 30, fill=dim(c, .6))
    return .8


def terminal(d, t, c, on):
    d.rounded_rectangle((90, 200, 934, 824), 100, outline=c, width=44)
    line(d, (270, 400), (410, 512), c, 52)
    line(d, (410, 512), (270, 624), c, 52)
    if t < .5:
        d.rounded_rectangle((480, 590, 720, 640), 20, fill=c)
    return .8


def trash(d, t, c, on):
    dy = -45 * max(0, math.sin(TAU * t))
    d.rounded_rectangle((400, 170 + dy, 624, 260 + dy), 40, fill=c)
    d.rounded_rectangle((190, 240 + dy, 834, 340 + dy), 50, fill=c)
    poly(d, [(250, 380), (774, 380), (720, 890), (304, 890)], c, 40)
    for x in (400, 512, 624):
        line(d, (x, 470), (x, 790), CLEAR, 36)
    return .8


def search(d, t, c, on):
    ox, oy = 28 * math.cos(TAU * t), 28 * math.sin(TAU * t)
    d.ellipse((160 + ox, 160 + oy, 700 + ox, 700 + oy), outline=c, width=60)
    line(d, (640 + ox, 640 + oy), (850 + ox, 850 + oy), c, 90)
    arc(d, 430 + ox, 430 + oy, 170, 200, 260, (255, 255, 255))
    return .8


def mail(d, t, c, on):
    dy = -14 * math.sin(TAU * t)
    d.rounded_rectangle((100, 260 + dy, 924, 800 + dy), 70, fill=c)
    p = [(130, 310 + dy), (512, 590 + dy), (894, 310 + dy)]
    line(d, p[0], p[1], CLEAR, 36)
    line(d, p[1], p[2], CLEAR, 36)
    r = 70 + 22 * (.5 + .5 * math.sin(TAU * t))
    d.ellipse((850 - r - 26, 230 - r - 26, 850 + r + 26, 230 + r + 26), fill=CLEAR)
    d.ellipse((850 - r, 230 - r, 850 + r, 230 + r), fill=(255, 70, 100))
    return .8


def copy(d, t, c, on):
    o = 22 * math.sin(TAU * t)
    d.rounded_rectangle((330, 150, 850, 730), 70, outline=c, width=48)
    d.rounded_rectangle((144 + o, 304 + o, 746 + o, 926 + o), 90, fill=CLEAR)
    d.rounded_rectangle((170 + o, 330 + o, 720 + o, 900 + o), 70, fill=c)
    for y in (520, 640):
        line(d, (280 + o, y + o), (600 + o, y + o), CLEAR, 36)
    return .8


def smile(d, t, c, on):
    d.ellipse((112, 112, 912, 912), outline=c, width=50)
    h = .1 if abs(t - .5) < .05 else 1
    for x in (380, 644):
        d.ellipse((x - 52, 380 - 52 * h, x + 52, 380 + 52 * h), fill=c)
    arc(d, 512, 520, 278, 25, 155, c)
    return .8


def clapper(d, t, c, on):
    ang = -14 * (.5 + .5 * math.cos(TAU * t)) ** 3
    d.rounded_rectangle((130, 430, 894, 870), 50, fill=c)
    d.line([(190, 560), (834, 560)], fill=CLEAR, width=30)
    d.polygon(rotp([(130, 300), (894, 300), (894, 410), (130, 410)], ang, 130, 410), fill=c)
    for k in range(5):
        d.line(rotp([(220 + 150 * k, 410), (290 + 150 * k, 300)], ang, 130, 410), fill=CLEAR, width=28)
    return .8


def cloud(d, t, c, on):
    d.ellipse((140, 430, 520, 810), fill=c)
    d.ellipse((270, 220, 770, 720), fill=c)
    d.ellipse((530, 430, 910, 810), fill=c)
    d.rectangle((330, 620, 720, 810), fill=c)
    y0 = 770 - 240 * t
    col = mix(c, (12, 13, 20), math.sin(math.pi * t))
    line(d, (512, y0), (512, y0 - 70), col, 50)
    d.polygon([(430, y0 - 60), (594, y0 - 60), (512, y0 - 150)], fill=col)
    return .8


def rocket(d, t, c, on):
    dy = -24 * math.sin(TAU * t)
    fl = 170 + 50 * math.sin(2 * TAU * t)
    d.polygon([(420, 760 + dy), (604, 760 + dy), (512, 760 + fl + dy)], fill=(255, 170, 50))
    d.polygon([(460, 760 + dy), (564, 760 + dy), (512, 760 + fl * .6 + dy)], fill=(255, 240, 160))
    d.polygon([(400, 520 + dy), (230, 720 + dy), (230, 800 + dy), (400, 730 + dy)], fill=c)
    d.polygon([(624, 520 + dy), (794, 720 + dy), (794, 800 + dy), (624, 730 + dy)], fill=c)
    d.ellipse((372, 90 + dy, 652, 800 + dy), fill=c)
    d.ellipse((442, 300 + dy, 582, 440 + dy), fill=CLEAR)
    return .9


def shield(d, t, c, on):
    poly(d, [(512, 130), (840, 240), (840, 520), (512, 900), (184, 520), (184, 240)], c, 40)
    p = min(1, t / .4) if t < .9 else (1 - t) / .1
    pts = [(350, 520), (470, 640), (690, 400)]
    k = p * 510
    for a, b in zip(pts, pts[1:]):
        L = math.dist(a, b)
        if k > 0:
            f = min(1, k / L)
            line(d, a, (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f), CLEAR, 70)
        k -= L
    return .8


def grid(d, t, c, on):
    for r in range(3):
        for q in range(3):
            x, y = 152 + 260 * q, 152 + 260 * r
            d.rounded_rectangle((x, y, x + 200, y + 200), 50, fill=dim(c, .4 + .6 * max(0, math.sin(TAU * (t - (r + q) / 6))) ** 2))
    return .8


def gamepad(d, t, c, on):
    d.rounded_rectangle((90, 300, 934, 720), 200, fill=c)
    d.ellipse((130, 520, 430, 860), fill=c)
    d.ellipse((594, 520, 894, 860), fill=c)
    line(d, (220, 505), (380, 505), CLEAR, 56)
    line(d, (300, 425), (300, 585), CLEAR, 56)
    k = int(t * 4) % 4
    for i, (x, y) in enumerate(((724, 425), (724, 585), (644, 505), (804, 505))):
        d.ellipse((x - 40, y - 40, x + 40, y + 40), fill=CLEAR)
        if i == k:
            d.ellipse((x - 28, y - 28, x + 28, y + 28), fill=(255, 255, 255))
    return .8


def music(d, t, c, on):
    dy = -35 * max(0, math.sin(TAU * t))
    for x, y in ((330, 730), (720, 650)):
        d.ellipse((x - 115, y - 95 + dy, x + 115, y + 95 + dy), fill=c)
    line(d, (425, 730 + dy), (425, 280 + dy), c, 56)
    line(d, (815, 650 + dy), (815, 200 + dy), c, 56)
    d.polygon([(397, 260 + dy), (843, 160 + dy), (843, 300 + dy), (397, 400 + dy)], fill=c)
    return .8


def sun(d, t, c, on):
    if on:
        d.ellipse((342, 342, 682, 682), fill=c)
        for k in range(8):
            a = math.radians(t * 45 + k * 45)
            line(d, (512 + 270 * math.cos(a), 512 + 270 * math.sin(a)), (512 + 380 * math.cos(a), 512 + 380 * math.sin(a)), c, 50)
    else:
        d.ellipse((342, 342, 682, 682), outline=c, width=44)
        for k in range(8):
            a = math.radians(k * 45 + 22.5)
            line(d, (512 + 300 * math.cos(a), 512 + 300 * math.sin(a)), (512 + 350 * math.cos(a), 512 + 350 * math.sin(a)), c, 40)
    return .9


def shuffle(d, t, c, on):
    A = [(130, 300), (380, 300), (640, 724), (800, 724)]
    B = [(130, 724), (380, 724), (640, 300), (800, 300)]
    for P in (A, B):
        for a, b in zip(P, P[1:]):
            line(d, a, b, c)
    d.polygon([(790, 640), (790, 808), (930, 724)], fill=c)
    d.polygon([(790, 216), (790, 384), (930, 300)], fill=c)
    if on:
        for P in (A, B):
            x, y = polypos(P, t)
            d.ellipse((x - 40, y - 40, x + 40, y + 40), fill=(255, 255, 255))
    return .8


MORE = [("volume_up", volume_up, "cyan", None), ("volume_down", volume_down, "cyan", None), ("home", home, "orange", None),
        ("folder", folder, "gold", None), ("globe", globe, "cyan", None), ("clock", clock, "violet", None),
        ("monitor", monitor, "cyan", "slash"), ("headphones", headphones, "pink", "slash"), ("keyboard", keyboard, "green", None),
        ("terminal", terminal, "green", None), ("trash", trash, "red", None), ("search", search, "violet", None),
        ("mail", mail, "gold", None), ("copy", copy, "cyan", None), ("smile", smile, "gold", None),
        ("clapper", clapper, "orange", None), ("cloud", cloud, "cyan", None), ("rocket", rocket, "violet", None),
        ("shield", shield, "green", None), ("grid", grid, "pink", None), ("gamepad", gamepad, "violet", None),
        ("music", music, "pink", None), ("sun", sun, "gold", "plain"), ("shuffle", shuffle, "green", "plain")]


def sheet():
    import glob
    fs = sorted(glob.glob("icons/*.gif"))
    cols, th = 10, 128
    sh = Image.new("RGB", (cols * th, -(-len(fs) // cols) * th))
    for i, f in enumerate(fs):
        im = Image.open(f)
        im.seek(min(10, im.n_frames - 1))
        sh.paste(im.convert("RGB").resize((th, th), Image.LANCZOS), (i % cols * th, i // cols * th))
    sh.save("icons_sheet.png")


if __name__ == "__main__":
    for name, fn, col, off in MORE:
        c = C[col]
        if off is None:
            save(name, frames(fn, c, True))
        else:
            save(f"{name}_on", frames(fn, c, True))
            save(f"{name}_off", frames(fn, c, False, off == "slash"))
    sheet()
