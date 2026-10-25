'use strict';
// Smoothly seek paused compositor animations: scroll powers every reveal and its reversal.
(()=>{
 const motion=window.StratusMotion,body=document.body,root=document.documentElement,header=document.querySelector('.topbar'),reduced=matchMedia('(prefers-reduced-motion: reduce)');if(!motion)return;
 const groups=[['.hero-content','rise'],['.hero-manifesto,.scene-coordinate,.hero-bottom','detail'],['.workspace-card,.spec-section,.release,.upcoming-item,.roadmap-process li,.faq-list details,.preset-guide,.release-focus-grid article,#feedback-form','rise'],['.showcase-shot,.water-story-image,#home-gallery','image'],['.reference-strip,.platform-strip,.workflow-note,.roadmap-note,.spec-footnote,.public-footer','line'],['main [data-view] h1,main [data-view] h2,main [data-view] h3','heading'],['main [data-view] p,main [data-view] dl,.carousel-controls','copy'],['main [data-view] .button,main [data-view] .text-link,.home-heading>a,.chapter-label','detail']];
 const revealDuration=2600,records=new Map(),active=new Set();let observer,dirty=true,lastWidth=0,lastHeight=0,lastPaused=null,scrolled=false,lastTick=0;
 const clamp=n=>Math.max(0,Math.min(1,n)),disabled=()=>reduced.matches||body.classList.contains('effects-paused');
 function make(el,type){
  const from=type==='line'?'translateY(18px) scale(.985)':type==='heading'?'translateY(36px)':type==='detail'?'translateY(18px)':type==='image'?'translateY(46px) scale(.985)':type==='copy'?'translateY(28px)':'translateY(44px)';
  const animation=el.animate([{opacity:0,transform:from},{opacity:1,transform:'translate(0,0) scale(1)'}],{duration:revealDuration,fill:'both',easing:'cubic-bezier(.22,.12,.32,1)'});animation.pause();const p=disabled()?1:0;animation.currentTime=p*revealDuration;
  el.dataset.reveal=type;el.classList.add('scroll-reveal','is-revealed');const siblings=[...el.parentElement.children],stagger=el.matches('.workspace-card,.release-focus-grid article,.showcase-shot,.roadmap-process li')?(siblings.indexOf(el)%3)*.025:0,record={el,animation,top:0,height:0,p,stagger};records.set(el,record);observer?.observe(el);active.add(record);
 }
 function register(){
  for(const [el,r] of records)if(!el.isConnected){r.animation.cancel();observer?.unobserve(el);active.delete(r);records.delete(el);}
  for(const [selector,type] of groups)for(const el of document.querySelectorAll(selector)){if(records.has(el)||el.parentElement.closest('[data-reveal]')||el.closest('.topbar,.spatial-journey,.atmosphere-wordmark,#scene-dialog,[data-scroll-static]'))continue;make(el,type);}
  dirty=true;motion.request();
 }
 if('IntersectionObserver'in window)observer=new IntersectionObserver(entries=>{for(const e of entries){const r=records.get(e.target);if(!r)continue;if(e.isIntersecting)active.add(r);else{active.delete(r);if(!disabled()&&!r.el.contains(document.activeElement)){r.animation.currentTime=0;r.p=0;r.el.dataset.revealProgress='0';}}}motion.request();},{rootMargin:'45% 0px 45% 0px'});
 function measure(s){for(const r of records.values()){if(r.el.closest('[data-view][hidden]'))continue;const b=r.el.getBoundingClientRect(),matrix=getComputedStyle(r.el).transform,m=matrix==='none'?null:new DOMMatrixReadOnly(matrix),offset=m?m.m42+(1-m.m22)*r.el.offsetHeight/2:0;r.top=b.top+s.y-offset;r.height=r.el.offsetHeight;}lastWidth=s.w;lastHeight=s.h;dirty=false;}
 motion.register('reversible-reveals',s=>{
  if((s.navBusy||header?.classList.contains('nav-animating'))&&!disabled())return {values:[],settling:false,progress:clamp(s.y/Math.max(1,s.height-s.h)),hasScrolled:s.y>24};
  const now=performance.now(),dt=lastTick?Math.min(48,now-lastTick):16,gain=1-Math.exp(-dt/320);lastTick=now;
  const paused=disabled();if(paused!==lastPaused){lastPaused=paused;if(paused)for(const r of records.values()){r.animation.currentTime=revealDuration;r.p=1;r.el.dataset.revealProgress='1';}dirty=true;}
  if(dirty||lastWidth!==s.w||lastHeight!==s.h)measure(s);
  const values=[],atEnd=s.y>=s.height-s.h-2;let settling=false;
  for(const r of active){if(r.el.closest('[data-view][hidden]'))continue;const top=r.top-s.y,bottom=top+r.height,pinned=r.el.contains(document.activeElement)||r.el.closest('form')?.contains(document.activeElement),enter=clamp((s.h*(1.14-r.stagger)-top)/(s.h*.68)),leave=clamp((bottom+s.h*.10)/(s.h*.42)),fullyVisibleAtEnd=atEnd&&top>=0&&bottom<=s.h+4,target=paused||pinned||fullyVisibleAtEnd?1:Math.min(enter,leave);let p=paused||pinned?1:r.p+(target-r.p)*gain;if(Math.abs(target-p)<.002)p=target;else settling=true;values.push([r,p]);}
  return {values,settling,progress:clamp(s.y/Math.max(1,s.height-s.h)),hasScrolled:s.y>24};
 },({values,settling,progress,hasScrolled})=>{motion.style(root,'--read-progress',progress);if(scrolled!==hasScrolled){scrolled=hasScrolled;body.classList.toggle('has-scrolled',scrolled);}for(const [r,p]of values)if(Math.abs(r.p-p)>.0001){r.p=p;r.animation.currentTime=p*revealDuration;r.el.dataset.revealProgress=p.toFixed(3);}if(settling)motion.request();});
 body.classList.add('motion-enabled','scroll-scrub');register();
 window.addEventListener('stratus:route-changed',()=>{dirty=true;motion.request();});
 window.addEventListener('hashchange',()=>{dirty=true;motion.request();});window.addEventListener('resize',()=>{dirty=true;motion.request();},{passive:true});reduced.addEventListener('change',motion.request);
 document.addEventListener('focusin',motion.request);document.addEventListener('focusout',motion.request);document.addEventListener('load',()=>{dirty=true;motion.request();},true);document.fonts?.ready.then(()=>{dirty=true;motion.request();});
 new ResizeObserver(()=>{dirty=true;motion.request();}).observe(document.querySelector('main'));
 new MutationObserver(rows=>{if(rows.some(r=>r.addedNodes.length||r.removedNodes.length))register();}).observe(document.querySelector('main'),{childList:true,subtree:true});
 new MutationObserver(()=>{const p=disabled();if(p!==lastPaused)motion.request();}).observe(body,{attributes:true,attributeFilter:['class']});
})();
