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
    return '<article class="card"><div class="tag"><span>'+(c.f==='online'?'Online':'Vor Ort')+'</span><span>'+esc(CAT[c.c]||c.c)+'</span>'+pl+'</div>'+
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
    var h=shownL.map(function(c){return '<button type="button" class="chip" data-cat="'+c[0]+'" aria-pressed="'+(S.cats.indexOf(c[0])>=0)+'">'+esc(c[1])+' <i>'+CATN[c[0]]+'</i></button>'}).join('');
    if(list.length>TOP)h+='<button type="button" class="chip ghost" id="catMore">'+(showAllCats?'Weniger Kategorien':'Alle '+list.length+' Kategorien')+'</button>';
    $('#catChips').innerHTML=h;
  };
  var match=function(c,skip){
    if(!base(c))return false;
    if(skip!=='cat'&&S.cats.length&&S.cats.indexOf(c.c)<0)return false;
    if(skip!=='fmt'&&S.fmt&&c.f!==S.fmt)return false;
    if(skip!=='plat'&&S.plat&&c.p!==S.plat)return false;
    if(S.city&&c.t!==S.city&&S.fmt!=='online'&&MODE!=='online')return false;
    var words=S.q.toLowerCase().split(/\s+/).filter(Boolean);
    if(!words.length)return true;
    var hay=(c.n+' '+c.x+' '+c.g+' '+c.t+' '+c.a+' '+(CAT[c.c]||'')+' '+(PLAT[c.p]||'')+' '+(c.f==='online'?'online':'vor ort')).toLowerCase();
    return words.every(function(w){return hay.indexOf(w)>=0});
  };
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
})();
