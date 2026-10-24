"""QA: dongu dikisi atlamasi, kenara tasma, tek-kare hatasi. Calistir: python qa.py"""
import glob, os
import numpy as np
from PIL import Image, ImageSequence


def load(f):
    im = Image.open(f)
    out = []
    for fr in ImageSequence.Iterator(im):
        out += [np.asarray(fr.convert("RGB"), dtype=np.int16)] * max(1, fr.info.get("duration", 40) // 40)
    return out


for d in ("icons", "icons_brand"):
    for f in sorted(glob.glob(f"{d}/*.gif")):
        fr = load(f)
        n = len(fr)
        diffs = [np.abs(fr[(i + 1) % n] - fr[i]).mean() for i in range(n)] if n > 1 else [0]
        med, mx, seam = np.median(diffs), max(diffs), diffs[-1]
        flags = []
        if n > 1 and mx > 3 * max(med, .15) and mx > .8:
            flags.append(f"ATLAMA kare{int(np.argmax(diffs))}->{(int(np.argmax(diffs)) + 1) % n} (maks {mx:.2f}, medyan {med:.2f})")
        edge = max(np.concatenate([x[:4].ravel(), x[-4:].ravel(), x[:, :4].ravel(), x[:, -4:].ravel()]).max() for x in fr)
        if edge > 110:
            flags.append(f"KENARA TASIYOR (piksel {edge})")
        if n == 144 or n < 1:
            flags.append("KARE SAYISI?")
        if flags:
            print(os.path.basename(f), n, "kare |", "; ".join(flags))
print("bitti")
