"""Marka tarzi ikonlar (YouTube, Twitch, Spotify, X, Instagram, Discord). Calistir: python brand_icons.py -> icons_brand/*.gif
Ticari marka tasir: kisisel kullanim icin; Market paketine KOYMA."""
import os
from more_icons import *  # noqa

BG = (12, 13, 20)
C.update({"yt": (255, 30, 30), "tw": (145, 70, 255), "sp": (30, 215, 96), "xx": (235, 235, 240),
          "ig": (225, 48, 108), "dc": (88, 101, 242)})


def youtube(d, t, c, on):
    d.rounded_rectangle((70, 250, 954, 774), 190, fill=c)
    s = 1 + .12 * math.sin(TAU * t)
    d.polygon([(512 + (x - 512) * s, 512 + (y - 512) * s) for x, y in ((420, 370), (420, 654), (668, 512))], fill=(255, 255, 255))
    return .7 + .3 * math.sin(TAU * t) ** 2


def twitch(d, t, c, on):
    poly(d, [(190, 130), (850, 130), (850, 590), (660, 590), (520, 730), (520, 590), (190, 590)], c, 44)
    for x in (480, 680):
        h = 190 * (.15 if abs(t - .5) < .05 else 1)
        d.rounded_rectangle((x - 32, 360 - h / 2, x + 32, 360 + h / 2), 20, fill=CLEAR)
    return .8


def spotify(d, t, c, on):
    d.ellipse((92, 92, 932, 932), fill=c)
    for i, (r, dy) in enumerate(((400, 0), (320, 30), (240, 60))):
        b = .4 + .6 * max(0, math.sin(TAU * (t - i / 6) + math.pi / 2)) ** 2
        arc(d, 512, 800 + dy, r, 228, 312, mix(c, BG, b))
    return .8


def xlogo(d, t, c, on):
    line(d, (210, 190), (814, 834), c, 110)
    line(d, (814, 190), (210, 834), c, 40)
    return .5 + .4 * math.sin(TAU * t) ** 2


def instagram(d, t, c, on):
    d.rounded_rectangle((110, 110, 914, 914), 260, outline=c, width=64)
    d.ellipse((322, 322, 702, 702), outline=c, width=60)
    r = 42 * (1 + .25 * math.sin(TAU * t))
    d.ellipse((730 - r, 294 - r, 730 + r, 294 + r), fill=c)
    return .8


def discord(d, t, c, on):
    d.rounded_rectangle((100, 250, 924, 740), 190, fill=c)
    d.ellipse((150, 560, 410, 830), fill=c)
    d.ellipse((614, 560, 874, 830), fill=c)
    dy = 14 * math.sin(TAU * t)
    for x in (360, 664):
        d.ellipse((x - 55, 470 + dy - 80, x + 55, 470 + dy + 80), fill=CLEAR)
    return .8


BRANDS = [("youtube", youtube, "yt"), ("twitch", twitch, "tw"), ("spotify", spotify, "sp"),
          ("x", xlogo, "xx"), ("instagram", instagram, "ig"), ("discord", discord, "dc")]

if __name__ == "__main__":
    os.makedirs("icons_brand", exist_ok=True)
    for name, fn, col in BRANDS:
        save(name, frames(fn, C[col], True))
        os.replace(f"icons/{name}.gif", f"icons_brand/{name}.gif")
