# 중국어판 Colab 노트북 — 생성형 AI 실습 카드를 중국어로 옮겨 실제로 실행하고 notebooks/colab/wNN_ai_practice.zh.ipynb 로 저장한다.
# 제목·프롬프트·박사의 판단은 언어팩 번역 메모리(langpack/work/zh/tm.json)에서, 코드 속 한국어 출력 글은 아래 ZH_CODE 표로 바꾼다.
# 사용: python3 build/zh_notebooks.py 11   (층 번호, 여러 개 가능)
import io, os, sys, json, base64, contextlib, platform, html
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd, sklearn, numpy
sys.path.insert(0, os.path.dirname(__file__))
from aicards import CARDS, DATA

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB = os.path.join(ROOT, 'notebooks', 'colab')
TM = json.load(open(os.path.join(ROOT, 'langpack', 'work', 'zh', 'tm.json'), encoding='utf-8'))
ZH_CODE = [  # 긴 것부터
    ('마리 / 무게 0g 기록:', '条 / 重量0g记录:'), ('전체:', '全部:'), ('평균 무게(g)', '平均重量(g)'), ('마리 수', '条数'), ('"마리"', '"条"'),
    ('시험 평균 오차(g)', '测试平均误差(g)'), ('학습 R2', '训练 R2'), ('시험 R2', '测试 R2'),
    ('나무 깊이 3', '深度3的树'), ('나무 제한 없음', '不限深度的树'), ('숲 300그루', '300棵树的森林')]

def zh(ko):
    v = TM.get(ko)
    if v is None: raise SystemExit('번역 메모리에 없음: ' + ko[:60])
    return v

_read = pd.read_csv
def read_csv(p, *a, **k):
    if isinstance(p, str) and p.startswith(DATA): p = os.path.join(ROOT, 'data', p[len(DATA):])
    return _read(p, *a, **k)
pd.read_csv = read_csv
plt.rcParams.update({'figure.figsize': (6.4, 3.8), 'figure.dpi': 100})

def md(s): return {'cell_type': 'markdown', 'metadata': {}, 'source': s.splitlines(True)}
env = 'Python %s · pandas %s · scikit-learn %s · NumPy %s · matplotlib %s' % (platform.python_version(), pd.__version__, sklearn.__version__, numpy.__version__, matplotlib.__version__)
for num in sys.argv[1:]:
    cells = [md('# %s层 · 生成式 AI 实习\n\n把提示词发给 AI 后得到的 Python 代码。请从上到下依次运行各单元格。\n数据直接从 GitHub 仓库读取。\n\n保存的结果是用 %s 运行的。在 Colab 中，小数点可能因库版本不同而略有差异。' % (int(num), env))]
    for k in (1, 2):
        c = CARDS[(num, k)]
        code = c['code']
        for a, b in ZH_CODE: code = code.replace(a, b)
        shots, buf = [], io.StringIO()
        def show(*a, **kw):
            fig = plt.gcf(); fig.tight_layout(); b = io.BytesIO(); fig.savefig(b, format='png', dpi=100); plt.close(fig); shots.append(base64.b64encode(b.getvalue()).decode())
        plt.show = show
        with contextlib.redirect_stdout(buf): exec(compile(code, 'zh_card_%s_%d' % (num, k), 'exec'), {'__name__': '__main__'})
        prompt = html.unescape(zh(c['prompt'].replace('\n', '<br>'))).replace('<br>', '\n')
        cells.append(md('## 实习 %d · %s\n\n**提示词**\n\n' % (k, zh(c['title'])) + '\n'.join('> ' + l for l in prompt.split('\n'))))
        outs = []
        if buf.getvalue().strip(): outs.append({'output_type': 'stream', 'name': 'stdout', 'text': buf.getvalue().splitlines(True)})
        for s in shots: outs.append({'output_type': 'display_data', 'metadata': {}, 'data': {'image/png': s, 'text/plain': ['<Figure>']}})
        cells.append({'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': outs, 'source': code.splitlines(True)})
        if c.get('judge'): cells.append(md('**博士的一句话判断** — ' + zh(c['judge'])))
    nb = {'cells': cells, 'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python'}, 'colab': {'provenance': []}}, 'nbformat': 4, 'nbformat_minor': 5}
    out = os.path.join(NB, 'w%s_ai_practice.zh.ipynb' % num)
    json.dump(nb, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(out, len(cells), 'cells')
