/* Einwilligungs-Banner. Aktuell gibt es keine einwilligungspflichtigen Dienste.
   Neue Dienste (z. B. Statistik) werden ueber window.CF_CONSENT.onGrant('statistik', fn) angebunden und laufen erst nach Zustimmung. */
(function(){
  var KEY='fdl_consent',VER=1,cats={statistik:false};
  function read(){try{var v=JSON.parse(localStorage.getItem(KEY));return v&&v.v===VER?v:null}catch(e){return null}}
  function save(c){try{localStorage.setItem(KEY,JSON.stringify({v:VER,c:c,t:Date.now()}))}catch(e){}}
  var hooks=[];
  window.CF_CONSENT={get:function(k){var s=read();return !!(s&&s.c[k])},
    onGrant:function(k,fn){if(this.get(k))fn();else hooks.push([k,fn])},open:function(){show(true)}};
  function apply(c){cats=c;hooks=hooks.filter(function(h){if(c[h[0]]){try{h[1]()}catch(e){}return false}return true})}
  var box;
  function close(){if(box){box.remove();box=null}}
  function choose(c){save(c);apply(c);close()}
  function show(force){
    if(box)return;
    var s=read();if(s&&!force)return;
    box=document.createElement('div');box.className='consent';box.setAttribute('role','dialog');box.setAttribute('aria-label','Datenschutz-Einstellungen');
    var cur=s?s.c:cats;
    box.innerHTML='<div class="consent-in"><h2>Deine Privatsphäre</h2>'+
      '<p>Diese Seite funktioniert ohne Tracking. Notwendig ist nur, was du selbst nutzt, etwa deine Merkliste. Optional können wir anonyme Statistik messen, um die Seite zu verbessern. Du entscheidest, und kannst es jederzeit im Footer ändern. Mehr in der <a href="/datenschutz/">Datenschutzerklärung</a>.</p>'+
      '<details class="consent-set"><summary>Einstellungen</summary>'+
      '<label class="check"><input type="checkbox" checked disabled> <span><b>Notwendig</b><br>Merkliste und diese Auswahl. Wird nur lokal in deinem Browser gespeichert.</span></label>'+
      '<label class="check"><input type="checkbox" id="cStat"'+(cur.statistik?' checked':'')+'> <span><b>Statistik</b><br>Anonyme Reichweitenmessung. Aktuell nicht aktiv, die Einstellung gilt für spätere Messung.</span></label>'+
      '<button type="button" class="btn" id="cSave">Auswahl speichern</button></details>'+
      '<div class="consent-btns"><button type="button" class="btn ghost" id="cNo">Nur notwendige</button><button type="button" class="btn" id="cAll">Alle akzeptieren</button></div></div>';
    document.body.appendChild(box);
    box.querySelector('#cNo').onclick=function(){choose({statistik:false})};
    box.querySelector('#cAll').onclick=function(){choose({statistik:true})};
    box.querySelector('#cSave').onclick=function(){choose({statistik:box.querySelector('#cStat').checked})};
    box.querySelector('#cNo').focus&&0;
  }
  var s=read();if(s)apply(s.c);
  document.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('[data-consent-open]');if(t){e.preventDefault();show(true)}});
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){show()});else show();
})();
