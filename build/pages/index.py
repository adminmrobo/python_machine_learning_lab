# 건물 안내도 (첫 화면)
IDX['desc'] = '파이썬 머신러닝 연구소 — 15층 건물을 한 주에 한 층씩. 초파리팀과 주판봇팀이 발표·상담·대항전으로 머신러닝을 처음부터 풀어 주는 강의 해설 (2026-2학기 파이썬머신러닝).'
IDX['cover_alt'] = '1~10층에 불이 켜지고 위층에 공사 비계와 크레인이 걸린 연구소 건물 앞 잔디밭에, 초파리팀·박사·주판봇팀 아홉 식구가 나란히 선 픽셀 그림'
IDX['refs'] = [dict(id='syllabus', title='강의계획서 — 파이썬머신러닝 (EB24220-02, 2026-2학기)', by='안상선 · 강남대학교 데이터사이언스전공'),
               dict(id='hongong', title='혼자 공부하는 머신러닝+딥러닝 (부교재)', by='박해선 · 한빛미디어'),
               dict(id='bench', title='데이터베이스 설계 연구실 (구성 참고 사이트)', by='안상선', URL='https://adminmrobo.github.io/data_base_design/')]
IDX['models'] = ['표지 그림은 16비트 픽셀풍 생성 그림(960×540 원화)을 1920·3840으로 키운 것입니다.', '12~15층은 강의 자료를 받으면 채웁니다.']
IDX['body'] = '''
<header class="hero"><div class="wrap">
<div class="kicker">강남대학교 · 파이썬머신러닝 · 2026-2학기 강의를 연구소 해설로</div>
<h1>파이썬 머신러닝 연구소<br><span style="font-size:.5em;color:#5b6874">15층 — 데이터 한 줄에서 실제 사례까지, 한 주에 한 층씩</span></h1>
<p class="question">“코드를 처음 보는 사람도, 데이터를 주고 규칙을 찾게 하는 일을 끝까지 따라갈 수 있을까?”</p>
<p>이 건물은 강의 15주를 15개 층으로 쌓았습니다. 층마다 <b>초파리팀</b>과 <b>주판봇팀</b>이 조별발표·개인발표·상담·토론을 하며 개념을 풀고, 마지막에는 <b>팀 대항전</b>을 벌입니다. 심판은 <b>박사</b>입니다. 수식은 말로 먼저 풀고, 코드는 접어 두었습니다. 버튼을 누르고 숫자가 어떻게 바뀌는지만 보면 됩니다.</p>
<section class="kpis"><div><b>15층</b><span>15주 (8층 · 15층은 점검실)</span></div><div><b>11층</b><span>지금 문을 연 층 (12~15층 공사 중)</span></div><div><b>2팀</b><span>초파리팀 · 주판봇팀 + 심판 박사</span></div><div><b>4곳</b><span>지하 실전 연습장의 가상 사업장</span></div></section>
<div class="talk">''' + say('doc', 'front', '한 주에 한 층씩 올라갑니다. 8층과 15층은 지난 층들을 다시 보는 <b>점검실</b>입니다.') + say('asst', 'smile', '코드를 처음 보는 분도 괜찮아요. 막히면 밑줄 친 낱말에 손가락을 대 보세요. 저도 그렇게 배웠어요.') + '''</div>
</div></header>
<section class="level" id="course"><div class="wrap"><h2>강좌 안내</h2>
<p>파이썬 기반의 머신러닝 기법과 응용 문제를 배웁니다. 지도학습의 분류·회귀 모형, 로지스틱 회귀, 의사결정나무와 그 사례를 중심으로 하고, 뒤쪽에서는 비지도학습, 딥러닝, 대규모 언어모델을 소개하며 머신러닝 모형과 비교합니다.</p>
<div class="tbl"><table><thead><tr><th>항목</th><th>내용 (강의계획서 기준)</th></tr></thead><tbody>
<tr><td>과목</td><td>파이썬머신러닝 (Python Machine Learning) · EB24220-02 · 3학점 · 데이터사이언스전공 4학년 전공선택</td></tr>
<tr><td>수업</td><td>목요일 4·5·6교시 · 이론과 실습 병행 (실습 6회) · 한·중 이중언어과정</td></tr>
<tr><td>평가</td><td>중간고사 40 · 기말고사 40 · 출석 10 · 기타 10 (절대평가) — 중간·기말은 프로젝트로 진행</td></tr>
<tr><td>AI 활용</td><td>AI 도구로 데이터 분석 코드 생성, 전처리, 인사이트 도출 전 과정을 허용 (OT에서는 Qwen · Kimi · DeepSeek을 안내)</td></tr>
<tr><td>교재</td><td>주교재: 자체 교안 (노션 강의 페이지) · 부교재: 박해선, 『혼자 공부하는 머신러닝+딥러닝』, 한빛미디어</td></tr>
</tbody></table></div>
<p style="font-size:14px;color:#5b6874">층 배치 안내: 1~7층은 강의계획서 순서와 같습니다. 9·10층은 실제로 받은 강의 자료(회귀 모델 읽기, 보험 실제 사례)로 채웠고, 각 층 첫머리에 계획서 주제와의 관계를 적었습니다. 11층은 11월 26일 자 교안(의사결정나무 · 랜덤포레스트 · 경사하강법 · 배치 · 에포크)으로 채웠습니다. 계획서의 11주차 주제(산업별 데이터시각화)와는 다르지만, 교안 끝의 차트 만들기 실습이 시각화 내용을 담고 있습니다.</p>
</div></section>
<section class="level" id="floors"><div class="wrap"><h2>15층 안내도</h2><p>위가 높은 층입니다. 초록 번호는 점검실, 줄무늬는 공사 중인 층입니다. 층마다 따로 읽어도 되도록 만들었고, 맨 위 “30초 복습”이 아래층과 이어 줍니다.</p>
{{TOWER}}</div></section>
<section class="level" id="teams"><div class="wrap"><h2>두 팀과 심판, 그리고 진행 방식</h2>
{{TEAMS}}
<div class="steps" style="margin-top:14px"><div><span class="n">1</span><b>조별발표</b>한 팀이 개념 하나를 맡아 발표하고, 상대 팀 조장이 빈틈을 짚습니다.</div><div><span class="n">2</span><b>개인발표</b>인턴이나 미공개 연구원 한 명이 실험을 직접 돌려 보며 설명합니다.</div><div><span class="n">3</span><b>상담</b>조수 하루나 인턴이 박사에게 막힌 곳을 묻습니다. 처음 배우는 분이 할 질문입니다.</div><div><span class="n">4</span><b>토론 · 팀 대항전</b>두 팀이 다른 방법을 고르고, 박사가 데이터로 판정합니다.</div></div>
</div></section>
<section class="level" id="how"><div class="wrap"><h2>공부하는 법</h2>
<div class="steps"><div><span class="n">1</span><b>상황부터</b>단계마다 박사의 “상황” 질문이 먼저 나옵니다. 정의보다 장면을 먼저 떠올리세요.</div><div><span class="n">2</span><b>눌러 보기</b>실험 패널의 손잡이를 움직이며 숫자가 어떻게 바뀌는지 봅니다. 망가지지 않습니다.</div><div><span class="n">3</span><b>수식은 조수와 함께</b>“조수가 대신 물어봅니다” 상자가 기호를 하나씩 읽어 주고, 작은 숫자로 한 번 계산합니다.</div><div><span class="n">4</span><b>AI 결과 의심하기</b>“AI·도구 결과 판단 코너”에서 그럴듯하지만 틀린 답을 골라내는 연습을 합니다.</div><div><span class="n">5</span><b>코드는 마지막에</b>접힌 “교안의 파이썬 코드로 보면”은 몰라도 됩니다. Colab 실습 때 펼쳐 보세요.</div></div>
</div></section>
<section class="level" id="tools"><div class="wrap"><h2>실습 도구와 자료</h2>
<div class="tbl"><table><thead><tr><th>도구 · 자료</th><th>쓰는 곳</th><th>열기</th></tr></thead><tbody>
<tr><td>Google Colab</td><td>모든 실습 (설치 없음)</td><td><a href="https://colab.research.google.com" target="_blank" rel="noopener">열기</a></td></tr>
<tr><td>rides.csv — 택시 1,200건 (수업용 합성 데이터)</td><td>2·3층 요금 회귀 · 이탈 분류</td><td><a href="data/rides.csv">내려받기</a></td></tr>
<tr><td>payments.csv — 결제 800건 (수업용 합성 데이터)</td><td>3층 k-NN · SVM 신규 사용자 분류</td><td><a href="data/payments.csv">내려받기</a></td></tr>
<tr><td>fishmarket_practice.csv — 물고기 159마리 (공개 Fish Market 데이터)</td><td>11층 나무 · 숲 · 경사하강법 · 프롬프트 실습</td><td><a href="data/fishmarket_practice.csv">내려받기</a></td></tr>
<tr><td>생선가게 KNN 노트북 01 · 02</td><td>4층 도미와 빙어</td><td><a href="https://github.com/adminmrobo/python_machine_learning_lab/tree/main/notebooks" target="_blank" rel="noopener">폴더</a></td></tr>
<tr><td>Teachable Machine</td><td>3층 딥러닝 체험 (그림 분류)</td><td><a href="https://teachablemachine.withgoogle.com/" target="_blank" rel="noopener">열기</a></td></tr>
<tr><td>실전 연습장</td><td>배운 것을 가상 사업장에서 운영</td><td><a href="practice/index.html">열기</a></td></tr>
</tbody></table></div>
</div></section>'''
