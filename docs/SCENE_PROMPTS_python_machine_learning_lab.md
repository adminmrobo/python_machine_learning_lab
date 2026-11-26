# 장면 그림 지시문 — 파이썬 머신러닝 연구소 1~10층 (Genspark용)

> 단계마다 1장, 모두 39장. 16비트 RPG 픽셀아트, 가로 3:2(1200×800, 원래 격자 300×200의 4배).
> 만드는 순서: 이미 받은 표지(cover_index)를 참고 그림으로 함께 올리고, 대화 하나에 3~5장씩 같은 층끼리 요청합니다.
> 받은 PNG는 이름 그대로 주시면 무손실 WebP로 바꿔 각 단계 맨 위에 넣습니다. 그림이 없으면 그 자리는 비어 있고, 설명 그림(코드로 그린 도식)은 그대로 보입니다.

## 공통 규칙 (모든 요청 앞에 붙임)

```
16-bit RPG pixel art, crisp hard pixel edges, no anti-aliasing, limited palette, native canvas 300x200 pixels upscaled 4x to 1200x800 (3:2) with nearest-neighbor.
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

| 파일 이름 | 층·단계 | 장면 (한국어 요약) |
|---|---|---|
| scene_01_lv1.png | 1층 단계 1 | 사람이 손으로 규칙을 적는 쪽과, 예시 메일을 보고 스스로 분류하는 주판봇 쪽. |
| scene_01_lv2.png | 1층 단계 2 | 정답지로 공부, 옷장 정리, 게임 점수 — 세 가지 학습 방식. |
| scene_01_lv3.png | 1층 단계 3 | 문제 정의 → 모델 선택 → 결과 검증 세 방. |
| scene_01_lv4.png | 1층 단계 4 | 세 AI 도구에 같은 부탁을 하고 답을 비교한다. |
| scene_02_lv1.png | 2층 단계 1 | 문제지(X)와 정답지의 빈 곳(y), 자와 분류 상자. |
| scene_02_lv2.png | 2층 단계 2 | 영수증 점들 사이로 직선을 긋고 빗나간 거리를 잰다. |
| scene_02_lv3.png | 2층 단계 3 | 카드를 섞어 학습용과 자물쇠 건 시험용으로 나눈다. |
| scene_02_lv4.png | 2층 단계 4 | 모두 “남는다”고 찍는 사이 떠나는 두 손님. |
| scene_03_lv1.png | 3층 단계 1 | 모의고사 다섯 번과 점수의 기복. |
| scene_03_lv2.png | 3층 단계 2 | 울린 경보와 진짜 불 — 정밀도와 재현율. |
| scene_03_lv3.png | 3층 단계 3 | 너그러운 채점자(MAE)와 큰 실수를 크게 보는 채점자(RMSE). |
| scene_03_lv4.png | 3층 단계 4 | 단서가 부족한 장부와 사진으로 하는 딥러닝 체험. |
| scene_04_lv1.png | 4층 단계 1 | 장부 숫자를 지도에 핀으로 꽂는다. |
| scene_04_lv2.png | 4층 단계 2 | 가장 가까운 이웃 다섯이 투표한다. |
| scene_04_lv3.png | 4층 단계 3 | 순서대로 자르면 한쪽에 몰리는 생선 상자. |
| scene_04_lv4.png | 4층 단계 4 | 눈금이 다른 자와 저울을 같은 자로 바꾼다. |
| scene_05_lv1.png | 5층 단계 1 | 모두 같은 일을 하는 세 자판기 — 분류 함수. |
| scene_05_lv2.png | 5층 단계 2 | 같은 원본은 한쪽에만 — 쌍둥이 시험지. |
| scene_05_lv3.png | 5층 단계 3 | 스무고개처럼 가장 잘 가르는 질문부터. |
| scene_05_lv4.png | 5층 단계 4 | 쉬운 짝, 어려운 짝, 새 특성 만들기. |
| scene_06_lv1.png | 6층 단계 1 | 배점으로 총점을 내고 커트라인으로 가른다. |
| scene_06_lv2.png | 6층 단계 2 | 틀린 것만 고치고 다 맞으면 멈추는 퍼셉트론. |
| scene_06_lv3.png | 6층 단계 3 | “비 온다” 대신 “강수 확률 70%”. |
| scene_06_lv4.png | 6층 단계 4 | 두 동네 사이에 가장 넓은 도로를 낸다. |
| scene_07_lv1.png | 7층 단계 1 | 오즈가 몇 배로 뛰는지. |
| scene_07_lv2.png | 7층 단계 2 | 직선으로 맞히고 남은 U자 무늬. |
| scene_07_lv3.png | 7층 단계 3 | 휘어지는 자와 고무줄 — 규제. |
| scene_07_lv4.png | 7층 단계 4 | 숲의 투표와 오답 노트 부스팅. |
| scene_08_lv1.png | 8층 단계 1 | 낱말 카드로 1~7층 복습. |
| scene_08_lv2.png | 8층 단계 2 | 중간 과제 다섯 문항 길잡이. |
| scene_08_lv3.png | 8층 단계 3 | 작은 숫자로 직접 계산해 보기. |
| scene_09_lv1.png | 9층 단계 1 | 엄한 채점자, 단위를 맞춘 채점자, 너그러운 채점자. |
| scene_09_lv2.png | 9층 단계 2 | 피자 한 판 중 모델이 설명한 몫. |
| scene_09_lv3.png | 9층 단계 3 | 재료 하나만 바꿨을 때의 효과 — 계수. |
| scene_09_lv4.png | 9층 단계 4 | 상금을 공정하게 나누는 SHAP. |
| scene_10_lv1.png | 10층 단계 1 | 100건 중 1~2건뿐인 청구. |
| scene_10_lv2.png | 10층 단계 2 | 냄새는 잘 맡지만 짖지 않는 탐지견. |
| scene_10_lv3.png | 10층 단계 3 | 꼬리가 긴 의료비. |
| scene_10_lv4.png | 10층 단계 4 | 평균 뒤에 숨은 그룹. |

### scene_01_lv1 — 1층 단계 1

```
Doctor at a whiteboard-free lab desk; on the left Sia writes a single rule card by hand while a flood of envelopes slips past her; on the right Abacus Bot sorts a tall stack of envelopes into two trays after looking at labeled examples. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_01_lv2 — 1층 단계 2

```
Three small rooms side by side: Sia studies with an answer sheet (stamped check marks only, no writing); Moa sorts a messy closet into piles of similar clothes; Fruit-fly researcher plays a retro arcade game and a gold star pops up. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_01_lv3 — 1층 단계 3

```
A hospital-like corridor inside the lab with three doors; Haru leads X1 from a door with a question-mark-shaped lamp, to a toolbox room, to a room with a big green check light. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_01_lv4 — 1층 단계 4

```
Moa types at a terminal; three different small robot assistants on three monitors answer at once; Fruit-fly researcher compares the three printouts with a magnifying glass. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_02_lv1 — 2층 단계 1

```
Two desks: an exam question booklet on one, an answer sheet with one blank row on the other; Sia points at the blank row while Abacus Bot holds a ruler and a two-slot sorting box. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_02_lv2 — 2층 단계 2

```
A taxi-fare wall made of pinned receipts arranged by distance; Haru stretches a long glowing string straight through them while X2 measures the small gaps with a tape. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_02_lv3 — 2층 단계 3

```
Doctor shuffles a big deck of cards; most cards go into a blue study basket, a few into a small amber chest locked with a padlock that Haru guards. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_02_lv4 — 2층 단계 4

```
Ten customers walk past a reception desk where a sleepy robot stamps every ticket the same way; two customers in red quietly leave through a side door unnoticed; Fruit-fly researcher spots them. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_03_lv1 — 3층 단계 1

```
Five practice exams in a row on a long table; Moa takes them one after another while X3 plots five dots on a small chalkboard-free stand showing ups and downs. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_03_lv2 — 3층 단계 2

```
A lab hallway with smoke detectors; some ring with no fire, one small fire in a trash bin is missed; Haru checks each alarm with a clipboard, Fruit-fly researcher holds a fire extinguisher. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_03_lv3 — 3층 단계 3

```
Two judges at a pixel scoreboard: a gentle judge giving small equal penalties, a strict judge giving one huge penalty for a big mistake; Sia and Moa watch. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_03_lv4 — 3층 단계 4

```
A payment counter with a big ledger; Abacus Bot tries to guess which customers are new but the ledger pages are mostly empty; X1 brings in a camera for a hands-on deep learning demo with photos. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_04_lv1 — 4층 단계 1

```
A fish market stall; Sia reads numbers from a notebook and Moa pins blue and red fish-shaped pins on a big map board, forming two groups. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_04_lv2 — 4층 단계 2

```
A new small green fish arrives at a fish-themed neighborhood; five nearby fish neighbors raise flags (three blue, two red) to vote; Haru counts. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_04_lv3 — 4층 단계 3

```
A long conveyor of fish boxes, all blue first and all red at the end; X2 cuts the line in the wrong place; Doctor shows a better mixed split on another conveyor. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_04_lv4 — 4층 단계 4

```
A suspicious big blue fish sits on a giant scale whose dial is huge, next to a tiny ruler; Fruit-fly researcher swaps both for two identical step counters. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_05_lv1 — 5층 단계 1

```
Three vending machines in a row (one with handwritten rule cards, one with neighbor photos, one with a yes/no question tree screen); X3 inserts a coin and a fish toy comes out. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_05_lv2 — 5층 단계 2

```
Twins sit at two separate exam desks separated by a screen; Doctor makes sure copies from the same original document all go to one side. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_05_lv3 — 5층 단계 3

```
A twenty-questions game show stage; Abacus Bot asks a big question and a crowd of mixed fish splits into two cleaner groups; Moa holds a mixing meter. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_05_lv4 — 5층 단계 4

```
Two pairs of fish: an easy pair standing far apart, a hard pair tangled together; Sia measures height divided by length with calipers and the tangled pair separates. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_06_lv1 — 6층 단계 1

```
An entrance exam hall; each subject gives points on a pixel score board and a single cutoff line on the floor separates pass and fail candidates; Haru adjusts the line. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_06_lv2 — 6층 단계 2

```
A teacher-robot with a red pen corrects only the wrong answers on a sheet and stops as soon as all are right; X1 notices the line barely misses a dot. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_06_lv3 — 6층 단계 3

```
A weather station on the roof; Moa reads a gauge that smoothly rises like an S-curve from sunny to rainy; an umbrella half open. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_06_lv4 — 6층 단계 4

```
A wide road painted between two neighborhoods of blue and red houses; Abacus Bot paints the center line; the two houses touching the road edges are highlighted. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_07_lv1 — 7층 단계 1

```
A horse-race style betting board without numbers, showing two bars; Fruit-fly researcher multiplies one bar with a magnifying lens while the probability bar grows only a bit. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_07_lv2 — 7층 단계 2

```
A battery testing lab; rows of batteries on a shelf, a straight measuring rod along their lifespans, and a curved U-shaped trail of leftover marks on the floor that Haru points at. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_07_lv3 — 7층 단계 3

```
X2 bends a flexible ruler into a curve while a rubber band attached to the wall pulls it back gently; two bins of coefficient blocks: one shrinks evenly, one drops small blocks to zero. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_07_lv4 — 7층 단계 4

```
A forest of many small pixel trees each holding a voting sign; next to it a line of trees passing a notebook of mistakes from one to the next; Moa compares two score bars. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_08_lv1 — 8층 단계 1

```
A cozy review room; Sia and Moa flip big flash cards on a table, Haru holds a photo album of the earlier floors. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_08_lv2 — 8층 단계 2

```
Five assignment folders on a desk with travel-plan style maps; Doctor points to a table layout drawn as blank grid lines. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_08_lv3 — 8층 단계 3

```
A driving-school simulator; Fruit-fly researcher holds the steering wheel while doing small calculations on a notepad; a green check lights up. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_09_lv1 — 9층 단계 1

```
Three judges grade the same answer sheet: a strict one with a square stamp, one translating it back to normal units with a root-shaped key, a lenient one with a small stamp. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_09_lv2 — 9층 단계 2

```
A big pixel pizza on a table; Abacus Bot eats most slices labeled by color only, a few slices remain; X3 compares with a plain average-only plate. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_09_lv3 — 9층 단계 3

```
A cooking class; Moa adds one spoon of salt and a taste meter jumps; other ingredients stay locked in place; Doctor wears an apron over the lab coat. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_09_lv4 — 9층 단계 4

```
A team award ceremony; a prize chest is split into stacks of coins of different heights for each player (Temperature, Charging shown only as icons: thermometer, plug); Haru does the fair split. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_10_lv1 — 10층 단계 1

```
An insurance office with a huge wall of a hundred tiny file folders, only one or two glowing red; a guard dog sleeps; Fruit-fly researcher looks for the red ones. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_10_lv2 — 10층 단계 2

```
A detector dog with a great nose sniffs a suspicious suitcase but does not bark; Sia lowers a lever on the dog collar so it barks more easily; X1 watches for false alarms. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_10_lv3 — 10층 단계 3

```
A hospital billing hall with a line of patients holding receipts of mostly small sizes and one giant receipt scroll; Abacus Bot estimates while Moa measures the long tail. 3:2 landscape, 16-bit RPG pixel art, no text.
```

### scene_10_lv4 — 10층 단계 4

```
A classroom report board with group bars (no text); one group bar much shorter; Doctor and Haru look closely at the group behind the class average. 3:2 landscape, 16-bit RPG pixel art, no text.
```
