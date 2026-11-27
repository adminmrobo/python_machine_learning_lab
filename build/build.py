#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""파이썬 머신러닝 연구소 — 15층 연구실 해설 빌드
   build/pages/wNN.py(층 원고) → weeks/wNN_slug.html (단일 파일), index.html, data/KG_00_registry.json, cover_manifest.json
   사용: python3 build/build.py"""
import os, re, json, base64, html, glob, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import pixel
from pics import PIC
from aicards import CARDS as AICARDS
CSS = open(os.path.join(HERE, 'lab.css'), encoding='utf-8').read() + open(os.path.join(HERE, 'ml.css'), encoding='utf-8').read()
JS = open(os.path.join(HERE, 'lab.js'), encoding='utf-8').read() + '\n' + open(os.path.join(HERE, 'ml.js'), encoding='utf-8').read()
KGX = open(os.path.join(HERE, 'kgx.js'), encoding='utf-8').read()
TODAY = '2026-11-26'
SITE = 'https://adminmrobo.github.io/python_machine_learning_lab/'
REPO = 'https://github.com/adminmrobo/python_machine_learning_lab'
SERIES = '파이썬 머신러닝 연구소'
AUTHOR = '안상선'; AUTHOR_URL = 'https://adminmrobo.github.io/who_am_i/who_am_i.html'; AFFIL = '(주)M-Robo 대표'
LICENSE = 'CC BY-NC 4.0'
E = html.escape
EXM = {k: v['key'] for k, v in json.load(open(os.path.join(HERE, 'expression_map.json'), encoding='utf-8')).items() if isinstance(v, dict) and 'key' in v}
for w in ('x1', 'x2', 'x3'):
    EXM.update({w + '_smile': w + '_e13', w + '_joy': w + '_e01', w + '_think': w + '_e09', w + '_proud': w + '_e16', w + '_shock': w + '_e24', w + '_wow': w + '_e04'})
EXM.update({'sia_sleepy': 'sia_e17', 'robo_calc': EXM.get('robo_calc', 'robo_e09')})
NAMES = {'doc': '박사', 'asst': '조수 하루', 'fly': '초파리 연구원', 'robo': '주판봇', 'sia': '인턴 시아', 'moa': '인턴 모아', 'x1': 'X1', 'x2': 'X2', 'x3': 'X3'}
TEAM = {'sia': 'f', 'x1': 'f', 'x2': 'f', 'fly': 'f', 'moa': 'r', 'asst': 'r', 'x3': 'r', 'robo': 'r', 'doc': 'j'}
DUEL_KEYS = ['fly_point', 'robo_coin', 'fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'doc_think', 'asst_smile', 'robo_meh', 'asst_report', 'robo_calc', 'asst_shock', 'robo_blush', 'doc_front', 'asst_firm']
BANNED = ['사다리', '관통', '칸', '수포자', '통포자', '수학 포기', '수학을 포기', '쉽죠', '당연히', '기초인데']

def key_of(k):
    return EXM.get(k, k)

def sprite_b64(key):
    k = key_of(key); who = k.split('_')[0]
    p = os.path.join(HERE, 'sprites', who, k + '.webp')
    if not os.path.exists(p):
        base = {'doc': 'doc_e08', 'asst': 'asst_e13', 'fly': 'fly_e10', 'robo': 'robo_e13', 'sia': 'sia_e13', 'moa': 'moa_e13', 'x1': 'x1_e13', 'x2': 'x2_e13', 'x3': 'x3_e13'}.get(who)
        p = os.path.join(HERE, 'sprites', who, (base or '') + '.webp')
        if not base or not os.path.exists(p): return None, None
        k = base
    return k, 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def face(who, mood='smile', size=56, cls=''):
    return '<img data-who="%s" data-mood="%s" width="%d" height="%d" alt="" aria-hidden="true"%s>' % (who, mood, size, size, (' class="%s"' % cls) if cls else '')

def say(who, mood, text):
    return '<div class="say">%s<div class="bub"><span class="who w-%s">%s</span><p>%s</p></div></div>' % (face(who, mood), who if who in ('doc', 'asst', 'fly', 'robo', 'sia', 'moa') else 'sia', NAMES[who] + ({'f': ' · 초파리팀', 'r': ' · 주판봇팀', 'j': ' · 심판'}.get(TEAM.get(who), '') if who not in ('fly', 'robo') else (' · 조장')), text)

def slugify(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
def esc_json(o): return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')

SCENE_CLS = {'조별발표': 'team', '개인발표': 'team', '상담': 'talk-s', '토론': 'judge', '심사': 'judge', '쪽지시험': 'judge', '실습': 'talk-s', '복습': 'judge'}
def scene_chip(sc):
    kind, team, who = sc
    cls = 'team-f' if team == '초파리팀' else 'team-r' if team == '주판봇팀' else 'judge' if team in ('심판', '전체', '두 팀') else 'talk-s'
    return '<span class="scene %s">%s · %s%s</span>' % (cls, kind, team, (' · ' + who) if who else '')

TEAMS_HTML = None
def teams_html():
    def mem(w, m, role): return '<div class="mem">%s<div><b>%s</b> — %s</div></div>' % (face(w, m, 40), NAMES[w], role)
    return ('<div class="teams"><div class="team f"><h4>🔴 초파리팀 — “일단 의심하고 짚어 본다”</h4>%s%s%s%s</div>'
            '<div class="team r"><h4>🔵 주판봇팀 — “크게, 많이, 빨리 해 본다”</h4>%s%s%s%s</div></div>'
            '<div class="judgebar">%s<div><b>박사 — 심판</b> · 발표가 끝나면 데이터로 판정하고, 처음 오신 분이 막힐 곳을 짚어 주는 선생님 역할도 함께 맡습니다.</div></div>') % (
        mem('fly', 'clip', '조장. 크고 복잡한 것을 일단 의심한다'), mem('sia', 'smile', '인턴 1. 조용하고 꼼꼼한 정리 담당 (가끔 졸음)'), mem('x1', 'smile', '미공개 연구원. 질문이 짧고 날카롭다'), mem('x2', 'smile', '미공개 연구원. 숫자 확인 담당'),
        mem('robo', 'smile', '조장. 크고 많은 숫자를 좋아한다'), mem('moa', 'smile', '인턴 2. 기록을 모으고 응원이 제일 크다'), mem('asst', 'smile', '조수. 처음 배우는 사람의 눈높이로 묻고 숫자를 발표'), mem('x3', 'smile', '미공개 연구원. 막내, 실험을 먼저 눌러 본다'),
        face('doc', 'front', 52))

# ── 지식 그래프 ─────────────────────────────────
def build_kg(P):
    page = P['id']; nodes, edges, seen = [], [], set()
    def N(id, type, ko, en, anchor, **kw):
        if id in seen: return
        seen.add(id); n = {'id': id, 'type': type, 'label': {'ko': ko, 'en': en}, 'page': page, 'anchor': anchor, 'domain': ['ml'], 'status': 'known', 'confidence': kw.pop('confidence', 'high')}
        n.update({k: v for k, v in kw.items() if v is not None}); nodes.append(n)
    def Lk(s, p, o, anchor, conf='high'): edges.append({'s': s, 'p': 'lab:' + p, 'o': o, 'anchor': anchor, 'confidence': conf})
    topic = 'lab:topic/pyml-w%s' % P['num']
    N(topic, 'Topic', P['title'], P['title_en'], '#top', definition={'ko': P['question']})
    N('lab:topic/python-machine-learning', 'Area', '파이썬 머신러닝', 'python machine learning', '#top', definition={'ko': '데이터에서 규칙을 찾아 예측하는 방법을 파이썬으로 실습하는 분야.'})
    Lk(topic, 'broader', 'lab:topic/python-machine-learning', '#top')
    cids = []
    for i, s in enumerate(P['steps']):
        cid = s.get('cid') or ('lab:concept/' + slugify(s['en'])); cids.append(cid); anc = '#' + s['id']
        N(cid, s.get('ctype', 'Concept'), s['concept'], s['en'], anc, definition={'ko': s.get('def', s['title'])}, level=i + 1, family='ml')
        Lk(cid, 'broader', topic, anc)
        sec = 'lab:section/%s-%s' % (page, s['id']); N(sec, 'Section', '%s 단계 %d' % (P['short'], i + 1), 'step %d' % (i + 1), anc); Lk(cid, 'explainedIn', sec, anc)
        if i > 0: Lk(cids[i - 1], 'prerequisiteOf', cid, anc)
        if s.get('limit'):
            lid = 'lab:limitation/%s-%s' % (page, s['id']); N(lid, 'Limitation', s.get('limit_label', '이 단계의 한계'), 'limitation of ' + s['en'], anc, definition={'ko': re.sub('<[^>]+>', '', s['limit'])[:160]})
            Lk(cid, 'hasLimitation', lid, anc)
            if i + 1 < len(P['steps']):
                nx = P['steps'][i + 1]; Lk(lid, 'addressedBy', nx.get('cid') or ('lab:concept/' + slugify(nx['en'])), '#' + nx['id'])
        if s.get('pair'):
            aid = 'lab:analogy/%s-%s' % (page, s['id']); N(aid, 'Analogy', s.get('analogy', '일상 비유'), 'analogy: ' + s['en'], anc, definition={'ko': re.sub('<[^>]+>', '', s['pair'][0][1])[:160]}); Lk(aid, 'analogyOf', cid, anc)
        if s.get('sim'):
            sid = 'lab:simulation/%s-%s' % (page, s['id']); N(sid, 'Simulation', s['sim'], 'simulation: ' + s['en'], anc); Lk(cid, 'demonstratedBy', sid, anc)
        for qi, q in enumerate(s.get('quiz', [])):
            qid = 'lab:quiz/%s-%s-%d' % (page, s['id'], qi + 1); N(qid, 'QuizItem', re.sub('<[^>]+>', '', q['q'])[:60], 'quiz %s-%d' % (s['id'], qi + 1), anc); Lk(qid, 'assesses', cid, anc)
    sid_list = [s['id'] for s in P['steps']]
    for k, g in P.get('gloss', {}).items():
        tid = 'lab:term/' + g[3]; stepid = g[4] if len(g) > 4 and g[4] in sid_list else sid_list[0]; ci = sid_list.index(stepid)
        N(tid, 'Term', k, g[3].replace('-', ' '), '#' + stepid, definition={'ko': g[2]})
        Lk(tid, 'explainedIn', 'lab:section/%s-%s' % (page, stepid), '#' + stepid); Lk(tid, 'partOf', cids[ci], '#' + stepid)
    for r in P['refs']: N('lab:work/' + r['id'], 'Work', r['title'], r.get('title_en', r['title']), '#sources')
    used = set()
    for f in P.get('facts', []):
        fid, text, kind, ref, stepid, loc = f; stepid = stepid if stepid in sid_list else sid_list[0]; ci = sid_list.index(stepid)
        cl = 'lab:claim/%s-%s' % (page, fid.lower())
        if kind == '미확인':
            q = cl.replace('claim', 'question'); N(q, 'Question', text, 'open question ' + fid, '#' + stepid, confidence='low'); Lk(cids[ci], 'raises', q, '#' + stepid, 'low'); continue
        N(cl, 'Claim', text, 'claim ' + fid, '#' + stepid, evidence=[fid], source=[{'ref': ref, 'loc': loc}]); Lk(cl, 'supports', cids[ci], '#' + stepid); Lk(cl, 'assertedIn', 'lab:work/' + ref, '#' + stepid); used.add(ref)
    for r in P['refs']:
        if r['id'] not in used: Lk(topic, 'derivedFrom', 'lab:work/' + r['id'], '#sources')
    N('lab:question/%s-core' % page, 'Question', P['question'], 'core question', '#top'); Lk(topic, 'raises', 'lab:question/%s-core' % page, '#top')
    d = P['duel']; dq = 'lab:question/%s-duel' % page; N(dq, 'Question', d['q'], 'duel question', '#duel'); Lk(cids[-1], 'raises', dq, '#duel')
    m1, m2, mt = 'lab:method/%s-fly' % page, 'lab:method/%s-robo' % page, 'lab:metric/%s' % page
    N(m1, 'Method', d['fly_pick'], 'option A (team fruit fly)', '#duel', definition={'ko': d['fly_line']}); N(m2, 'Method', d['robo_pick'], 'option B (team abacus bot)', '#duel', definition={'ko': d['robo_line']}); N(mt, 'Metric', d['metric'], 'duel metric', '#duel')
    st = min(d.get('step', len(cids) - 1), len(cids) - 1)
    Lk(m1, 'contrastsWith', m2, '#duel'); Lk(m1, 'evaluatedBy', mt, '#duel'); Lk(m2, 'evaluatedBy', mt, '#duel'); Lk(m1, 'relatedTo', cids[st], '#duel'); Lk(m2, 'relatedTo', cids[st], '#duel')
    for pre in P.get('prereq', []):
        pid = 'lab:topic/pyml-w%s' % pre; N(pid, 'Topic', '%d층' % int(pre), 'floor %d' % int(pre), '#top'); Lk(pid, 'prerequisiteOf', topic, '#top')
    ids = {n['id'] for n in nodes}
    for e in edges: assert e['s'] in ids and e['o'] in ids, (page, e)
    deg = {i: 0 for i in ids}
    for e in edges: deg[e['s']] += 1; deg[e['o']] += 1
    iso = [i for i, v in deg.items() if v == 0]; assert not iso, (page, iso)
    return {'version': '1.0', 'page': page, 'domain': ['ml'], 'nodes': nodes, 'edges': edges}

def jsonld(kg, meta):
    ctx = {'@vocab': 'urn:lab:', 'lab': 'urn:lab:', 'skos': 'http://www.w3.org/2004/02/skos/core#', 'schema': 'https://schema.org/'}
    g = []
    for n in kg['nodes']:
        t = ['lab:' + n['type']] + (['skos:Concept', 'schema:DefinedTerm'] if n['type'] in ('Concept', 'Method', 'Term', 'Limitation', 'Metric', 'Topic', 'Area') else [])
        o = {'@id': n['id'], '@type': t, 'skos:prefLabel': [{'@value': n['label']['ko'], '@language': 'ko'}, {'@value': n['label']['en'], '@language': 'en'}]}
        if n.get('definition'): o['skos:definition'] = {'@value': n['definition']['ko'], '@language': 'ko'}
        g.append(o)
    for e in kg['edges']: g.append({'@id': e['s'], e['p']: {'@id': e['o']}})
    g.append({'@id': meta['url'], '@type': 'schema:LearningResource', 'schema:name': meta['title'], 'schema:inLanguage': 'ko', 'schema:author': {'@type': 'schema:Person', 'schema:name': AUTHOR}, 'schema:license': LICENSE})
    return {'@context': ctx, '@graph': g}

# ── 조각 ───────────────────────────────────────
def cover_img(key, alt, chip, rel='../'):
    if os.path.exists(os.path.join(ROOT, 'assets', 'img', key + '.webp')):
        # 표지: 1920(1x)과 원본 크기(2x) 두 장 — 고해상도 화면은 2x를 받음
        hp = os.path.join(ROOT, 'assets', 'img', key + '@2x.webp'); srcset = ''
        if os.path.exists(hp):
            from PIL import Image
            srcset = ' srcset="%sassets/img/%s.webp 1920w, %sassets/img/%s@2x.webp %dw" sizes="100vw"' % (rel, key, rel, key, Image.open(hp).width)
        return ('<!-- lab-cover --><header class="cover has-img" id="cover" role="img" aria-label="%s"><img class="cover-img" src="%sassets/img/%s.webp"%s width="1920" height="1080" alt="%s" decoding="async" fetchpriority="high">'
                '<span class="cover-chip">%s</span></header><!-- /lab-cover -->') % (E(alt), rel, key, srcset, E(alt), chip)
    return None

def cover(P):
    key = 'cover_%s' % P['num']
    im = cover_img(key, P['cover_alt'], '%s · %s' % (SERIES, P['chip']))
    if im: return im
    shelf = ''.join(face(w, m, 112) for w, m in P.get('cover_cast', (('fly', 'point'), ('sia', 'smile'), ('doc', 'front'), ('moa', 'cheer'), ('robo', 'coin'))))
    return ('<!-- lab-cover --><header class="cover" id="cover" data-img="cover_%s" role="img" aria-label="%s">%s<div class="shelf">%s</div>'
            '<span class="cover-chip">%s · %s</span></header><!-- /lab-cover -->') % (P['num'], E(P['cover_alt']), pixel.scene(P['num']), shelf, SERIES, P['chip'])

def whymath(s):
    h = ['<div class="whymath">']
    if s.get('why'):
        w = s['why']
        h.append('<div class="whybox"><h4>왜 이 방법을 쓰나</h4><ol><li><b>문제 상황</b> — %s</li><li><b>앞 방법의 한계</b> — %s</li><li><b>그래서 이렇게</b> — %s</li></ol><div class="easy"><b>쉽게 말하면</b> %s</div></div>' % (w['problem'], w['limit'], w['solution'], w['easy']))
    if s.get('math'):
        m = s['math']
        rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % r for r in m['rows'])
        h.append('<div class="mathbox"><h4>수학 수식을 어려워하는 조수가 대신 물어봅니다</h4><div class="q">%s<p>“%s”</p></div>'
                 '<p><b>학교 수학으로 보면</b> — %s</p>%s<table><thead><tr><th>식 조각</th><th>읽는 법과 뜻</th></tr></thead><tbody>%s</tbody></table>'
                 '<div class="calc"><b>숫자로 한 번 해 보기</b><br>%s</div><div class="q">%s<p>%s</p></div></div>' % (
            face('asst', 'shock', 44), m['q'], m['school'], ('<div class="eqline">%s</div>' % m['eq']) if m.get('eq') else '', rows, m['calc'], face('asst', 'spark', 44), m['comment']))
    h.append('</div>')
    return ''.join(h) if len(h) > 2 else ''

def glance_html(P, s):
    g = PIC.get((P['num'], s['id']))
    if not g: return ''
    alt = ' '.join(g['look'])
    svg = g['svg'].replace('<svg ', '<svg role="img" aria-label="%s" ' % E(alt), 1)
    look = ''.join('<li><b class="n">%s</b><span>%s</span></li>' % ('①②③'[k], t) for k, t in enumerate(g['look']))
    sk = 'scene_%s_%s' % (P['num'], s['id']); scene = ''
    if os.path.exists(os.path.join(ROOT, 'assets', 'img', 'scene', sk + '.webp')):
        scene = '<figure class="scenepic"><img src="../assets/img/scene/%s.webp" width="1200" height="800" alt="%s" loading="lazy" decoding="async"></figure>' % (sk, E(g['like']))
    return scene + ('<div class="glance"><figure class="picfig">%s<figcaption>그림 속 번호 ①②③은 옆 설명의 순서와 같습니다.</figcaption></figure>'
            '<div class="gltext"><p class="kicker">한눈에 보기</p><ol class="look">%s</ol><p class="like"><span>비유</span>%s</p></div></div>') % (svg, look, g['like'])

def tryit_html(P, s):
    g = PIC.get((P['num'], s['id']))
    if not g or not g.get('tryit'): return ''
    return '<ol class="tryit"><li class="hd">이렇게 해 보세요</li>%s</ol>' % ''.join('<li>%s</li>' % t for t in g['tryit'])

def deep(title, sub, inner):
    if not inner.strip(): return ''
    return '<details class="deep"><summary><span class="dt">%s</span><span class="ds">%s</span></summary><div class="in">%s</div></details>' % (title, sub, inner)

AI_OUT = None
COLAB = 'https://colab.research.google.com/github/adminmrobo/python_machine_learning_lab/blob/main/notebooks/colab/w%s_ai_practice.ipynb'
def aicard_html(P, k):
    global AI_OUT
    c = AICARDS.get((P['num'], k))
    if not c: return ''
    if AI_OUT is None: AI_OUT = json.load(open(os.path.join(ROOT, 'build', 'aicards_out.json'), encoding='utf-8'))
    r = AI_OUT['cards']['%s_%d' % (P['num'], k)]
    imgs = ''
    for im in r['imgs']:
        src = os.path.join(ROOT, 'assets', 'img', 'run', im); webp = im.replace('.png', '.webp')
        dst = os.path.join(ROOT, 'assets', 'img', 'run', webp)
        if os.path.exists(src) and (not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src)):
            from PIL import Image; Image.open(src).save(dst, 'WEBP', lossless=True)
        imgs += '<img src="../assets/img/run/%s" width="640" height="380" alt="%s — 실행 결과 그래프" loading="lazy" decoding="async">' % (webp, E(c['title']))
    n = c['code'].count('\n') + 1
    return ('<section class="level aisec" id="ai%d"><div class="wrap"><div class="aicard">'
            '<div class="aihead"><span class="aitag">생성형 AI 실습 %d</span><h3>%s</h3></div>'
            '<div class="aistep"><span class="ain">1</span><b>이렇게 물었습니다 — 프롬프트</b></div>%s'
            '<div class="aistep"><span class="ain">2</span><b>AI가 낸 파이썬 코드</b></div>'
            '<details class="codecell"><summary>코드 %d줄 펼쳐 보기 <span>(몰라도 됩니다 · 그대로 복사해 Colab에 붙여 넣으면 돌아갑니다)</span></summary><pre><code>%s</code></pre></details>'
            '<div class="aistep"><span class="ain">3</span><b>실제로 실행한 결과</b></div>'
            '<div class="runout"><div class="rh">▶ 출력</div>%s%s</div>'
            '<div class="aistep"><span class="ain">4</span><b>그대로 믿어도 될까? — 박사의 판단</b></div>%s'
            '<div class="aifoot"><a class="colabbtn" href="%s" target="_blank" rel="noopener">Colab에서 열어 직접 실행하기</a>'
            '<p>코드는 이 페이지를 만들 때 생성형 AI가 작성한 응답 예시이고, 결과는 그 코드를 그대로 실행한 것입니다 (%s). Colab에서는 라이브러리 버전에 따라 소수점이 조금 다를 수 있습니다.</p></div>'
            '</div></div></section>') % (k, k, c['title'], say(c['who'], 'think', c['prompt'].replace('\n', '<br>')), n, E(c['code']),
            ('<pre>%s</pre>' % E(r['out'])) if r['out'] else '', imgs, say('doc', 'smile', c['judge']), COLAB % P['num'], AI_OUT['env'])

ILL_ALT = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ill_alt.json'), encoding='utf-8'))
def ill_html(P, k):
    key = 'ill_%s_%d' % (P['num'], k)
    if not os.path.exists(os.path.join(ROOT, 'assets', 'img', 'ill', key + '.webp')): return ''
    return '<section class="level illsec"><div class="wrap"><figure class="ill"><img src="../assets/img/ill/%s.webp" width="1200" height="800" alt="%s" loading="lazy" decoding="async"><figcaption>%s</figcaption></figure></div></section>' % (key, E(ILL_ALT.get(key, '')), ILL_ALT.get(key, ''))

def step_html(P, i, s):
    h = ['<section class="level" id="%s"><div class="wrap">' % s['id']]
    h.append('<div class="lvhead"><span class="hex">%d</span><div><h2>%s</h2>%s<span class="tag m">개념: %s</span><span class="tag a">%s</span></div></div>' % (
        i + 1, s['title'], ''.join(scene_chip(sc) for sc in s.get('scenes', [])), s['concept'], s['tag']))
    h.append(glance_html(P, s))
    tr = tryit_html(P, s)
    if s.get('panel'): h.append('<div class="panel"><p class="ptitle">%s</p>%s%s</div>' % (s.get('panel_title', '직접 해 보기'), tr, s['panel'])); tr = ''
    if s.get('field'):  # 현장 예시 — 접지 않고 바로 보이게
        ft, fb = s['field']; h.append('<div class="field"><b>%s</b><p>%s</p></div>' % (ft, fb))
    if s.get('flow'):
        f = s['flow']; h.append('<div class="panel"><p class="ptitle">흐름으로 보기 — %s</p>%s<canvas class="cv flow" id="%s" style="height:%dpx" role="img" aria-label="%s"></canvas><p class="cvcap">%s</p></div>' % (f['title'], tr, f['id'], f.get('h', 230), E(f['alt']), f['cap']))
    # 천천히 읽고 싶을 때 — 접어 둔 자세한 설명
    a = (('<p class="kicker" style="margin-top:4px">상황</p>' + say('doc', 'think', s['situation'])) if s.get('situation') else '') + whymath(s)
    h.append(deep('왜 이 방법을 쓰나 · 수식 천천히 보기', '박사의 질문과 조수의 수식 질문', a))
    b = []
    if s.get('pair'):
        (lt, lb), (rt, rb) = s['pair']; b.append('<div class="pair"><div><h4>%s</h4><p>%s</p></div><div><h4>%s</h4><p>%s</p></div></div>' % (lt, lb, rt, rb))
    if s.get('body'): b.append(s['body'])
    if s.get('talk'): b.append('<div class="stalk">%s</div>' % ''.join(say(*t) for t in s['talk']))
    if s.get('explain'):
        b.append('<div class="explain"><b>풀어서 보면</b>%s%s%s</div>' % (s['explain'], ('<p class="interp"><b>이 숫자는 업무에서 —</b> %s</p>' % s['interp']) if s.get('interp') else '', ('<p class="limit"><b>이 단계의 한계 —</b> %s</p>' % s['limit']) if s.get('limit') else ''))
    if s.get('changed'): b.append('<p class="changed"><b>원자료와 다른 값 —</b> %s</p>' % s['changed'])
    if s.get('say'): b.append(say(*s['say']))
    h.append(deep('팀 대화와 자세한 풀이', '일상 비유 · 실험 결과 읽기 · 이 단계의 한계', ''.join(b)))
    if s.get('aicheck'): h.append(deep('AI·도구 결과 판단 코너', 'AI가 낸 답에서 이상한 점 찾기', s['aicheck']))
    if s.get('code'):
        rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % (E(c), m) for c, m in s['code'])
        h.append(deep('교안의 파이썬 코드로 보면', '몰라도 됩니다', '<div class="tbl"><table><thead><tr><th>코드 한 줄</th><th>뜻</th></tr></thead><tbody>%s</tbody></table></div>' % rows))
    if s.get('check'):  # 교안의 「여기까지 됐나요?」 — 스스로 점검 3줄 + 막혔을 때 AI에게 물을 한 줄
        c = s['check']; h.append('<div class="selfcheck"><p class="sct">✓ %s</p><ol>%s</ol><p class="ask"><b>막혔다면 이렇게 물어봐 —</b> <q>%s</q></p></div>' % (c['title'], ''.join('<li>%s</li>' % x for x in c['items']), c['ask']))
    if s.get('quiz'): h.append('<div class="quiz" data-quiz="%s"></div>' % s['id'])
    h.append('</div></section>')
    return '\n'.join(x for x in h if x)

def duel_html(d):
    return '''<section class="level" id="duel"><div class="wrap">
<h2>팀 대항전 — %s</h2><p>%s</p>
<div class="duel" id="duelbox">
 <div class="head"><div>%s<div><b>초파리팀</b><br><span style="font-size:13px">%s</span></div></div><div class="vs">VS</div><div>%s<div><b>주판봇팀</b><br><span style="font-size:13px">%s</span></div></div></div>
 <div class="cards"><div><b>초파리팀의 선택: %s</b><p>“%s”</p></div><div><b>주판봇팀의 선택: %s</b><p>“%s”</p></div></div>
 <p style="margin:6px 0 4px;font-size:14px;color:#5b6874">먼저 맞혀 보기 — 심판 박사의 판정 기준: <b>%s</b></p>
 <div class="ctrl guess"><button type="button" class="bt" aria-pressed="false">초파리팀이 이길 것 같다</button><button type="button" class="bt" aria-pressed="false">주판봇팀이 이길 것 같다</button><span class="gnote" style="font-size:13px;color:#5b6874"></span></div>
 <div class="ctrl"><button type="button" class="bt primary go">결과 보기</button><button type="button" class="bt reset">다시 닫기</button></div>
 <div class="res" aria-live="polite">
  <div class="bars"><div class="bar f"><span>초파리팀</span><i><s></s></i><b></b></div><div class="bar r"><span>주판봇팀</span><i><s></s></i><b></b></div></div>
  <div class="say">%s<div class="bub"><span class="who w-asst">조수 하루 · 점수판</span><p class="ann"></p></div></div>
  <div class="say">%s<div class="bub"><span class="who w-doc">박사 · 심판</span><p class="ver"></p></div></div>
 </div>
</div>
%s
</div></section>''' % (d['q'], d['intro'], face('fly', 'point', 84), d.get('fly_who', '발표: 시아 · X1 · X2'), face('robo', 'coin', 84), d.get('robo_who', '발표: 모아 · 하루 · X3'),
       d['fly_pick'], d['fly_line'], d['robo_pick'], d['robo_line'], d['metric'], face('asst', 'firm'), face('doc', 'front'), d.get('after', ''))

def collect_sprites(body):
    keys = set(re.findall(r'data-who="(\w+)" data-mood="(\w+)"', body)); want = {'%s_%s' % k for k in keys} | set(DUEL_KEYS)
    sp = {}
    for k in sorted(want):
        kk, b = sprite_b64(k)
        if b: sp[kk] = b
    exmap = {k: key_of(k) for k in sorted(want)}
    return sp, exmap

def head(title, desc, og_title, url, extra='', og='cover_index'):
    return ('<!DOCTYPE html>\n<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            '<title>%s</title><meta name="description" content="%s"><meta property="og:title" content="%s"><meta property="og:type" content="article"><meta property="og:url" content="%s">'
            '<meta property="og:image" content="%sassets/img/og/%s.png"><meta property="og:image:width" content="960"><meta property="og:image:height" content="540"><meta name="twitter:card" content="summary_large_image">%s'
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet"><style>%s</style></head>') % (
        E(title), E(desc), E(og_title), url, SITE, og, extra, CSS)

def footer(P, prev, nxt, rel='../'):
    src_rows = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (E(r['title']), E(r.get('by', '')), ('<a href="%s" target="_blank" rel="noopener">열기</a>' % E(r['URL'])) if r.get('URL') else '') for r in P.get('refs', []))
    pager = '<div class="pager">%s%s</div>' % (('<a href="%s"><small>← 아래층</small>%s</a>' % (prev[0], E(prev[1]))) if prev else '<span></span>',
                                               ('<a href="%s" style="text-align:right"><small>위층 →</small>%s</a>' % (nxt[0], E(nxt[1]))) if nxt else '<a href="%sindex.html" style="text-align:right"><small>처음으로</small>건물 안내도</a>' % rel)
    return ('<footer id="sources"><div class="wrap">%s<h4>예시값 · 설명용 모형인 것</h4><ul>%s</ul><h4>이 페이지</h4>'
            '<p>글 · %s (<a href="%s" target="_blank" rel="noopener">소개</a>) · %s · 시리즈 「%s」 · 라이선스 %s · <a href="%s">저장소</a> · <a href="%sindex.html">건물 안내도</a></p>'
            '<p>캐릭터 그림: 연구실 캐릭터 팩(fruitfly-lab-expressions, 저작권자 허락 없이 재사용 불가). 페이지 안 실험은 브라우저에서 계산하는 교육용 모형이며, 실제 Colab 실행 결과와 소수점이 조금 다를 수 있습니다.</p>%s</div></footer>') % (
        ('<h4>출처</h4><div class="tbl"><table><thead><tr><th>자료</th><th>저자·발행</th><th>링크</th></tr></thead><tbody>%s</tbody></table></div>' % src_rows) if src_rows else '',
        ''.join('<li>%s</li>' % x for x in P.get('models', ['페이지 안 실험의 점 분포는 설명용 모형입니다.'])), AUTHOR, AUTHOR_URL, AFFIL, SERIES, LICENSE, REPO, rel, pager)

def page_html(P, prev, nxt, fname):
    kg = build_kg(P); url = SITE + 'weeks/' + fname
    meta = {'title': P['title'] + ' — ' + P['subtitle'], 'series': SERIES, 'number': P['num'], 'creator': [{'name': AUTHOR + ' (' + AFFIL + ')', 'role': 'author'}],
            'contributor': [{'name': 'AI 보조 제작', 'role': 'assistant'}], 'date': TODAY, 'version': '1.0', 'language': ['ko'], 'license': LICENSE, 'url': url,
            'about': [n['id'] for n in kg['nodes'] if n['type'] == 'Concept'][:6], 'educationalLevel': '입문 (파이썬·데이터를 처음 배우는 학부생)', 'learningResourceType': 'interactive explainer',
            'basedOn': [r['id'] for r in P['refs']], 'registry': 'data/KG_00_registry.json',
            'suggestedCitation': '%s (2026). %s — %s. %s %s층, v1.0. %s' % (AUTHOR, P['title'], P['subtitle'], SERIES, int(P['num']), url)}
    refs = []
    for r in P['refs']:
        c = {k: v for k, v in r.items() if k in ('id', 'type', 'title', 'author', 'issued', 'publisher', 'URL', 'note')}
        c.setdefault('type', 'document'); c['lab'] = {'work': 'lab:work/' + r['id'], 'role': r.get('role', 'background'), 'supports': [], 'verified': {'title': True, 'authors': True, 'year': True}, 'checkedBy': '저자 자료 확인 ' + TODAY, 'note': r.get('note', '')}
        refs.append(c)
    B = []
    navs = [('top', '처음'), ('first', '3줄'), ('crew', '두 팀'), ('why', '왜')] + [(s['id'], '%d %s' % (i + 1, s['short'])) for i, s in enumerate(P['steps'])] + P.get('nav_extra', []) + [('duel', '대항전'), ('summary', '정리'), ('kg', '색인'), ('export', '꾸러미')]
    B.append('<nav class="top" aria-label="이 페이지 차례"><a class="brand" href="../index.html"><span class="hex">%s</span>%s</a><div class="links">%s</div></nav>' % (int(P['num']), SERIES, ''.join('<a href="#%s">%s</a>' % a for a in navs)))
    B.append(cover(P))
    kp = ''.join('<div><b>%s</b><span>%s</span></div>' % kv for kv in P['kpis'])
    B.append('<main id="top"><header class="hero"><div class="wrap"><div class="kicker">%s</div><h1>%s<br><span style="font-size:.55em;color:#5b6874">%s</span></h1><p class="question">%s</p>%s<section class="kpis" aria-label="이 층의 숫자 요약">%s</section><p style="font-size:13px;color:#5b6874">%s</p><div class="talk">%s</div></div></header>' % (
        P['kicker'], P['title'], P['subtitle'], P['question'], P['intro'], kp, P.get('kpi_note', ''), ''.join(say(*t) for t in P['hero_talk'])))
    f3 = P['first3']
    abbr = ''.join('<li><b>%s</b> — %s</li>' % a for a in P.get('abbr', []))
    B.append('<section class="level" id="first" style="padding-top:20px"><div class="wrap"><div class="first3"><h3>처음 오신 분께 — 이 층을 3줄로</h3><ol><li><b>무엇을</b> %s</li><li><b>왜 중요한가</b> %s</li><li><b>업무에서는</b> %s</li></ol>'
             '<span class="nocode">코드·수식을 몰라도 됩니다. 버튼을 누르고 숫자가 어떻게 바뀌는지만 보세요.</span>%s</div></div></section>' % (f3[0], f3[1], f3[2], ('<details><summary>이 층에 나오는 영어 약어 풀이</summary><ul>%s</ul></details>' % abbr) if abbr else ''))
    notion = ''.join('<div class="notion"><span class="nb">↗</span><a href="%s" target="_blank" rel="noopener">%s</a><span>%s</span></div>' % (E(u), t, d) for t, u, d in P.get('links', []))
    B.append('<section class="level" id="crew"><div class="wrap"><h2>오늘의 두 팀과 심판</h2>%s<div class="steps"><div><b>밑줄 친 낱말</b>점선 밑줄을 누르거나 손가락으로 대면 뜻이 나옵니다.</div><div><b>직접 해 보기</b>버튼과 손잡이는 눌러도 아무것도 망가지지 않습니다.</div><div><b>진행 표시</b><span id="qprog">퀴즈 0/0</span> · 맨 위 초록 막대는 읽은 만큼 차오릅니다.</div></div>%s%s</div></section>' % (
        teams_html(), ('<div class="recap"><b>30초 복습 — </b>%s</div>' % P['recap']) if P.get('recap') else '', notion))
    why = ''.join('<div><span class="n">%d</span><b>%s</b>%s</div>' % (i + 1, a, b) for i, (a, b) in enumerate(P['why']))
    B.append('<section class="level" id="why"><div class="wrap"><h2>%s</h2><div class="steps">%s</div>%s%s</div></section>' % (P.get('why_title', '왜 이 층에 왔나'), why, P.get('bigpicture', ''), say(*P['why_say']) if P.get('why_say') else ''))
    last = len(P['steps']) - 1
    for i, s in enumerate(P['steps']):
        B.append(step_html(P, i, s))
        if P['num'] in ('12', '13', '14', '15'): continue
        if i == 0: B.append(ill_html(P, 1))
        if i == 1: B.append(aicard_html(P, 1))
        if i == 2: B.append(ill_html(P, 2))
        if i == last: B.append(aicard_html(P, 2))
    for xs in P.get('extra_sections', []): B.append(xs)
    B.append(duel_html(P['duel']))
    B.append('<section class="level" id="summary"><div class="wrap"><h2>정리 — 한 장으로</h2>%s</div></section>' % P['summary'])
    B.append('<section class="level outro" id="outro"><div class="wrap"><h2>오늘의 마무리</h2><div class="talk">%s</div>%s</div></section>' % (''.join(say(*t) for t in P['outro']), P.get('next_note', '')))
    B.append('<section class="level" id="more"><div class="wrap"><details class="deep more"><summary><span class="dt">더 공부하고 싶은 분께 — 지식 색인 · 자료 꾸러미</span><span class="ds">이 층의 개념 지도와 내려받기 (몰라도 됩니다)</span></summary><div class="in">')
    B.append('<section class="kgx kgx-sec level" id="kg"><div class="kgx-wrap"><h2>지식 색인 — 이 층에서 찾아보기</h2><p class="kgx-sub">이 층에 나온 개념, 용어, 주장, 열린 질문을 한곳에 모았습니다. 검색하고, 항목을 눌러 관계를 보고, “본문”으로 돌아갑니다.</p><div id="kg-mount"></div></div></section>')
    B.append('<section class="kgx kgx-sec level" id="export"><div class="kgx-wrap"><h2>온톨로지·서지 꾸러미 — 이 층의 지식을 가져가기</h2><p class="kgx-sub">지식 색인을 출처와 함께 파일로 내려받습니다. Zotero(BibTeX·RIS), Protégé(Turtle), Neo4j·Gephi(CSV), 여러 페이지 합치기(kg.json)에 씁니다.</p><div id="export-mount"></div></div></section></div></details></div></section></main>')
    B.append(footer(P, prev, nxt))
    body = '\n'.join(B)
    sp, exmap = collect_sprites(body)
    quiz = {s['id']: s['quiz'] for s in P['steps'] if s.get('quiz')}; quiz.update(P.get('extra_quiz', {}))
    flows = ','.join('%s:%s' % (json.dumps(s['flow']['id']), s['flow']['js']) for s in P['steps'] if s.get('flow'))
    data_js = 'var SPRITE=%s;\nvar EXMAP=%s;\nvar QUIZ=%s;\nvar GL=%s;\nvar FLOWS={%s};\nvar CARDS=%s;\n' % (esc_json(sp), esc_json(exmap), esc_json(quiz), esc_json({k: v[:3] for k, v in P.get('gloss', {}).items()}), flows, esc_json(P.get('cards', {})))
    d = P['duel']
    duel_js = 'var DUEL={el:"#duelbox",higherIsBetter:%s,drawMargin:%s,run:function(){%s},announce:function(r){%s},verdict:function(res,r){%s}};' % ('true' if d.get('higher', True) else 'false', d.get('margin', 0), d['run'], d['announce'], d['verdict'])
    doc = head('%s — %s · %s' % (P['title'], P['subtitle'], SERIES), P['desc'], meta['title'], url, '<meta name="citation_title" content="%s"><meta name="citation_author" content="%s"><meta name="dc.language" content="ko"><meta name="dc.rights" content="%s">' % (E(meta['title']), AUTHOR, LICENSE), og='cover_%s' % P['num'])
    doc += ('<body><div id="prog"></div><div id="tip" role="tooltip"></div>\n%s\n<script type="application/json" id="kg-raw">%s</script><script type="application/ld+json" id="kg-ld">%s</script>'
            '<script type="application/json" id="refs-csl">%s</script><script type="application/json" id="page-meta">%s</script>'
            '<script>%s%s\nvar PAGE={init:function(LAB){%s}};</script><script>%s</script><script>%s</script></body></html>') % (
        body, esc_json(kg), esc_json(jsonld(kg, meta)), esc_json(refs), esc_json(meta), data_js, duel_js, P.get('js', ''), JS, KGX)
    return doc, kg

def slot_html(P, prev, nxt, fname):
    url = SITE + 'weeks/' + fname
    body = ('<nav class="top"><a class="brand" href="../index.html"><span class="hex">%d</span>%s</a><div class="links"><a href="#top">처음</a><a href="#plan">계획</a></div></nav>%s'
            '<main id="top"><header class="hero"><div class="wrap"><div class="kicker">%s</div><h1>%s<br><span style="font-size:.55em;color:#5b6874">공사 중인 층 — 강의 자료를 받으면 문을 엽니다</span></h1>'
            '<div class="talk">%s%s</div></div></header><section class="level" id="plan"><div class="wrap"><div class="slotbox"><h2>이 층의 계획</h2><p><b>강의계획서의 주제:</b> %s</p>%s<p>지금 보이는 1~10층을 먼저 둘러보고, <a href="../practice/index.html">실전 연습장</a>에서 배운 것을 운영해 보세요.</p></div></div></section></main>') % (
        int(P['num']), SERIES, cover(P), P['kicker'], P['title'], say('robo', 'smile', P['robo']), say('doc', 'front', P['doc']), P['plan'], P.get('note', ''))
    body += footer(P, prev, nxt)
    sp, exmap = collect_sprites(body)
    return head('%s · %s' % (P['title'], SERIES), P['desc'], P['title'], url, og='cover_%s' % P['num']) + '<body><div id="prog"></div><div id="tip"></div>%s<script>var SPRITE=%s;var EXMAP=%s;</script><script>%s</script></body></html>' % (body, esc_json(sp), esc_json(exmap), JS)

def index_html(pages, IDX):
    rows = []
    for P, fn in reversed(pages):
        k = P['kind']
        rows.append('<a class="fl%s" href="weeks/%s"><span class="no">%dF</span><span class="ti"><b>%s</b><span>%s</span></span><span class="imgs">%s</span></a>' % (
            {'review': ' rev', 'slot': ' slot'}.get(k, ''), fn, int(P['num']), E(P['title']), E(P['toc']), ''.join(face(w, m, 28) for w, m in P.get('toc_faces', [('fly', 'clip'), ('robo', 'smile')])) if k != 'slot' else '🚧'))
    tower = '<div class="tower"><div class="roof">옥상 · 실전 연습장으로 가는 계단은 1층 로비 옆</div>%s<a class="fl prac" href="practice/index.html"><span class="no">B1</span><span class="ti"><b>지하 실전 연습장</b><span>생선가게 · 택시회사 · 배터리 공장 · 보험사를 직접 운영해 보는 대시보드</span></span><span class="imgs">%s</span></a><div class="base"></div></div>' % (''.join(rows), face('doc', 'front', 28) + face('asst', 'smile', 28))
    body = IDX['body'].replace('{{TOWER}}', tower).replace('{{TEAMS}}', teams_html())
    cov = '<!-- lab-cover --><header class="cover" id="cover" role="img" aria-label="%s">%s<div class="shelf">%s</div><span class="cover-chip">%s · 건물 안내도</span></header><!-- /lab-cover -->' % (
        E(IDX['cover_alt']), pixel.scene('00'), ''.join(face(w, m, 112) for w, m in (('fly', 'point'), ('sia', 'smile'), ('x1', 'smile'), ('doc', 'front'), ('x3', 'smile'), ('moa', 'cheer'), ('robo', 'coin'))), SERIES)
    cov = cover_img('cover_index', IDX['cover_alt'], SERIES + ' · 건물 안내도', '') or cov
    full = '<nav class="top"><a class="brand" href="index.html"><span class="hex">Py</span>%s</a><div class="links"><a href="#course">강좌 안내</a><a href="#floors">15층 안내도</a><a href="#teams">두 팀</a><a href="#how">공부하는 법</a><a href="#tools">실습 도구</a><a href="practice/index.html">실전 연습장</a></div></nav>%s<main id="top">%s</main>' % (SERIES, cov, body)
    full += footer({'refs': IDX['refs'], 'models': IDX['models']}, None, None, '')
    sp, exmap = collect_sprites(full)
    return head(SERIES + ' — 파이썬 머신러닝 15층 연구실 해설', IDX['desc'], SERIES, SITE) + '<body><div id="prog"></div><div id="tip"></div>%s<script>var SPRITE=%s;var EXMAP=%s;</script><script>%s</script></body></html>' % (full, esc_json(sp), esc_json(exmap), JS)

def check(name, doc):
    text = re.sub(r'<script[^>]*>.*?</script>', ' ', doc, flags=re.S)
    text = re.sub(r'<style>.*?</style>', ' ', text, flags=re.S)
    text = re.sub(r'<svg.*?</svg>', ' ', text, flags=re.S)
    bad = [w for w in BANNED if w in text]
    # 스크립트 안의 대사·퀴즈도 검사
    js_bad = [w for w in BANNED if w in ''.join(re.findall(r'var (?:QUIZ|GL|DUEL)=.*?;\n', doc, flags=re.S))]
    if bad or js_bad: print('  !! 금지어', name, bad, js_bad)

def main():
    pages = []
    for f in sorted(glob.glob(os.path.join(HERE, 'pages', 'w*.py'))):
        g = {'say': say, 'face': face, 'E': E, 'json': json}
        exec(open(f, encoding='utf-8').read(), g); P = g['PAGE']; P.setdefault('id', 'pyml_w' + P['num'])
        P.setdefault('chip', '%dF · %d주차' % (int(P['num']), int(P['num'])))
        pages.append((P, 'w%s_%s.html' % (P['num'], P['slug'])))
    os.makedirs(os.path.join(ROOT, 'weeks'), exist_ok=True)
    reg = {'version': '1.0', 'series': SERIES, 'updated': TODAY, 'domain': 'ml', 'ids': {}}; rep = []
    for i, (P, fn) in enumerate(pages):
        prev = (pages[i - 1][1], pages[i - 1][0]['chip'] + ' ' + pages[i - 1][0]['title']) if i else None
        nxt = (pages[i + 1][1], pages[i + 1][0]['chip'] + ' ' + pages[i + 1][0]['title']) if i + 1 < len(pages) else None
        if P['kind'] == 'slot':
            doc = slot_html(P, prev, nxt, fn); kg = None
        else:
            doc, kg = page_html(P, prev, nxt, fn)
            for n in kg['nodes']:
                if n['type'] in ('Concept', 'Term', 'Topic', 'Area', 'Method', 'Work'):
                    reg['ids'].setdefault(n['id'], {'ko': n['label']['ko'], 'en': n['label']['en'], 'type': n['type'], 'pages': []})
                    if P['id'] not in reg['ids'][n['id']]['pages']: reg['ids'][n['id']]['pages'].append(P['id'])
        open(os.path.join(ROOT, 'weeks', fn), 'w', encoding='utf-8').write(doc); check(fn, doc)
        nq = sum(len(s.get('quiz', [])) for s in P.get('steps', []))
        rep.append('%s %-40s %6.0f KB  nodes %3s quiz %2d' % (P['num'], fn, len(doc.encode()) / 1024, len(kg['nodes']) if kg else '-', nq))
    IDX = {}; exec(open(os.path.join(HERE, 'pages', 'index.py'), encoding='utf-8').read(), {'face': face, 'say': say, 'E': E, 'IDX': IDX})
    doc = index_html(pages, IDX); open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(doc); check('index.html', doc)
    os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
    json.dump(reg, open(os.path.join(ROOT, 'data', 'KG_00_registry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if os.path.exists(os.path.join(HERE, 'practice.py')):
        g = {'say': say, 'face': face, 'E': E, 'cover_img': cover_img, 'head': head, 'footer': footer, 'collect_sprites': collect_sprites, 'esc_json': esc_json, 'JS': JS, 'pixel': pixel, 'SERIES': SERIES, 'SITE': SITE, 'check': check, 'ROOT': ROOT}
        exec(open(os.path.join(HERE, 'practice.py'), encoding='utf-8').read(), g)
    print('\n'.join(rep))

if __name__ == '__main__':
    main()
