"""Ek ikon seti 3. Calistir: python more_icons2.py  (icons/ klasorune ekler, tabloyu yeniler)"""
from more_icons import *  # noqa

BG = (12, 13, 20)


def calendar(d, t, c, on):
    d.rounded_rectangle((110, 200, 914, 880), 80, fill=c)
    d.rounded_rectangle((290, 110, 370, 290), 40, fill=c)
    d.rounded_rectangle((654, 110, 734, 290), 40, fill=c)
    d.line([(182, 400), (842, 400)], fill=CLEAR, width=30)
    k = int(t * 8) % 8
    for i in range(8):
        x, y = 200 + 170 * (i % 4), 470 + 160 * (i // 4)
        d.rounded_rectangle((x, y, x + 110, y + 110), 24, fill=(255, 255, 255) if i == k else CLEAR)
    return .8


def bookmark(d, t, c, on):
    dy = -40 * max(0, math.sin(TAU * t)) ** 2
    poly(d, [(260, 140 + dy), (764, 140 + dy), (764, 880 + dy), (512, 680 + dy), (260, 880 + dy)], c, 60)
    star4(d, 760, 200 + dy, 90 * math.sin(math.pi * t), (255, 255, 255))
    return .8


def eye(d, t, c, on):
    top = [(x, 512 - 270 * (1 - ((x - 512) / 400) ** 2) ** .8) for x in range(112, 913, 20)]
    bot = [(x, 1024 - y) for x, y in reversed(top)]
    pts = top + bot
    d.line(pts + pts[:2], fill=c, width=44, joint="curve")
    ox = 50 * math.sin(TAU * t) if on else 0
    d.ellipse((512 + ox - 150, 362, 512 + ox + 150, 662), fill=c)
    d.ellipse((512 + ox - 62, 450, 512 + ox + 62, 574), fill=CLEAR)
    return .8


def link(d, t, c, on):
    s = 22 * math.sin(TAU * t)
    for a, b in (((290 - s, 290 - s), (470 - s, 470 - s)), ((554 + s, 554 + s), (734 + s, 734 + s))):
        line(d, a, b, c, 200)
        line(d, a, b, CLEAR, 80)
    line(d, (410, 410), (614, 614), c, 56)
    return .8


def key(d, t, c, on):
    d.ellipse((140, 322, 520, 702), outline=c, width=72)
    line(d, (500, 512), (880, 512), c, 72)
    line(d, (760, 512), (760, 650), c, 64)
    line(d, (860, 512), (860, 620), c, 64)
    return .8


ROT[key] = (lambda t: 8 * math.sin(TAU * t), (330, 512))


def trophy(d, t, c, on):
    d.ellipse((90, 190, 310, 450), outline=c, width=48)
    d.ellipse((714, 190, 934, 450), outline=c, width=48)
    d.polygon([(270, 130), (754, 130), (700, 500), (512, 650), (324, 500)], fill=c)
    d.rounded_rectangle((462, 620, 562, 780), 20, fill=c)
    d.rounded_rectangle((330, 770, 694, 890), 40, fill=c)
    star4(d, 512, 340, 110 * (.7 + .3 * math.sin(TAU * t)), (255, 255, 255))
    return .8


def crown(d, t, c, on):
    poly(d, [(130, 760), (170, 320), (340, 520), (512, 230), (684, 520), (854, 320), (894, 760)], c, 40)
    d.rounded_rectangle((130, 790, 894, 890), 40, fill=c)
    for i, (x, y) in enumerate(((170, 320), (512, 230), (854, 320))):
        r = 36 + 18 * max(0, math.sin(TAU * (t - i / 3)))
        d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 255, 255))
    return .8


def diamond(d, t, c, on):
    poly(d, [(300, 260), (724, 260), (920, 460), (512, 900), (104, 460)], c, 40)
    for a, b in (((104, 460), (920, 460)), ((300, 260), (420, 460)), ((724, 260), (604, 460)), ((420, 460), (512, 900)), ((604, 460), (512, 900))):
        d.line([a, b], fill=CLEAR, width=22)
    star4(d, 640, 330, 120 * max(0, math.sin(math.pi * t)), (255, 255, 255))
    return .8


def hourglass(d, t, c, on):
    d.rounded_rectangle((190, 100, 834, 180), 30, fill=c)
    d.rounded_rectangle((190, 844, 834, 924), 30, fill=c)
    for P in ([(260, 200), (764, 200), (512, 512)], [(260, 824), (764, 824), (512, 512)]):
        d.line(P + P[:2], fill=c, width=44, joint="curve")
    f = min(1, t / .08, (1 - t) / .08)  # kum dongu basinda/sonunda solar: dikis gorunmez
    y = 215 + 270 * t
    hw = 230 * (512 - y) / 312
    if hw > 5:
        d.polygon([(512 - hw, y), (512 + hw, y), (512, 505)], fill=dim(c, .8 * f))
    yt = 810 - 280 * t
    hb = 230 * (810 - yt) / 300
    d.polygon([(512 - hb, 810), (512 + hb, 810), (512, yt)], fill=dim(c, .8 * f))
    if t < .95:
        d.line([(512, 520), (512, 790)], fill=dim(c, .8 * f), width=12)
    return .8


def target(d, t, c, on):
    for i, r in enumerate((380, 260)):
        d.ellipse((512 - r, 512 - r, 512 + r, 512 + r), outline=dim(c, .3 + .7 * max(0, math.sin(TAU * (t - i / 3) + math.pi / 2)) ** 2), width=48)
    d.ellipse((392, 392, 632, 632), fill=dim(c, .3 + .7 * max(0, math.sin(TAU * (t - 2 / 3) + math.pi / 2)) ** 2))
    return .8


def chart(d, t, c, on):
    for i, h in enumerate((220, 360, 500, 700)):
        hh = h * (.85 + .15 * math.sin(TAU * (t + i / 4)))
        d.rounded_rectangle((140 + 200 * i, 880 - hh, 280 + 200 * i, 880), 50, fill=dim(c, .55 + .45 * i / 3))
    return .8


FONT2 = ImageFont.truetype("arialbd.ttf", 470)


def coin(d, t, c, on):
    dy = -45 * max(0, math.sin(TAU * t))
    d.ellipse((112, 112 + dy, 912, 912 + dy), fill=c)
    d.ellipse((212, 212 + dy, 812, 812 + dy), outline=CLEAR, width=26)
    d.text((512, 520 + dy), "$", font=FONT2, fill=CLEAR, anchor="mm")
    star4(d, 800, 230 + dy, 90 * math.sin(math.pi * ((t + .3) % 1)), (255, 255, 255))
    return .8


def code(d, t, c, on):
    parts = [[(330, 320), (150, 512), (330, 704)], [(694, 320), (874, 512), (694, 704)]]
    for i, P in enumerate(parts):
        col = dim(c, .45 + .55 * max(0, math.sin(TAU * (t - i * .5) + math.pi / 2)))
        line(d, P[0], P[1], col, 60)
        line(d, P[1], P[2], col, 60)
    line(d, (590, 250), (434, 774), dim(c, .45 + .55 * max(0, math.sin(TAU * (t - .25) + math.pi / 2))), 60)
    return .8


def upload(d, t, c, on):
    dy = -40 * math.sin(TAU * t)
    line(d, (512, 400 + dy), (512, 760 + dy), c)
    poly(d, [(290, 420 + dy), (734, 420 + dy), (512, 170 + dy)], c, 40)
    line(d, (200, 890), (824, 890), c)
    return .8


def refresh(d, t, c, on):
    for s in (0, 180):
        a = t * 360 + s
        arc(d, 512, 512, 380, a, a + 140, c)
        e = math.radians(a + 140)
        ex, ey = 512 + 352 * math.cos(e), 512 + 352 * math.sin(e)
        tx, ty, nx, ny = -math.sin(e), math.cos(e), math.cos(e), math.sin(e)
        d.polygon([(ex + tx * 130, ey + ty * 130), (ex + nx * 100, ey + ny * 100), (ex - nx * 100, ey - ny * 100)], fill=c)
    return .8


def ghost(d, t, c, on):
    dy = -30 * math.sin(TAU * t)
    d.ellipse((212, 120 + dy, 812, 720 + dy), fill=c)
    d.rectangle((212, 420 + dy, 812, 870 + dy), fill=c)
    for x in (312, 512, 712):
        d.ellipse((x - 100, 790 + dy, x + 100, 990 + dy), fill=CLEAR)
    ox = 18 * math.sin(TAU * t)
    for x in (400, 624):
        d.ellipse((x + ox - 55, 380 + dy - 70, x + ox + 55, 380 + dy + 70), fill=CLEAR)
    d.ellipse((472, 540 + dy, 552, 640 + dy), fill=CLEAR)
    return .8


def wand(d, t, c, on):
    line(d, (230, 860), (680, 410), c, 76)
    star4(d, 770, 320, 170 * (.7 + .3 * math.sin(TAU * t)), (255, 240, 150))
    for k, (x, y) in enumerate(((880, 560), (600, 170), (910, 160))):
        star4(d, x, y, 70 * math.sin(math.pi * ((t + k / 3) % 1)), (255, 255, 255))
    return .8


def snowflake(d, t, c, on):
    for k in range(6):
        a = math.radians(t * 60 + k * 60)
        ca, sa = math.cos(a), math.sin(a)
        line(d, (512, 512), (512 + 380 * ca, 512 + 380 * sa), c, 40)
        bx, by = 512 + 260 * ca, 512 + 260 * sa
        for da in (-45, 45):
            b = a + math.radians(da)
            line(d, (bx, by), (bx + 110 * math.cos(b), by + 110 * math.sin(b)), c, 36)
    return .8


def rain(d, t, c, on):
    d.ellipse((180, 270, 480, 570), fill=c)
    d.ellipse((310, 140, 710, 540), fill=c)
    d.ellipse((540, 270, 840, 570), fill=c)
    d.rectangle((330, 420, 690, 570), fill=c)
    for k in range(4):
        u = (t + k / 4) % 1
        x, y = 280 + 150 * k - 40 * u, 640 + 240 * u
        line(d, (x, y), (x - 30, y + 80), mix((255, 255, 255), BG, u), 40)
    return .8


MORE2 = [("calendar", calendar, "violet", None), ("bookmark", bookmark, "orange", None), ("eye", eye, "cyan", "slash"),
         ("link", link, "green", None), ("key", key, "gold", None), ("trophy", trophy, "gold", None),
         ("crown", crown, "gold", None), ("diamond", diamond, "cyan", None), ("hourglass", hourglass, "orange", None),
         ("target", target, "red", None), ("chart", chart, "green", None), ("coin", coin, "gold", None),
         ("code", code, "violet", None), ("upload", upload, "cyan", None), ("refresh", refresh, "green", None),
         ("ghost", ghost, "violet", None), ("wand", wand, "pink", None), ("snowflake", snowflake, "cyan", None),
         ("rain", rain, "cyan", None)]

if __name__ == "__main__":
    for name, fn, col, off in MORE2:
        c = C[col]
        if off is None:
            save(name, frames(fn, c, True))
        else:
            save(f"{name}_on", frames(fn, c, True))
            save(f"{name}_off", frames(fn, c, False, off == "slash"))
    sheet()
