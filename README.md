**[한국어](#ko) · [中文](#zh)**

---

<a id="ko"></a>

# 파이썬 머신러닝 연구소 — 15층 연구실 해설

강남대학교 「파이썬머신러닝」(EB24220-02, 2026년 2학기) 강의를 **15층짜리 프로그래밍 연구소 건물**로 옮긴 해설 사이트입니다. 한 주에 한 층씩 올라가며, 파이썬과 머신러닝을 처음 배우는 분이 데이터 한 줄에서 실제 사례까지 따라올 수 있게 만들었습니다.

- **진행 방식** 층마다 **초파리팀**(조장 초파리 연구원 · 인턴 시아 · X1 · X2)과 **주판봇팀**(조장 주판봇 · 인턴 모아 · 조수 하루 · X3)이 조별발표 · 개인발표 · 상담 · 토론으로 개념을 풀고, 마지막에 **팀 대항전**을 벌입니다. 심판은 **박사**입니다.
- **저자** 안상선 ((주)M-Robo 대표) · [소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)
- **부교재** 박해선, 『혼자 공부하는 머신러닝+딥러닝』, 한빛미디어
- **라이선스** CC BY-NC 4.0 (캐릭터 그림 제외)

## 언어

이 시리즈는 한국어 원본과 외국어판 1개로 볼 수 있다.

- 고르는 방법: 화면 최상단 메뉴의 🌐 언어 선택 상자나 오른쪽 아래 🌐 배너에서 고른다. 고른 언어는 브라우저에 기억된다.
- 자동 전환: 한국어 페이지에 처음 들어오면, 브라우저 언어가 지원 언어일 때 그 언어판으로 옮겨 간다. 번역판 주소로 들어오면 그대로 연다.
- 주소 끝에 `?lang=en`처럼 붙이면 그 언어로 바로 연다.
- 언어판 파일은 `이름.언어코드.html` 꼴이다.

<!-- i18n:langtable -->
| 언어 | 파일 이름 | 바로 보기 |
|---|---|---|
| 한국어 | `index.html` | [바로 보기](https://adminmrobo.github.io/python_machine_learning_lab/index.html) |
| 中文 | `index.zh.html` | [바로 보기](https://adminmrobo.github.io/python_machine_learning_lab/index.zh.html) |
<!-- /i18n:langtable -->

## 보기

- 첫 화면 — https://adminmrobo.github.io/python_machine_learning_lab/
- 내려받았다면 `index.html`을 브라우저로 열면 됩니다. 페이지마다 CSS·JS·그림이 한 파일에 들어 있습니다.

## 15층

| 층 | 주차 | 페이지 | 대항전 |
|---|---|---|---|
| 1F | 1 | [인공지능 모델의 개요](weeks/w01_ai_model_overview.html) | 초파리팀 승 |
| 2F | 2 | [지도학습 ① 분류와 회귀](weeks/w02_classification_and_regression.html) | 초파리팀 승 |
| 3F | 3 | [지도학습 ② 점수로 두 모델 비교하기](weeks/w03_scores_and_cross_validation.html) | 초파리팀 승 |
| 4F | 4 | [지도학습 ③ 생선가게의 k-최근접 이웃](weeks/w04_fish_market_knn.html) | 초파리팀 승 |
| 5F | 5 | [특성공학과 교차검증 — 분류 모델은 모두 하나의 함수](weeks/w05_one_function_rule_knn_tree.html) | 조건부 |
| 6F | 6 | [로지스틱 회귀 — 직선 하나, 세 모델](weeks/w06_logistic_perceptron_svm.html) | 초파리팀 승 |
| 7F | 7 | [모델 성능 개선 — 규제 · 앙상블 · 하이퍼파라미터](weeks/w07_improving_models_battery.html) | 초파리팀 승 |
| 8F | 8 | [**중간 점검실**](weeks/w08_midterm_review.html) | 초파리팀 승 |
| 9F | 9 | [회귀 모델 읽기 — 오차 · 결정계수 · SHAP](weeks/w09_reading_regression_models.html) | 주판봇팀 승 |
| 10F | 10 | [실제 사례 — 드문 청구 잡기와 의료비 예측](weeks/w10_real_cases_insurance.html) | 초파리팀 승 |
| 11F | 11 | [물고기 한 마리에서 — 나무 · 숲 · 내리막 걸음](weeks/w11_fish_trees_forest_gradient.html) | 주판봇팀 승 |
| 12F~15F | 12~15 | 공사 중 (강의 자료를 받으면 엽니다) | — |
| B1 | — | [**지하 실전 연습장**](practice/index.html) — 생선가게 · 택시회사 · 배터리 공장 · 보험사 | 미션 판정 |

## 구성

```
index.html                 건물 안내도 (강좌 안내 · 15층 · 두 팀 · 공부하는 법 · 실습 도구)
weeks/wNN_*.html           층 페이지 (단일 파일)
practice/index.html        지하 실전 연습장 (네 장면, 미션 자동 판정)
data/rides.csv             택시 1,200건 (수업용 합성 데이터)
data/payments.csv          결제 800건 (수업용 합성 데이터)
data/fishmarket_practice.csv  물고기 159마리 (JSE fishcatch — 1917년 핀란드 랭겔매베시 호수 어획 기록, 11층)
data/KG_00_registry.json   지식 그래프 등록부
notebooks/                 실습 노트북 (출력 제거, 정답 변환 오류 'No': 1 → 0 수정)
build/                     빌드 (python3 build/build.py)
  pages/wNN.py · index.py  층별 원고
  lab.css · ml.css         공통 스타일
  lab.js · ml.js · kgx.js  공통 위젯 · 머신러닝 실험 위젯 · 지식 색인
  pixel.py                 픽셀 대체 표지 (15층 건물)
  practice.py              실전 연습장
  sprites/                 캐릭터 표정 (96px)
docs/                      검토 보고서 · 그림 지시문
```

## 숫자에 대하여

- 2·3층의 숫자는 rides.csv · payments.csv로 교안과 같은 설정에서 **다시 실행해 확인**했습니다. 교안 예시와 다른 곳은 페이지의 「원자료와 다른 값」 상자에 밝혔습니다.
- 5~10층의 점수는 각 교안이 보고한 실행 결과를 옮겼습니다.
- 11층의 숫자는 fishmarket_practice.csv로 이 사이트를 만들 때 **직접 실행**한 값입니다. 교안의 표·차트는 수업용 가상 수치라, 다른 곳은 「원자료와 다른 값」 상자에 밝혔습니다.
- 페이지 안 실험의 점 분포 중 일부는 설명용 모형이며, 바닥글에 표시했습니다.

---

<a id="zh"></a>

# Python机器学习研究所 —— 15 层研究室讲解

这是把江南大学「Python 机器学习」（EB24220-02，2026 年第 2 学期）课程搬进**一座 15 层的编程研究所大楼**的讲解网站。每周上一层楼，让初学 Python 和机器学习的人能从一行数据一路跟到真实案例。

- **进行方式** 每层由**果蝇队**（组长果蝇研究员 · 实习生西娅 · X1 · X2）和**算盘宝队**（组长算盘宝 · 实习生茉雅 · 助手 Haru · X3）通过小组发表 · 个人发表 · 咨询 · 讨论讲解概念，最后进行**团队对抗赛**。裁判是**博士**。
- **作者** Ahn Sangsun（M-Robo 公司 CEO）· [简介](https://adminmrobo.github.io/who_am_i/who_am_i.html)
- **辅助教材** 朴海善，《自学机器学习+深度学习》，Hanbit Media
- **许可证** CC BY-NC 4.0（角色图片除外）

## 语言

本系列可以阅读韩语原版和 1 个外语版。

- 选择方法：在页面最上方菜单的 🌐 语言选择框或右下角的 🌐 横幅中选择。所选语言会被浏览器记住。
- 自动切换：首次进入韩语页面时，如果浏览器语言是支持的语言，就会跳转到该语言版。从翻译版地址进入则直接打开。
- 在地址末尾加上 `?lang=en` 这样的参数，就能直接以该语言打开。
- 语言版文件采用 `名称.语言代码.html` 的形式。

<!-- i18n:langtable -->
| 语言 | 文件名 | 直接查看 |
|---|---|---|
| 한국어 | `index.html` | [直接查看](https://adminmrobo.github.io/python_machine_learning_lab/index.html) |
| 中文 | `index.zh.html` | [直接查看](https://adminmrobo.github.io/python_machine_learning_lab/index.zh.html) |
<!-- /i18n:langtable -->

## 查看

- 首页 —— https://adminmrobo.github.io/python_machine_learning_lab/index.zh.html
- 如果已下载，用浏览器打开 `index.html` 即可。每个页面的 CSS·JS·图片都包含在一个文件中。

## 15 层

| 楼层 | 周次 | 页面 | 对抗赛 |
|---|---|---|---|
| 1F | 1 | [人工智能模型概述](weeks/w01_ai_model_overview.zh.html) | 果蝇队胜 |
| 2F | 2 | [监督学习 ① 分类与回归](weeks/w02_classification_and_regression.zh.html) | 果蝇队胜 |
| 3F | 3 | [监督学习 ② 用分数比较两个模型](weeks/w03_scores_and_cross_validation.zh.html) | 果蝇队胜 |
| 4F | 4 | [监督学习 ③ 鱼店的K近邻](weeks/w04_fish_market_knn.zh.html) | 果蝇队胜 |
| 5F | 5 | [特征工程与交叉验证 —— 分类模型都是一个函数](weeks/w05_one_function_rule_knn_tree.zh.html) | 有条件 |
| 6F | 6 | [逻辑回归 —— 一条直线，三个模型](weeks/w06_logistic_perceptron_svm.zh.html) | 果蝇队胜 |
| 7F | 7 | [提升模型性能 —— 正则化 · 集成 · 超参数](weeks/w07_improving_models_battery.zh.html) | 果蝇队胜 |
| 8F | 8 | [**期中检查室**](weeks/w08_midterm_review.zh.html) | 果蝇队胜 |
| 9F | 9 | [读懂回归模型 —— 误差 · 决定系数 · SHAP](weeks/w09_reading_regression_models.zh.html) | 算盘宝队胜 |
| 10F | 10 | [真实案例 —— 捕捉罕见理赔与预测医疗费](weeks/w10_real_cases_insurance.zh.html) | 果蝇队胜 |
| 11F | 11 | [从一条鱼开始 —— 树 · 森林 · 下坡的脚步](weeks/w11_fish_trees_forest_gradient.zh.html) | 算盘宝队胜 |
| 12F~15F | 12~15 | 施工中（收到讲义后开放） | — |
| B1 | — | [**地下实战练习场**](practice/index.zh.html) —— 鱼店 · 出租车公司 · 电池工厂 · 保险公司 | 任务判定 |

## 构成

```
index.html                 건물 안내도 (강좌 안내 · 15층 · 두 팀 · 공부하는 법 · 실습 도구)
weeks/wNN_*.html           층 페이지 (단일 파일)
practice/index.html        지하 실전 연습장 (네 장면, 미션 자동 판정)
data/rides.csv             택시 1,200건 (수업용 합성 데이터)
data/payments.csv          결제 800건 (수업용 합성 데이터)
data/fishmarket_practice.csv  鱼159条（JSE fishcatch — 1917年芬兰朗厄尔迈韦西湖渔获记录，11层）
data/KG_00_registry.json   지식 그래프 등록부
notebooks/                 실습 노트북 (출력 제거, 정답 변환 오류 'No': 1 → 0 수정)
build/                     빌드 (python3 build/build.py)
  pages/wNN.py · index.py  층별 원고
  lab.css · ml.css         공통 스타일
  lab.js · ml.js · kgx.js  공통 위젯 · 머신러닝 실험 위젯 · 지식 색인
  pixel.py                 픽셀 대체 표지 (15층 건물)
  practice.py              실전 연습장
  sprites/                 캐릭터 표정 (96px)
docs/                      검토 보고서 · 그림 지시문
```

## 关于数字

- 2·3 层的数字已用 rides.csv · payments.csv 按与讲义相同的设置**重新运行确认**。与讲义示例不同之处，已在页面的「与原始资料不同的值」框中说明。
- 5~10 层的分数照搬了各讲义报告的运行结果。
- 11 层的数字是制作本网站时用 fishmarket_practice.csv **亲自运行**的值。讲义的表格·图表是课堂用虚拟数值，不同之处已在「与原始资料不同的值」框中说明。
- 页面内实验的部分点分布是说明用模型，已在页脚标注。
