# 지하 실전 연습장 — practice/index.html (build.py가 exec로 실행)
import os
TABS = [
 dict(id='fish', name='생선가게', icon='🐟', title='생선가게 — 경계에 선 생선 판정하기',
  scn='가게에 하루 수십 마리가 들어옵니다. 대부분은 한눈에 도미·빙어지만, 가끔 <b>25cm · 150g</b>처럼 애매한 생선이 옵니다. 판정기(KNN)의 설정을 정해 애매한 생선도 바르게 판정하게 만드세요. 사장님 판정으로는 이 생선은 <b>도미</b>입니다.',
  green='데이터: 도미 35 · 빙어 14 (부교재 실습값)', blue='내 결정: 눈금(원래 단위 / 표준화)과 이웃 수 k, 새 생선 위치',
  widget='<div class="mlw" data-w="knn" data-cfg=\'{"k":5,"p":[25,150]}\' id="w_fish"></div>',
  missions=[('m1','최적 찾기 — 수상한 생선(25cm · 150g 근처)이 <b>도미</b>로 판정되는 설정을 만드세요.'),('m2','함정 관찰 — <b>원래 단위</b>에서 k를 1 · 3 · 9로 바꿔 보세요. k=1에서는 도미, k=3부터는 빙어로 판정이 뒤집히는 것을 확인하세요.'),('m3','유지 확인 — <b>표준화</b> 상태에서 k를 3·5·7로 바꿔도 도미 판정이 유지되는지 확인하세요.')],
  back=[('4층 단계 4 — 수상한 도미','../weeks/w04_fish_market_knn.html#lv4'),('4층 단계 2 — KNN','../weeks/w04_fish_market_knn.html#lv2')]),
 dict(id='taxi', name='택시회사', icon='🚕', title='택시회사 — 떠날 손님에게 쿠폰 보내기',
  scn='시험 손님 240명 중 약 20%가 다음 달 떠날 예정입니다. 쿠폰 한 장은 <b>3천 원</b>, 떠난 손님 한 명의 손실은 <b>5만 원</b>입니다(예시). 이탈 점수의 문턱값을 정해 쿠폰 받을 손님을 고르세요.',
  green='시장 조건: 이탈 약 20% · 쿠폰 3천 원 · 손님 손실 5만 원 (예시)', blue='내 결정: 문턱값 (이 점수 이상이면 쿠폰)',
  widget='<div class="mlw" data-w="cm" data-cfg=\'{"n":240,"rate":0.204,"sep":0.3,"sd":0.55,"seed":21,"th":0.5,"posName":"이탈","negName":"남음","shift":-1.8,"cost":{"fn":5,"fp":0.3,"unit":"만 원"}}\' id="w_taxi"></div>',
  missions=[('m1','최적 찾기 — 총비용이 가능한 최솟값의 <b>110% 이내</b>가 되는 문턱값을 찾으세요.'),('m2','함정 관찰 — 정확도는 기준선 근처(±0.01)인데 <b>잡아낸 이탈 손님이 0명</b>인 상태를 만들어 보세요.'),('m3','조건 확인 — 떠날 손님의 <b>70% 이상</b>(재현율 0.7)을 잡으면서 비용이 최솟값의 130% 이내인지 확인하세요.')],
  back=[('2층 단계 4 — 정확도의 함정','../weeks/w02_classification_and_regression.html#lv4'),('3층 단계 2 — 네 점수','../weeks/w03_scores_and_cross_validation.html#lv2')]),
 dict(id='battery', name='배터리 공장', icon='🔋', title='배터리 공장 — 수명 예측 모델 들이기',
  scn='공장에 수명 예측 모델 하나를 들입니다. 후보 넷의 학습·시험·교차검증 R²가 있습니다(7층 교안 값). 그리고 불량 판정 로지스틱의 점수 손잡이로 판정이 바뀌는 지점을 확인합니다.',
  green='데이터: 배터리 600개 (시뮬레이션) · 학습 480 · 시험 120', blue='내 결정: 들일 모델 · 불량 점수 z',
  widget='<div class="mlw" data-w="gap" data-cfg=\'{"y0":0.85,"yl":"R²","warn":0.03,"models":[{"name":"선형","tr":0.893,"te":0.904,"cv":0.893},{"name":"다항+Ridge","tr":0.977,"te":0.975,"cv":0.974},{"name":"랜덤포레스트","tr":0.992,"te":0.935,"cv":0.942},{"name":"부스팅","tr":0.991,"te":0.956,"cv":0.961}]}\' id="w_bat"></div><div class="mlw" data-w="sigmoid" data-cfg=\'{"z":-2,"pos":"불량","neg":"정상"}\' id="w_sig"></div>',
  missions=[('m1','최적 찾기 — 처음 보는 배터리(시험·교차검증)에서 가장 정확한 모델을 고르세요.'),('m2','함정 관찰 — 학습 점수와 시험 점수의 차이(격차)가 <b>가장 큰</b> 모델을 고르세요.'),('m3','경계 확인 — 불량 확률이 <b>0.45~0.55</b> 사이가 되는 점수 z를 찾으세요 (판정이 바뀌는 곳).')],
  back=[('7층 단계 4 — 과적합 격차','../weeks/w07_improving_models_battery.html#lv4'),('6층 단계 3 — 시그모이드','../weeks/w06_logistic_perceptron_svm.html#lv3')]),
 dict(id='insure', name='보험사', icon='🛡️', title='보험사 — 드문 청구 미리 안내하기',
  scn='여행자보험 계약 2,000건 중 청구는 약 1.5%뿐입니다. 청구 가능성이 높은 계약에 사전 안내를 보내면 놓친 청구 1건당 손실 <b>50만 원</b>을 줄이고, 안내 1건 비용은 <b>2만 원</b>입니다(예시). 문턱값을 정하세요.',
  green='시장 조건: 청구 약 1.5% · 놓침 50만 원 · 안내 2만 원 (예시)', blue='내 결정: 문턱값',
  widget='<div class="mlw" data-w="cm" data-cfg=\'{"n":2000,"rate":0.0146,"sep":0.9,"sd":0.7,"seed":13,"th":0.5,"posName":"청구","negName":"청구 없음","shift":-3.2,"h":180,"cost":{"fn":50,"fp":2,"unit":"만 원"}}\' id="w_ins"></div>',
  missions=[('m1','최적 찾기 — 총비용이 최솟값의 <b>110% 이내</b>가 되는 문턱값을 찾으세요.'),('m2','함정 관찰 — 정확도 <b>0.98 이상</b>인데 재현율이 <b>0.1 이하</b>인 상태를 만들어 보세요.'),('m3','조건 확인 — 재현율 <b>0.6 이상</b>을 유지하면서 정밀도가 얼마나 낮아지는지 확인하세요 (재현율 ≥ 0.6 상태 만들기).')],
  back=[('10층 단계 1 — 청구 1.46%','../weeks/w10_real_cases_insurance.html#lv1'),('10층 단계 2 — 다섯 모델과 문턱값','../weeks/w10_real_cases_insurance.html#lv2')]),
]

def tab_html(t):
    mis = ''.join('<li data-m="%s"><span class="mk">○</span> %s</li>' % m for m in t['missions'])
    back = ' · '.join('<a href="%s">%s</a>' % b for b in t['back'])
    return ('<section class="ptab" id="tab-%s" hidden><div class="wrap"><h2>%s %s</h2><div class="pr-scn">%s</div>'
            '<div class="steps"><div style="border-left:4px solid #13733a"><b>초록 — 환경 조건</b>%s</div><div style="border-left:4px solid #1e55c8"><b>파랑 — 내 결정</b>%s</div></div>'
            '<div class="panel">%s</div><section class="kpis pk"></section>'
            '<div class="ptalk">%s%s%s%s</div>'
            '<div class="pr-tasks"><h3>미션 (조작한 뒤에만 판정합니다)</h3><ol class="mis">%s</ol></div><p class="recap"><b>배운 곳 다시 보기 —</b> %s</p></div></section>') % (
        t['id'], t['icon'], t['title'], t['scn'], t['green'], t['blue'], t['widget'],
        say('doc', 'think', '<span class="t-doc">…</span>'), say('asst', 'report', '<span class="t-asst">…</span>'), say('fly', 'magnify', '<span class="t-fly">…</span>'), say('robo', 'coin', '<span class="t-robo">…</span>'), mis, back)

JSP = r'''
(function(){var L=LAB,$=L.$,$$=L.$$;
var TABS=['fish','taxi','battery','insure'];
function show(id){if(TABS.indexOf(id)<0)id='fish';TABS.forEach(function(t){$('#tab-'+t).hidden=t!==id;var b=$('.tabbar [data-t="'+t+'"]');if(b)b.setAttribute('aria-pressed',t===id);});
 if(location.hash!=='#'+id)history.replaceState(null,'','#'+id);window.dispatchEvent(new Event('resize'));}
$$('.tabbar button').forEach(function(b){b.onclick=function(){show(b.dataset.t);};});
window.addEventListener('hashchange',function(){show(location.hash.slice(1));});
var touched={};TABS.forEach(function(t){var s=$('#tab-'+t);['input','click','change'].forEach(function(ev){s.addEventListener(ev,function(e){if(e.target.closest('.panel'))touched[t]=true;},true);});});
function setM(t,m,ok){var li=$('#tab-'+t+' [data-m="'+m+'"]');if(!li)return;if(ok&&touched[t]){li.classList.add('pass');li.querySelector('.mk').textContent='●';}}
function talk(t,d,a,f,r){var s=$('#tab-'+t);s.querySelector('.t-doc').innerHTML=d;s.querySelector('.t-asst').innerHTML=a;s.querySelector('.t-fly').innerHTML=f;s.querySelector('.t-robo').innerHTML=r;}
function kp(t,items){L.kpis($('#tab-'+t+' .pk'),items);}
/* 생선가게 */
var fs={raw:{},std:{}};
$('#w_fish').addEventListener('mlchange',function(e){var s=e.detail,near=Math.abs(s.p[0]-25)<2.5&&Math.abs(s.p[1]-150)<40;
 kp('fish',[['판정',s.pred?'도미':'빙어','이웃 '+s.k+'마리 중 도미 '+s.v1,s.pred?'good':'bad'],['눈금',s.scale?'표준화':'원래 단위','',s.scale?'good':''],['이웃 수 k',s.k,''],['새 생선',s.p[0].toFixed(1)+'cm · '+Math.round(s.p[1])+'g',near?'수상한 생선 근처':'']]);
 if(near){(s.scale?fs.std:fs.raw)[s.k]=s.pred;}
 setM('fish','m1',near&&s.pred===1);
 setM('fish','m2',fs.raw[1]===1&&fs.raw[3]===0&&fs.raw[9]===0);
 setM('fish','m3',fs.std[3]===1&&fs.std[5]===1&&fs.std[7]===1);
 talk('fish',near?(s.pred?'판정 도미 — 사장님 판정과 같습니다. 눈금을 맞춘 덕분입니다.':'판정 빙어 — 시험 점수는 1.0이어도 경계 사례에서는 틀립니다.'):'새 생선을 25cm · 150g 근처로 옮겨 판정해 보세요.',
  '이웃 '+s.k+'마리 중 도미 '+s.v1+'마리, 빙어 '+(s.k-s.v1)+'마리예요.',
  s.scale?'표준화 상태야. 길이도 이제 제 목소리를 내.':'원래 단위면 무게(g)가 거리를 다 정해. 길이 10cm 차이는 거의 안 보여.',
  s.scale?'눈금 바꾸니까 이웃이 바뀌었네…':'시험 1.0이면 충분하다니까! 그대로 가자!');});
/* 문턱값 장면 공통 */
function thScene(t,id,o){var el=$(id),best=null,scanning=true;
 for(var th=0.02;th<=0.981;th+=0.01){el._set({th:th});var c=el._state.cost;if(best==null||c<best.c)best={c:c,th:th};}
 el._set({th:0.5});scanning=false;
 el.addEventListener('mlchange',function(e){if(scanning)return;var s=e.detail,ratio=s.cost/best.c;
  kp(t,[['총비용',Math.round(s.cost*10)/10+'만 원','최솟값의 '+Math.round(ratio*100)+'%',ratio<=1.1?'good':ratio>1.5?'bad':''],['재현율',s.rec.toFixed(2),'놓침 '+s.fn+'건',s.rec>=o.rec?'good':''],['정밀도',s.pre==null?'계산 불가':s.pre.toFixed(2),'헛경보 '+s.fp+'건',''],['정확도',s.acc.toFixed(3),'기준선 '+s.base.toFixed(3),Math.abs(s.acc-s.base)<0.01?'bad':'']]);
  setM(t,'m1',ratio<=1.1);
  setM(t,'m2',o.trap(s));
  setM(t,'m3',o.m3(s,ratio));
  talk(t,ratio<=1.1?'비용 기준 최적 근처입니다. 이 문턱값을 보고서에 근거와 함께 쓰세요.':(s.tp===0?'아무도 고르지 않았습니다. 정확도가 높아도 쓸모없는 상태입니다.':'비용을 기준으로 문턱값을 더 움직여 보세요.'),
   '잡아냄 '+s.tp+' · 놓침 '+s.fn+' · 헛경보 '+s.fp+'. 비용 '+Math.round(s.cost*10)/10+'만 원이에요.',
   s.fp>s.tp*10?'헛경보가 잡아낸 수의 10배가 넘어. 안내 비용이 정말 싼지 확인해.':'정확도 말고 비용으로 보자. 놓침 한 건이 비싸니까.',
   s.acc>=s.base-0.005?'정확도 '+s.acc.toFixed(3)+'! 이 정도면 최고 아니야?':'정확도가 떨어졌어… 그래도 비용이 줄었다면 괜찮은 건가?');});
 el._set({th:0.5});}
thScene('taxi','#w_taxi',{rec:0.7,trap:function(s){return s.tp===0&&Math.abs(s.acc-s.base)<=0.01;},m3:function(s,r){return s.rec>=0.7&&r<=1.3;}});
thScene('insure','#w_ins',{rec:0.6,trap:function(s){return s.acc>=0.98&&s.rec<=0.1;},m3:function(s){return s.rec>=0.6;}});
/* 배터리 공장 */
var bat={sel:-1,p:null};
function batUpd(){var M=['선형','다항+Ridge','랜덤포레스트','부스팅'],T=[0.904,0.975,0.935,0.956],G=[-0.011,0.002,0.057,0.035];
 kp('battery',[['선택 모델',bat.sel<0?'—':M[bat.sel],'',bat.sel===1?'good':''],['시험 R²',bat.sel<0?'—':T[bat.sel].toFixed(3),'',bat.sel===1?'good':''],['격차',bat.sel<0?'—':G[bat.sel].toFixed(3),'학습 − 시험',bat.sel>=0&&G[bat.sel]>0.03?'bad':''],['불량 확률',bat.p==null?'—':bat.p.toFixed(3),'',bat.p!=null&&bat.p>=0.45&&bat.p<=0.55?'good':'']]);
 setM('battery','m1',bat.sel===1);setM('battery','m2',bat.sel===2);setM('battery','m3',bat.p!=null&&bat.p>=0.45&&bat.p<=0.55);
 talk('battery',bat.sel===1?'다항 + Ridge — 시험·교차검증 모두 0.97대, 격차 0.002. 공장에 들일 만합니다.':bat.sel===2?'랜덤포레스트 — 학습 0.992, 시험 0.935. 외운 흔적입니다.':'시험·교차검증 점수로 고르세요.',
  bat.sel<0?'모델 버튼을 눌러 주세요.':'학습과 시험 차이는 '+G[bat.sel].toFixed(3)+'이에요.','학습 점수만 보면 숲이 1등이지. 그게 함정이야.','나무 300그루가 제일 크고 든든해 보이는데!');}
$('#w_bat').addEventListener('mlchange',function(e){bat.sel=e.detail.sel;batUpd();});
$('#w_sig').addEventListener('mlchange',function(e){bat.p=e.detail.p;batUpd();});
batUpd();
show(location.hash.slice(1)||'fish');
})();
'''

body_tabs = ''.join(tab_html(t) for t in TABS)
bar = '<div class="tabbar ctrl" role="tablist">%s</div>' % ''.join('<button type="button" class="bt" data-t="%s" aria-pressed="false">%s %s</button>' % (t['id'], t['icon'], t['name']) for t in TABS)
css_extra = '<style>.ptab .kpis{margin:10px 0}.dk.good b{color:#13733a}.dk.bad b{color:#c93030}.mis li{margin:6px 0}.mis li.pass{color:#13733a}.mis li.pass .mk{color:#13733a}.ptalk .say{margin:6px 0}.tabbar{position:sticky;top:54px;z-index:20;background:#fff;padding:8px 0;border-bottom:1px solid #d5dbe2}</style>'
body = ('<nav class="top"><a class="brand" href="../index.html"><span class="hex">B1</span>%s</a><div class="links"><a href="#fish">생선가게</a><a href="#taxi">택시회사</a><a href="#battery">배터리 공장</a><a href="#insure">보험사</a><a href="../index.html">건물 안내도</a></div></nav>'
        '<!-- lab-cover --><header class="cover" id="cover" role="img" aria-label="연구소 건물 지하 연습장 표지">%s<div class="shelf">%s</div><span class="cover-chip">%s · 지하 실전 연습장</span></header><!-- /lab-cover -->'
        '<main id="top"><header class="hero"><div class="wrap"><div class="kicker">마지막 장 · 실전 연습장</div><h1>지하 실전 연습장<br><span style="font-size:.55em;color:#5b6874">네 곳의 가상 사업장을 직접 운영해 보기</span></h1>'
        '<p>1~10층에서 배운 것을 가상 사업장에서 씁니다. 장면마다 <b>초록</b>은 바꿀 수 없는 환경 조건, <b>파랑</b>은 여러분의 결정입니다. 손잡이를 움직이면 성적표와 네 캐릭터의 말이 바뀌고, 미션은 조작한 뒤에만 판정합니다. 주소 끝에 <code>#taxi</code>처럼 장면 이름을 붙이면 그 장면이 바로 열립니다.</p>'
        '<div class="talk">%s</div></div></header><div class="wrap">%s</div>%s'
        '<section class="level"><div class="wrap"><div class="slotbox"><h2>네 장면이 함께 묻는 질문</h2><p>생선가게의 눈금, 택시회사와 보험사의 문턱값, 배터리 공장의 격차 — 네 장면 모두 “점수 하나가 좋아 보여도 업무 목적의 기준으로 다시 재면 답이 바뀐다”는 같은 질문을 던집니다. 여러분이 고른 설정을 보고서에 쓴다면, 어떤 숫자를 근거로 들겠습니까?</p>'
        '<p style="font-size:14px;color:#5b6874">모형의 한계: 택시·보험사 장면의 점수 분포와 비용은 설명용 모형이고, 배터리 점수는 교안 값, 생선은 실습 데이터입니다. 숫자는 교육용 예시이며 경영·보험·투자 권고가 아닙니다. 기록은 이 탭에만 있고 저장되지 않습니다.</p></div></div></section></main>') % (
    SERIES, pixel.scene('pr'), ''.join(face(w, m, 112) for w, m in (('fly', 'magnify'), ('asst', 'report'), ('doc', 'think'), ('robo', 'coin'))), SERIES,
    say('doc', 'front', '여기는 지하 연습장입니다. 정답 버튼은 없습니다 — 미션 판정만 있습니다.') + say('moa', 'cheer', '보험사부터 해 보세요! 10층에서 본 숫자가 그대로 나와요.'), bar, body_tabs)
P = {'refs': [dict(id='w04', title='4층 생선가게 (부교재 실습 데이터)', by='안상선'), dict(id='w07', title='7층 배터리 공장 (회귀모델 1 교안)', by='안상선'), dict(id='w10', title='10층 보험 실제 사례 (실제 케이스 교안)', by='안상선')],
     'models': ['택시·보험사 점수 분포와 비용은 설명용 모형입니다.']}
full = body + footer(P, None, None, '../')
sp, exmap = collect_sprites(full)
doc = head('지하 실전 연습장 · ' + SERIES, '파이썬 머신러닝 연구소 실전 연습장 — 생선가게 KNN, 택시 이탈 쿠폰, 배터리 모델 선택, 보험 드문 청구를 직접 운영하는 대시보드.', '지하 실전 연습장', SITE + 'practice/index.html', css_extra)
doc += '<body><div id="prog"></div><div id="tip"></div>%s<script>var SPRITE=%s;var EXMAP=%s;</script><script>%s</script><script>window.addEventListener("DOMContentLoaded",function(){setTimeout(function(){%s},0);});</script></body></html>' % (full, esc_json(sp), esc_json(exmap), JS, JSP)
os.makedirs(os.path.join(ROOT, 'practice'), exist_ok=True)
open(os.path.join(ROOT, 'practice', 'index.html'), 'w', encoding='utf-8').write(doc)
check('practice/index.html', doc)
print('practice/index.html %.0f KB' % (len(doc.encode()) / 1024))
