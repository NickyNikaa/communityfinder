(function(){
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
function nf(n){return n.toLocaleString('de-DE')}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
var CF=window.CF||{email:'',endpoint:''};

/* Menü */
var mb=$('#menuBtn');
if(mb)mb.addEventListener('click',function(){var o=$('#mainNav').classList.toggle('open');this.setAttribute('aria-expanded',o)});

/* Formulare: Endpoint oder Mailprogramm */
function deliver(subject,fields,done){
  var lines=fields.map(function(f){return f[0]+': '+f[1]}).join('\n');
  if(CF.endpoint){
    var fd=new FormData();fields.forEach(function(f){fd.append(f[0],f[1])});fd.append('_subject',subject);
    fetch(CF.endpoint,{method:'POST',body:fd,headers:{'Accept':'application/json'}}).then(function(r){done(r.ok?'sent':'error')}).catch(function(){done('error')});
  }else{
    location.href='mailto:'+CF.email+'?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(lines);
    done('mailto');
  }
}
function ok(box,title,text,mailto){
  box.innerHTML='';var d=document.createElement('div');d.className='ok';
  var h=document.createElement('h3');h.textContent=title;var p=document.createElement('p');p.textContent=text;
  d.appendChild(h);d.appendChild(p);
  if(mailto&&CF.email){var p2=document.createElement('p');p2.style.marginTop='10px';p2.textContent='Falls sich nichts geöffnet hat, schreib direkt an '+CF.email+'.';d.appendChild(p2)}
  box.appendChild(d);
}
var MAIL=/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

var cf=$('#contactForm');
if(cf){
  var way='mail';
  try{var qt=new URLSearchParams(location.search).get('thema');if(qt&&$('#cTopic').querySelector('option[value="'+qt+'"]'))$('#cTopic').value=qt}catch(e){}
  $('#cWay').addEventListener('click',function(e){
    var b=e.target.closest('button');if(!b)return;way=b.getAttribute('data-v');
    $$('#cWay button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
    $('#callBox').hidden=way!=='call';
    if(way==='call')$('#cPhone').focus();
  });
  var PHONE=/^[+()\d][\d\s()\/.+-]{5,}$/;
  cf.addEventListener('submit',function(e){
    e.preventDefault();var n=$('#cName').value.trim(),m=$('#cMail').value.trim(),msg=$('#cMsg').value.trim(),err=$('#cErr'),ph=$('#cPhone').value.trim();
    if(!n){err.textContent='Bitte gib deinen Namen an.';$('#cName').focus();return}
    if(!MAIL.test(m)){err.textContent='Bitte gib eine gültige E-Mail-Adresse an.';$('#cMail').focus();return}
    if(way==='call'&&!PHONE.test(ph)){err.textContent='Für einen Rückruf brauchen wir deine Telefonnummer.';$('#cPhone').focus();return}
    if(msg.length<5){err.textContent='Schreib uns bitte kurz, worum es geht.';$('#cMsg').focus();return}
    err.textContent='';
    var topic=$('#cTopic').options[$('#cTopic').selectedIndex].text;
    var f=[['Name',n],['E-Mail',m],['Thema',topic],['Antwort gewünscht',way==='call'?'Rückruf':'Per E-Mail']];
    if(way==='call'){f.push(['Telefon',ph]);f.push(['Erreichbar',$('#cWhen').value])}
    f.push(['Nachricht',msg]);
    deliver('Anfrage FindeDeineLeute.de: '+topic,f,function(s){
      if(s==='error'){err.textContent='Das Senden hat nicht geklappt. Bitte versuche es erneut oder schreib uns direkt per E-Mail.';return}
      var tail=way==='call'?'Wir rufen dich unter '+ph+' zurück ('+$('#cWhen').value.toLowerCase()+').':'Wir antworten dir per E-Mail an '+m+'.';
      ok($('#contactBox'),'Danke, '+n.split(' ')[0]+'.',s==='sent'?'Deine Anfrage ist angekommen. '+tail:'Dein Mailprogramm öffnet sich mit der vorbereiteten Anfrage. Sende sie ab, dann melden wir uns bei dir. '+tail,s==='mailto');
    });
  });
}

/* Verzeichnis: jede Änderung filtert sofort */
if($('#grid')){
  var PAGE=24,MODE=$('#grid').getAttribute('data-mode')||'all';
  var S={q:'',cats:[],fmt:MODE==='online'?'online':'',city:'',plat:'',sort:'rec',shown:PAGE};
  var CATS=[['sport','Sport & Fitness'],['outdoor','Outdoor & Natur'],['wellbeing','Wellbeing'],['tanz','Tanz'],['musik','Musik & Chor'],['kunst','Kunst & Handwerk'],['foto','Foto & Film'],['spiele','Brett- & Rollenspiele'],['gaming','Gaming & E-Sport'],['lernen','Bücher & Lernen'],['sprachen','Sprachen & Austausch'],['essen','Essen & Trinken'],['business','Business & Karriere'],['tech','Tech & Code'],['leute','Neue Leute'],['queer','Queer'],['frauen','Frauen'],['familie','Eltern & Familie'],['tiere','Tiere'],['mobil','Mobilität & Rad'],['reisen','Reisen'],['engagement','Umwelt & Engagement'],['studium','Studium']];
  var PLAT={website:'Website',instagram:'Instagram',facebook:'Facebook',meetup:'Meetup',discord:'Discord',telegram:'Telegram',whatsapp:'WhatsApp',reddit:'Reddit',slack:'Slack',signal:'Signal',forum:'Forum',sonstige:'Weitere'};
  var CAT={};CATS.forEach(function(c){CAT[c[0]]=c[1]});
  var C=[],CITIES=[],SLUG={},RANK={},CNT={},BYID={},CATN={},PLATN={};
  var lastFocus=null,TOP=99,showAllCats=false;
  var cardHtml=function(c){
    var place=c.t==='Online'?'Online':c.t+(c.a?' · '+c.a:'');
    var pl=(c.f==='online'||c.p==='meetup'||c.p==='discord'||c.p==='telegram'||c.p==='whatsapp'||c.p==='instagram'||c.p==='facebook')&&c.p&&c.p!=='website'?'<span>'+esc(PLAT[c.p]||c.p)+'</span>':'';
    return '<article class="card">'+saveBtn(c)+'<div class="tag"><span>'+(c.f==='online'?'Online':'Vor Ort')+'</span><span>'+esc(CAT[c.c]||c.c)+'</span>'+pl+'</div>'+
     '<h3><button type="button" data-open="'+c.i+'">'+esc(c.n)+'</button></h3><div class="sub">'+esc(place)+'</div>'+
     '<p class="d">'+esc(c.x)+'</p><div class="note">'+esc(c.w||'')+'</div></article>';
  };
  var robin=function(list){
    var by={},order=[],out=[],i=0,more=true;
    list.forEach(function(c){if(!by[c.t]){by[c.t]=[];order.push(c.t)}by[c.t].push(c)});
    order.sort(function(a,b){return (RANK[a]===undefined?999:RANK[a])-(RANK[b]===undefined?999:RANK[b])});
    while(more){more=false;order.forEach(function(t){if(by[t][i]){out.push(by[t][i]);more=true}});i++}
    return out;
  };
  var base=function(c){return MODE==='online'?c.f==='online':true};
  var chipsHtml=function(){
    var list=CATS.filter(function(c){return CATN[c[0]]}).sort(function(a,b){return CATN[b[0]]-CATN[a[0]]});
    var shownL=showAllCats?list:list.filter(function(c,i){return i<TOP||S.cats.indexOf(c[0])>=0});
    var kn=C.filter(function(c){return match(c,'q')&&isKi(c)}).length;var kon=S.q.trim()&&S.q.trim().split(/\s+/).every(function(w){return KIALIAS.test(w.toLowerCase())});
    var h=(kn||kon?'<button type="button" class="chip topic" data-topic="ki" aria-pressed="'+!!kon+'">KI &amp; AI <i>'+kn+'</i></button>':'')+shownL.map(function(c){return '<button type="button" class="chip" data-cat="'+c[0]+'" aria-pressed="'+(S.cats.indexOf(c[0])>=0)+'">'+esc(c[1])+' <i>'+CATN[c[0]]+'</i></button>'}).join('');
    if(list.length>TOP)h+='<button type="button" class="chip ghost" id="catMore">'+(showAllCats?'Weniger Kategorien':'Alle '+list.length+' Kategorien')+'</button>';
    $('#catChips').innerHTML=h;
  };
  var KIRE=/\b(ki|ai|künstliche intelligenz|machine learning|maschinelles lernen|data science|chatgpt|llms?|deep learning|openai|mlops|prompt\w*|generative)\b/;
  var KIALIAS=/^(ki|ai|a\.i\.|ki-|künstliche|kuenstliche|intelligenz|chatgpt|llm|llms|machine|prompting|openai|mlops)$/;
  var match=function(c,skip){
    if(!base(c))return false;
    if(skip!=='cat'&&S.cats.length&&S.cats.indexOf(c.c)<0)return false;
    if(skip!=='fmt'&&S.fmt&&c.f!==S.fmt)return false;
    if(skip!=='plat'&&S.plat&&c.p!==S.plat)return false;
    if(S.city&&c.t!==S.city&&S.fmt!=='online'&&MODE!=='online')return false;
    var words=skip==='q'?[]:S.q.toLowerCase().split(/\s+/).filter(Boolean);
    if(!words.length)return true;
    var hay=(c.n+' '+c.x+' '+c.g+' '+c.t+' '+c.a+' '+(CAT[c.c]||'')+' '+(PLAT[c.p]||'')+' '+(c.f==='online'?'online':'vor ort')).toLowerCase();
    return words.every(function(w){return KIALIAS.test(w)?KIRE.test(hay):hay.indexOf(w)>=0});
  };
  var isKi=function(c){return KIRE.test((c.n+' '+c.x+' '+c.g).toLowerCase())};
  var sync=function(){
    $('#q').value=S.q;if($('#city'))$('#city').value=S.city;$('#sort').value=S.sort;if($('#plat'))$('#plat').value=S.plat;
    $$('#fmt button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-v')===S.fmt)});
    var cl=$('#cityLink');if(cl){if(S.city&&SLUG[S.city]){cl.hidden=false;cl.href='/'+SLUG[S.city]+'/';cl.textContent='Alle Communities in '+S.city+' ansehen'}else cl.hidden=true}
    try{var p=new URLSearchParams();if(S.q)p.set('q',S.q);if(S.city)p.set('stadt',S.city);if(S.cats.length)p.set('kategorie',S.cats.join(','));if(S.fmt&&MODE!=='online')p.set('format',S.fmt);if(S.plat)p.set('plattform',S.plat);var qs=p.toString();history.replaceState(null,'',location.pathname+(qs?'?'+qs:''))}catch(e){}
  };
  var counts=function(){
    CATN={};PLATN={};
    C.forEach(function(c){
      if(match(c,'cat'))CATN[c.c]=(CATN[c.c]||0)+1;
      if(match(c,'plat')&&c.p)PLATN[c.p]=(PLATN[c.p]||0)+1;
    });
    S.cats.forEach(function(k){if(!CATN[k])CATN[k]=0});
    var ps=$('#plat');
    if(ps){var keep=S.plat;ps.innerHTML='<option value="">Alle Plattformen</option>'+Object.keys(PLAT).filter(function(k){return PLATN[k]||k===keep}).map(function(k){return '<option value="'+k+'">'+PLAT[k]+' ('+(PLATN[k]||0)+')</option>'}).join('');ps.value=keep}
    var pc=$('#platChips');
    if(pc){pc.innerHTML='<button type="button" class="chip" data-plat="" aria-pressed="'+(S.plat==='')+'">Alle</button>'+Object.keys(PLAT).filter(function(k){return PLATN[k]||k===S.plat}).sort(function(a,b){return (PLATN[b]||0)-(PLATN[a]||0)}).map(function(k){return '<button type="button" class="chip" data-plat="'+k+'" aria-pressed="'+(S.plat===k)+'">'+PLAT[k]+' <i>'+(PLATN[k]||0)+'</i></button>'}).join('')}
    chipsHtml();
  };
  var renderGrid=function(){
    sync();counts();
    var words=S.q.trim();
    var list=C.filter(function(c){return match(c)});
    if(S.sort==='az')list=list.slice().sort(function(a,b){return a.n.localeCompare(b.n,'de')});
    else if(!S.city&&!words&&MODE!=='online')list=robin(list);
    else if(MODE==='online')list=list.slice().sort(function(a,b){return b.q-a.q||a.n.localeCompare(b.n,'de')});
    $('#count').textContent=nf(list.length)+(list.length===1?' Community gefunden':' Communities gefunden')+(S.city&&MODE!=='online'?' in '+S.city:'');
    var part=list.slice(0,S.shown);
    $('#grid').innerHTML=part.length?part.map(cardHtml).join(''):'<div class="empty"><h3>Keine Treffer</h3><p>Zu dieser Auswahl gibt es noch keine Community. Probiere einen anderen Begriff oder setze die Filter zurück.</p><button class="btn primary" type="button" id="emptyReset">Filter zurücksetzen</button></div>';
    var more=$('#more');more.hidden=list.length<=S.shown;more.textContent='Mehr anzeigen ('+nf(list.length-S.shown)+' weitere)';
  };
  var change=function(){S.shown=PAGE;renderGrid()};
  var reset=function(){S={q:'',cats:[],fmt:MODE==='online'?'online':'',city:'',plat:'',sort:'rec',shown:PAGE};renderGrid()};
  var openC=function(id){
    var c=BYID[id];if(!c)return;lastFocus=document.activeElement;
    var facts=[['Stadt',c.t==='Online'?'Online':c.t+(c.a?', '+c.a:'')],['Format',c.f==='online'?'Online':'Vor Ort']];
    if(c.p)facts.push(['Plattform',PLAT[c.p]||c.p]);
    facts.push(['Wann',c.w||'Siehe Seite der Community']);
    if(c.m)facts.push(['Größe',c.m]);if(c.v)facts.push(['Zuletzt geprüft',new Date(c.v).toLocaleDateString('de-DE')]);
    var host='';try{host=c.l?new URL(c.l).hostname.replace(/^www\./,''):''}catch(e){}
    $('#modal').innerHTML='<button class="x" type="button" id="mClose" aria-label="Schließen">✕</button>'+
     '<div class="chips"><span class="pill">'+esc(CAT[c.c]||c.c)+'</span><span class="pill '+(c.f==='online'?'on':'off')+'">'+(c.f==='online'?'Online':'Vor Ort')+'</span></div>'+
     '<h2 id="mTitle">'+esc(c.n)+'</h2><p style="color:var(--muted)">'+esc(c.x)+'</p>'+
     '<dl class="facts">'+facts.map(function(f){return '<div><dt>'+f[0]+'</dt><dd>'+esc(f[1])+'</dd></div>'}).join('')+'</dl>'+
     '<p class="note" style="margin-bottom:22px">Angaben stammen aus öffentlichen Quellen und können sich ändern. Aktuelle Termine findest du bei der Community selbst.</p>'+
     '<div class="actions">'+(c.l?'<a class="btn primary" target="_blank" rel="noopener noreferrer" href="'+esc(c.l)+'">Zur Community'+(host?' ('+esc(host)+')':'')+'</a>':'')+
     (SLUG[c.t]?'<a class="btn ghost" href="/'+SLUG[c.t]+'/#c'+c.i+'">Mehr aus '+esc(c.t)+'</a>':'')+'<button class="btn ghost" type="button" id="mClose2">Schließen</button></div>';
    $('#overlay').hidden=false;$('#mClose').focus();
  };
  var closeC=function(){$('#overlay').hidden=true;if(lastFocus&&lastFocus.focus)lastFocus.focus()};
  document.addEventListener('click',function(e){
    var o=e.target.closest('[data-open]');if(o){openC(o.getAttribute('data-open'));return}
    if(e.target.id==='overlay'||e.target.id==='mClose'||e.target.id==='mClose2'){closeC();return}
    if(e.target.id==='emptyReset')reset();
  });
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!$('#overlay').hidden)closeC()});
  fetch('/communities.json').then(function(r){return r.json()}).then(function(j){
    C=j.items;CITIES=j.cities.map(function(c){return c[0]});j.cities.forEach(function(c,i){SLUG[c[0]]=c[1];RANK[c[0]]=i});
    C.forEach(function(c){CNT[c.t]=(CNT[c.t]||0)+1;BYID[c.i]=c});
    if($('#city'))$('#city').innerHTML='<option value="">Alle Städte</option>'+CITIES.map(function(n){return '<option value="'+esc(n)+'">'+esc(n)+' ('+(CNT[n]||0)+')</option>'}).join('');
    try{var p=new URLSearchParams(location.search);S.q=p.get('q')||'';S.city=p.get('stadt')||'';S.cats=(p.get('kategorie')||'').split(',').filter(function(k){return CAT[k]});if(MODE!=='online')S.fmt=p.get('format')||'';S.plat=p.get('plattform')||''}catch(e){}
    if(S.city&&CITIES.indexOf(S.city)<0)S.city='';
    if(S.plat&&!PLAT[S.plat])S.plat='';
    renderGrid();
  }).catch(function(){$('#count').textContent='Das Verzeichnis konnte nicht geladen werden. Bitte lade die Seite neu.'});
  $('#q').addEventListener('input',function(){S.q=this.value;change()});
  if($('#city'))$('#city').addEventListener('change',function(){S.city=this.value;change()});
  $('#sort').addEventListener('change',function(){S.sort=this.value;change()});
  if($('#plat'))$('#plat').addEventListener('change',function(){S.plat=this.value;change()});
  if($('#platChips'))$('#platChips').addEventListener('click',function(e){var b=e.target.closest('[data-plat]');if(!b)return;S.plat=b.getAttribute('data-plat');change()});
  if($('#fmt'))$('#fmt').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;S.fmt=b.getAttribute('data-v');change()});
  $('#catChips').addEventListener('click',function(e){
    if(e.target.id==='catMore'){showAllCats=!showAllCats;chipsHtml();return}
    var tp=e.target.closest('[data-topic]');if(tp){S.q=tp.getAttribute('aria-pressed')==='true'?'':'KI';change();return}
    var b=e.target.closest('[data-cat]');if(!b)return;var k=b.getAttribute('data-cat'),ix=S.cats.indexOf(k);
    if(ix>=0)S.cats.splice(ix,1);else S.cats.push(k);change();
  });
  $('#reset').addEventListener('click',reset);
  $('#more').addEventListener('click',function(){S.shown+=PAGE;renderGrid()});
  $('#q').form&&$('#q').form.addEventListener('submit',function(e){e.preventDefault()});
}
/* Startseite: Stadtwahl sofort anwenden */
var hs=$('.hero form.search select');
if(hs)hs.addEventListener('change',function(){this.form.submit()});

/* Lebendigkeit: Einblenden, Zähler, Karussell, Filter mobil */
(function(){
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var rv=$$('.reveal');
if('IntersectionObserver' in window&&!reduce){
  rv.forEach(function(e){e.classList.add('rv-on')});
  var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
  rv.forEach(function(e){io.observe(e)});
}
var cn=$('[data-count]');
if(cn&&!reduce){var T=+cn.getAttribute('data-count'),t0=null;function st(t){if(!t0)t0=t;var p=Math.min((t-t0)/1100,1),v=Math.round(T*(1-Math.pow(1-p,3)));cn.textContent=nf(v);if(p<1)requestAnimationFrame(st)}requestAnimationFrame(st)}
var rail=$('#rail');
if(rail){$$('.rail-btn').forEach(function(b){b.addEventListener('click',function(){rail.scrollBy({left:(+b.getAttribute('data-dir'))*Math.max(rail.clientWidth*.8,280),behavior:reduce?'auto':'smooth'})})})}
var ft=$('#fToggle'),fl=$('#filters');
if(ft&&fl){ft.addEventListener('click',function(){var o=fl.classList.toggle('open');ft.setAttribute('aria-expanded',o);ft.textContent=o?'Filter ausblenden':'Filter anzeigen'})}
})();

/* ===== Merkliste ===== */
var SK='fdl_saved';
var HEART='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7.5-4.6-9.6-9.2C1 8.6 2.8 5 6.2 5c2 0 3.4 1.1 4.1 2.3L12 9.6l1.7-2.3C14.4 6.1 15.8 5 17.8 5c3.4 0 5.2 3.6 3.8 6.8C19.5 16.4 12 21 12 21Z"/></svg>';
function getSaved(){try{var a=JSON.parse(localStorage.getItem(SK)||'[]');return Array.isArray(a)?a:[]}catch(e){return[]}}
function putSaved(a){try{localStorage.setItem(SK,JSON.stringify(a))}catch(e){}}
function saveBtn(c){return '<button type="button" class="save" data-save="'+esc(c.k||'')+'" aria-pressed="false" aria-label="'+esc(c.n)+' merken">'+HEART+'</button>'}
var toastT;
function toast(msg,link){var t=$('#toast');if(!t){t=document.createElement('div');t.id='toast';t.className='toast';t.setAttribute('role','status');document.body.appendChild(t)}
  t.innerHTML=esc(msg)+(link?' <a href="'+link[1]+'">'+esc(link[0])+'</a>':'');t.classList.add('on');clearTimeout(toastT);toastT=setTimeout(function(){t.classList.remove('on')},3200)}
function syncSaved(){var s=getSaved();
  $$('[data-save]').forEach(function(b){b.setAttribute('aria-pressed',s.indexOf(b.getAttribute('data-save'))>-1?'true':'false')});
  var n=$('#savedCount');if(n){n.textContent=s.length?String(s.length):''}
  var l=$('.saved-link');if(l)l.classList.toggle('has',s.length>0)}
document.addEventListener('click',function(e){
  var b=e.target.closest('[data-save]');if(!b)return;e.preventDefault();e.stopPropagation();
  var k=b.getAttribute('data-save');if(!k)return;var s=getSaved(),i=s.indexOf(k);
  if(i>-1){s.splice(i,1);putSaved(s);toast('Von der Merkliste entfernt')}else{s.push(k);putSaved(s);toast('Auf deiner Merkliste',['Ansehen','/merkliste/'])}
  syncSaved();if(window.__mlRender)window.__mlRender();
},true);
syncSaved();
var gr=$('#grid');if(gr&&window.MutationObserver){new MutationObserver(syncSaved).observe(gr,{childList:true})}

/* ===== Kalender-Logik ===== */
var DOW=['Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag'],BYD=['MO','TU','WE','TH','FR','SA','SU'];
function dim(d){return new Date(d.getFullYear(),d.getMonth()+1,0).getDate()}
function matches(sc,d){var wd=(d.getDay()+6)%7;if(wd!==sc.d)return false;if(!sc.o.length)return true;
  var n=Math.floor((d.getDate()-1)/7)+1,last=d.getDate()+7>dim(d);return sc.o.indexOf(n)>-1||(sc.o.indexOf(-1)>-1&&last)}
function p2(n){return (n<10?'0':'')+n}
function ymd(d){return d.getFullYear()+p2(d.getMonth()+1)+p2(d.getDate())}
function occurrences(items,from,days){var out=[];for(var i=0;i<days;i++){var d=new Date(from.getFullYear(),from.getMonth(),from.getDate()+i);
  items.forEach(function(it){it.sc.forEach(function(sc){if(matches(sc,d))out.push({d:d,it:it,sc:sc})})})}
  out.sort(function(a,b){return a.d-b.d||(a.sc.t||'99').localeCompare(b.sc.t||'99')||a.it.n.localeCompare(b.it.n)});return out}
function dayLabel(d,today){var diff=Math.round((d-today)/864e5);var base=DOW[(d.getDay()+6)%7]+', '+d.getDate()+'. '+['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'][d.getMonth()];return {t:base,today:diff===0,tom:diff===1}}
function icsFor(it,sc){var first=null,t0=new Date();t0=new Date(t0.getFullYear(),t0.getMonth(),t0.getDate());
  for(var i=0;i<62&&!first;i++){var d=new Date(t0.getFullYear(),t0.getMonth(),t0.getDate()+i);if(matches(sc,d))first=d}
  if(!first)return null;
  var rule=sc.o.length?'FREQ=MONTHLY;BYDAY='+sc.o.map(function(n){return n+BYD[sc.d]}).join(','):'FREQ=WEEKLY;BYDAY='+BYD[sc.d];
  var ds,de;if(sc.t){var h=+sc.t.slice(0,2),m=sc.t.slice(3);ds='DTSTART:'+ymd(first)+'T'+p2(h)+m+'00';de='DTEND:'+ymd(first)+'T'+p2((h+1)%24)+m+'00'}
  else{var nx=new Date(first.getFullYear(),first.getMonth(),first.getDate()+1);ds='DTSTART;VALUE=DATE:'+ymd(first);de='DTEND;VALUE=DATE:'+ymd(nx)}
  function e2(s){return String(s).replace(/([,;\\])/g,'\\$1').replace(/\n/g,'\\n')}
  var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//FindeDeineLeute.de//DE','CALSCALE:GREGORIAN','BEGIN:VEVENT','UID:'+it.k+'-'+sc.d+'-'+sc.t+'@findedeineleute.de','DTSTAMP:'+ymd(new Date())+'T000000Z',ds,de,'RRULE:'+rule,'SUMMARY:'+e2(it.n),'DESCRIPTION:'+e2('Zeiten laut Verzeichnis: '+it.w+'. Bitte vorab bei der Community prüfen. '+(it.l||'https://findedeineleute.de/')),it.l?'URL:'+it.l:'','END:VEVENT','END:VCALENDAR'].filter(Boolean);
  return L.join('\r\n')}
function dlIcs(it,sc){var s=icsFor(it,sc);if(!s)return;var b=new Blob([s],{type:'text/calendar;charset=utf-8'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download=it.n.replace(/[^\w\-]+/g,'_').slice(0,40)+'.ics';document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(u);a.remove()},500)}
var CALIDX=[];
function calHtml(occ,today,showCity){if(!occ.length)return '<p class="note">In diesem Zeitraum sind keine festen Termine eingetragen.</p>';
  var days=[],cur=null;occ.forEach(function(o){var k=ymd(o.d);if(!cur||cur.k!==k){cur={k:k,d:o.d,l:[]};days.push(cur)}cur.l.push(o)});
  return days.map(function(g){var lb=dayLabel(g.d,today);
    return '<div class="cal-day"><h2>'+lb.t+(lb.today?' <span class="today">Heute</span>':lb.tom?' <span class="today">Morgen</span>':'')+'</h2>'+
    g.l.map(function(o){CALIDX.push(o);var i=CALIDX.length-1,it=o.it;
      return '<div class="cal-item"><time>'+(o.sc.t||'')+'</time><div><div class="nm">'+esc(it.n)+'</div><div class="sb">'+(showCity?esc(it.t)+' · ':'')+esc(it.w)+(it.a?' · '+esc(it.a):'')+'</div></div><div class="cal-actions">'+(it.l?'<a class="btn ghost sm" target="_blank" rel="noopener noreferrer" href="'+esc(it.l)+'">Zur Community</a>':'')+'<button type="button" class="btn ghost sm" data-ics="'+i+'">In Kalender</button>'+saveBtn(it)+'</div></div>'}).join('')+'</div>'}).join('')}
document.addEventListener('click',function(e){var b=e.target.closest('[data-ics]');if(!b)return;var o=CALIDX[+b.getAttribute('data-ics')];if(o){dlIcs(o.it,o.sc);toast('Kalenderdatei geladen')}});
/* Kalender-Seite */
var cb=$('#calBox');
if(cb){var CAL=[],RNG=7,SLUGBYCITY={};
  var today=new Date();today=new Date(today.getFullYear(),today.getMonth(),today.getDate());
  var calRender=function(){CALIDX=[];var sl=$('#calCity').value,items=CAL.filter(function(x){return !sl||x.slug===sl});
    cb.innerHTML=calHtml(occurrences(items,today,RNG),today,!sl);syncSaved();
    try{var u=new URL(location.href);if(sl)u.searchParams.set('stadt',sl);else u.searchParams.delete('stadt');history.replaceState(null,'',u)}catch(e){}};
  fetch('/calendar.json').then(function(r){return r.json()}).then(function(j){
    CAL=j.items;
    var q=new URLSearchParams(location.search).get('stadt');if(q&&$('#calCity option[value="'+q+'"]'))$('#calCity').value=q;
    calRender()}).catch(function(){cb.innerHTML='<p class="err">Der Kalender konnte nicht geladen werden. Bitte lade die Seite neu.</p>'});
  $('#calCity').addEventListener('change',calRender);
  $$('#calRange button').forEach(function(b){b.addEventListener('click',function(){RNG=+b.getAttribute('data-v');$$('#calRange button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});calRender()})});
}
/* Stadtseite: Diese Woche */
var wb=$('#woche');
if(wb){try{var wd=JSON.parse($('#weekData').textContent),td=new Date();td=new Date(td.getFullYear(),td.getMonth(),td.getDate());
  var oc=occurrences(wd,td,7);if(oc.length){$('#weekList').innerHTML=calHtml(oc,td,false);wb.hidden=false;syncSaved()}}catch(e){}}

/* ===== Merkliste-Seite ===== */
var mg=$('#mlGrid');
if(mg){var ALL=null,shared=null;
  try{var lp=new URLSearchParams(location.search).get('l');if(lp)shared=lp.split(',').filter(Boolean).slice(0,200)}catch(e){}
  var mlRender=function(){if(!ALL)return;var keys=shared||getSaved(),by={};ALL.items.forEach(function(c){by[c.k]=c});
    var list=keys.map(function(k){return by[k]}).filter(Boolean),sm={};ALL.cities.forEach(function(c){sm[c[0]]=c[1]});
    var ban=$('#mlBanner'),bar=$('#mlBar');
    ban.innerHTML=shared?'<div class="banner"><span><b>Jemand hat dir eine Liste geschickt.</b> '+list.length+' Communities.</span><button type="button" class="btn primary sm" id="mlTake">Alle auf meine Merkliste</button></div>':'';
    if(!list.length){mg.innerHTML='<div class="empty"><h3>Noch nichts gemerkt</h3><p>Tippe bei einer Community auf das Herz, dann siehst du sie hier.</p><a class="btn primary" href="/entdecken/">Communities entdecken</a></div>';bar.hidden=true;return}
    mg.innerHTML=list.map(function(c){var place=c.t==='Online'?'Online':c.t+(c.a?' · '+c.a:'');
      return '<article class="card">'+saveBtn(c)+'<div class="tag"><span>'+(c.f==='online'?'Online':'Vor Ort')+'</span><span>'+esc(c.t)+'</span></div><h3>'+(c.l?'<a target="_blank" rel="noopener noreferrer" href="'+esc(c.l)+'">'+esc(c.n)+'</a>':esc(c.n))+'</h3><div class="sub">'+esc(place)+'</div><p class="d">'+esc(c.x)+'</p>'+(c.w?'<div class="note">'+esc(c.w)+'</div>':'')+(sm[c.t]?'<div class="note"><a href="/'+sm[c.t]+'/#c'+c.i+'">Mehr aus '+esc(c.t)+'</a></div>':'')+'</article>'}).join('');
    var url=location.origin+'/merkliste/?l='+list.map(function(c){return c.k}).join(',');
    bar.hidden=false;bar.innerHTML=(shared?'':'')+'<button type="button" class="btn primary sm" id="mlCopy">Link kopieren</button><a class="btn ghost sm" target="_blank" rel="noopener noreferrer" href="https://wa.me/?text='+encodeURIComponent('Das sind Communities, die ich bei FindeDeineLeute.de gefunden habe: '+url)+'">Per WhatsApp teilen</a><a class="btn ghost sm" href="mailto:?subject='+encodeURIComponent('Communities für uns')+'&body='+encodeURIComponent('Schau mal, die habe ich bei FindeDeineLeute.de gefunden:\n'+url)+'">Per E-Mail</a>'+(navigator.share?'<button type="button" class="btn ghost sm" id="mlShare">Teilen</button>':'')+(shared?'':'<button type="button" class="btn ghost sm" id="mlClear">Liste leeren</button>');
    $('#mlCopy').onclick=function(){if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(url).then(function(){toast('Link kopiert')},function(){prompt('Link kopieren:',url)})}else{prompt('Link kopieren:',url)}};
    var sh=$('#mlShare');if(sh)sh.onclick=function(){navigator.share({title:'Meine Communities',url:url}).catch(function(){})};
    var cl=$('#mlClear');if(cl)cl.onclick=function(){putSaved([]);syncSaved();mlRender()};
    var tk=$('#mlTake');if(tk)tk.onclick=function(){var s=getSaved();keys.forEach(function(k){if(s.indexOf(k)<0)s.push(k)});putSaved(s);shared=null;history.replaceState(null,'','/merkliste/');syncSaved();mlRender();toast('Zur Merkliste hinzugefügt')};
    syncSaved()};
  window.__mlRender=function(){if(!shared)mlRender()};
  fetch('/communities.json').then(function(r){return r.json()}).then(function(j){ALL=j;mlRender()}).catch(function(){mg.innerHTML='<p class="err">Die Merkliste konnte nicht geladen werden. Bitte lade die Seite neu.</p>'});
}

/* ===== Newsletter ===== */
var nf2=$('#nlForm');
if(nf2){nf2.addEventListener('submit',function(e){e.preventDefault();var m=$('#nlMail').value.trim(),er=$('#nlErr');er.textContent='';
  if(!MAIL.test(m)){er.textContent='Bitte gib eine gültige E-Mail-Adresse ein.';return}
  if(!$('#nlOk').checked){er.textContent='Bitte stimme dem Erhalt des Newsletters zu.';return}
  deliver('Newsletter-Anmeldung',[['E-Mail',m],['Stadt',$('#nlCity').value||'keine Angabe'],['Einwilligung','Ja, ich möchte den Newsletter erhalten und habe die Datenschutzerklärung gelesen.']],function(s){
    ok($('#nlBox'),s==='error'?'Das hat nicht geklappt':'Fast geschafft',s==='error'?'Bitte schreib uns direkt eine E-Mail.':'Sende die vorbereitete E-Mail ab. Wir tragen dich ein und bestätigen kurz.',s==='mailto')})})}
})();
