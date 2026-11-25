# 파이썬 머신러닝 연구소 — 15층 연구실 해설

강남대학교 「파이썬머신러닝」(EB24220-02, 2026년 2학기) 강의를 **15층짜리 프로그래밍 연구소 건물**로 옮긴 해설 사이트입니다. 한 주에 한 층씩 올라가며, 파이썬과 머신러닝을 처음 배우는 분이 데이터 한 줄에서 실제 사례까지 따라올 수 있게 만들었습니다.

- **진행 방식** 층마다 **초파리팀**(조장 초파리 연구원 · 인턴 시아 · X1 · X2)과 **주판봇팀**(조장 주판봇 · 인턴 모아 · 조수 하루 · X3)이 조별발표 · 개인발표 · 상담 · 토론으로 개념을 풀고, 마지막에 **팀 대항전**을 벌입니다. 심판은 **박사**입니다.
- **저자** 안상선 ((주)M-Robo 대표) · [소개](https://adminmrobo.github.io/who_am_i/who_am_i.html)
- **부교재** 박해선, 『혼자 공부하는 머신러닝+딥러닝』, 한빛미디어
- **라이선스** CC BY-NC 4.0 (캐릭터 그림 제외)

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
| 11F~15F | 11~15 | 공사 중 (강의 자료를 받으면 엽니다) | — |
| B1 | — | [**지하 실전 연습장**](practice/index.html) — 생선가게 · 택시회사 · 배터리 공장 · 보험사 | 미션 판정 |

## 구성

```
index.html                 건물 안내도 (강좌 안내 · 15층 · 두 팀 · 공부하는 법 · 실습 도구)
weeks/wNN_*.html           층 페이지 (단일 파일)
practice/index.html        지하 실전 연습장 (네 장면, 미션 자동 판정)
data/rides.csv             택시 1,200건 (수업용 합성 데이터)
data/payments.csv          결제 800건 (수업용 합성 데이터)
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
- 페이지 안 실험의 점 분포 중 일부는 설명용 모형이며, 바닥글에 표시했습니다.
