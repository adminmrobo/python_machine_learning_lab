/* ══ 연구실 공용 모듈 (낮의 연구실 · 파이썬 머신러닝 연구소) ══
   도우미 → 캐릭터(Cast) → 용어(Gloss) → 학습(Study·퀴즈) → 대결(Duel) → 흐름 캔버스(Flow) → SQL 실습실(SQLLab) → 기타 위젯 */
(function(){'use strict';
var $=function(s,r){return (r||document).querySelector(s);}, $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s));};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});};
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
function rng(seed){var s=seed>>>0||1; return function(){s^=s<<13;s>>>=0;s^=s>>17;s^=s<<5;s>>>=0;return (s>>>0)/4294967296;};}
function fit(cv){var r=cv.getBoundingClientRect(),d=window.devicePixelRatio||1,w=Math.max(10,Math.round(r.width)),h=Math.max(10,Math.round(r.height));
  if(cv.width!==w*d||cv.height!==h*d){cv.width=w*d;cv.height=h*d;} var c=cv.getContext('2d'); c.setTransform(d,0,0,d,0,0); return {c:c,W:w,H:h};}
var MODS=[],vis=new WeakMap(),io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){vis.set(e.target,e.isIntersecting);});}):null;
function addMod(el,fn){MODS.push({el:el,fn:fn}); if(io)io.observe(el); else vis.set(el,true); fn(0);}
var last=0;
function loop(t){var dt=Math.min(.05,(t-(last||t))/1000); last=t; MODS.forEach(function(m){if(vis.get(m.el)&&!RM)m.fn(dt);}); requestAnimationFrame(loop);}
window.addEventListener('resize',function(){MODS.forEach(function(m){m.fn(0);});});
function stamp(c,W,txt){c.save(); c.font='700 11px '+getComputedStyle(document.body).fontFamily; var w=Math.max(c.measureText(txt).width,txt.length*10.5)+12; c.translate(W-w-8,8); c.rotate(-.03);
  c.strokeStyle='#a35c00'; c.fillStyle='rgba(255,255,255,.9)'; c.lineWidth=1.5; c.beginPath(); c.rect(0,0,w,18); c.fill(); c.stroke(); c.fillStyle='#a35c00'; c.fillText(txt,6,13); c.restore();}

/* ── 캐릭터 ── */
var ALIAS={doc_front:'doc_e08',doc_board:'doc_e07',doc_judge:'doc_e10',doc_verdict:'doc_e18',doc_magic:'doc_e16',doc_think:'doc_e09',
 asst_smile:'asst_e13',asst_firm:'asst_e12',asst_report:'asst_e07',asst_spark:'asst_e01',asst_shock:'asst_e24',asst_sigh:'asst_e02',asst_proud:'asst_e16',
 fly_clip:'fly_e10',fly_point:'fly_e08',fly_arms:'fly_e16',fly_coffee:'fly_e13',fly_cry:'fly_e21',fly_type:'fly_e09',fly_magnify:'fly_e07',
 robo_smile:'robo_e13',robo_coin:'robo_e16',robo_chart:'robo_e07',robo_happy:'robo_e12',robo_sigh:'robo_e20',robo_meh:'robo_e18',robo_cry:'robo_e21',robo_wow:'robo_e04',robo_blush:'robo_e14',robo_calc:'robo_e09',
 sia_smile:'sia_e13',sia_sleepy:'sia_e17',moa_smile:'moa_e13',moa_cheer:'moa_e12'};
var BASE={doc:'doc_e08',asst:'asst_e13',fly:'fly_e10',robo:'robo_e13',sia:'sia_e13',moa:'moa_e13',x1:'x1_e13',x2:'x2_e13',x3:'x3_e13'};
if(window.EXMAP)for(var _k in EXMAP)ALIAS[_k]=EXMAP[_k];
function src(who,mood){var S=window.SPRITE||{}; var k=who+'_'+mood; k=ALIAS[k]||k; return S[k]||S[ALIAS[who+'_'+mood]]||S[BASE[who]]||'';}
var Cast={fill:function(){$$('img[data-who]').forEach(function(im){var s=src(im.dataset.who,im.dataset.mood||'front'); if(s)im.src=s;});},
  set:function(im,who,mood){if(!im)return; var s=src(who,mood); if(!s)return; if(RM){im.src=s;return;} im.style.transition='opacity .1s'; im.style.opacity=0; setTimeout(function(){im.src=s; im.style.opacity=1;},100);}};
window.Cast=Cast;

/* ── 용어 말풍선 ── */
function Gloss(GL){
  var tip=$('#tip'); if(!tip||!GL)return; var keys=Object.keys(GL).sort(function(a,b){return b.length-a.length;}); if(!keys.length)return;
  var done={},re=new RegExp('('+keys.map(function(k){return k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}).join('|')+')');
  $$('main section.level:not(#kg):not(#export) p, main section.level:not(#kg):not(#export) li, header.hero p').forEach(function(p){
    if(p.closest('.quiz,.sqllab,.duel,.say,pre,table,.kgx'))return;
    var w=document.createTreeWalker(p,NodeFilter.SHOW_TEXT,null),nodes=[],n; while((n=w.nextNode()))nodes.push(n);
    nodes.forEach(function(t){ if(t.parentNode.closest('a,code,.gl,b.nogl'))return; var m=re.exec(t.nodeValue); if(!m||done[m[1]])return; done[m[1]]=1;
      var sp=document.createElement('span'); sp.className='gl'; sp.tabIndex=0; sp.dataset.k=m[1]; sp.textContent=m[1];
      var after=t.splitText(m.index); after.nodeValue=after.nodeValue.slice(m[1].length); t.parentNode.insertBefore(sp,after);});
  });
  function show(e){var k=e.target.closest('.gl'); if(!k)return; var g=GL[k.dataset.k]; tip.innerHTML='<b>'+esc(g[0])+'</b> <span style="color:#5b6874">· '+esc(g[1])+'</span><br>'+esc(g[2]);
    var r=k.getBoundingClientRect(); tip.style.display='block'; var x=Math.min(window.scrollX+r.left,window.scrollX+document.documentElement.clientWidth-tip.offsetWidth-10); tip.style.left=Math.max(6,x)+'px'; tip.style.top=(window.scrollY+r.bottom+6)+'px';}
  document.addEventListener('pointerover',show); document.addEventListener('focusin',show);
  document.addEventListener('pointerout',function(e){if(e.target.closest('.gl'))tip.style.display='none';});
  document.addEventListener('focusout',function(){tip.style.display='none';});
}

/* ── 퀴즈 ── */
var QSTAT={done:0,ok:0,total:0,by:{}};
function Quiz(el,items){
  var h='<div class="qh">확인 퀴즈 · '+items.length+'문항</div>';
  items.forEach(function(q,i){QSTAT.total++; h+='<div class="q" data-i="'+i+'"><p>Q'+(i+1)+'. '+q.q+'</p><div class="opts">'+q.o.map(function(o,j){return '<button type="button" class="bt" data-j="'+j+'">'+(j+1)+') '+o+'</button>';}).join('')+'</div>'+
    (q.hint?'<details class="hint"><summary>힌트</summary>'+q.hint+'</details>':'')+'<div class="why" hidden></div></div>';});
  el.innerHTML=h;
  $$('.q',el).forEach(function(qe){var q=items[+qe.dataset.i],answered=false;
    $$('.opts button',qe).forEach(function(b){b.onclick=function(){var j=+b.dataset.j; var ok=j===q.a;
      $$('.opts button',qe).forEach(function(x){x.classList.remove('ok','no');}); b.classList.add(ok?'ok':'no'); if(!ok)$$('.opts button',qe)[q.a].classList.add('ok');
      var w=$('.why',qe); w.hidden=false; w.innerHTML=(ok?'<b style="color:#13733a">맞아요.</b> ':'<b style="color:#c9302c">다시 볼까요.</b> ')+q.why;
      if(!answered){answered=true;QSTAT.done++; if(ok)QSTAT.ok++; QSTAT.by[(el.dataset.quiz||'q')+':'+qe.dataset.i]={ok:ok}; updProg();}};});});
}
function updProg(){var e=$('#qprog'); if(e)e.textContent='퀴즈 '+QSTAT.done+'/'+QSTAT.total+' · 맞힘 '+QSTAT.ok;}

/* ── 대결 ── */
function Duel(cfg){
  var el=$(cfg.el); if(!el)return; var imF=$('img[data-who=fly]',el),imR=$('img[data-who=robo]',el),imD=$('.res img[data-who=doc]',el),imA=$('.res img[data-who=asst]',el);
  Cast.set(imF,'fly','point'); Cast.set(imR,'robo','coin');
  $$('.guess button',el).forEach(function(b){b.onclick=function(){$$('.guess button',el).forEach(function(x){x.setAttribute('aria-pressed',x===b);}); $('.gnote',el).textContent='예상을 적어 두었습니다. 이제 결과를 봅시다.';};});
  $('.go',el).onclick=function(){
    var r=cfg.run(); el.classList.add('open'); var hib=cfg.higherIsBetter!==false;
    var mx=Math.max(Math.abs(r.fly),Math.abs(r.robo))||1;
    $('.bar.f s',el).style.width=(100*Math.abs(r.fly)/mx)+'%'; $('.bar.r s',el).style.width=(100*Math.abs(r.robo)/mx)+'%';
    $('.bar.f b',el).textContent=r.flyTxt||r.fly; $('.bar.r b',el).textContent=r.roboTxt||r.robo;
    var res; if(r.foul)res='X'; else if(r.cond)res='C'; else if(Math.abs(r.fly-r.robo)<=(cfg.drawMargin||0))res='D'; else res=((r.fly>r.robo)===hib)?'F':'R';
    var M={F:['judge','spark','arms','sigh'],R:['judge','spark',(Math.abs(r.fly-r.robo)/mx>.1?'cry':'coffee'),'happy'],D:['think','smile','coffee','meh'],C:['think','report','coffee','calc'],X:['judge','shock','arms','blush']}[res];
    Cast.set(imD,'doc',M[0]); Cast.set(imA,'asst',M[1]); Cast.set(imF,'fly',M[2]); Cast.set(imR,'robo',M[3]);
    $('.ann',el).innerHTML=cfg.announce(r); $('.ver',el).innerHTML=cfg.verdict(res,r);
  };
  $('.reset',el).onclick=function(){el.classList.remove('open'); Cast.set(imF,'fly','point'); Cast.set(imR,'robo','coin'); $$('.bar s',el).forEach(function(s){s.style.width=0;});};
}

/* ── 흐름 캔버스: 데이터 카드(나르미)가 단계를 지나며 바뀐다 ── */
function Flow(cv,o){
  var st=o.stations,items=o.items,t=0,speed=o.speed||.45,W,H,cols=o.colors||['#c9302c','#9b3fb5','#13733a','#1e55c8','#a35c00','#0b7a86'];
  var font=getComputedStyle(document.body).fontFamily;
  function draw(dt){var F=fit(cv),c=F.c; W=F.W; H=F.H; t+=dt*speed; c.clearRect(0,0,W,H);
    var n=st.length,pad=14,bw=(W-pad*2)/n,by=34,bh=H-by-28;
    st.forEach(function(s,i){var x=pad+i*bw+4; c.fillStyle='#f6f8fa'; c.strokeStyle='#d5dbe2'; c.lineWidth=1; c.beginPath(); c.roundRect?c.roundRect(x,by,bw-8,bh,10):c.rect(x,by,bw-8,bh); c.fill(); c.stroke();
      c.fillStyle=cols[i%cols.length]; c.font='700 13px '+font; c.textAlign='center'; c.fillText(s,x+(bw-8)/2,by-10);
      if(i<n-1){c.fillStyle='#9aa5b1'; c.beginPath(); var ax=x+bw-6,ay=by+bh/2; c.moveTo(ax-2,ay-6); c.lineTo(ax+4,ay); c.lineTo(ax-2,ay+6); c.fill();}});
    var lanes=Math.min(items.length,Math.max(1,Math.floor(bh/30)));
    items.forEach(function(it,k){
      var lane=k%lanes,ph=((t+k*(n/items.length))%(n+0.6)); if(RM)ph=Math.min(n-0.01,k%n+.5);
      var i=Math.min(n-1,Math.floor(ph)),f=ph-i,x=pad+i*bw+4+(bw-8)*Math.min(1,f),y=by+14+lane*((bh-24)/lanes);
      var lab=it[Math.min(i,it.length-1)],bad=o.bad&&o.bad(it,i);
      c.font='13px '+font; var tw=Math.min(bw-14,c.measureText(lab).width+16); var bx=Math.max(pad+i*bw+6,Math.min(x-tw/2,pad+(i+1)*bw-tw-6));
      c.fillStyle=bad?'#fcebea':'#ffffff'; c.strokeStyle=bad?'#c9302c':cols[i%cols.length]; c.lineWidth=1.5; c.beginPath(); c.roundRect?c.roundRect(bx,y,tw,22,6):c.rect(bx,y,tw,22); c.fill(); c.stroke();
      c.fillStyle=bad?'#c9302c':'#16212b'; c.textAlign='left'; c.save(); c.beginPath(); c.rect(bx,y,tw,22); c.clip(); c.fillText(lab,bx+8,y+15.5); c.restore();
    });
    if(o.stamp!==false)stamp(c,W,o.stamp||'설명용 모형');
  }
  addMod(cv,draw);
}

/* 표 그리기 도우미 (위젯용) */
function tableHTML(cols,rows,opt){opt=opt||{};
  return '<div class="dbtab"><table>'+(opt.cap?'<caption>'+esc(opt.cap)+'</caption>':'')+'<thead><tr>'+cols.map(function(c,i){return '<th'+(opt.pk&&opt.pk.indexOf(i)>=0?' style="text-decoration:underline"':'')+'>'+esc(c)+'</th>';}).join('')+'</tr></thead><tbody>'+
    rows.map(function(r,i){var cl=opt.cls?opt.cls(r,i):''; return '<tr'+(cl?' class="'+cl+'"':'')+'>'+r.map(function(v){return v==null?'<td class="null" style="color:#5b6874;font-style:italic">NULL</td>':'<td>'+esc(v)+'</td>';}).join('')+'</tr>';}).join('')+'</tbody></table></div>';}

/* ── 진행 막대 ── */
function prog(){var p=$('#prog'); if(!p)return; var h=document.documentElement; p.style.width=(100*h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight))+'%';}
window.addEventListener('scroll',prog,{passive:true});

/* ── 낱말 카드 ── */
function Flash(el,cards){el.classList.add('flash'); el.innerHTML=cards.map(function(c,i){return '<button type="button" class="bt" data-i="'+i+'">'+c[0]+'</button>';}).join('');
  $$('button',el).forEach(function(b){var c=cards[+b.dataset.i],f=false; b.onclick=function(){f=!f; b.classList.toggle('flip',f); b.innerHTML=f?c[1]:c[0];};});}


/* ── 실전 연습장 공통 도구 ── */
function kpis(el,items){el.innerHTML=items.map(function(k){return '<div class="dk '+(k[3]||'')+'"><span>'+k[0]+'</span><b>'+k[1]+'</b>'+(k[2]?'<small>'+k[2]+'</small>':'')+'</div>';}).join('');}
var PALC=['#1e55c8','#c93030','#13733a','#a35c00','#9b3fb5','#0b7a86'];
function chart(cv,o){var f=fit(cv),c=f.c,W=f.W,H=f.H,L=46,R=10,T=14,B=34,ser=o.series,lab=o.labels,n=lab.length;
 c.clearRect(0,0,W,H);c.font='12px '+getComputedStyle(document.body).fontFamily;
 var mx=o.ymax||Math.max.apply(null,[1].concat.apply([],ser.map(function(s){return s.data;})));mx=mx*1.1;
 c.strokeStyle='#e3e8ee';c.fillStyle='#5b6874';c.textAlign='right';
 for(var g=0;g<=4;g++){var y=T+(H-T-B)*(1-g/4);c.beginPath();c.moveTo(L,y);c.lineTo(W-R,y);c.stroke();c.fillText((o.yfmt||function(v){v=Math.round(v);return v>=1e8?(v/1e8).toFixed(1)+'억':v>=1e4?(Math.round(v/1e3)/10).toLocaleString()+'만':v.toLocaleString();})(mx*g/4),L-6,y+4);}
 var bw=(W-L-R)/n;c.textAlign='center';
 var step=Math.max(1,Math.ceil(n/Math.max(1,Math.floor((W-L-R)/42))));
 lab.forEach(function(t,i){if(i%step===0)c.fillText(t,L+bw*(i+.5),H-B+16);});
 ser.forEach(function(s,si){c.fillStyle=c.strokeStyle=s.color||PALC[si%6];
  if((o.type||'bar')==='bar'){var w=bw*.8/ser.length;s.data.forEach(function(v,i){var h=(H-T-B)*v/mx;c.fillRect(L+bw*i+bw*.1+w*si,H-B-h,w-1,h);});}
  else{c.lineWidth=2.5;c.beginPath();s.data.forEach(function(v,i){var x=L+bw*(i+.5),y=H-B-(H-T-B)*v/mx;i?c.lineTo(x,y):c.moveTo(x,y);});c.stroke();}});
 if(ser.length>1||o.legend){var x=L+4;c.textAlign='left';ser.forEach(function(s,si){c.fillStyle=s.color||PALC[si%6];c.fillRect(x,2,10,10);c.fillStyle='#16212b';c.fillText(s.name,x+14,11);x+=c.measureText(s.name).width+30;});}
}
window.QSTAT=QSTAT;window.LAB={$:$,$$:$$,esc:esc,rng:rng,fit:fit,addMod:addMod,stamp:stamp,Gloss:Gloss,Quiz:Quiz,Duel:Duel,Flow:Flow,tableHTML:tableHTML,Flash:Flash,RM:RM,kpis:kpis,chart:chart};
window.addEventListener('DOMContentLoaded',function(){
  Cast.fill();
  if(window.QUIZ)Object.keys(QUIZ).forEach(function(k){var e=document.querySelector('.quiz[data-quiz="'+k+'"]'); if(e)Quiz(e,QUIZ[k]);});
  updProg();
  if(window.GL)Gloss(GL);
  $$('canvas.flow').forEach(function(cv){var o=window.FLOWS&&FLOWS[cv.id]; if(o)Flow(cv,o);});
  if(window.DUEL)Duel(DUEL);
  $$('.flash[data-cards]').forEach(function(el){var o=window.CARDS&&CARDS[el.dataset.cards]; if(o)Flash(el,o);});
  if(window.PAGE&&PAGE.init)PAGE.init(window.LAB);
  requestAnimationFrame(loop); prog();
});
})();
