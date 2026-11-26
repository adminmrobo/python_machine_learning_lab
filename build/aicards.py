# 층마다 생성형 AI 실습 카드 2장 — 프롬프트 → AI가 낸 파이썬 코드 → 실제 실행 결과 → 박사의 한 줄 판단
# 코드는 이 사이트를 만들 때 생성형 AI가 작성한 응답 예시이고, run_cards.py가 실제로 실행해 결과를 저장한다.
# 결과는 build/aicards_out.json, 그래프는 assets/img/run/, Colab 노트북은 notebooks/colab/ 에 생긴다.

DATA = 'https://raw.githubusercontent.com/adminmrobo/python_machine_learning_lab/main/data/'
INSURANCE = 'https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv'

CARDS = {}
def C(num, k, who, title, prompt, code, judge=''):
    CARDS[(num, k)] = dict(who=who, title=title, prompt=prompt, code=code.strip('\n'), judge=judge)

# ───────── 1층 ─────────
C('01', 1, 'sia', '규칙 vs 머신러닝, 스팸 메일 8통으로 비교하기',
'파이썬 초보입니다. 메일 8통(스팸 4, 정상 4)으로 작은 예제를 만들어 주세요.\n① “무료”가 있으면 스팸이라는 규칙\n② 단어를 세어 배우는 머신러닝(나이브 베이즈)\n새 메일 3통을 두 방법으로 판정해 나란히 보여 주세요.', '''
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 메일 8통과 정답 (1 = 스팸, 0 = 정상)
mails = ["무료 쿠폰 당첨 지금 클릭", "회의 자료 공유드립니다",
         "할인 이벤트 무료 배송", "내일 점심 약속 확인",
         "당첨 축하 상금 수령", "보고서 초안 검토 부탁",
         "무료 체험 지금 신청", "프로젝트 일정 변경 안내"]
labels = [1, 0, 1, 0, 1, 0, 1, 0]

# ① 사람이 정한 규칙
def rule(text):
    return 1 if "무료" in text else 0

# ② 머신러닝: 단어 개수를 세어 학습
vec = CountVectorizer()
model = MultinomialNB().fit(vec.fit_transform(mails), labels)

name = {1: "스팸", 0: "정상"}
for t in ["상금 당첨 확인 바랍니다", "무료 회의실 예약 안내", "일정 공유드립니다"]:
    ml = model.predict(vec.transform([t]))[0]
    print(t, "→ 규칙:", name[rule(t)], "/ 머신러닝:", name[ml])
''')
C('01', 2, 'moa', '처음 받은 데이터 파일 열어 보기',
'rides.csv라는 택시 이용 데이터가 있어요. 파이썬으로 불러와서\n① 몇 행·몇 열인지 ② 처음 5줄 ③ 이탈(churned) 손님 수를 보여 주고\n요금(fare) 분포를 그래프로 그려 주세요. 그래프 글자는 영어로 해 주세요.', '''
import pandas as pd
import matplotlib.pyplot as plt

url = "%srides.csv"
df = pd.read_csv(url)

print("행, 열:", df.shape)
print(df.head())
print(df["churned"].value_counts())   # 0 = 남은 손님, 1 = 떠난 손님

df["fare"].plot.hist(bins=30, edgecolor="white")
plt.xlabel("fare (KRW)"); plt.ylabel("rides"); plt.title("Fare distribution")
plt.show()
''' % DATA)

# ───────── 2층 ─────────
C('02', 1, 'x1', '택시 요금 맞히기 (회귀)',
'rides.csv에서 거리(distance_km)와 시간(duration_min)으로 요금(fare)을 맞히는 선형 회귀를 만들어 주세요.\n학습 80% / 시험 20%로 나누고, 시험용으로 RMSE·MAE·R²를 출력하고\n실제 요금과 예측 요금을 점으로 비교하는 그래프도 그려 주세요(그래프 글자는 영어).', '''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("%srides.csv")
X = df[["distance_km", "duration_min"]]
y = df["fare"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)

print("RMSE:", round(mean_squared_error(y_test, pred) ** 0.5), "원")
print("MAE :", round(mean_absolute_error(y_test, pred)), "원")
print("R²  :", round(r2_score(y_test, pred), 3))
print("기본요금(절편):", round(model.intercept_), "/ km당:", round(model.coef_[0]), "/ 분당:", round(model.coef_[1]))

plt.scatter(y_test, pred, s=12)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color="red")
plt.xlabel("actual fare"); plt.ylabel("predicted fare"); plt.title("Actual vs predicted")
plt.show()
''' % DATA)
C('02', 2, 'x2', '정확도의 함정 — 떠날 손님 맞히기 (분류)',
'rides.csv로 손님 이탈(churned)을 맞히는 로지스틱 회귀를 만들어 주세요.\n정확도만 보지 말고 혼동행렬과 재현율(떠난 손님 중 잡은 비율)도 보여 주세요.\n그리고 class_weight="balanced"로 바꿨을 때와 비교해 주세요.', '''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix

df = pd.read_csv("%srides.csv")
X = df[["distance_km", "duration_min", "hour", "is_weekend", "fare"]]
y = df["churned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

for cw in [None, "balanced"]:
    model = make_pipeline(StandardScaler(), LogisticRegression(class_weight=cw))
    pred = model.fit(X_train, y_train).predict(X_test)
    print("class_weight =", cw)
    print("  정확도:", round(accuracy_score(y_test, pred), 3), "/ 재현율:", round(recall_score(y_test, pred), 3))
    print("  혼동행렬 [[남음→남음, 남음→이탈], [이탈→남음, 이탈→이탈]]")
    print(" ", confusion_matrix(y_test, pred).tolist())
''' % DATA)

# ───────── 3층 ─────────
C('03', 1, 'x3', '모의고사 다섯 번 — 교차검증',
'rides.csv 이탈 예측에서 얕은 나무(max_depth=3)와 깊은 나무(제한 없음)를\n5겹 교차검증으로 비교해 주세요. 점수는 재현율로, 다섯 번 점수와 평균·표준편차를 출력하고\n막대그래프로 비교해 주세요(그래프 글자는 영어).', '''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("%srides.csv")
X = df[["distance_km", "duration_min", "hour", "is_weekend", "fare"]]
y = df["churned"]
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

result = {}
for name, depth in [("shallow (3)", 3), ("deep (None)", None)]:
    tree = DecisionTreeClassifier(max_depth=depth, class_weight="balanced", random_state=0)
    s = cross_val_score(tree, X, y, cv=cv, scoring="recall")
    result[name] = s
    print(name, "다섯 번:", s.round(3), "평균:", round(s.mean(), 3), "±", round(s.std(), 3))

pd.DataFrame(result, index=[f"fold {i}" for i in range(1, 6)]).plot.bar(rot=0)
plt.ylabel("recall"); plt.title("5-fold cross-validation"); plt.ylim(0, 1)
plt.show()
''' % DATA)
C('03', 2, 'sia', '새 손님 찾기 — 기준선과 먼저 비교하기',
'payments.csv에서 새 손님(is_new_user)을 맞히고 싶어요.\n“모두 기존 손님”이라고 답하는 기준선, SVM, k-NN(k=5) 세 가지의\n정확도와 “시험용 새 손님 중 몇 명을 찾았는지”를 표로 비교해 주세요.\n(금액 amount에 빈 값이 있다고 들었어요. 처리 방법도 알려 주세요.)', '''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("%spayments.csv")
print("빈 값 개수:", df.isna().sum().to_dict())
df["amount"] = df["amount"].fillna(df["amount"].median())   # 빈 금액은 중앙값으로 채움
X = pd.get_dummies(df[["hour", "items", "amount", "channel", "city"]], dtype=int)
y = df["is_new_user"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

models = {"기준선(모두 기존)": DummyClassifier(strategy="most_frequent"),
          "SVM": make_pipeline(StandardScaler(), SVC()),
          "k-NN (k=5)": make_pipeline(StandardScaler(), KNeighborsClassifier(5))}
rows = []
for name, m in models.items():
    pred = m.fit(X_train, y_train).predict(X_test)
    found = int(((pred == 1) & (y_test == 1)).sum())
    rows.append([name, round((pred == y_test).mean(), 3), f"{found} / {int(y_test.sum())}"])
print(pd.DataFrame(rows, columns=["모델", "정확도", "찾은 새 손님"]).to_string(index=False))
''' % DATA)

# ───────── 4층 ─────────
C('04', 1, 'moa', '도미와 빙어를 점으로 찍어 보기',
'도미 35마리와 빙어 14마리의 길이·무게 데이터(fish_bream_smelt.csv)가 있어요.\n길이를 가로축, 무게를 세로축으로 산점도를 그려 주세요.\n종류마다 색을 다르게 하고, 그래프 글자는 영어로 해 주세요.', '''
import pandas as pd
import matplotlib.pyplot as plt

fish = pd.read_csv("%sfish_bream_smelt.csv")
print(fish["species"].value_counts())

for sp, color in [("bream", "tab:blue"), ("smelt", "tab:red")]:
    part = fish[fish["species"] == sp]
    plt.scatter(part["length"], part["weight"], label=sp, color=color)
plt.scatter(25, 150, marker="^", s=120, color="green", label="new fish (25cm, 150g)")
plt.xlabel("length (cm)"); plt.ylabel("weight (g)"); plt.legend(); plt.title("Bream vs smelt")
plt.show()
''' % DATA)
C('04', 2, 'x1', '수상한 생선 — 표준화 전과 후',
'k-NN(k=5)으로 길이 25cm·무게 150g인 생선이 도미인지 빙어인지 판정해 주세요.\n원래 단위 그대로 한 번, 표준화(평균 0·표준편차 1)한 뒤 한 번.\n두 경우 가장 가까운 이웃 5마리의 종류도 보여 주세요.', '''
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

fish = pd.read_csv("%sfish_bream_smelt.csv")
X = fish[["length", "weight"]].to_numpy()
y = fish["species"].to_numpy()
new = np.array([[25, 150]])

# ① 원래 단위
kn = KNeighborsClassifier(n_neighbors=5).fit(X, y)
idx = kn.kneighbors(new, return_distance=False)[0]
print("원래 단위 → 판정:", kn.predict(new)[0], "/ 이웃:", list(y[idx]))

# ② 표준화: (값 − 평균) ÷ 표준편차
mean, std = X.mean(axis=0), X.std(axis=0)
Xs, new_s = (X - mean) / std, (new - mean) / std
kn_s = KNeighborsClassifier(n_neighbors=5).fit(Xs, y)
idx = kn_s.kneighbors(new_s, return_distance=False)[0]
print("표준화 후 → 판정:", kn_s.predict(new_s)[0], "/ 이웃:", list(y[idx]))
''' % DATA)

# ───────── 5층 ─────────
C('05', 1, 'x2', '질문 나무가 만든 규칙 읽기',
'fish_bream_smelt.csv로 깊이 2짜리 의사결정나무를 만들어 주세요.\n나무가 고른 질문을 글(규칙)로 출력하고, 나무 그림도 그려 주세요.', '''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

fish = pd.read_csv("%sfish_bream_smelt.csv")
X, y = fish[["length", "weight"]], fish["species"]

tree = DecisionTreeClassifier(max_depth=2, random_state=0).fit(X, y)
print(export_text(tree, feature_names=["length", "weight"]))
print("학습 데이터 정확도:", tree.score(X, y))

plot_tree(tree, feature_names=["length", "weight"], class_names=list(tree.classes_), filled=True)
plt.show()
''' % DATA)
C('05', 2, 'x3', '나누는 약속 — 순서대로 자르기 vs 비율 맞추기',
'fish_bream_smelt.csv는 도미 35마리 다음에 빙어 14마리가 차례로 들어 있어요.\n① 앞 35마리로 학습, 뒤 14마리로 시험\n② train_test_split(stratify=...)로 비율 맞춰 나누기\n두 방법의 k-NN 시험 정확도와 시험용 종류 수를 비교해 주세요.', '''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

fish = pd.read_csv("%sfish_bream_smelt.csv")
X, y = fish[["length", "weight"]], fish["species"]

# ① 순서대로 자르기
kn = KNeighborsClassifier().fit(X[:35], y[:35])
print("① 순서대로 → 시험 정확도:", kn.score(X[35:], y[35:]), "/ 시험용:", y[35:].value_counts().to_dict())

# ② 비율 맞춰 나누기
X_tr, X_te, y_tr, y_te = train_test_split(X, y, stratify=y, random_state=42)
kn = KNeighborsClassifier().fit(X_tr, y_tr)
print("② 비율 맞춤 → 시험 정확도:", kn.score(X_te, y_te), "/ 시험용:", y_te.value_counts().to_dict())
''' % DATA)

# ───────── 6층 ─────────
C('06', 1, 'sia', '로지스틱 회귀의 점수 z와 확률',
'fish_bream_smelt.csv를 표준화한 뒤 로지스틱 회귀로 도미/빙어를 분류해 주세요.\n배점(계수)과 b(절편)를 보여 주고, 생선 3마리의 점수 z와 도미일 확률을 출력해 주세요.\n시그모이드 곡선 위에 그 3마리를 표시한 그래프도 그려 주세요(영어).', '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

fish = pd.read_csv("%sfish_bream_smelt.csv")
X = fish[["length", "weight"]]
y = (fish["species"] == "bream").astype(int)          # 1 = 도미

scaler = StandardScaler().fit(X)
lr = LogisticRegression().fit(scaler.transform(X), y)
print("배점 w (길이, 무게):", lr.coef_[0].round(2), "/ b:", lr.intercept_.round(2))

samples = pd.DataFrame({"length": [25, 12, 31], "weight": [150, 15, 600]})
z = lr.decision_function(scaler.transform(samples))
p = lr.predict_proba(scaler.transform(samples))[:, 1]
for (L, W), zi, pi in zip(samples.to_numpy(), z, p):
    print(f"길이 {L}cm, 무게 {W}g → z = {zi:.2f}, 도미일 확률 = {pi:.3f}")

zz = np.linspace(-8, 8, 200)
plt.plot(zz, 1 / (1 + np.exp(-zz)))
plt.scatter(z, p, color="red", zorder=3)
plt.axhline(0.5, ls="--", color="gray"); plt.xlabel("score z"); plt.ylabel("P(bream)"); plt.title("Sigmoid")
plt.show()
''' % DATA)
C('06', 2, 'x1', '직선을 긋는 세 방법 비교 — 퍼셉트론·로지스틱·SVM',
'rides.csv 이탈 예측에서 퍼셉트론, 로지스틱 회귀, 선형 SVM을 비교해 주세요.\n모두 표준화하고 class_weight="balanced"를 쓰고,\n시험용 정확도와 재현율을 표로 보여 주세요.', '''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, recall_score

df = pd.read_csv("%srides.csv")
X = df[["distance_km", "duration_min", "hour", "is_weekend", "fare"]]
y = df["churned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

models = {"퍼셉트론": Perceptron(class_weight="balanced", random_state=0),
          "로지스틱 회귀": LogisticRegression(class_weight="balanced"),
          "선형 SVM": LinearSVC(class_weight="balanced")}
rows = []
for name, m in models.items():
    pred = make_pipeline(StandardScaler(), m).fit(X_train, y_train).predict(X_test)
    rows.append([name, round(accuracy_score(y_test, pred), 3), round(recall_score(y_test, pred), 3)])
print(pd.DataFrame(rows, columns=["모델", "정확도", "재현율"]).to_string(index=False))
''' % DATA)

# ───────── 7층 ─────────
C('07', 1, 'moa', '배터리 수명 직선으로 맞히고 남은 무늬 보기',
'battery_sim.csv(시뮬레이션 600개)로 배터리 수명(cycles)을 선형 회귀로 맞혀 주세요.\n시험용 R²를 출력하고, 가로축 평균 온도·세로축 잔차(실제−예측) 그래프를 그려\n남은 무늬가 있는지 보여 주세요(그래프 글자는 영어).', '''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("%sbattery_sim.csv")
X = df[["avg_temp", "fast_charge", "depth_of_discharge", "daily_use"]]
y = df["cycles"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lin = LinearRegression().fit(X_train, y_train)
print("시험용 R²:", round(lin.score(X_test, y_test), 3))
print("계수:", {c: round(float(w), 1) for c, w in zip(X.columns, lin.coef_)})

resid = y_test - lin.predict(X_test)
plt.scatter(X_test["avg_temp"], resid, s=12)
plt.axhline(0, color="red")
plt.xlabel("average temperature (C)"); plt.ylabel("residual (cycles)"); plt.title("Residuals vs temperature")
plt.show()
''' % DATA)
C('07', 2, 'x2', '곡선·숲·부스팅 — 학습 점수와 시험 점수의 차이',
'battery_sim.csv로 다항(2차)+Ridge, 랜덤포레스트(300그루), 그래디언트 부스팅을 비교해 주세요.\n학습 R²와 시험 R², 그 차이(격차)를 표로 보여 주세요.', '''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

df = pd.read_csv("%sbattery_sim.csv")
X = df[["avg_temp", "fast_charge", "depth_of_discharge", "daily_use"]]
y = df["cycles"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {"다항+Ridge": make_pipeline(PolynomialFeatures(2), StandardScaler(), Ridge(alpha=1.0)),
          "랜덤포레스트": RandomForestRegressor(n_estimators=300, random_state=0),
          "부스팅": GradientBoostingRegressor(random_state=0)}
rows = []
for name, m in models.items():
    m.fit(X_train, y_train)
    tr, te = m.score(X_train, y_train), m.score(X_test, y_test)
    rows.append([name, round(tr, 3), round(te, 3), round(tr - te, 3)])
print(pd.DataFrame(rows, columns=["모델", "학습 R²", "시험 R²", "격차"]).to_string(index=False))
''' % DATA)

# ───────── 8층 ─────────
C('08', 1, 'sia', '손계산한 정밀도·재현율, 코드로 맞춰 보기',
'진짜 불 4곳 중 경보가 3곳을 잡았고, 경보는 모두 5번 울렸어요.\n이 상황을 정답(y_true)과 예측(y_pred) 리스트로 만들어\n정밀도·재현율·F1과 혼동행렬을 출력해 주세요. 제 손계산(3/5, 3/4)과 맞는지 보고 싶어요.', '''
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix

# 10곳: 1 = 진짜 불, 0 = 불 없음
y_true = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# 경보: 불 3곳을 잡고, 1곳을 놓치고, 불 없는 2곳에서 울림
y_pred = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]

print("정밀도:", precision_score(y_true, y_pred))   # 울린 5번 중 맞은 3번
print("재현율:", recall_score(y_true, y_pred))      # 진짜 불 4곳 중 잡은 3곳
print("F1    :", round(f1_score(y_true, y_pred), 3))
print("혼동행렬:", confusion_matrix(y_true, y_pred).tolist())
''')
C('08', 2, 'moa', 'MAE와 RMSE — 큰 실수 하나의 무게',
'택시 요금 5건의 예측이 각각 +300, −500, +200, −3000, +400원 빗나갔어요.\nMAE와 RMSE를 계산하고, 크게 빗나간 넷째 건을 −300원으로 고치면\n두 값이 각각 얼마나 내려가는지 보여 주세요.', '''
import numpy as np

errors = np.array([300, -500, 200, -3000, 400])   # 예측 − 실제

def report(e, title):
    mae = np.abs(e).mean()
    rmse = np.sqrt((e ** 2).mean())
    print(f"{title}: MAE = {mae:,.0f}원, RMSE = {rmse:,.0f}원")
    return mae, rmse

a = report(errors, "고치기 전")
fixed = errors.copy(); fixed[3] = -300
b = report(fixed, "넷째 건 고친 뒤")
print(f"내려간 양: MAE {a[0] - b[0]:,.0f}원, RMSE {a[1] - b[1]:,.0f}원")
''')

# ───────── 9층 ─────────
C('09', 1, 'x3', '배터리 5개로 MSE·RMSE·MAE·R² 직접 확인',
'배터리 5개의 실제 수명은 1334, 704, 1101, 568, 1371이고\n예측은 1200, 850, 1010, 640, 1330이에요.\n잔차와 MSE, RMSE, MAE, R²를 계산해 주세요. 공식도 주석으로 달아 주세요.', '''
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

actual = np.array([1334, 704, 1101, 568, 1371])
pred   = np.array([1200, 850, 1010, 640, 1330])

resid = actual - pred                      # 잔차 = 실제 − 예측
print("잔차:", resid)
mse = mean_squared_error(actual, pred)     # 잔차² 의 평균
print("MSE :", round(mse, 1))
print("RMSE:", round(np.sqrt(mse), 1))      # √MSE → 원래 단위(사이클)
print("MAE :", mean_absolute_error(actual, pred))   # |잔차| 의 평균
print("R²  :", round(r2_score(actual, pred), 3))     # 1 − SSE ÷ SST
''')
C('09', 2, 'x1', '어떤 특성이 수명을 가장 많이 설명하나 — 순열 중요도',
'battery_sim.csv로 랜덤포레스트 회귀를 만든 뒤\n특성마다 값을 섞어 보면 시험 점수가 얼마나 떨어지는지(순열 중요도) 계산해 주세요.\n막대그래프로 보여 주세요(그래프 글자는 영어).', '''
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance

df = pd.read_csv("%sbattery_sim.csv")
X = df[["avg_temp", "fast_charge", "depth_of_discharge", "daily_use"]]
y = df["cycles"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestRegressor(n_estimators=300, random_state=0).fit(X_train, y_train)
imp = permutation_importance(rf, X_test, y_test, n_repeats=10, random_state=0)
s = pd.Series(imp.importances_mean, index=X.columns).sort_values()
print((s.round(3)).to_string())

s.plot.barh()
plt.xlabel("drop in test R2 when shuffled"); plt.title("Permutation importance")
plt.show()
''' % DATA)

# ───────── 10층 ─────────
C('10', 1, 'moa', '의료비 데이터 첫인상 — 꼬리가 긴 분포',
'보험 의료비 데이터(insurance.csv)를 불러와서\n의료비(charges)의 평균과 중앙값, 흡연 여부별 평균을 보여 주고\n의료비 히스토그램을 그려 주세요(그래프 글자는 영어).', '''
import pandas as pd
import matplotlib.pyplot as plt

url = "%s"
df = pd.read_csv(url)
print("행, 열:", df.shape)
print("평균:", round(df["charges"].mean()), "/ 중앙값:", round(df["charges"].median()))
print(df.groupby("smoker")["charges"].mean().round(0))

df["charges"].plot.hist(bins=40, edgecolor="white")
plt.axvline(df["charges"].mean(), color="red", label="mean")
plt.axvline(df["charges"].median(), color="green", label="median")
plt.xlabel("charges (USD)"); plt.ylabel("people"); plt.legend(); plt.title("Medical charges")
plt.show()
''' % INSURANCE)
C('10', 2, 'x2', '평균만 답하기 vs 부스팅 — 그룹별 오차까지',
'insurance.csv로 의료비를 맞히는 그래디언트 부스팅을 만들고\n“평균만 답하기”와 MAE를 비교해 주세요.\n그리고 시험용에서 흡연자·비흡연자·의료비 상위 10% 그룹별 MAE도 보여 주세요.', '''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("%s")
X = pd.get_dummies(df.drop(columns="charges"), drop_first=True, dtype=int)
y = df["charges"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

base = np.full(len(y_test), y_train.mean())
gb = GradientBoostingRegressor(random_state=0).fit(X_train, y_train)
pred = gb.predict(X_test)
print("평균만 답하기 MAE:", round(mean_absolute_error(y_test, base)))
print("부스팅 MAE       :", round(mean_absolute_error(y_test, pred)))

groups = {"흡연자": X_test["smoker_yes"] == 1,
          "비흡연자": X_test["smoker_yes"] == 0,
          "상위 10%%": y_test >= y_test.quantile(0.9)}
for g, mask in groups.items():
    print(g, "MAE:", round(mean_absolute_error(y_test[mask], pred[mask])), f"({int(mask.sum())}명)")
''' % INSURANCE)

# 박사의 한 줄 판단 — 실제 실행 결과를 보고 쓴 문장
JUDGE = {'01_1': '‘무료’가 없는 당첨 메일은 규칙이 놓치고 머신러닝이 잡았습니다. 하지만 정상일 수도 있는 ‘무료 회의실 예약 안내’는 둘 다 스팸이라 했어요. 메일 8통으로 배운 결과라 아직 믿기엔 이릅니다.',
 '01_2': '1,200건 중 떠난 손님은 218명(약 18%)입니다. 정답이 한쪽으로 쏠려 있다는 것을 처음부터 알아 두면 2층의 ‘정확도 함정’을 피할 수 있어요.',
 '02_1': 'R² 0.921, 평균 1,049원 빗나감 — 본문 값과 몇 원 차이입니다. 기본요금 3,006원·km당 788원·분당 145원처럼 계수가 상식에 맞는지도 꼭 확인하세요.',
 '02_2': '정확도 0.796인데 떠난 손님 49명 중 0명을 잡았습니다. balanced로 바꾸자 정확도는 0.617로 내려갔지만 24명을 잡았어요. 어느 쪽이 나은지는 ‘놓친 손님 1명’의 비용으로 정합니다.',
 '03_1': '얕은 나무 평균 0.499, 깊은 나무 0.184 — 깊은 나무는 외우기만 했습니다. 다만 얕은 나무도 다섯 번 점수가 0.33~0.73으로 크게 흔들려, 한 번 점수만 믿으면 안 됩니다.',
 '03_2': 'AI 코드가 빈 금액 32개를 중앙값으로 채웠습니다. SVM은 기준선과 똑같이 새 손님을 0명 찾았고, k-NN은 7명을 찾았지만 정확도는 더 낮습니다. 본문 숫자(0.719, 4명)와 다른 것은 나누는 방법과 빈 값 처리가 달라서입니다.',
 '04_1': '초록 세모(25cm, 150g)는 길이로 보면 도미 무리 가까이 있습니다. 하지만 세로축 숫자(무게)가 훨씬 커서 컴퓨터는 다르게 볼 수 있어요. 다음 카드에서 확인합니다.',
 '04_2': '원래 단위에서는 이웃 5마리 중 4마리가 빙어라 ‘빙어’, 표준화하니 5마리 모두 도미라 ‘도미’입니다. 단위가 다른 특성은 같은 자로 바꿔야 한다는 것을 결과가 그대로 보여 줍니다.',
 '05_1': '깊이 2를 허락했지만 나무는 ‘무게 130.95g 이하인가?’ 질문 하나로 끝냈습니다. 학습 정확도 1.0은 이 쉬운 짝에서는 어떤 모델도 받는 점수라, 어려운 짝으로 다시 확인해야 합니다.',
 '05_2': '순서대로 자르면 시험용 14마리가 모두 빙어라 정확도 0.0, 비율 맞춰 나누면 1.0입니다. 모델은 같은데 나누는 방법만으로 점수가 끝과 끝으로 갈렸어요.',
 '06_1': 'z가 0보다 크면 확률이 0.5를 넘습니다(25cm·150g → z 1.16 → 0.762). 이 생선은 경계 가까이에 있으니, 0.762라는 숫자를 “확실히 도미”로 읽으면 안 됩니다.',
 '06_2': '로지스틱과 선형 SVM은 재현율 0.75로 같고, 퍼셉트론은 정확도가 조금 높지만 떠난 손님을 절반만 잡았습니다. 직선을 긋는 방법보다 “무엇을 놓치면 안 되나”가 고르는 기준입니다.',
 '07_1': 'R² 0.916으로 잘 맞는 것 같지만, 잔차가 낮은 온도와 높은 온도 양쪽에서 위로 휘는 U자 무늬를 남겼습니다. 직선이 놓친 곡선 관계가 있다는 신호입니다.',
 '07_2': '다항+Ridge가 시험 R² 0.945로 가장 높고 격차도 0.004로 가장 작습니다. 숲은 학습 0.989로 높지만 격차 0.059 — 조금 외웠어요. 이 데이터는 곡선 관계를 넣어 만든 시뮬레이션이라 곡선 모델이 유리하다는 점도 기억하세요.',
 '08_1': '정밀도 0.6(=3/5), 재현율 0.75(=3/4) — 손계산과 같습니다. 혼동행렬 [[4, 2], [1, 3]]에서 2는 헛경보, 1은 놓친 불입니다.',
 '08_2': '큰 실수 하나를 고치자 MAE는 540원, RMSE는 1,026원 내려갔습니다. RMSE가 큰 실수에 훨씬 민감하다는 것을 숫자로 확인했어요.',
 '09_1': 'MSE 10,883.6, RMSE 104.3, MAE 96.8 — 본문 손계산과 같습니다. R² 0.898은 배터리 5개만으로 낸 값이라 참고로만 봅니다.',
 '09_2': '평균 온도를 섞으면 시험 R²가 1.24만큼 떨어져 가장 중요한 특성입니다. 중요도는 “모델이 많이 기대는 정도”이지 “원인”이 아니라는 점은 계수 읽기와 같습니다.',
 '10_1': '평균 13,270달러가 중앙값 9,382달러보다 큽니다 — 아주 비싼 일부가 평균을 끌어올린, 꼬리가 긴 분포예요. 흡연자 평균은 비흡연자의 약 3.8배입니다.',
 '10_2': '부스팅 MAE 2,453달러로 평균만 답하기(9,593달러)보다 약 74% 줄었습니다. 그룹별로는 의료비 상위 10%의 오차가 가장 큽니다. 본문 그래프의 그룹별 숫자와는 다르니, 보고서에는 그룹을 나눈 기준과 설정을 함께 적습니다.'}
for _k, _v in JUDGE.items():
    _n, _i = _k.split("_"); CARDS[(_n, int(_i))]["judge"] = _v
