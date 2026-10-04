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
if(cf)cf.addEventListener('submit',function(e){
  e.preventDefault();var n=$('#cName').value.trim(),m=$('#cMail').value.trim(),msg=$('#cMsg').value.trim(),err=$('#cErr');
  if(!n){err.textContent='Bitte gib deinen Namen an.';$('#cName').focus();return}
  if(!MAIL.test(m)){err.textContent='Bitte gib eine gültige E-Mail-Adresse an.';$('#cMail').focus();return}
  if(msg.length<5){err.textContent='Schreib uns bitte kurz, worum es geht.';$('#cMsg').focus();return}
  err.textContent='';
  deliver('Kontakt CommunityFinder.de: '+$('#cTopic').value,[['Name',n],['E-Mail',m],['Thema',$('#cTopic').value],['Nachricht',msg]],function(s){
    if(s==='error'){err.textContent='Das Senden hat nicht geklappt. Bitte versuche es erneut oder schreib uns direkt per E-Mail.';return}
    ok($('#contactBox'),'Danke, '+n.split(' ')[0]+'.',s==='sent'?'Deine Nachricht ist angekommen. Wir melden uns bei dir unter '+m+'.':'Dein Mailprogramm öffnet sich mit der vorbereiteten Nachricht. Sende sie ab, dann melden wir uns bei dir.',s==='mailto');
  });
});

/* Terminwunsch */
var bf=$('#bookForm');
if(bf){
  var TYPES=[
   {id:'orientierung',n:'Orientierung für dich',d:'20 Min. · Wir finden gemeinsam passende Communities.'},
   {id:'eintragen',n:'Community eintragen',d:'30 Min. · Du stellst deine Gruppe vor, wir legen den Eintrag an.'},
   {id:'kooperation',n:'Kooperation oder Presse',d:'20 Min. · Für Partner, Vereine und Medien.'}];
  var TIMES=['09:30','11:00','13:30','15:00','16:30','18:00'];
  var B={type:'orientierung',date:null,time:null,days:12};
  try{var qt=new URLSearchParams(location.search).get('anliegen');if(qt&&TYPES.some(function(t){return t.id===qt}))B.type=qt}catch(e){}
  var dkey=function(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')};
  var weekdays=function(n){var out=[],d=new Date();d.setHours(12,0,0,0);d.setDate(d.getDate()+1);while(out.length<n){if(d.getDay()!==0&&d.getDay()!==6)out.push(new Date(d));d.setDate(d.getDate()+1)}return out};
  var render=function(){
    $('#types').innerHTML=TYPES.map(function(t){return '<button type="button" class="type" data-t="'+t.id+'" aria-pressed="'+(B.type===t.id)+'"><div><b>'+t.n+'</b><span>'+t.d+'</span></div></button>'}).join('');
    $('#days').innerHTML=weekdays(B.days).map(function(d){var k=dkey(d);return '<button type="button" class="day" data-d="'+k+'" aria-pressed="'+(B.date===k)+'"><small>'+d.toLocaleDateString('de-DE',{weekday:'short'})+'</small><strong>'+d.getDate()+'</strong><small>'+d.toLocaleDateString('de-DE',{month:'short'})+'</small></button>'}).join('');
    $('#times').innerHTML=B.date?TIMES.map(function(t){return '<button type="button" class="time" data-tm="'+t+'" aria-pressed="'+(B.time===t)+'">'+t+' Uhr</button>'}).join(''):'<p class="note">Wähle zuerst einen Tag, dann kannst du eine Uhrzeit vorschlagen.</p>';
    var ty=TYPES.filter(function(t){return t.id===B.type})[0];$('#sType').textContent=ty.n;
    var dEl=$('#sDate'),tEl=$('#sTime');
    if(B.date){var p=B.date.split('-');dEl.textContent=new Date(p[0],p[1]-1,p[2]).toLocaleDateString('de-DE',{weekday:'long',day:'numeric',month:'long',year:'numeric'});dEl.className=''}else{dEl.textContent='Noch nicht gewählt';dEl.className='empty-v'}
    if(B.time){tEl.textContent=B.time+' Uhr';tEl.className=''}else{tEl.textContent='Noch nicht gewählt';tEl.className='empty-v'}
  };
  $('#types').addEventListener('click',function(e){var b=e.target.closest('[data-t]');if(b){B.type=b.getAttribute('data-t');render()}});
  $('#days').addEventListener('click',function(e){var b=e.target.closest('[data-d]');if(b){B.date=b.getAttribute('data-d');render()}});
  $('#times').addEventListener('click',function(e){var b=e.target.closest('[data-tm]');if(b){B.time=b.getAttribute('data-tm');render()}});
  $('#moreDays').addEventListener('click',function(){B.days+=10;render()});
  bf.addEventListener('submit',function(e){
    e.preventDefault();var err=$('#bErr'),n=$('#bName').value.trim(),m=$('#bMail').value.trim();
    if(!B.date||!B.time){err.textContent='Bitte wähle einen Tag und eine Uhrzeit.';return}
    if(!n){err.textContent='Bitte gib deinen Namen an.';$('#bName').focus();return}
    if(!MAIL.test(m)){err.textContent='Bitte gib eine gültige E-Mail-Adresse an, damit wir dir den Termin bestätigen können.';$('#bMail').focus();return}
    err.textContent='';
    var ty=TYPES.filter(function(t){return t.id===B.type})[0],p=B.date.split('-');
    var ds=new Date(p[0],p[1]-1,p[2]).toLocaleDateString('de-DE',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
    deliver('Terminwunsch CommunityFinder.de: '+ty.n,[['Name',n],['E-Mail',m],['Anliegen',ty.n],['Wunschtermin',ds+', '+B.time+' Uhr'],['Nachricht',$('#bMsg').value.trim()]],function(s){
      if(s==='error'){err.textContent='Das Senden hat nicht geklappt. Bitte versuche es erneut oder schreib uns direkt per E-Mail.';return}
      ok($('#bookBox'),'Dein Terminwunsch ist vorbereitet, '+n.split(' ')[0]+'.',s==='sent'?ty.n+', '+ds+' um '+B.time+' Uhr. Wir bestätigen den Termin per E-Mail an '+m+'.':'Dein Mailprogramm öffnet sich mit dem Terminwunsch ('+ty.n+', '+ds+' um '+B.time+' Uhr). Sende die Nachricht ab, dann bestätigen wir den Termin per E-Mail.',s==='mailto');
    });
  });
  render();
}

/* Verzeichnis */
if($('#grid')){
  var PAGE=24,S={q:'',cat:'',fmt:'',city:'',sort:'rec',shown:PAGE};
  var CATS=[['sport','Sport & Outdoor'],['wellbeing','Wellbeing'],['kultur','Kultur & Kreativ'],['spiele','Spiele'],['lernen','Bücher & Lernen'],['essen','Essen & Trinken'],['business','Business & Tech'],['leute','Neue Leute'],['queer','Queer'],['engagement','Engagement & Stadt']];
  var CAT={};CATS.forEach(function(c){CAT[c[0]]=c[1]});
  var C=[],CITIES=[],SLUG={},RANK={},CNT={},BYID={};
  var lastFocus=null;
  var cardHtml=function(c){
    var place=c.t==='Online'?'Online':c.t+(c.a&&c.s!=='criticalmass.de'?' · '+c.a:'');
    return '<article class="card"><div class="tile" aria-hidden="true"><em>'+(c.f==='online'?'Online':'Vor Ort')+'</em><span>'+esc(c.n.charAt(0))+'</span></div>'+
     '<div><h3><button type="button" data-open="'+c.i+'">'+esc(c.n)+'</button></h3><div class="sub">'+esc(CAT[c.c]+' · '+place)+'</div></div>'+
     '<p class="d">'+esc(c.x)+'</p><div class="note">'+esc((c.w?c.w+' · ':'')+'Quelle: '+c.s.split(',')[0])+'</div></article>';
  };
  var robin=function(list){
    var by={},order=[],out=[],i=0,more=true;
    list.forEach(function(c){if(!by[c.t]){by[c.t]=[];order.push(c.t)}by[c.t].push(c)});
    order.sort(function(a,b){return (RANK[a]===undefined?999:RANK[a])-(RANK[b]===undefined?999:RANK[b])});
    while(more){more=false;order.forEach(function(t){if(by[t][i]){out.push(by[t][i]);more=true}});i++}
    return out;
  };
  var sync=function(){
    $('#q').value=S.q;$('#city').value=S.city;$('#sort').value=S.sort;
    $$('#catChips .chip').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-cat')===S.cat)});
    $$('#fmt button').forEach(function(b){b.setAttribute('aria-pressed',b.getAttribute('data-v')===S.fmt)});
    var cl=$('#cityLink');if(S.city&&SLUG[S.city]){cl.hidden=false;cl.href='/'+SLUG[S.city]+'/';cl.textContent='Alle Communities in '+S.city+' ansehen'}else cl.hidden=true;
    try{var p=new URLSearchParams();if(S.q)p.set('q',S.q);if(S.city)p.set('stadt',S.city);if(S.cat)p.set('kategorie',S.cat);if(S.fmt)p.set('format',S.fmt);var qs=p.toString();history.replaceState(null,'',location.pathname+(qs?'?'+qs:''))}catch(e){}
  };
  var renderGrid=function(){
    sync();
    var words=S.q.toLowerCase().split(/\s+/).filter(Boolean);
    var list=C.filter(function(c){
      if(S.cat&&c.c!==S.cat)return false;
      if(S.fmt&&c.f!==S.fmt)return false;
      if(S.city&&c.t!==S.city&&S.fmt!=='online')return false;
      if(!words.length)return true;
      var hay=(c.n+' '+c.x+' '+c.g+' '+c.t+' '+c.a+' '+CAT[c.c]+' '+(c.f==='online'?'online':'vor ort')).toLowerCase();
      return words.every(function(w){return hay.indexOf(w)>=0});
    });
    if(S.sort==='az')list=list.slice().sort(function(a,b){return a.n.localeCompare(b.n,'de')});
    else if(!S.city&&!words.length)list=robin(list);
    $('#count').textContent=nf(list.length)+(list.length===1?' Community gefunden':' Communities gefunden')+(S.city?' in '+S.city:'');
    var part=list.slice(0,S.shown);
    $('#grid').innerHTML=part.length?part.map(cardHtml).join(''):'<div class="empty"><h3>Keine Treffer</h3><p>Zu dieser Auswahl gibt es noch keine Community. Probiere einen anderen Begriff, eine andere Stadt oder setze die Filter zurück.</p><button class="btn primary" type="button" id="emptyReset">Filter zurücksetzen</button></div>';
    var more=$('#more');more.hidden=list.length<=S.shown;more.textContent='Mehr anzeigen ('+nf(list.length-S.shown)+' weitere)';
  };
  var change=function(){S.shown=PAGE;renderGrid()};
  var reset=function(){S={q:'',cat:'',fmt:'',city:'',sort:'rec',shown:PAGE};renderGrid()};
  var openC=function(id){
    var c=BYID[id];if(!c)return;lastFocus=document.activeElement;
    var facts=[['Stadt',c.t==='Online'?'Online':c.t+(c.a?', '+c.a:'')],['Format',c.f==='online'?'Online':'Vor Ort'],['Wann',c.w||'Siehe Webseite der Community']];
    if(c.m)facts.push(['Größe',c.m]);facts.push(['Quelle',c.s]);
    var host='';try{host=c.l?new URL(c.l).hostname.replace(/^www\./,''):''}catch(e){}
    $('#modal').innerHTML='<button class="x" type="button" id="mClose" aria-label="Schließen">✕</button>'+
     '<div class="chips"><span class="pill">'+esc(CAT[c.c])+'</span><span class="pill '+(c.f==='online'?'on':'off')+'">'+(c.f==='online'?'Online':'Vor Ort')+'</span></div>'+
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
    $('#city').innerHTML='<option value="">Alle Städte</option>'+CITIES.map(function(n){return '<option value="'+esc(n)+'">'+esc(n)+' ('+(CNT[n]||0)+')</option>'}).join('');
    $('#catChips').innerHTML=CATS.map(function(c){return '<button type="button" class="chip" data-cat="'+c[0]+'" aria-pressed="false">'+esc(c[1])+'</button>'}).join('');
    try{var p=new URLSearchParams(location.search);S.q=p.get('q')||'';S.city=p.get('stadt')||'';S.cat=p.get('kategorie')||'';S.fmt=p.get('format')||''}catch(e){}
    if(S.city&&CITIES.indexOf(S.city)<0)S.city='';
    if(S.cat&&!CAT[S.cat])S.cat='';
    renderGrid();
  }).catch(function(){$('#count').textContent='Das Verzeichnis konnte nicht geladen werden. Bitte lade die Seite neu.'});
  $('#q').addEventListener('input',function(){S.q=this.value;change()});
  $('#city').addEventListener('change',function(){S.city=this.value;change()});
  $('#sort').addEventListener('change',function(){S.sort=this.value;change()});
  $('#fmt').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;S.fmt=b.getAttribute('data-v');change()});
  $('#catChips').addEventListener('click',function(e){var b=e.target.closest('[data-cat]');if(!b)return;S.cat=(S.cat===b.getAttribute('data-cat'))?'':b.getAttribute('data-cat');change()});
  $('#reset').addEventListener('click',reset);
  $('#more').addEventListener('click',function(){S.shown+=PAGE;renderGrid()});
}
})();
