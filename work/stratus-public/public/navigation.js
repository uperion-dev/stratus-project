'use strict';
// The navigation splits: its left piece travels to the logo, while the remainder closes at the right.
(()=>{
 const header=document.querySelector('.topbar'),motion=window.StratusMotion,reduced=matchMedia('(prefers-reduced-motion: reduce)');if(!header||!motion)return;
 const brand=header.querySelector('.brand'),nav=header.querySelector('nav'),links=[...nav.querySelectorAll('a')],label=brand.querySelector('span');if(!brand||!nav||!links.length)return;
 const cluster=document.createElement('div');cluster.className='brand-cluster';brand.before(cluster);cluster.append(brand);label.classList.add('brand-label');
 const toggle=document.createElement('button');toggle.type='button';toggle.className='nav-expand';toggle.setAttribute('aria-label','Expand navigation');toggle.setAttribute('aria-expanded','true');toggle.setAttribute('aria-controls','public-navigation');toggle.innerHTML='<svg viewBox="0 0 18 18" aria-hidden="true"><path d="M6 4.5 12 9 6 13.5Z"/></svg>';cluster.append(toggle);nav.id='public-navigation';
 const track=document.createElement('div');track.className='nav-track';track.append(...links);nav.append(track);const backplate=document.createElement('div');backplate.className='nav-backplate';backplate.setAttribute('aria-hidden','true');nav.prepend(backplate);nav.classList.add('nav-split-frame');header.classList.add('navigation-ready');
 const traveller=document.createElement('div');traveller.className='nav-traveller';traveller.setAttribute('aria-hidden','true');traveller.inert=true;traveller.innerHTML='<div class="nav-flight-label"></div><span class="nav-flight-arrow">'+toggle.innerHTML+'</span>';header.append(traveller);
 const collapser=document.createElement('div');collapser.className='nav-collapser';collapser.setAttribute('aria-hidden','true');collapser.inert=true;collapser.innerHTML='<div class="nav-half-content"></div><span class="nav-current-label"></span>';header.append(collapser);
 let manual=false,lastY=scrollY,mode='',flight=null,flightEffects=[],geometry='',focusAfterExpansion=null;
 function stopFlight(){for(const effect of flightEffects)effect.cancel();flightEffects=[];flight=null;traveller.style.visibility='hidden';collapser.style.visibility='hidden';header.classList.remove('nav-splitting');if(focusAfterExpansion&&document.activeElement===document.body)focusAfterExpansion.focus({preventScroll:true});focusAfterExpansion=null;}
 function copyTrack(offset){const copy=track.cloneNode(true);copy.style.transform=`translateX(${offset}px)`;for(const link of copy.querySelectorAll('a')){link.removeAttribute('href');link.tabIndex=-1;link.inert=true;link.removeAttribute('aria-hidden');}return copy;}
 function animateSplit(v){
  if(v.paused){stopFlight();return;}
  header.classList.add('nav-splitting');traveller.style.visibility='visible';collapser.style.visibility='visible';
  if(flight){for(const effect of flightEffects){effect.playbackRate=v.compact?1:-1;effect.play();}return;}
  if(!v.compact){stopFlight();return;}
  // Two equal physical halves collapse independently; the original controls stay hidden until rejoined.
  const start={x:v.inset+v.available-v.fullWidth+v.pieceWidth/2,y:v.openTop+28},end={x:v.inset+74,y:v.brandTop+28},depth=Math.min(220,v.available*.2);
  const c1={x:start.x+Math.min(20,v.inset),y:start.y+depth},c2={x:end.x+Math.min(170,v.available*.3),y:Math.max(start.y,end.y)+depth};
  traveller.style.offsetPath=`path("M ${start.x} ${start.y} C ${c1.x} ${c1.y} ${c2.x} ${c2.y} ${end.x} ${end.y}")`;
  traveller.querySelector('.nav-flight-label').replaceChildren(copyTrack(-v.navScroll));
  collapser.querySelector('.nav-half-content').replaceChildren(copyTrack(-v.pieceWidth-v.navScroll));
  collapser.querySelector('.nav-current-label').textContent=v.active.textContent;
  collapser.style.right=`${v.inset}px`;
  const travelTiming={duration:640,fill:'both',easing:'cubic-bezier(.42,0,.2,1)'},collapseTiming={duration:360,fill:'both',easing:'cubic-bezier(.22,.65,.2,1)'};
  flight=traveller.animate([{offsetDistance:'0%'},{offsetDistance:'100%'}],travelTiming);
  const leftSize=traveller.animate([{width:`${v.pieceWidth}px`,height:'56px'},{width:'44px',height:'44px'}],collapseTiming);
  const leftLabel=traveller.querySelector('.nav-flight-label').animate([{opacity:1,offset:0},{opacity:0,offset:.25},{opacity:0,offset:1}],travelTiming);
  const arrow=traveller.querySelector('.nav-flight-arrow').animate([{opacity:0,offset:0},{opacity:0,offset:.3},{opacity:1,offset:.7},{opacity:1,offset:1}],travelTiming);
  const handoff=traveller.animate([{opacity:1,offset:0},{opacity:1,offset:.8},{opacity:0,offset:1}],{...travelTiming,easing:'linear'});
  const rightSize=collapser.animate([{width:`${v.pieceWidth}px`,height:'56px',top:`${v.openTop}px`},{width:`${v.closedWidth}px`,height:'56px',top:`${v.brandTop}px`}],collapseTiming);
  const rightLabel=collapser.querySelector('.nav-half-content').animate([{opacity:1,offset:0},{opacity:0,offset:.4},{opacity:0,offset:1}],collapseTiming);
  const rightCurrent=collapser.querySelector('.nav-current-label').animate([{opacity:0,offset:0},{opacity:0,offset:.25},{opacity:1,offset:1}],collapseTiming);
  flightEffects=[flight,leftSize,leftLabel,arrow,handoff,rightSize,rightLabel,rightCurrent];
  rightSize.onfinish=()=>{if(rightSize.playbackRate>0&&mode==='compact'){collapser.style.visibility='hidden';header.classList.remove('nav-splitting');}};
  flight.onfinish=()=>{if(flight.playbackRate<0)stopFlight();else traveller.style.visibility='hidden';};
 }

 function read(s){
  const changed=Math.abs(s.y-lastY)>1;lastY=s.y;if(changed)manual=false;
  const view=document.querySelector('[data-view]:not([hidden])'),anchor=view?.querySelector('.immersive-hero,.section-intro'),bottom=anchor?.getBoundingClientRect().bottom??1,past=bottom<=0;
  if(!past)manual=false;const compact=past&&!manual,active=nav.querySelector('[aria-current=page]')||links[0],inset=Math.max(12,s.w*.04),available=s.w-inset*2,fullWidth=Math.min(track.scrollWidth+12,available),narrow=available<185+fullWidth+24,closedWidth=active.offsetWidth+12,openTop=narrow?76:14,brandTop=narrow?10:14;
  return {compact,past,active,mode:compact?'compact':past?'peek':'open',inset,available,fullWidth,narrow,openTop,brandTop,closedWidth,pieceWidth:fullWidth/2,navScroll:nav.scrollLeft,y:compact?brandTop:openTop,width:compact?closedWidth:fullWidth,shift:compact?-active.offsetLeft:0,paused:s.paused||reduced.matches};
 }
 function write(v){
  const changed=mode!==v.mode,splitChanged=(mode==='compact')!==v.compact,hadMode=!!mode,nextGeometry=`${v.inset}/${v.fullWidth}/${v.openTop}/${v.closedWidth}`;
  if(flight&&geometry!==nextGeometry)stopFlight();geometry=nextGeometry;
  if(changed){mode=v.mode;header.dataset.navMode=mode;header.classList.toggle('nav-compact',v.compact);header.classList.toggle('nav-peek',mode==='peek');const expanderFocused=document.activeElement===toggle;toggle.setAttribute('aria-expanded',String(!v.compact));toggle.setAttribute('aria-label','Expand navigation');toggle.tabIndex=v.compact?0:-1;toggle.setAttribute('aria-hidden',String(!v.compact));if(!v.compact&&expanderFocused){v.active.focus({preventScroll:true});focusAfterExpansion=v.active;}if(v.compact)focusAfterExpansion=null;toggle.inert=!v.compact;
   if(v.compact&&links.includes(document.activeElement)&&document.activeElement!==v.active)toggle.focus({preventScroll:true});
   if(v.compact)nav.scrollLeft=0;
   for(const link of links){const hide=v.compact&&link!==v.active;link.inert=hide;link.tabIndex=hide?-1:0;if(hide)link.setAttribute('aria-hidden','true');else link.removeAttribute('aria-hidden');}
  }
  motion.style(header,'--header-inset',`${v.inset}px`);motion.style(nav,'--nav-top',`${v.y}px`);
  motion.style(nav,'--nav-width',`${v.width}px`);motion.style(track,'--nav-track-shift',`${v.shift}px`);
  header.classList.toggle('nav-stacked',v.narrow);header.classList.toggle('nav-motion-off',v.paused);
  if(v.paused&&flight)stopFlight();else if(splitChanged&&hadMode)animateSplit(v);
 }
 motion.register('compact-navigation',read,write);
 toggle.addEventListener('click',()=>{manual=!manual;lastY=scrollY;motion.request();});
 window.addEventListener('keydown',e=>{if(e.key==='Escape'&&manual){manual=false;motion.request();}});
 nav.addEventListener('click',e=>{const link=e.target.closest('a');if(link){if(link.getAttribute('href')===location.hash){e.preventDefault();window.scrollTo({top:0,behavior:reduced.matches?'instant':'smooth'});}manual=false;motion.request();}});
 brand.addEventListener('click',e=>{if(location.hash==='#overview'){e.preventDefault();window.scrollTo({top:0,behavior:reduced.matches?'instant':'smooth'});}});
 window.addEventListener('hashchange',()=>{manual=false;lastY=scrollY;motion.request();});reduced.addEventListener('change',motion.request);document.fonts?.ready.then(motion.request);
 new MutationObserver(motion.request).observe(nav,{subtree:true,attributes:true,attributeFilter:['aria-current']});motion.request();
})();
