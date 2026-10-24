/* FindeDeineLeute.de: einzelne Events aus /assets/events.json im Kalender und auf Stadtseiten */
(function(){
"use strict";
var MON=["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"],DOW=["Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag"];
function esc(s){return String(s==null?"":s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
function p2(n){return (n<10?"0":"")+n;}
function pd(s){var a=s.split("-");return new Date(+a[0],+a[1]-1,+a[2]);}
function ymd(d){return d.getFullYear()+p2(d.getMonth()+1)+p2(d.getDate());}
var css='.evbox{margin:0 0 40px}.evbox>h2{margin:0 0 6px}.evbox .evsub{margin:0 0 18px;opacity:.7;font-size:.95rem}'
+'.evtop{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}.evtop a{display:inline-flex;gap:6px;align-items:center;padding:7px 12px;border:1px solid rgba(0,0,0,.12);border-radius:999px;background:#fff;color:inherit;text-decoration:none;font-size:.85rem}.evtop a b{color:#c2185b}'
+'.evtag{display:inline-block;margin-left:8px;padding:2px 8px;border-radius:999px;background:rgba(194,24,91,.1);color:#c2185b;font-size:.72rem;font-weight:600;vertical-align:middle}'
+'.evtag.run{background:rgba(43,143,214,.12);color:#1f6fae}'
+'.evbox .cal-item time{min-width:52px}';
function ics(e){var d=pd(e.d),ds,de;
 if(e.t){var h=+e.t.slice(0,2),m=e.t.slice(3);ds="DTSTART:"+ymd(d)+"T"+p2(h)+m+"00";de="DTEND:"+ymd(d)+"T"+p2((h+1)%24)+m+"00";}
 else{var n=new Date(d.getFullYear(),d.getMonth(),d.getDate()+1);ds="DTSTART;VALUE=DATE:"+ymd(d);de="DTEND;VALUE=DATE:"+ymd(n);}
 function q(s){return String(s).replace(/([,;\\])/g,"\\$1").replace(/\n/g,"\\n");}
 return ["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//FindeDeineLeute.de//DE","BEGIN:VEVENT","UID:"+e.c+"-"+e.d+"-"+e.t+"@findedeineleute.de","DTSTAMP:"+ymd(new Date())+"T000000Z",ds,de,"SUMMARY:"+q(e.cn+": "+e.n),"DESCRIPTION:"+q((e.x?e.x+". ":"")+"Bitte vorab bei der Community prüfen. "+e.l),"LOCATION:"+q(e.city+(e.o?", "+e.o:"")),"URL:"+e.l,"END:VEVENT","END:VCALENDAR"].join("\r\n");}
function dl(e){var b=new Blob([ics(e)],{type:"text/calendar;charset=utf-8"}),u=URL.createObjectURL(b),a=document.createElement("a");a.href=u;a.download=(e.cn+"_"+e.d).replace(/[^\w\-]+/g,"_")+".ics";document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(u);a.remove();},500);}
function gcal(e){var d=pd(e.d),dt;
 if(e.t){var h=+e.t.slice(0,2),m=e.t.slice(3);dt=ymd(d)+"T"+p2(h)+m+"00/"+ymd(d)+"T"+p2((h+1)%24)+m+"00";}
 else{var n=new Date(d.getFullYear(),d.getMonth(),d.getDate()+1);dt=ymd(d)+"/"+ymd(n);}
 return "https://calendar.google.com/calendar/render?action=TEMPLATE&text="+encodeURIComponent(e.cn+": "+e.n)+"&dates="+dt+"&ctz=Europe/Berlin&details="+encodeURIComponent((e.x?e.x+". ":"")+"Bitte vorab bei der Community prüfen. "+e.l)+"&location="+encodeURIComponent(e.city+(e.o?", "+e.o:""));}
function dayLabel(d,today){var diff=Math.round((d-today)/864e5);return {t:DOW[d.getDay()]+", "+d.getDate()+". "+MON[d.getMonth()],today:diff===0,tom:diff===1};}
function listHtml(list,today,showCity,store){
 if(!list.length)return '<p class="note">Aktuell sind hier keine anstehenden Events eingetragen.</p>';
 var days=[],cur=null;
 list.forEach(function(e){if(!cur||cur.d!==e.d){cur={d:e.d,l:[]};days.push(cur);}cur.l.push(e);});
 return days.map(function(g){var lb=dayLabel(pd(g.d),today);
  return '<div class="cal-day"><h3 style="font-size:1.05rem;margin:18px 0 8px">'+lb.t+(lb.today?' <span class="today">Heute</span>':lb.tom?' <span class="today">Morgen</span>':'')+'</h3>'+
  g.l.map(function(e){store.push(e);var i=store.length-1;
   return '<div class="cal-item"><time>'+esc(e.t)+'</time><div><div class="nm">'+esc(e.n)+'<span class="evtag'+(e.k==="run"?' run':'')+'">'+(e.k==="run"?'Regelmäßiger Run':'Event')+'</span></div><div class="sb">'+esc(e.cn)+(showCity?' · '+esc(e.city):'')+(e.o?' · '+esc(e.o):'')+(e.x?' · '+esc(e.x):'')+'</div></div><div class="cal-actions"><a class="btn ghost sm" target="_blank" rel="noopener noreferrer" href="'+esc(e.l)+'">Zur Community</a><button type="button" class="btn ghost sm" data-evg="'+i+'">Google Kalender</button><button type="button" class="btn ghost sm" data-evics="'+i+'">Apple/Outlook</button></div></div>';}).join('')+'</div>';}).join('');
}
function top(all,today,slug){
 var cnt={},meta={},lim=new Date(today.getFullYear(),today.getMonth(),today.getDate()-30);
 all.forEach(function(e){if(slug&&e.s!==slug)return;if(pd(e.d)<lim)return;cnt[e.c]=(cnt[e.c]||0)+1;meta[e.c]=e;});
 var ks=Object.keys(cnt).sort(function(a,b){return cnt[b]-cnt[a];}).slice(0,6);
 if(ks.length<3)return "";
 return '<div class="evtop" aria-label="Aktivste Communities">'+ks.map(function(k){return '<a href="'+esc(meta[k].l)+'" target="_blank" rel="noopener noreferrer">'+esc(meta[k].cn)+' <b>'+cnt[k]+' Events</b></a>';}).join('')+'</div>';
}
function ready(f){if(document.readyState!=="loading")f();else document.addEventListener("DOMContentLoaded",f);}
ready(function(){
 var cb=document.getElementById("calBox"),path=location.pathname,m=path.match(/^\/([a-z-]+)\/$/),wb=document.getElementById("woche"),sec=document.querySelector("section.csec");
 var isCity=!cb&&m&&(wb||sec)&&document.querySelector(".pagehead")&&!document.getElementById("citiesAll");
 if(!cb&&!isCity)return;
 fetch("/assets/events.json").then(function(r){return r.json();}).then(function(j){
  var all=j.events||[],store=[],today=new Date();today=new Date(today.getFullYear(),today.getMonth(),today.getDate());
  var st=document.createElement("style");st.textContent=css;document.head.appendChild(st);
  var box=document.createElement("section");box.className="evbox";box.id="evBox";
  function render(){
   store.length=0;var slug=cb?document.getElementById("calCity").value:m[1];
   var end=new Date(today.getFullYear(),today.getMonth(),today.getDate()+(cb?45:30));
   var list=all.filter(function(e){var d=pd(e.d);if(+d===+today&&e.t){var n=new Date();if(e.t<p2(n.getHours())+":"+p2(n.getMinutes()))return false;}return d>=today&&d<=end&&(!slug||e.s===slug);});
   if(!isCity)list=list.slice(0,60);
   if(isCity&&!list.length){box.hidden=true;return;}
   box.hidden=false;
   box.innerHTML='<h2>'+(cb?"Einzelne Events":"Anstehende Events")+'</h2><p class="evsub">'+(cb?"Konkrete Termine einzelner Communities, direkt von deren öffentlichen Ankündigungen.":"Die nächsten Termine der Communities in dieser Stadt.")+'</p>'+(cb?top(all,today,slug):"")+listHtml(list,today,cb&&!slug,store);
  }
  if(cb){cb.parentNode.insertBefore(box,cb);var sel=document.getElementById("calCity");if(sel)sel.addEventListener("change",render);}
  else{var a=wb||sec;a.parentNode.insertBefore(box,a);}
  render();
  document.addEventListener("click",function(ev){var g=ev.target.closest("[data-evg]");if(g){var ge=store[+g.getAttribute("data-evg")];if(ge)window.open(gcal(ge),"_blank","noopener");return;}var b=ev.target.closest("[data-evics]");if(!b)return;var e=store[+b.getAttribute("data-evics")];if(e)dl(e);});
 }).catch(function(){});
});
})();
