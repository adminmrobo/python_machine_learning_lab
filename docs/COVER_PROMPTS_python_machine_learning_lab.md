# 표지 그림 지시문 — 파이썬 머신러닝 연구소 (Genspark용)

> 그림 17장: 목차 표지 1 + 층 표지 15 + 지하 실전 연습장 1. 모두 **16비트 RPG 픽셀아트**, 가로 16:9.
> 만드는 순서: ① 목차 표지를 먼저 받아 그림체를 확정 → ② 나머지 16장에는 그 그림을 참고 그림으로 함께 올린다.
> 캐릭터 참고 그림: 저장소 `build/sprites/` 의 기본 표정(doc_e08 · asst_e13 · fly_e10 · robo_e13 · sia_e13 · moa_e13 · x1_e13 · x2_e13 · x3_e13)을 함께 첨부한다.

## 공통 규칙 (모든 요청 앞에 붙임)

```
16-bit RPG pixel art, crisp hard pixel edges, no anti-aliasing, limited palette, native canvas 480x270 pixels upscaled 4x to 1920x1080 with nearest-neighbor.
Bright white-and-pale-sky-blue background, clean daylight research-building mood.
ABSOLUTELY NO text, letters, numbers, logos or signs anywhere in the image.
Characters must match the attached reference sprites exactly (faces, hair, outfits, colors). Do not add a white robot.
Cast (use only those named in each prompt):
- Doctor: man with thin teal square glasses, swept-back black-and-white hair tied in a short ponytail, white lab coat.
- Assistant Haru: girl with long pink hair in two buns with a navy streak, white lab coat, jeans.
- Fruit-fly researcher: small humanoid fruit fly with big red compound eyes, white lab coat over black vest, black gloves.
- Abacus Bot: boxy beige robot with a green screen face showing sparkly eyes, holding a wooden abacus.
- Intern Sia: girl with long straight black hair and side-swept bangs, dark dress with white collar.
- Intern Moa: girl with long light-brown hair, white ribbon and checkered ribbon above the ears, cream outfit with red bow.
- X1 / X2 / X3: mysterious dark silhouettes; X1 has a pink ribbon, X2 a teal glasses glint, X3 a small yellow bell.
Height order: Doctor ≥ Haru > Abacus Bot > Fruit fly (fruit fly is the smallest).
Team colors: Fruit-fly team = red accents (Sia, X1, X2); Abacus-Bot team = teal accents (Moa, Haru, X3).
```

## 목록

| 키 | 파일 이름 | 쓰는 곳 |
|---|---|---|
| cover_index | cover_index.png | 첫 화면 |
| cover_01 ~ cover_15 | cover_01.png ~ cover_15.png | 각 층 |
| cover_practice | cover_practice.png | 지하 실전 연습장 |

<a id="cover_index"></a>
### cover_index — 건물 안내도
| 항목 | 내용 |
|---|---|
| 대체 글 (alt) | 15층짜리 픽셀 연구소 건물 앞에 두 팀과 박사가 서 있는 표지. 1~10층은 불이 켜지고 11~15층은 공사 중이다. |

```
A tall 15-floor programming research building seen from the front, left-center of the frame. Floors 1–10 have warm lit windows with tiny monitors showing colorful code-like bars (no readable text); floors 11–15 are wrapped in yellow scaffolding with an orange crane on the roof.
In front of the entrance on a green lawn: the Fruit-fly team on the left (Fruit-fly researcher pointing forward, Intern Sia, X1, X2 with red accents), the Abacus-Bot team on the right (Abacus Bot holding its abacus, Intern Moa cheering, Assistant Haru, X3 with teal accents), and the Doctor in the middle holding a small referee whistle.
Cheerful, welcoming first-day mood.
```

<a id="cover_01"></a>
### cover_01 — 1층 로비 · 인공지능 모델의 개요
| 대체 글 (alt) | 연구소 1층 로비. 안내 데스크 위 큰 모니터 앞에서 박사가 두 팀에게 건물 지도를 펼쳐 보인다. |
```
Interior of the building's ground-floor lobby: a reception desk with a big monitor showing abstract colored code bars, a pixel floor-map board of a 15-floor building on the wall.
The Doctor unfolds a large building map; Fruit-fly researcher and Abacus Bot stand on opposite sides like team captains; Haru and Moa peek in with curiosity.
```

<a id="cover_02"></a>
### cover_02 — 2층 · 분류와 회귀 (택시)
| 대체 글 (alt) | 2층 실험실 창밖으로 노란 택시가 보이고, 칠판에 점들 사이 직선과 두 무리 사이 경계선이 그려져 있다. |
```
2nd-floor lab overlooking a street with a yellow taxi. A whiteboard shows two simple diagrams drawn with pixels: dots with a straight line through them, and two colored dot groups split by a boundary line.
Intern Moa presents at the board; Abacus Bot holds up a coin happily; Fruit-fly researcher frowns at a scoreboard that shows only colored bars.
```

<a id="cover_03"></a>
### cover_03 — 3층 · 점수로 두 모델 비교
| 대체 글 (alt) | 3층에 화재경보기와 막대 점수판이 있고, 조수 하루가 점수판 막대 다섯 개를 가리킨다. |
```
3rd-floor lab with a ceiling fire alarm (red light), a big bar-chart scoreboard with five bars of different heights, and a magnifying glass on the desk.
Assistant Haru points at the five bars; X1 holds a small checklist; Abacus Bot looks shocked at a tall single bar.
```

<a id="cover_04"></a>
### cover_04 — 4층 · 생선가게의 KNN
| 대체 글 (alt) | 4층 생선가게 진열대에 큰 파란 도미와 작은 빨간 빙어가 있고, 저울 위에 애매한 생선 한 마리가 놓여 있다. |
```
A cozy fish-market counter inside the 4th floor: large blue bream fish and small slim red smelt fish on ice, a scale in the center holding one medium "suspicious" fish with a question-mark-shaped bubble (no text).
X3 happily points at the fish; Fruit-fly researcher holds a magnifying glass; Abacus Bot carries a giant crate of fish.
```

<a id="cover_05"></a>
### cover_05 — 5층 · 분류 모델은 하나의 함수
| 대체 글 (alt) | 5층 벽면에 질문 상자들이 갈래 길로 이어진 의사결정나무가 그려져 있고, 일곱 종류의 물고기 그림이 붙어 있다. |
```
5th-floor lab wall with a large pixel decision-tree diagram (purple boxes connected by branching lines, green and pink leaf boxes), and seven different fish silhouettes pinned around it.
Assistant Haru presents; X1 and X2 compare two similar-looking fish side by side.
```

<a id="cover_06"></a>
### cover_06 — 6층 · 직선 하나, 세 모델
| 대체 글 (alt) | 6층 바닥에 빨간 점과 파란 점 무리 사이로 검은 직선과 청록 점선 두 줄이 도로처럼 그어져 있다. |
```
6th-floor lab floor drawn like a game map: a cluster of red dots and a cluster of blue squares, separated by a black straight line with two teal dashed lines forming a wide "road" between them; an S-shaped curve glowing on a wall screen.
Intern Sia stands on the road center line; Abacus Bot proudly draws a line too close to the blue dots.
```

<a id="cover_07"></a>
### cover_07 — 7층 · 성능 개선 (배터리 공장)
| 대체 글 (alt) | 7층 배터리 공장 라인에 초록 눈금 배터리가 흐르고, 한쪽에 나무 모형 숲과 곡선 그래프가 있다. |
```
7th-floor battery factory line: batteries with green charge bars moving on a conveyor, gears turning; on one side a tiny model forest of many small trees, on the other a smooth curved graph on a screen.
X2 compares three bars of different heights on a tablet; Abacus Bot hugs the model forest.
```

<a id="cover_08"></a>
### cover_08 — 8층 · 중간 점검실
| 대체 글 (alt) | 8층 점검실 칠판 앞에서 박사가 점검표를 들고, 시아는 졸고 모아는 낱말 카드를 들고 있다. |
```
8th-floor review room: the Doctor holds a big clipboard checklist with green check marks (no text) in front of a chalkboard covered with simple icons (fish, taxi, battery, tree).
Intern Sia yawns sleepily at a desk; Intern Moa holds up flash cards cheerfully; both teams sit together.
```

<a id="cover_09"></a>
### cover_09 — 9층 · 회귀 모델 읽기
| 대체 글 (alt) | 9층 대형 화면에 출발선에서 좌우로 뻗는 빨강·파랑 막대 그래프가 있고, 피자 한 판 그림이 조각나 있다. |
```
9th-floor analysis room: a large screen with a waterfall bar chart (red and blue bars stepping left and right from a dotted start line), and a pixel pizza with one slice missing on a side screen.
X1 presents pointing at the pizza; Abacus Bot celebrates a small trophy.
```

<a id="cover_10"></a>
### cover_10 — 10층 · 보험 실제 사례
| 대체 글 (alt) | 10층에 파란 방패와 빨간 우산이 있고, 서류 더미 속에서 아주 작은 빨간 점 몇 개를 돋보기로 찾는다. |
```
10th-floor insurance office: a blue shield emblem and a red umbrella icon on the wall (no text), tall stacks of documents, and among thousands of tiny grey dots only a few small red dots glowing.
Fruit-fly researcher searches with a magnifying glass; Assistant Haru reads a long receipt; Intern Moa sits in a counseling chair talking to the Doctor.
```

<a id="cover_11"></a>
### cover_11 ~ cover_15 — 공사 중인 층 (같은 틀, 소품만 다름)
| 대체 글 (alt) | 해당 층이 노란 비계와 주황 고깔로 덮여 있고, 주판봇이 자재 상자를 나른다. |
```
An upper floor of the research building under construction: yellow scaffolding, orange traffic cones, a crane hook. Abacus Bot carries a crate of materials.
Floor-specific prop in the crate: 11 = blank picture frames; 12 = colored marbles sorted into three groups; 13 = a small game controller with a star; 14 = open books and speech bubbles (no text); 15 = a rooftop stage with spotlights.
```

<a id="cover_practice"></a>
### cover_practice — 지하 실전 연습장
| 대체 글 (alt) | 지하 연습장에 생선가게·택시 차고·배터리 라인·보험 창구가 네 개의 무대처럼 나란히 있고 캐릭터들이 각 무대에서 일한다. |
```
Basement practice arena of the building, split into four small side-by-side stage sets: a fish counter, a taxi garage, a battery conveyor, an insurance service desk.
Fruit-fly researcher at the fish counter, Assistant Haru at the taxi garage, Abacus Bot at the battery line, the Doctor at the insurance desk; soft white lighting, game-level atmosphere.
```

## 받은 뒤 반영 방법

- 원래 격자(480×270)를 찾아 `NEAREST` 정수배로만 키운 무손실 WebP(1920×1080)로 `assets/img/cover_NN.webp`에 저장.
- 공유 미리보기(og:image)와 목차 썸네일은 표지에서 정수배로 잘라 만든다.
- 표정이 팩과 다르면 기존 그림 + 표정 그림을 첨부해 “표정만 편집”으로 다시 요청.
