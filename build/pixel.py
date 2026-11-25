# 픽셀 대체 표지 — 15층 프로그래밍 연구소 건물 (SVG, shape-rendering="crispEdges")
# 장면 96×54 격자. 왼쪽은 건물(층 = 주차), 오른쪽은 주제 소품. 그림 안에 글자를 넣지 않는다.
W, H = 96, 54
K = '#2a2f3a'
PAL = dict(k=K, w='#ffffff', g='#e3e8ee', G='#c9d2dc', s='#9aa5b1', b='#cfe0f7', B='#5b86c9', m='#cdeedd', M='#2f9a62',
           p='#f3d6ea', P='#c42a6e', l='#e6dcf7', L='#7a3fd6', y='#fbe7b0', Y='#d69e2e', o='#f4c7a1', O='#b8642b',
           r='#f6c6c3', R='#c93030', t='#bfe6ea', T='#0b7a86', n='#8a6a4a', N='#5e4630', sky='#eef5fb', gr='#9fd3a8')
def P(c): return PAL.get(c, c)

class Grid:
    def __init__(s, w, h): s.w, s.h, s.c = w, h, [[None] * w for _ in range(h)]
    def px(s, x, y, col):
        if 0 <= x < s.w and 0 <= y < s.h: s.c[y][x] = P(col)
    def fill(s, x, y, w, h, col):
        for j in range(h):
            for i in range(w): s.px(x + i, y + j, col)
    def rect(s, x, y, w, h, fill, line='k'):
        for j in range(h):
            for i in range(w):
                s.px(x + i, y + j, line if (line and (i in (0, w - 1) or j in (0, h - 1))) else fill)
    def hline(s, x, y, n, col='k'):
        for i in range(n): s.px(x + i, y, col)
    def vline(s, x, y, n, col='k'):
        for j in range(n): s.px(x, y + j, col)
    def disc(s, cx, cy, r, fill, line='k'):
        for y in range(cy - r, cy + r + 1):
            for x in range(cx - r, cx + r + 1):
                d = (x - cx) ** 2 + (y - cy) ** 2
                if d <= r * r + r * .6: s.px(x, y, line if d > (r - 1) ** 2 + (r - 1) * .6 else fill)
    def svg(s):
        out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" shape-rendering="crispEdges" aria-hidden="true">' % (s.w, s.h)]
        for y in range(s.h):
            x = 0
            while x < s.w:
                col = s.c[y][x]
                if col is None: x += 1; continue
                n = 1
                while x + n < s.w and s.c[y][x + n] == col: n += 1
                out.append('<rect x="%d" y="%d" width="%d" height="1" fill="%s"/>' % (x, y, n, col)); x += n
        out.append('</svg>')
        return ''.join(out)

def building(g, cur, done=10):
    x0, wd = 5, 36
    g.fill(x0 - 1, 2, wd + 2, 1, 'k'); g.fill(x0 + 12, 0, 12, 2, 'k')  # 옥상
    g.fill(x0 + 16, 0, 4, 1, 'Y')
    for i in range(1, 16):
        y = 49 - i * 3
        lit = i <= done; here = i == cur
        g.fill(x0, y, wd, 3, 'g' if not here else 'y')
        g.hline(x0, y + 2, wd, 'G')
        for wx in range(x0 + 3, x0 + wd - 3, 5):
            col = ('M' if here else 'Y') if lit else ('s' if i < 16 else 'g')
            g.fill(wx, y, 3, 2, col if lit else 'G')
            if lit and not here: g.px(wx, y, 'w')
        if i > done:  # 공사 중 — 비계
            g.px(x0 + 1, y + 1, 'O'); g.px(x0 + wd - 2, y + 1, 'O')
            for k in range(x0, x0 + wd, 4): g.px(k, y + 1, 'Y')
    g.vline(x0 - 1, 3, 47); g.vline(x0 + wd, 3, 47)
    if cur and 1 <= cur <= 15:
        y = 49 - cur * 3
        g.hline(x0 - 2, y - 1, wd + 4, 'O'); g.hline(x0 - 2, y + 3, wd + 4, 'O')
        g.fill(x0 + wd + 1, y, 3, 3, 'O')
    g.fill(x0 + 14, 46, 8, 4, 'B'); g.vline(x0 + 18, 46, 4, 'k')  # 정문

def prop(g, n):
    ox, oy = 50, 14
    if n in ('00', '01'):  # 로비: 안내 데스크와 모니터
        g.rect(ox + 2, oy + 18, 34, 10, 'n', 'N'); g.rect(ox + 8, oy + 4, 22, 14, 'w')
        g.fill(ox + 10, oy + 6, 18, 10, 'b')
        for j, c in enumerate('MBYRL'): g.hline(ox + 11 + (j % 2) * 2, oy + 7 + j * 2, 8 + j % 3 * 3, c)
        g.fill(ox + 17, oy + 18, 4, 1, 'k')
    elif n == '02':  # 택시와 동전
        g.rect(ox + 4, oy + 12, 30, 9, 'y', 'k'); g.rect(ox + 10, oy + 6, 18, 7, 'b', 'k'); g.vline(ox + 19, oy + 6, 7)
        g.disc(ox + 11, oy + 21, 3, 's'); g.disc(ox + 27, oy + 21, 3, 's'); g.fill(ox + 17, oy + 4, 4, 2, 'R')
        g.disc(ox + 38, oy + 6, 3, 'Y')
    elif n == '03':  # 점수판: 두 막대와 돋보기
        g.rect(ox + 2, oy + 2, 34, 24, 'w'); g.fill(ox + 8, oy + 12, 6, 13, 'B'); g.fill(ox + 18, oy + 7, 6, 18, 'O'); g.fill(ox + 28, oy + 16, 4, 9, 'M')
        g.disc(ox + 33, oy + 24, 4, 't'); g.hline(ox + 36, oy + 28, 4); g.hline(ox + 37, oy + 29, 4)
    elif n == '04':  # 도미와 빙어, 저울
        g.disc(ox + 14, oy + 10, 7, 'B'); g.fill(ox + 21, oy + 7, 5, 7, 'B'); g.px(ox + 10, oy + 8, 'w'); g.px(ox + 10, oy + 9, 'k')
        g.fill(ox + 26, oy + 9, 9, 3, 'R'); g.px(ox + 34, oy + 9, 'k'); g.fill(ox + 24, oy + 8, 2, 5, 'R')
        g.fill(ox + 4, oy + 22, 32, 2, 'k'); g.fill(ox + 19, oy + 19, 2, 3, 'k'); g.rect(ox + 12, oy + 24, 16, 4, 'G')
    elif n == '05':  # 의사결정나무
        g.rect(ox + 16, oy + 1, 8, 5, 'l', 'L')
        for x in (ox + 6, ox + 28): g.rect(x, oy + 11, 8, 5, 'l', 'L')
        for x in (ox + 1, ox + 11, ox + 23, ox + 33): g.rect(x, oy + 21, 6, 5, 'm' if x % 2 else 'r')
        g.vline(ox + 19, oy + 6, 3); g.hline(ox + 10, oy + 9, 22); g.vline(ox + 10, oy + 9, 2); g.vline(ox + 31, oy + 9, 2)
        g.vline(ox + 9, oy + 16, 3); g.hline(ox + 4, oy + 19, 11); g.vline(ox + 4, oy + 19, 2); g.vline(ox + 14, oy + 19, 2)
        g.vline(ox + 31, oy + 16, 3); g.hline(ox + 26, oy + 19, 11); g.vline(ox + 26, oy + 19, 2); g.vline(ox + 36, oy + 19, 2)
    elif n == '06':  # 직선으로 가르기 + 여유 폭
        for i, (x, y) in enumerate([(4, 6), (8, 10), (6, 15), (12, 5), (11, 13), (24, 20), (28, 16), (30, 24), (33, 19), (26, 26)]):
            g.fill(ox + x, oy + y, 2, 2, 'R' if i < 5 else 'B')
        for t in range(30):
            yy = int(oy + 27 - t * .8); g.px(ox + 4 + t, yy, 'k'); g.px(ox + 8 + t, yy, 'T'); g.px(ox + t, yy, 'T')
    elif n == '07':  # 배터리와 톱니
        g.rect(ox + 4, oy + 6, 22, 14, 'w'); g.fill(ox + 26, oy + 10, 2, 6, 'k')
        for i in range(4): g.fill(ox + 6 + i * 5, oy + 8, 4, 10, 'M' if i < 3 else 'g')
        g.disc(ox + 33, oy + 22, 5, 's'); g.disc(ox + 33, oy + 22, 2, 'w')
        for dx, dy in ((0, -6), (0, 6), (-6, 0), (6, 0)): g.fill(ox + 32 + dx, oy + 21 + dy, 2, 2, 'k')
    elif n == '08':  # 점검표
        g.rect(ox + 8, oy + 2, 24, 28, 'w'); g.fill(ox + 15, oy + 1, 10, 3, 's')
        for j in range(5):
            g.rect(ox + 11, oy + 7 + j * 4, 3, 3, 'm' if j < 4 else 'w'); g.hline(ox + 16, oy + 8 + j * 4, 12, 'G')
    elif n == '09':  # 기여도 막대
        g.rect(ox + 2, oy + 2, 36, 26, 'w'); g.vline(ox + 12, oy + 4, 22, 's')
        for j, (a, b, c) in enumerate(((12, 26, 'R'), (12, 20, 'R'), (6, 12, 'B'), (9, 12, 'B'))): g.fill(ox + min(a, b), oy + 6 + j * 5, abs(b - a) or 1, 3, c)
    elif n == '10':  # 방패와 우산 (보험)
        g.fill(ox + 6, oy + 6, 14, 12, 'B'); g.fill(ox + 8, oy + 18, 10, 3, 'B'); g.fill(ox + 10, oy + 21, 6, 2, 'B'); g.fill(ox + 12, oy + 9, 2, 8, 'w'); g.fill(ox + 9, oy + 12, 8, 2, 'w')
        g.disc(ox + 30, oy + 10, 7, 'R')
        g.fill(ox + 23, oy + 11, 15, 2, 'w'); g.vline(ox + 30, oy + 11, 13); g.hline(ox + 28, oy + 24, 3)
    else:  # 공사 중
        g.vline(ox + 30, oy + 0, 28, 'Y'); g.hline(ox + 10, oy + 1, 24, 'Y'); g.vline(ox + 12, oy + 2, 8, 'k'); g.rect(ox + 9, oy + 10, 7, 5, 'O')
        g.fill(ox + 4, oy + 24, 6, 4, 'O'); g.fill(ox + 5, oy + 20, 4, 4, 'O'); g.fill(ox + 6, oy + 17, 2, 3, 'O'); g.fill(ox + 5, oy + 22, 4, 1, 'w')

def scene(num, done=10):
    g = Grid(W, H)
    g.fill(0, 0, W, H, 'sky'); g.fill(0, 50, W, 4, 'gr'); g.hline(0, 50, W, 'M')
    cur = int(num) if num not in ('00', 'pr') else 0
    building(g, cur, done)
    prop(g, num if num in ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10') else 'x')
    return '<div class="px-scene">' + g.svg() + '</div>'

if __name__ == '__main__':
    open('/tmp/px.svg', 'w').write(scene('04')[24:-6])
