/* ══ 파이썬 머신러닝 연구소 — 실험 위젯 (외부 라이브러리 없음) ══
   <div class="mlw" data-w="이름" data-cfg='{...}'></div> 를 ML.init()이 찾아 붙인다.
   위젯은 el._state 에 현재 상태를 남기고 'mlchange' 이벤트를 보낸다 (실전 연습장 미션 판정용). */
(function(){'use strict';
var L=window.LAB;
function $(s,r){return (r||document).querySelector(s);} function $$(s,r){return [].slice.call((r||document).querySelectorAll(s));}
function emit(el,st){el._state=st; el.dispatchEvent(new CustomEvent('mlchange',{detail:st,bubbles:true}));}
var FONT=function(){return getComputedStyle(document.body).fontFamily;};
var C={blue:'#1e55c8',red:'#c93030',green:'#13733a',amber:'#a35c00',purple:'#9b3fb5',teal:'#0b7a86',grid:'#e3e8ee',ink:'#16212b',mut:'#5b6874'};
function f(v,n){return (Math.round(v*Math.pow(10,n||0))/Math.pow(10,n||0)).toLocaleString('ko-KR',{minimumFractionDigits:n||0,maximumFractionDigits:n||0});}
function cvs(el,h){var c=document.createElement('canvas'); c.className='cv'; c.style.height=(h||280)+'px'; el.appendChild(c); return c;}
function axes(c,W,H,o){ // o: x0,x1,y0,y1,xl,yl  → 좌표 변환 반환
  var Lm=o.L||52,R=12,T=12,B=36; c.strokeStyle=C.grid; c.fillStyle=C.mut; c.font='12px '+FONT(); c.lineWidth=1;
  var X=function(v){return Lm+(v-o.x0)/(o.x1-o.x0)*(W-Lm-R);}, Y=function(v){return H-B-(v-o.y0)/(o.y1-o.y0)*(H-T-B);};
  for(var i=0;i<=4;i++){var xv=o.x0+(o.x1-o.x0)*i/4,yv=o.y0+(o.y1-o.y0)*i/4;
    c.beginPath();c.moveTo(X(xv),T);c.lineTo(X(xv),H-B);c.stroke(); c.beginPath();c.moveTo(Lm,Y(yv));c.lineTo(W-R,Y(yv));c.stroke();
    c.textAlign='center'; c.fillText(o.fx?o.fx(xv):f(xv,o.dx||0),X(xv),H-B+15); c.textAlign='right'; c.fillText(o.fy?o.fy(yv):f(yv,o.dy||0),Lm-5,Y(yv)+4);}
  c.textAlign='center'; c.fillStyle=C.ink; c.fillText(o.xl||'',(Lm+W-R)/2,H-4);
  c.save(); c.translate(12,(T+H-B)/2); c.rotate(-Math.PI/2); c.fillText(o.yl||'',0,0); c.restore();
  return {X:X,Y:Y,inv:function(px,py){return [o.x0+(px-Lm)/(W-Lm-R)*(o.x1-o.x0), o.y0+(H-B-py)/(H-T-B)*(o.y1-o.y0)];}};
}
function dot(c,x,y,col,r,shape){c.fillStyle=col; c.strokeStyle='#fff'; c.lineWidth=1.2; c.beginPath();
  if(shape==='tri'){c.moveTo(x,y-r-2);c.lineTo(x+r+2,y+r);c.lineTo(x-r-2,y+r);c.closePath();}
  else if(shape==='sq'){c.rect(x-r,y-r,2*r,2*r);} else c.arc(x,y,r,0,7); c.fill(); c.stroke();}
function ctrl(el,html){var d=document.createElement('div'); d.className='ctrl'; d.innerHTML=html; el.appendChild(d); return d;}
function box(el,cls){var d=document.createElement('div'); d.className=cls||'insight'; el.appendChild(d); return d;}
function seg(el,opts,cur,on){ // 버튼 묶음
  var d=ctrl(el,opts.map(function(o){return '<button type="button" class="bt" data-v="'+o[0]+'" aria-pressed="'+(o[0]===cur)+'">'+o[1]+'</button>';}).join(''));
  $$('button',d).forEach(function(b){b.onclick=function(){$$('button',d).forEach(function(x){x.setAttribute('aria-pressed',x===b);}); on(b.dataset.v);};}); return d;}
function slider(el,lab,min,max,step,val,on,fmt){var d=document.createElement('label'); d.className='sl';
  d.innerHTML='<span>'+lab+'</span><input type="range" min="'+min+'" max="'+max+'" step="'+step+'" value="'+val+'"><b></b>'; el.appendChild(d);
  var i=$('input',d),b=$('b',d); function u(){b.textContent=fmt?fmt(+i.value):i.value; on(+i.value);} i.oninput=u; u(); return i;}

/* ── 데이터: 도미 35 + 빙어 14 (혼자 공부하는 머신러닝+딥러닝 2장 실습값) ── */
var FL=[25.4,26.3,26.5,29.0,29.0,29.7,29.7,30.0,30.0,30.7,31.0,31.0,31.5,32.0,32.0,32.0,33.0,33.0,33.5,33.5,34.0,34.0,34.5,35.0,35.0,35.0,35.0,36.0,36.0,37.0,38.5,38.5,39.5,41.0,41.0,9.8,10.5,10.6,11.0,11.2,11.3,11.8,11.8,12.0,12.2,12.4,13.0,14.3,15.0];
var FW=[242,290,340,363,430,450,500,390,450,500,475,500,500,340,600,600,700,700,610,650,575,685,620,680,700,725,720,714,850,1000,920,955,925,975,950,6.7,7.5,7.0,9.7,9.8,8.7,10.0,9.9,9.8,12.2,13.4,12.2,19.7,19.9];
var FISH=FL.map(function(l,i){return [l,FW[i],i<35?1:0];});
var RIDES=[[4.36,9533],[1.13,6323],[12.25,17985],[2.37,7170],[11.12,18431],[14.21,21017],[7.33,15001],[19.04,25856],[4.44,9403],[6.94,12831],[7.43,10614],[2.3,5037],[6.93,11070],[4.55,12570],[1.9,7555],[4.32,7870],[11.4,19217],[4.47,6634],[6.38,10768],[4.07,7965],[6.29,11954],[3.0,5523],[1.35,6964],[1.83,4946],[2.97,4348],[6.99,10586],[8.14,9997],[1.38,9015],[3.18,6564],[4.11,7592],[9.04,13105],[3.91,6502],[6.69,10609],[3.57,5833],[4.3,9857],[6.4,9814],[2.32,5195],[8.48,14979],[1.76,7417],[2.9,7110],[2.37,7167],[8.01,14659],[4.62,8423],[3.84,8859],[1.56,6195],[10.0,16639],[10.28,16881],[4.6,9137],[6.78,11755],[4.63,7118],[13.12,22690],[4.42,10014],[5.12,8953],[3.18,8212],[1.81,4049],[5.1,10909],[7.96,12821],[2.86,8347],[15.65,21829],[8.59,14629]];
function meanStd(a){var m=a.reduce(function(s,v){return s+v;},0)/a.length; var s=Math.sqrt(a.reduce(function(t,v){return t+(v-m)*(v-m);},0)/a.length); return [m,s||1];}
function knnPredict(train,p,k,scale){ // train: [x,y,label]
  var mx=meanStd(train.map(function(r){return r[0];})),my=meanStd(train.map(function(r){return r[1];}));
  var tf=scale?function(a,b){return [(a-mx[0])/mx[1],(b-my[0])/my[1]];}:function(a,b){return [a,b];};
  var q=tf(p[0],p[1]); var ds=train.map(function(r,i){var t=tf(r[0],r[1]); return {i:i,d:Math.hypot(t[0]-q[0],t[1]-q[1]),y:r[2]};}).sort(function(a,b){return a.d-b.d;}).slice(0,k);
  var v1=ds.filter(function(d){return d.y===1;}).length; return {nb:ds,v1:v1,v0:k-v1,pred:v1*2>k?1:0,mx:mx,my:my};}
var W={};

/* ① KNN 생선 판정기 */
W.knn=function(el,o){
  var st={k:o.k||5,scale:!!o.scale,p:o.p||[25,150]}, wrap=document.createElement('div'); el.appendChild(wrap); var out=null, cv=cvs(wrap,o.h||300);
  seg(el,[['raw','원래 단위 (cm · g)'],['std','표준화 (평균 0 · 표준편차 1)']],st.scale?'std':'raw',function(v){st.scale=v==='std';draw();});
  var sc=ctrl(el,''); slider(sc,'이웃 수 k',1,15,2,st.k,function(v){st.k=v;draw();});
  out=box(el); cv.style.cursor='crosshair';
  var T=null;
  function draw(){if(!out)return; var F=L.fit(cv),c=F.c; c.clearRect(0,0,F.W,F.H);
    var r=knnPredict(FISH,st.p,st.k,st.scale); var t=st.scale?function(a,b){return [(a-r.mx[0])/r.mx[1],(b-r.my[0])/r.my[1]];}:function(a,b){return [a,b];};
    var o2=st.scale?{x0:-2.5,x1:2,y0:-2,y1:2,xl:'길이 (표준화 점수)',yl:'무게 (표준화 점수)',dx:1,dy:1}:{x0:0,x1:45,y0:0,y1:1100,xl:'길이 (cm)',yl:'무게 (g)'};
    if(o.equal&&!st.scale){o2={x0:0,x1:1100,y0:0,y1:1100,xl:'길이 (cm) — 무게와 같은 눈금',yl:'무게 (g)'};}
    T=axes(c,F.W,F.H,o2); var q=t(st.p[0],st.p[1]);
    r.nb.forEach(function(n){var a=t(FISH[n.i][0],FISH[n.i][1]); c.strokeStyle='rgba(22,33,43,.35)'; c.setLineDash([4,3]); c.beginPath(); c.moveTo(T.X(q[0]),T.Y(q[1])); c.lineTo(T.X(a[0]),T.Y(a[1])); c.stroke(); c.setLineDash([]);});
    FISH.forEach(function(p,i){var a=t(p[0],p[1]); var isN=r.nb.some(function(n){return n.i===i;}); dot(c,T.X(a[0]),T.Y(a[1]),p[2]?C.blue:C.red,isN?6:4,'c'); if(isN){c.strokeStyle=C.ink;c.lineWidth=1.5;c.beginPath();c.arc(T.X(a[0]),T.Y(a[1]),8,0,7);c.stroke();}});
    dot(c,T.X(q[0]),T.Y(q[1]),C.green,7,'tri');
    c.font='12px '+FONT(); c.fillStyle=C.blue; c.textAlign='left'; c.fillText('● 도미',62,22); c.fillStyle=C.red; c.fillText('● 빙어',112,22); c.fillStyle=C.green; c.fillText('▲ 새 생선',162,22);
    var lab=r.pred?'도미':'빙어';
    out.innerHTML='새 생선 <b>길이 '+f(st.p[0],1)+'cm · 무게 '+f(st.p[1])+'g</b> → 가까운 '+st.k+'마리 중 도미 <b>'+r.v1+'</b> · 빙어 <b>'+r.v0+'</b> → 판정 <b style="color:'+(r.pred?C.blue:C.red)+'">'+lab+'</b>'+
      (st.scale?' <span class="pill ok">표준화</span>':' <span class="pill no">원래 단위</span>')+'<br><span style="font-size:13px;color:#5b6874">그래프를 누르면 새 생선을 옮길 수 있습니다. 점선은 가장 가까운 이웃입니다.</span>';
    emit(el,{k:st.k,scale:st.scale,p:st.p.slice(),pred:r.pred,v1:r.v1});}
  cv.addEventListener('click',function(e){if(!T)return; var b=cv.getBoundingClientRect(),v=T.inv(e.clientX-b.left,e.clientY-b.top);
    if(st.scale){var r=knnPredict(FISH,st.p,1,true); v=[v[0]*r.mx[1]+r.mx[0],v[1]*r.my[1]+r.my[0]];}
    st.p=[Math.max(5,Math.min(45,v[0])),Math.max(1,Math.min(1100,v[1]))]; draw();});
  window.addEventListener('resize',draw); draw();
  el._set=function(s){for(var k in s)st[k]=s[k]; draw();};
};

/* ② 데이터 나누기 실험 (49마리) */
W.split=function(el,o){
  var mode='order',seed=55; var strip=box(el,'strip'), out=box(el);
  seg(el,[['order','순서대로 자르기 (앞 35 · 뒤 14)'],['shuffle','섞어서 자르기'],['strat','비율 맞춰 자르기']],'order',function(v){mode=v;run();});
  var c2=ctrl(el,'<button type="button" class="bt">다시 섞기 (다른 난수)</button>'); $('button',c2).onclick=function(){seed=(seed*7+13)%997;run();};
  function rnd(s){var x=s; return function(){x=(x*16807)%2147483647; return x/2147483647;};}
  function run(){var idx=FISH.map(function(_,i){return i;}),tr=[],te=[];
    if(mode==='order'){tr=idx.slice(0,35);te=idx.slice(35);}
    else if(mode==='shuffle'){var r=rnd(seed+1); idx.sort(function(){return r()-.5;}); tr=idx.slice(0,36); te=idx.slice(36);}
    else{var r2=rnd(seed+1),b=idx.filter(function(i){return FISH[i][2];}).sort(function(){return r2()-.5;}),s=idx.filter(function(i){return !FISH[i][2];}).sort(function(){return r2()-.5;});
      te=b.slice(0,9).concat(s.slice(0,4)); tr=b.slice(9).concat(s.slice(4));}
    var T=tr.map(function(i){return FISH[i];}), ok=te.filter(function(i){return knnPredict(T,FISH[i],5,false).pred===FISH[i][2];}).length, acc=ok/te.length;
    strip.innerHTML=FISH.map(function(p,i){var inT=te.indexOf(i)>=0; return '<i class="'+(p[2]?'b':'s')+(inT?' t':'')+'" title="'+(p[2]?'도미':'빙어')+' '+(inT?'시험용':'학습용')+'"></i>';}).join('');
    var tb=te.filter(function(i){return FISH[i][2];}).length;
    out.innerHTML='시험용 '+te.length+'마리 = 도미 <b>'+tb+'</b> · 빙어 <b>'+(te.length-tb)+'</b> (전체 비율은 도미 35 : 빙어 14) · 학습용 '+tr.length+'마리 → 시험 정확도 <b style="color:'+(acc<.5?C.red:C.green)+'">'+f(acc,2)+'</b>'+
      (mode==='order'?'<br>학습용에 빙어가 한 마리도 없습니다. 모델은 빙어를 본 적이 없으니 맞힐 수가 없습니다 (표본이 한쪽으로 쏠림).':'');
    emit(el,{mode:mode,acc:acc,testBream:tb,testN:te.length});}
  run();
};

/* ③ 혼동행렬 · 문턱값 (점수 분포는 설명용 모형) */
W.cm=function(el,o){
  var n=o.n||240,rate=o.rate||.18,sep=o.sep||1.2,seed=o.seed||7,th=o.th==null?.5:o.th; var R=L.rng(seed);
  function nrm(){var u=Math.max(1e-9,R()),v=R(); return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
  var npos=Math.max(1,Math.round(n*rate)),pts=[];
  for(var i=0;i<n;i++){var y=i<npos?1:0; var z=(y?sep:-sep)+nrm()*(o.sd||1)+(o.shift||-1.2); pts.push([1/(1+Math.exp(-z)),y]);}
  var cv=cvs(el,o.h||170), sl=ctrl(el,''), tb=box(el,'cmwrap');
  slider(sl,'문턱값 (이 점수 이상이면 “예”로 판정)',0.02,0.98,0.01,th,function(v){th=v;draw();},function(v){return v.toFixed(2);});
  function draw(){var F=L.fit(cv),c=F.c,Wd=F.W,H=F.H; c.clearRect(0,0,Wd,H);
    var T=axes(c,Wd,H,{x0:0,x1:1,y0:0,y1:1,xl:'모델이 매긴 점수 (0~1)',yl:'',dx:1,fy:function(){return '';}});
    pts.forEach(function(p,i){var yy=p[1]?.72:.28; var jitter=((i*37)%23)/23*.16-.08; dot(c,T.X(p[0]),T.Y(yy+jitter),p[1]?C.red:C.blue,p[1]?3.6:2.6,'c');});
    c.strokeStyle=C.amber; c.lineWidth=2; c.beginPath(); c.moveTo(T.X(th),8); c.lineTo(T.X(th),H-36); c.stroke();
    c.fillStyle=C.ink; c.font='12px '+FONT(); c.textAlign='left'; c.fillText(o.posName?'● '+o.posName:'● 실제 예',Wd-150,20); c.fillStyle=C.blue; c.fillText(o.negName?'● '+o.negName:'● 실제 아니오',Wd-150,36);
    var tp=0,fp=0,fn=0,tn=0; pts.forEach(function(p){var yh=p[0]>=th?1:0; if(yh&&p[1])tp++; else if(yh)fp++; else if(p[1])fn++; else tn++;});
    var acc=(tp+tn)/n,pre=tp+fp?tp/(tp+fp):null,rec=tp/(tp+fn),f1=pre&&rec?2*pre*rec/(pre+rec):0,base=1-npos/n;
    var pn=o.posName||'예',nn=o.negName||'아니오';
    var cost=o.cost?(fn*o.cost.fn+fp*o.cost.fp):null;
    tb.innerHTML='<div class="cmgrid"><div></div><div class="h">판정: '+nn+'</div><div class="h">판정: '+pn+'</div>'+
      '<div class="h">실제: '+nn+'</div><div class="tn"><b>'+tn+'</b><span>맞게 넘김 (TN)</span></div><div class="fp"><b>'+fp+'</b><span>헛경보 (FP)</span></div>'+
      '<div class="h">실제: '+pn+'</div><div class="fn"><b>'+fn+'</b><span>놓침 (FN)</span></div><div class="tp"><b>'+tp+'</b><span>잡아냄 (TP)</span></div></div>'+
      '<div class="mets"><span>정확도 <b>'+f(acc,3)+'</b></span><span>정밀도 <b>'+(pre==null?'계산 불가':f(pre,3))+'</b></span><span>재현율 <b>'+f(rec,3)+'</b></span><span>F1 <b>'+f(f1,3)+'</b></span><span class="base">기준선 “모두 '+nn+'” 정확도 '+f(base,3)+'</span>'+
      (cost!=null?'<span class="cost">비용 합계 <b>'+f(cost)+(o.cost.unit||'')+'</b> (놓침 1건 '+f(o.cost.fn)+' · 헛경보 1건 '+f(o.cost.fp)+')</span>':'')+'</div>';
    emit(el,{th:th,tp:tp,fp:fp,fn:fn,tn:tn,acc:acc,pre:pre,rec:rec,f1:f1,base:base,cost:cost});}
  window.addEventListener('resize',draw); draw(); el._set=function(s){if(s.th!=null){th=s.th;$('input',sl).value=th;$('b',sl).textContent=th.toFixed(2);} draw();};
};

/* ④ 직선 긋기 (택시 요금 60건, 실제 rides.csv에서 뽑음) */
W.reg=function(el,o){
  var P=o.data||RIDES, xs=P.map(function(p){return p[0];}), ys=P.map(function(p){return p[1];}), mx=meanStd(xs)[0], my=meanStd(ys)[0];
  var sxy=0,sxx=0; P.forEach(function(p){sxy+=(p[0]-mx)*(p[1]-my); sxx+=(p[0]-mx)*(p[0]-mx);}); var A=sxy/sxx,B=my-A*mx;
  var st={a:o.a||500,b:o.b||8000}; var cv=cvs(el,o.h||290), sl=ctrl(el,''), out=box(el);
  var ia=slider(sl,'기울기 (1km당 요금)',0,1500,10,st.a,function(v){st.a=v;draw();},function(v){return f(v)+'원';});
  var ib=slider(sl,'출발값 (0km일 때)',0,12000,100,st.b,function(v){st.b=v;draw();},function(v){return f(v)+'원';});
  var bt=ctrl(el,'<button type="button" class="bt primary">가장 잘 맞는 직선 (최소제곱)</button><button type="button" class="bt">평균만 답하기</button>');
  $$('button',bt)[0].onclick=function(){set(Math.round(A/10)*10,Math.round(B/100)*100);}; $$('button',bt)[1].onclick=function(){set(0,Math.round(my/100)*100);};
  function set(a,b){st.a=a;st.b=b;ia.value=a;ib.value=b;ia.oninput();ib.oninput();}
  function draw(){var F=L.fit(cv),c=F.c; c.clearRect(0,0,F.W,F.H); var T=axes(c,F.W,F.H,{x0:0,x1:20,y0:0,y1:28000,xl:'이동 거리 (km)',yl:'요금 (원)',fy:function(v){return f(v/1000)+'천';}});
    var se=0,ae=0,st0=0; P.forEach(function(p){var yh=st.a*p[0]+st.b; c.strokeStyle='rgba(163,92,0,.45)'; c.beginPath(); c.moveTo(T.X(p[0]),T.Y(p[1])); c.lineTo(T.X(p[0]),T.Y(yh)); c.stroke(); se+=(p[1]-yh)*(p[1]-yh); ae+=Math.abs(p[1]-yh); st0+=(p[1]-my)*(p[1]-my);});
    P.forEach(function(p){dot(c,T.X(p[0]),T.Y(p[1]),C.blue,3.5);});
    c.strokeStyle=C.red; c.lineWidth=2.5; c.beginPath(); c.moveTo(T.X(0),T.Y(st.b)); c.lineTo(T.X(20),T.Y(st.b+20*st.a)); c.stroke(); c.lineWidth=1;
    var n=P.length,rmse=Math.sqrt(se/n),mae=ae/n,r2=1-se/st0;
    out.innerHTML='평균 오차 MAE <b>'+f(mae)+'원</b> · RMSE <b>'+f(rmse)+'원</b> · 결정계수 R² <b>'+f(r2,3)+'</b> <span style="color:#5b6874">(평균 요금 '+f(my)+'원 · RMSE는 평균의 '+f(rmse/my*100,1)+'%)</span><br><span style="font-size:13px;color:#5b6874">주황 세로선이 “빗나간 만큼(오차)”입니다. 세로선이 짧아지게 손잡이를 움직여 보세요.</span>';
    emit(el,{a:st.a,b:st.b,mae:mae,rmse:rmse,r2:r2,bestA:A,bestB:B});}
  window.addEventListener('resize',draw); draw();
};

/* ⑤ 오차 다섯 건 계산표 */
W.err5=function(el,o){
  var rows=o.rows||[[9000,10000],[12000,11000],[8500,8500],[15000,12000],[11000,10000]];
  var t=document.createElement('div'); t.className='tbl'; el.appendChild(t); var out=box(el);
  t.innerHTML='<table><thead><tr><th>건</th><th>예측</th><th>실제</th><th>오차 (예측−실제)</th><th>오차²</th></tr></thead><tbody>'+rows.map(function(r,i){return '<tr><td>'+(i+1)+'</td><td><input type="number" step="500" value="'+r[0]+'" style="width:96px"></td><td>'+f(r[1])+'</td><td class="e"></td><td class="e2"></td></tr>';}).join('')+'</tbody></table>';
  function run(){var se=0,ae=0,mx=0,mi=0; $$('tbody tr',t).forEach(function(tr,i){var p=+$('input',tr).value,e=p-rows[i][1]; $('.e',tr).textContent=f(e); $('.e2',tr).textContent=f(e*e); se+=e*e; ae+=Math.abs(e); if(Math.abs(e)>mx){mx=Math.abs(e);mi=i;}});
    $$('tbody tr',t).forEach(function(tr,i){tr.style.background=i===mi&&mx>0?'#fdf3e1':'';});
    var n=rows.length; out.innerHTML='MAE = 오차 크기 합 '+f(ae)+' ÷ '+n+' = <b>'+f(ae/n)+'원</b> · RMSE = √(오차² 평균 '+f(se/n)+') = <b>'+f(Math.sqrt(se/n))+'원</b><br>주황 줄(가장 크게 빗나간 건)을 고쳐 보세요. RMSE가 MAE보다 더 크게 움직입니다.';
    emit(el,{mae:ae/n,rmse:Math.sqrt(se/n)});}
  $$('input',t).forEach(function(i){i.oninput=run;}); run();
};

/* ⑥ 5겹 교차검증 */
W.kfold=function(el,o){
  var models=o.models, cur=0, t=0, cv=cvs(el,o.h||170), out=box(el);
  if(models.length>1) seg(el,models.map(function(m,i){return [String(i),m.name];}),'0',function(v){cur=+v;draw(0);});
  function draw(dt){t+=dt||0; var F=L.fit(cv),c=F.c,Wd=F.W,H=F.H; c.clearRect(0,0,Wd,H); var m=models[cur],k=m.s.length,act=Math.floor(t/1.1)%k; if(L.RM)act=k-1;
    var bw=(Wd-150)/k; c.font='12px '+FONT();
    for(var r=0;r<k;r++){var y=10+r*((H-20)/k); c.fillStyle=C.mut; c.textAlign='left'; c.fillText((r+1)+'회차',4,y+14);
      for(var j=0;j<k;j++){c.fillStyle=j===r?(r<=act?'#fdf3e1':'#f6f8fa'):(r<=act?'#e6eefb':'#f6f8fa'); c.strokeStyle=j===r?C.amber:'#d5dbe2'; c.fillRect(50+j*bw,y,bw-4,(H-20)/k-6); c.strokeRect(50+j*bw,y,bw-4,(H-20)/k-6);
        if(j===r){c.fillStyle=C.amber; c.textAlign='center'; c.fillText('시험',50+j*bw+bw/2-2,y+14);}}
      if(r<=act){c.fillStyle=C.ink; c.textAlign='left'; c.fillText(m.lab+' '+m.s[r].toFixed(2),Wd-92,y+14);}}
    var mean=m.s.reduce(function(a,b){return a+b;},0)/k, sd=Math.sqrt(m.s.reduce(function(a,b){return a+(b-mean)*(b-mean);},0)/k);
    out.innerHTML='<b>'+m.name+'</b> — 다섯 번의 시험 점수 '+m.s.map(function(v){return v.toFixed(2);}).join(' · ')+' → 평균 <b>'+mean.toFixed(3)+'</b> ± 흔들림(표준편차) <b>'+sd.toFixed(3)+'</b>'+(m.note?'<br><span style="font-size:13px;color:#5b6874">'+m.note+'</span>':'');
    emit(el,{model:cur,mean:mean,sd:sd});}
  L.addMod(cv,draw);
};

/* ⑦ 시그모이드 */
W.sigmoid=function(el,o){
  var z=o.z||0,th=.5, cv=cvs(el,o.h||230), sl=ctrl(el,''), out=box(el);
  slider(sl,'점수 z',-6,6,.1,z,function(v){z=v;draw();},function(v){return v.toFixed(1);});
  slider(sl,'문턱값',.1,.9,.05,th,function(v){th=v;draw();},function(v){return v.toFixed(2);});
  function draw(){var F=L.fit(cv),c=F.c; c.clearRect(0,0,F.W,F.H); var T=axes(c,F.W,F.H,{x0:-6,x1:6,y0:0,y1:1,xl:'점수 z = w·x + b',yl:'확률',dy:2});
    c.strokeStyle=C.purple; c.lineWidth=2.5; c.beginPath(); for(var x=-6;x<=6.01;x+=.1){var y=1/(1+Math.exp(-x)); x===-6?c.moveTo(T.X(x),T.Y(y)):c.lineTo(T.X(x),T.Y(y));} c.stroke();
    c.strokeStyle=C.amber; c.lineWidth=1.5; c.setLineDash([5,4]); c.beginPath(); c.moveTo(T.X(-6),T.Y(th)); c.lineTo(T.X(6),T.Y(th)); c.stroke(); c.setLineDash([]);
    var p=1/(1+Math.exp(-z)); dot(c,T.X(z),T.Y(p),p>=th?C.red:C.blue,7);
    out.innerHTML='z = <b>'+z.toFixed(1)+'</b> → 확률 σ(z) = 1 ÷ (1 + e<sup>−z</sup>) = <b>'+p.toFixed(3)+'</b> → 문턱값 '+th.toFixed(2)+' 기준 판정 <b>'+(p>=th?(o.pos||'예 (1)'):(o.neg||'아니오 (0)'))+'</b>';
    emit(el,{z:z,p:p,th:th});}
  window.addEventListener('resize',draw); draw();
};

/* ⑧ 직선 하나, 세 모델 (퍼셉트론 · 로지스틱 · 선형 SVM) — 점은 설명용 모형 */
W.linmod=function(el,o){
  var R=L.rng(o.seed||11),D=[]; function nrm(){var u=Math.max(1e-9,R()),v=R(); return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
  for(var i=0;i<40;i++){var y=i<20?1:-1; D.push([(y>0?1.1:-1.1)+nrm()*.55+(o.overlap?nrm()*.3:0),(y>0?.9:-.9)+nrm()*.55,y]);}
  var st={ang:30,b:0,mode:o.mode||'perc'}; var cv=cvs(el,o.h||300);
  seg(el,[['perc','퍼셉트론 — 맞다/틀리다만'],['logi','로지스틱 — 확률로'],['svm','선형 SVM — 여유 폭까지']],st.mode,function(v){st.mode=v;draw();});
  var sl=ctrl(el,''), ia=slider(sl,'직선 기울기 (각도)',-90,90,1,st.ang,function(v){st.ang=v;draw();},function(v){return v+'°';}), ib=slider(sl,'직선 위치',-2,2,.05,st.b,function(v){st.b=v;draw();},function(v){return v.toFixed(2);});
  var bt=ctrl(el,'<button type="button" class="bt primary">이 모델 방식으로 자동 맞추기</button>'); out=box(el);
  function wv(){var a=st.ang*Math.PI/180; return [-Math.sin(a),Math.cos(a)];} // 직선 방향 각도 → 법선
  function score(w,b){var err=0,ll=0,mg=1e9,hl=0; D.forEach(function(p){var z=w[0]*p[0]+w[1]*p[1]+b,yz=p[2]*z; if(yz<=0)err++; ll+=Math.log(1+Math.exp(-yz*2)); mg=Math.min(mg,yz); hl+=Math.max(0,1-yz*2);}); return {err:err,ll:ll/D.length,mg:mg,hl:hl/D.length};}
  $('button',bt).onclick=function(){var best=null; outer: for(var a=-90;a<=90;a+=1){for(var b=-2;b<=2.001;b+=.05){var w=[-Math.sin(a*Math.PI/180),Math.cos(a*Math.PI/180)],s=score(w,b),key=st.mode==='perc'?s.err:st.mode==='logi'?s.ll:(s.err*10-s.mg);
      if(st.mode==='perc'&&s.err===0){best={a:a,b:b};break outer;} if(!best||key<best.k)best={a:a,b:b,k:key};}}
    st.ang=best.a; st.b=Math.round(best.b*100)/100; ia.value=st.ang; ib.value=st.b; ia.oninput(); ib.oninput();};
  var out=null;
  function draw(){if(!out)return; var F=L.fit(cv),c=F.c,Wd=F.W,H=F.H; c.clearRect(0,0,Wd,H); var T=axes(c,Wd,H,{x0:-3,x1:3,y0:-3,y1:3,xl:'특성 1 (표준화)',yl:'특성 2 (표준화)',dx:0,dy:0,L:40});
    var w=wv(),b=st.b,s=score(w,b);
    if(st.mode==='logi'){for(var gx=-3;gx<3;gx+=.2)for(var gy=-3;gy<3;gy+=.2){var p=1/(1+Math.exp(-2*(w[0]*(gx+.1)+w[1]*(gy+.1)+b))); c.fillStyle='rgba('+Math.round(201*p+30*(1-p))+','+Math.round(48*p+85*(1-p))+','+Math.round(48*p+200*(1-p))+',.13)'; c.fillRect(T.X(gx),T.Y(gy+.2),T.X(gx+.2)-T.X(gx)+1,T.Y(gy)-T.Y(gy+.2)+1);}}
    function line(off,col,dash){c.strokeStyle=col; c.lineWidth=dash?1.5:2.5; c.setLineDash(dash?[6,4]:[]); c.beginPath(); var first=true;
      for(var x=-3;x<=3.001;x+=.05){var y=Math.abs(w[1])>1e-6?(-(b-off)-w[0]*x)/w[1]:null; if(y==null)continue; if(first){c.moveTo(T.X(x),T.Y(y));first=false;} else c.lineTo(T.X(x),T.Y(y));}
      if(Math.abs(w[1])<1e-6){var xx=-(b-off)/w[0]; c.moveTo(T.X(xx),T.Y(-3)); c.lineTo(T.X(xx),T.Y(3));} c.stroke(); c.setLineDash([]);}
    if(st.mode==='svm'&&s.mg>0){line(s.mg,'rgba(11,122,134,.8)',1); line(-s.mg,'rgba(11,122,134,.8)',1);}
    c.save(); c.beginPath(); c.rect(T.X(-3),T.Y(3),T.X(3)-T.X(-3),T.Y(-3)-T.Y(3)); c.clip(); line(0,C.ink,0); c.restore();
    D.forEach(function(p){var z=w[0]*p[0]+w[1]*p[1]+b,bad=p[2]*z<=0,sup=st.mode==='svm'&&Math.abs(p[2]*z-s.mg)<.02; dot(c,T.X(p[0]),T.Y(p[1]),p[2]>0?C.red:C.blue,sup?6.5:4.5,p[2]>0?'c':'sq'); if(bad){c.strokeStyle=C.amber;c.lineWidth=2;c.beginPath();c.arc(T.X(p[0]),T.Y(p[1]),9,0,7);c.stroke();}});
    var msg=st.mode==='perc'?'틀린 점 <b>'+s.err+'개</b>. 퍼셉트론은 틀린 점이 0개가 되는 순간 멈춥니다 — 어디서 멈출지는 정해져 있지 않습니다.':
      st.mode==='logi'?'틀린 점 <b>'+s.err+'개</b> · 평균 로그 손실 <b>'+s.ll.toFixed(3)+'</b> (작을수록 확률이 정답 쪽으로 확실). 배경 색이 진할수록 확률이 0이나 1에 가깝습니다.':
      '틀린 점 <b>'+s.err+'개</b> · 가장 가까운 점까지의 여유 폭 <b>'+(s.mg>0?s.mg.toFixed(2):'없음 (틀린 점이 있음)')+'</b>. 크게 표시된 점이 서포트 벡터 — 이 점들만 직선 위치를 정합니다.';
    out.innerHTML=msg+' <span style="font-size:13px;color:#5b6874">(점은 설명용 모형)</span>'; emit(el,{mode:st.mode,err:s.err,ll:s.ll,mg:s.mg,ang:st.ang,b:st.b});}
  window.addEventListener('resize',draw); draw();
};

/* ⑨ 지니 불순도 계산기 */
W.gini=function(el,o){
  var c=ctrl(el,'<label class="sl"><span>A 종 마리 수</span><input type="number" min="0" max="99" value="'+(o.a||8)+'" style="width:70px"></label><label class="sl"><span>B 종 마리 수</span><input type="number" min="0" max="99" value="'+(o.b||2)+'" style="width:70px"></label>');
  var bar=box(el,'gbar'), out=box(el);
  function run(){var a=+$$('input',c)[0].value||0,b=+$$('input',c)[1].value||0,n=a+b||1,pa=a/n,pb=b/n,g=1-pa*pa-pb*pb;
    bar.innerHTML='<i style="width:'+(pa*100)+'%;background:#1e55c8"></i><i style="width:'+(pb*100)+'%;background:#c93030"></i>';
    out.innerHTML='비율 A '+pa.toFixed(2)+' · B '+pb.toFixed(2)+' → 지니 = 1 − ('+pa.toFixed(2)+'² + '+pb.toFixed(2)+'²) = 1 − ('+(pa*pa).toFixed(4)+' + '+(pb*pb).toFixed(4)+') = <b>'+g.toFixed(3)+'</b> '+(g===0?'<span class="pill ok">한 종만 — 가장 깔끔</span>':g>=.49?'<span class="pill no">반반 — 가장 섞임</span>':'');
    emit(el,{a:a,b:b,g:g});}
  $$('input',c).forEach(function(i){i.oninput=run;}); run();
};

/* ⑩ 학습 점수 vs 시험 점수 (과적합 탐지기) */
W.gap=function(el,o){
  var M=o.models, cv=cvs(el,o.h||250), sel=-1, out=box(el);
  var bt=ctrl(el,M.map(function(m,i){return '<button type="button" class="bt" data-i="'+i+'">'+m.name+'</button>';}).join(''));
  $$('button',bt).forEach(function(b){b.onclick=function(){sel=+b.dataset.i; $$('button',bt).forEach(function(x){x.setAttribute('aria-pressed',x===b);}); draw();};});
  function draw(){var F=L.fit(cv),c=F.c,Wd=F.W,H=F.H; c.clearRect(0,0,Wd,H); var y0=o.y0==null?.8:o.y0;
    var T=axes(c,Wd,H,{x0:0,x1:M.length,y0:y0,y1:1,xl:'',yl:o.yl||'점수',dy:2,fx:function(){return '';}});
    M.forEach(function(m,i){var x=T.X(i+.5),bw=Math.min(26,(T.X(1)-T.X(0))/4); [['tr',C.blue],['te',C.amber],['cv',C.green]].forEach(function(k,j){if(m[k[0]]==null)return; var v=Math.max(y0,m[k[0]]); c.fillStyle=k[1]; c.globalAlpha=sel<0||sel===i?1:.35; c.fillRect(x+(j-1.5)*bw,T.Y(v),bw-3,T.Y(y0)-T.Y(v)); c.globalAlpha=1;});
      c.fillStyle=C.ink; c.font='12px '+FONT(); c.textAlign='center'; c.fillText(m.name,x,H-20);});
    c.textAlign='left'; c.fillStyle=C.blue; c.fillText('■ 학습',60,18); c.fillStyle=C.amber; c.fillText('■ 시험',110,18); c.fillStyle=C.green; c.fillText('■ 5겹 교차검증',160,18);
    if(sel>=0){var m=M[sel],g=m.tr-m.te; out.innerHTML='<b>'+m.name+'</b> — 학습 '+m.tr.toFixed(3)+' · 시험 '+m.te.toFixed(3)+(m.cv!=null?' · 교차검증 '+m.cv.toFixed(3):'')+' → 학습과 시험의 차이 <b>'+g.toFixed(3)+'</b> '+(g>(o.warn||.03)?'<span class="pill no">외운 흔적 (과적합 의심)</span>':'<span class="pill ok">차이 작음</span>')+(m.note?'<br>'+m.note:'');}
    else out.innerHTML='모델 버튼을 눌러 학습 점수와 시험 점수의 차이를 보세요. '+(o.hint||'');
    emit(el,{sel:sel});}
  window.addEventListener('resize',draw); draw();
};

/* ⑪ 기여도 막대 (SHAP 읽기 연습, 값은 설명용 예시) */
W.contrib=function(el,o){
  var cases=o.cases,cur=0, cv=cvs(el,o.h||230), out=box(el);
  seg(el,cases.map(function(k,i){return [String(i),k.name];}),'0',function(v){cur=+v;draw();});
  function draw(){var F=L.fit(cv),c=F.c,Wd=F.W,H=F.H; c.clearRect(0,0,Wd,H); var k=cases[cur],items=k.items,base=o.base, x=base, lo=base, hi=base;
    items.forEach(function(it){x+=it[1]; lo=Math.min(lo,x); hi=Math.max(hi,x);}); lo=Math.min(lo,base)-80; hi=Math.max(hi,base)+80;
    var T=axes(c,Wd,H,{x0:lo,x1:hi,y0:0,y1:items.length+1,xl:o.unit||'',yl:'',fy:function(){return '';},L:90}); x=base; c.font='12px '+FONT();
    c.fillStyle=C.mut; c.textAlign='right'; c.fillText('출발점(평균)',86,T.Y(items.length+.5)+4); c.strokeStyle=C.mut; c.setLineDash([3,3]); c.beginPath(); c.moveTo(T.X(base),12); c.lineTo(T.X(base),H-36); c.stroke(); c.setLineDash([]);
    items.forEach(function(it,i){var y=T.Y(items.length-i)-9,nx=x+it[1]; c.fillStyle=it[1]<0?C.blue:C.red; c.fillRect(Math.min(T.X(x),T.X(nx)),y,Math.abs(T.X(nx)-T.X(x))||1,18);
      c.fillStyle=C.ink; c.textAlign='right'; c.fillText(it[0],86,y+13); c.textAlign='left'; c.fillText((it[1]>0?'+':'')+f(it[1]),Math.max(T.X(x),T.X(nx))+4,y+13); x=nx;});
    out.innerHTML='출발점 '+f(base)+' '+(o.u||'')+' → 기여도를 차례로 더하면 이 배터리의 예측 <b>'+f(x)+' '+(o.u||'')+'</b>. '+(k.note||'')+' <span style="font-size:13px;color:#5b6874">(값은 설명용 예시)</span>';
    emit(el,{cur:cur,pred:x});}
  window.addEventListener('resize',draw); draw();
};

/* ⑫ 규칙 하나로 가르기 (임계값 하나) */
W.rule=function(el,o){
  var R=L.rng(o.seed||5),A=[],B=[]; function nrm(){var u=Math.max(1e-9,R()),v=R(); return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
  for(var i=0;i<o.na;i++)A.push(o.ma+nrm()*o.sa); for(i=0;i<o.nb;i++)B.push(o.mb+nrm()*o.sb);
  var th=o.th, cv=cvs(el,o.h||170), sl=ctrl(el,''), out=box(el);
  slider(sl,'기준값',o.x0,o.x1,o.step||.1,th,function(v){th=v;draw();},function(v){return v.toFixed(1)+' '+(o.unit||'');});
  function draw(){var F=L.fit(cv),c=F.c; c.clearRect(0,0,F.W,F.H); var T=axes(c,F.W,F.H,{x0:o.x0,x1:o.x1,y0:0,y1:1,xl:o.xl,yl:'',fy:function(){return '';},dx:0});
    A.forEach(function(v,i){dot(c,T.X(v),T.Y(.68+((i*31)%17)/17*.24),C.blue,3.5);}); B.forEach(function(v,i){dot(c,T.X(v),T.Y(.1+((i*29)%17)/17*.24),C.red,3.5,'sq');});
    c.strokeStyle=C.amber; c.lineWidth=2; c.beginPath(); c.moveTo(T.X(th),8); c.lineTo(T.X(th),F.H-36); c.stroke();
    var ok=A.filter(function(v){return o.aAbove?v>th:v<=th;}).length+B.filter(function(v){return o.aAbove?v<=th:v>th;}).length, acc=ok/(A.length+B.length), base=Math.max(A.length,B.length)/(A.length+B.length);
    c.font='12px '+FONT(); c.textAlign='left'; c.fillStyle=C.blue; c.fillText('● '+o.an,60,20); c.fillStyle=C.red; c.fillText('■ '+o.bn,60+o.an.length*13+30,20);
    out.innerHTML='규칙 “'+o.xl.split(' (')[0]+' '+(o.aAbove?'&gt;':'≤')+' '+th.toFixed(1)+'이면 '+o.an+'” → 맞힌 비율 <b>'+acc.toFixed(3)+'</b> · 기준선(많은 쪽으로 모두 답하기) '+base.toFixed(3)+' '+(acc>base+.05?'<span class="pill ok">기준선보다 낫다</span>':'<span class="pill no">기준선과 비슷하거나 낮다</span>');
    emit(el,{th:th,acc:acc,base:base});}
  window.addEventListener('resize',draw); draw();
};

window.ML={init:function(root){$$('.mlw[data-w]',root).forEach(function(el){if(el._ml)return; el._ml=1; var o={}; try{o=JSON.parse(el.dataset.cfg||'{}');}catch(e){} if(W[el.dataset.w]){try{W[el.dataset.w](el,o);}catch(e){console.error('widget',el.dataset.w,e);}}});},W:W,FISH:FISH,RIDES:RIDES,knnPredict:knnPredict};
window.addEventListener('DOMContentLoaded',function(){ML.init(document);});
})();
