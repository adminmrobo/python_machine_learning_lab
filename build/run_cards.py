# 생성형 AI 실습 카드의 코드를 실제로 실행해 결과(출력 글·그래프)를 저장하고, 층마다 Colab 노트북을 만든다.
# 사용: python3 build/run_cards.py   (인터넷 대신 저장소 data/ 와 /tmp/insurance.csv 를 읽는다)
import io, os, sys, json, base64, contextlib, platform
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd, sklearn, numpy
sys.path.insert(0, os.path.dirname(__file__))
from aicards import CARDS, DATA, INSURANCE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'assets', 'img', 'run'); os.makedirs(IMG, exist_ok=True)
NB = os.path.join(ROOT, 'notebooks', 'colab'); os.makedirs(NB, exist_ok=True)
LOCAL = {DATA: os.path.join(ROOT, 'data') + '/', INSURANCE: '/tmp/insurance.csv'}
_read = pd.read_csv
def read_csv(p, *a, **k):
    for url, loc in LOCAL.items():
        if isinstance(p, str) and p.startswith(url): p = loc + p[len(url):] if loc.endswith('/') else loc
    return _read(p, *a, **k)
pd.read_csv = read_csv
plt.rcParams.update({'figure.figsize': (6.4, 3.8), 'figure.dpi': 100})

out = {}
for (num, k), c in sorted(CARDS.items()):
    shots = []
    def show(*a, **kw):
        fig = plt.gcf(); fig.tight_layout()
        name = 'w%s_ai%d_%d.png' % (num, k, len(shots) + 1)
        fig.savefig(os.path.join(IMG, name), dpi=100); plt.close(fig); shots.append(name)
    plt.show = show
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(c['code'], 'card_%s_%d' % (num, k), 'exec'), {'__name__': '__main__'})
    out['%s_%d' % (num, k)] = dict(out=buf.getvalue().rstrip('\n'), imgs=shots)
    print(num, k, 'ok', len(shots), 'img')

env = 'Python %s · pandas %s · scikit-learn %s · NumPy %s · matplotlib %s' % (platform.python_version(), pd.__version__, sklearn.__version__, numpy.__version__, matplotlib.__version__)
json.dump(dict(env=env, cards=out), open(os.path.join(ROOT, 'build', 'aicards_out.json'), 'w'), ensure_ascii=False, indent=1)

# 층마다 Colab 노트북 (프롬프트 → 코드 → 저장된 실행 결과)
def md(s): return {'cell_type': 'markdown', 'metadata': {}, 'source': s.splitlines(True)}
for num in sorted({n for n, _ in CARDS}):
    cells = [md('# %s층 · 생성형 AI 실습\n\n프롬프트를 AI에게 보내 받은 파이썬 코드입니다. 위에서부터 셀을 차례로 실행해 보세요.\n데이터는 GitHub 저장소에서 바로 불러옵니다.\n\n저장된 결과는 %s 로 실행한 것입니다. Colab에서는 라이브러리 버전에 따라 소수점이 조금 다를 수 있습니다.' % (int(num), env))]
    for k in (1, 2):
        c = CARDS[(num, k)]; r = out['%s_%d' % (num, k)]
        cells.append(md('## 실습 %d · %s\n\n**프롬프트**\n\n' % (k, c['title']) + '\n'.join('> ' + l for l in c['prompt'].split('\n'))))
        outputs = []
        if r['out']: outputs.append({'output_type': 'stream', 'name': 'stdout', 'text': (r['out'] + '\n').splitlines(True)})
        for im in r['imgs']:
            outputs.append({'output_type': 'display_data', 'metadata': {}, 'data': {'image/png': base64.b64encode(open(os.path.join(IMG, im), 'rb').read()).decode(), 'text/plain': ['<Figure>']}})
        cells.append({'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': outputs, 'source': c['code'].splitlines(True)})
        if c.get('judge'): cells.append(md('**박사의 한 줄 판단** — ' + c['judge']))
    nb = {'cells': cells, 'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python'}, 'colab': {'provenance': []}}, 'nbformat': 4, 'nbformat_minor': 5}
    json.dump(nb, open(os.path.join(NB, 'w%s_ai_practice.ipynb' % num), 'w'), ensure_ascii=False, indent=1)
print(env)
