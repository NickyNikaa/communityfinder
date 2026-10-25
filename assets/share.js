/* FindeDeineLeute.de: Teilen-Buttons fuer Communities und Events (ohne externe Dienste) */
(function(){
"use strict";
var ICON='<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 15V3M8 7l4-4 4 4M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
var css='.sharebtn{width:38px;height:38px;display:inline-grid;place-items:center;border-radius:50%;border:1px solid var(--line,#ddd);background:#fff;color:var(--muted,#666);cursor:pointer;padding:0;flex:none;transition:transform .2s,box-shadow .2s}'
+'.sharebtn svg{width:18px;height:18px}.sharebtn:hover{transform:scale(1.08);box-shadow:0 4px 14px rgba(43,143,214,.25);color:#2b8fd6}'
+'.card .sharebtn{position:absolute;right:62px;top:16px;z-index:3}'
+'.card>.tag{padding-right:104px}'
+'.sharemenu{position:fixed;z-index:9999;min-width:210px;background:#fff;border:1px solid rgba(0,0,0,.1);border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,.18);padding:8px}'
+'.sharemenu .shh{padding:8px 12px 6px;font-size:.78rem;opacity:.65;max-width:260px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
+'.sharemenu a,.sharemenu button{display:flex;width:100%;align-items:center;gap:10px;padding:10px 12px;border:0;background:none;border-radius:10px;font:500 .92rem/1.2 inherit;color:inherit;text-decoration:none;cursor:pointer;text-align:left}'
+'.sharemenu a:hover,.sharemenu button:hover,.sharemenu a:focus-visible,.sharemenu button:focus-visible{background:rgba(139,92,246,.1);outline:none}'
+'.shtoast{position:fixed;left:50%;bottom:28px;transform:translateX(-50%);z-index:10000;background:#1b1b1f;color:#fff;padding:11px 18px;border-radius:999px;font-size:.9rem;box-shadow:0 8px 28px rgba(0,0,0,.3)}';
function add(){var s=document.createElement("style");s.textContent=css;document.head.appendChild(s);}
function txt(el){return el?el.textContent.replace(/\s+/g," ").trim():"";}
function ctx(btn){
 var row=btn.closest("li.row[id]"),card=btn.closest("article.card"),ci=btn.closest(".cal-item"),o=location.origin;
 if(row){var t=txt(row.querySelector("h3"));return {title:t,url:o+location.pathname+"#"+row.id,text:t+" auf FindeDeineLeute.de"};}
 if(card){var a=card.querySelector("h3 a"),t2=txt(a||card.querySelector("h3"));return {title:t2,url:a?a.href:o+"/",text:t2+" auf FindeDeineLeute.de"};}
 if(ci){var nm=ci.querySelector(".nm");if(nm){nm=nm.cloneNode(true);var tg=nm.querySelector(".evtag");if(tg)tg.remove();}
  var day=ci.closest(".cal-day"),h=day?day.querySelector("h2,h3"):null,d=h?txt(h).replace(/\s*(Heute|Morgen)$/,""):"",tm=txt(ci.querySelector("time")),sel=document.getElementById("calCity"),m=location.pathname.match(/^\/([a-z-]+)\/$/),slug=(sel&&sel.value)||(m&&m[1]!=="kalender"?m[1]:"");
  var t3=txt(nm),sb=txt(ci.querySelector(".sb")),isEv=!!(ci.querySelector(".nm .evtag")),cn=isEv?sb.split(" · ")[0]:"";if(cn)t3=cn+": "+t3;return {title:t3,url:o+"/kalender/"+(slug?"?stadt="+slug:""),text:t3+(d?", "+d:"")+(tm?", "+tm+" Uhr":"")+" | FindeDeineLeute.de"};}
 return {title:document.title,url:location.href,text:document.title};
}
var menu=null;
function close(){if(menu){menu.remove();menu=null;}}
function toast(m){var t=document.createElement("div");t.className="shtoast";t.setAttribute("role","status");t.textContent=m;document.body.appendChild(t);setTimeout(function(){t.remove();},2200);}
function copy(u){
 function fb(){var i=document.createElement("input");i.value=u;i.style.position="fixed";i.style.opacity="0";document.body.appendChild(i);i.select();try{document.execCommand("copy");toast("Link kopiert");}catch(e){toast("Kopieren nicht möglich");}i.remove();}
 if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(u).then(function(){toast("Link kopiert");},fb);}else fb();
}
function open(btn){
 close();var c=ctx(btn),m=document.createElement("div");m.className="sharemenu";m.setAttribute("role","menu");
 var h='<div class="shh">'+c.title.replace(/</g,"&lt;")+'</div>';
 if(navigator.share)h+='<button type="button" data-a="native" role="menuitem">Teilen …</button>';
 h+='<a data-a="wa" role="menuitem" target="_blank" rel="noopener noreferrer" href="https://wa.me/?text='+encodeURIComponent(c.text+"\n"+c.url)+'">WhatsApp</a>';
 h+='<button type="button" data-a="copy" role="menuitem">Link kopieren (z. B. für Instagram)</button>';
 m.innerHTML=h;document.body.appendChild(m);menu=m;
 var r=btn.getBoundingClientRect(),w=m.offsetWidth,x=Math.max(8,Math.min(window.innerWidth-w-8,r.right-w)),y=r.bottom+8;if(y+m.offsetHeight>window.innerHeight-8)y=Math.max(8,r.top-m.offsetHeight-8);
 m.style.left=x+"px";m.style.top=y+"px";tOpen=Date.now();
 m.addEventListener("click",function(e){var b=e.target.closest("[data-a]");if(!b)return;var a=b.getAttribute("data-a");
  if(a==="native"){navigator.share({title:c.title,text:c.text,url:c.url}).catch(function(){});close();}
  else if(a==="copy"){copy(c.url);close();}
  else close();});
 var f=m.querySelector("a,button");if(f)f.focus();
}
document.addEventListener("click",function(e){var b=e.target.closest(".sharebtn");if(b){e.preventDefault();e.stopPropagation();if(menu&&menu._b===b){close();}else{open(b);if(menu)menu._b=b;}return;}if(menu&&!e.target.closest(".sharemenu"))close();},true);
document.addEventListener("keydown",function(e){if(e.key==="Escape")close();});
var tOpen=0;window.addEventListener("scroll",function(){if(Date.now()-tOpen>500)close();},{passive:true});
function mk(){var b=document.createElement("button");b.type="button";b.className="sharebtn";b.setAttribute("aria-label","Teilen");b.title="Teilen";b.setAttribute("aria-haspopup","menu");b.innerHTML=ICON;return b;}
function enhance(){
 [].forEach.call(document.querySelectorAll("li.row[id] .ra, .cal-actions"),function(n){if(n.getAttribute("data-sh"))return;n.setAttribute("data-sh","1");var s=n.querySelector(".save"),b=mk();if(s)n.insertBefore(b,s);else n.appendChild(b);});
 [].forEach.call(document.querySelectorAll("article.card"),function(n){if(n.getAttribute("data-sh"))return;n.setAttribute("data-sh","1");n.appendChild(mk());});
}
function ready(f){if(document.readyState!=="loading")f();else document.addEventListener("DOMContentLoaded",f);}
ready(function(){add();enhance();var t=null;if(window.MutationObserver){new MutationObserver(function(){clearTimeout(t);t=setTimeout(enhance,60);}).observe(document.body,{childList:true,subtree:true});}});
})();
