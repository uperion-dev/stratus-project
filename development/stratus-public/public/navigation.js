'use strict';
// The navigation splits: its left piece travels to the logo, while the remainder closes at the right.
(()=>{
 const header=document.querySelector('.topbar'),motion=window.StratusMotion,reduced=matchMedia('(prefers-reduced-motion: reduce)');if(!header||!motion)return;
 const brand=header.querySelector('.brand'),nav=header.querySelector('nav'),links=[...nav.querySelectorAll('a')],label=brand.querySelector('span');if(!brand||!nav||!links.length)return;
 const cluster=document.createElement('div');cluster.className='brand-cluster';brand.before(cluster);cluster.append(brand);label.classList.add('brand-label');
 const toggle=document.createElement('button');toggle.type='button';toggle.className='nav-expand';toggle.setAttribute('aria-label','Expand navigation');toggle.setAttribute('aria-expanded','true');toggle.setAttribute('aria-controls','public-navigation');toggle.innerHTML='<svg viewBox="0 0 18 18" aria-hidden="true"><path d="M6 4.5 12 9 6 13.5Z"/></svg>';cluster.append(toggle);nav.id='public-navigation';
 const track=document.createElement('div');track.className='nav-track';track.append(...links);const navViewport=document.createElement('div');navViewport.className='nav-viewport';navViewport.append(track);nav.append(navViewport);for(const side of ['start','end']){const cue=document.createElement('span');cue.className=`nav-scroll-cue nav-scroll-cue-${side}`;cue.setAttribute('aria-hidden','true');cue.innerHTML=`<svg viewBox="0 0 12 18"><path d="${side==='start'?'M8 4 3 9l5 5':'m4 4 5 5-5 5'}"/></svg>`;nav.append(cue);}const backplate=document.createElement('div');backplate.className='nav-backplate';backplate.setAttribute('aria-hidden','true');nav.prepend(backplate);nav.classList.add('nav-split-frame');header.classList.add('navigation-ready');
 const traveller=document.createElement('div');traveller.className='nav-traveller';traveller.setAttribute('aria-hidden','true');traveller.inert=true;traveller.innerHTML='<div class="nav-flight-label"></div><span class="nav-flight-arrow">'+toggle.innerHTML+'</span>';header.append(traveller);
 const collapser=document.createElement('div');collapser.className='nav-collapser';collapser.setAttribute('aria-hidden','true');collapser.inert=true;collapser.innerHTML='<div class="nav-half-content"></div><span class="nav-current-label"></span>';header.append(collapser);
 let manual=false,lastY=scrollY,mode='',flight=null,flightEffects=[],geometry='',focusAfterExpansion=null,layoutCache=null,layoutDirty=true,observedAnchor=null,lastPaused=null,lastActive=null,expandedScroll=0,scrollStateFrame=0;
 function stopFlight(){for(const effect of flightEffects)effect.cancel();flightEffects=[];flight=null;traveller.style.visibility='hidden';collapser.style.visibility='hidden';header.classList.remove('nav-splitting');nav.inert=false;if(mode!=='compact')navViewport.scrollLeft=expandedScroll;requestScrollState();motion.request();if(focusAfterExpansion&&document.activeElement===document.body)focusAfterExpansion.focus({preventScroll:true});focusAfterExpansion=null;}
 function copyTrack(offset){const copy=track.cloneNode(true);copy.style.transform=`translateX(${offset}px)`;for(const link of copy.querySelectorAll('a')){link.removeAttribute('href');link.tabIndex=-1;link.inert=true;link.removeAttribute('aria-hidden');}return copy;}
 const leftCopy=copyTrack(0),rightCopy=copyTrack(0),copyLinks=[...leftCopy.querySelectorAll('a'),...rightCopy.querySelectorAll('a')];
 traveller.querySelector('.nav-flight-label').replaceChildren(leftCopy);collapser.querySelector('.nav-half-content').replaceChildren(rightCopy);
 // A quiet ease-in accelerates into a damped elastic arrival. Sampled once per trip.
 function travelEase(t){if(t<=0)return 0;if(t>=1)return 1;if(t<.3)return .17*Math.pow(t/.3,2);const q=(t-.3)/.7;return .17+.83*(1-Math.exp(-7.5*q)*(Math.cos(9*q)+.72*Math.sin(9*q)));}
 function travelFrames(compact,at=compact?0:1,distance=compact?0:1){const frames=[];for(let i=0;i<=64;i++){const u=i/64,offset=compact?at+(1-at)*u:at*(1-u),p=compact?distance+(1-distance)*travelEase(u):distance*(1-travelEase(u));frames.push({offsetDistance:`${p*100}%`,offset});}if(!compact)frames.reverse();if(frames[0].offset>0)frames.unshift({...frames[0],offset:0});if(frames.at(-1).offset<1)frames.push({...frames.at(-1),offset:1});return frames;}
 function animateSplit(v){
  if(v.paused){stopFlight();return;}
  header.classList.add('nav-splitting');nav.inert=true;traveller.style.visibility='visible';collapser.style.visibility='visible';if(!v.compact)navViewport.scrollLeft=v.expandedScroll;requestScrollState();
  if(flight){const at=Math.max(0,Math.min(1,Number(flight.currentTime)/640)),distance=parseFloat(getComputedStyle(traveller).offsetDistance)/100;flight.effect.setKeyframes(travelFrames(v.compact,at,Number.isFinite(distance)?distance:at));for(const effect of flightEffects){effect.playbackRate=v.compact?1:-1;effect.play();}return;}
  // Two equal physical halves collapse independently; the original controls stay hidden until rejoined.
  const start={x:v.inset+v.available-v.fullWidth+v.pieceWidth/2,y:v.openTop+28},end={x:v.inset+74,y:v.brandTop+28},depth=Math.min(220,v.available*.2);
  const c1={x:start.x+Math.min(20,v.inset),y:start.y+depth},c2={x:end.x+Math.min(170,v.available*.3),y:Math.max(start.y,end.y)+depth};
  traveller.style.offsetPath=`path("M ${start.x} ${start.y} C ${c1.x} ${c1.y} ${c2.x} ${c2.y} ${end.x} ${end.y}")`;
  leftCopy.style.transform=`translateX(${-v.navScroll}px)`;rightCopy.style.transform=`translateX(${-v.pieceWidth-v.navScroll}px)`;
  copyLinks.forEach((link,i)=>{if(i%links.length===v.activeIndex)link.setAttribute('aria-current','page');else link.removeAttribute('aria-current');});
  collapser.querySelector('.nav-current-label').textContent=v.active.textContent;
  collapser.style.right=`${v.inset}px`;
  // One reversible clock keeps both halves arriving at the seam together.
  const travelTiming={duration:640,fill:'both',easing:'cubic-bezier(.42,0,.2,1)'},joinTiming={duration:640,fill:'both',easing:'linear'},collapseEase='cubic-bezier(.42,0,.58,1)',collapsedAt=360/640;
  header.style.setProperty('--nav-material-width',`${v.fullWidth}px`);
  for(const surface of [traveller,collapser]){surface.style.setProperty('--lg-x',v.lightX);surface.style.setProperty('--lg-y',v.lightY);}
  flight=traveller.animate(travelFrames(v.compact),{...travelTiming,easing:'linear'});
  const leftSize=traveller.animate([{width:`${v.pieceWidth}px`,height:'56px',borderTopLeftRadius:'28px',borderBottomLeftRadius:'28px',borderTopRightRadius:'0px',borderBottomRightRadius:'0px',borderRightColor:'transparent',offset:0,easing:collapseEase},{width:'44px',height:'44px',borderTopLeftRadius:'22px',borderBottomLeftRadius:'22px',borderTopRightRadius:'22px',borderBottomRightRadius:'22px',borderRightColor:'var(--lg-rim)',offset:collapsedAt},{width:'44px',height:'44px',borderTopLeftRadius:'22px',borderBottomLeftRadius:'22px',borderTopRightRadius:'22px',borderBottomRightRadius:'22px',borderRightColor:'var(--lg-rim)',offset:1}],joinTiming);
  const leftLabel=traveller.querySelector('.nav-flight-label').animate([{opacity:1,offset:0},{opacity:0,offset:.25},{opacity:0,offset:1}],travelTiming);
  const arrow=traveller.querySelector('.nav-flight-arrow').animate([{opacity:0,offset:0},{opacity:0,offset:.3},{opacity:1,offset:.7},{opacity:1,offset:1}],travelTiming);
  // The final 115 ms of expansion blends matching surfaces rather than switching scenes.
  const handoff=traveller.animate([{opacity:0,offset:0},{opacity:1,offset:.18},{opacity:1,offset:.8},{opacity:0,offset:1}],joinTiming);
  const rightSize=collapser.animate([{width:`${v.pieceWidth}px`,height:'56px',top:`${v.openTop}px`,borderTopLeftRadius:'0px',borderBottomLeftRadius:'0px',borderLeftColor:'transparent',offset:0,easing:collapseEase},{width:`${v.closedWidth}px`,height:'56px',top:`${v.brandTop}px`,borderTopLeftRadius:'28px',borderBottomLeftRadius:'28px',borderLeftColor:'var(--lg-rim)',offset:collapsedAt},{width:`${v.closedWidth}px`,height:'56px',top:`${v.brandTop}px`,borderTopLeftRadius:'28px',borderBottomLeftRadius:'28px',borderLeftColor:'var(--lg-rim)',offset:1}],joinTiming);
  const rightLabel=collapser.querySelector('.nav-half-content').animate([{opacity:1,offset:0},{opacity:0,offset:.25},{opacity:0,offset:1}],joinTiming);
  const rightCurrent=collapser.querySelector('.nav-current-label').animate([{opacity:0,offset:0},{opacity:0,offset:.35},{opacity:1,offset:collapsedAt},{opacity:1,offset:1}],joinTiming);
  const rightBlend=collapser.animate([{opacity:0,offset:0},{opacity:1,offset:.18},{opacity:1,offset:1}],joinTiming);
  const liveBlend=nav.animate([{opacity:1,offset:0},{opacity:0,offset:.18},{opacity:0,offset:1}],joinTiming);
  // The hidden live controls only change layout once, after their fade has finished.
  const livePose=nav.animate([{width:`${v.fullWidth}px`,top:`${v.openTop}px`,offset:0},{width:`${v.fullWidth}px`,top:`${v.openTop}px`,offset:.18,easing:'steps(1,end)'},{width:`${v.closedWidth}px`,top:`${v.brandTop}px`,offset:.19},{width:`${v.closedWidth}px`,top:`${v.brandTop}px`,offset:1}],joinTiming);
  const trackPose=track.animate([{transform:'translateX(0px)',offset:0},{transform:'translateX(0px)',offset:.18,easing:'steps(1,end)'},{transform:`translateX(${-v.activeOffset}px)`,offset:.19},{transform:`translateX(${-v.activeOffset}px)`,offset:1}],joinTiming);
  flightEffects=[flight,leftSize,leftLabel,arrow,handoff,rightSize,rightLabel,rightCurrent,rightBlend,liveBlend,livePose,trackPose];
  rightSize.onfinish=()=>{if(rightSize.playbackRate>0&&mode==='compact'){liveBlend.cancel();livePose.cancel();trackPose.cancel();collapser.style.visibility='hidden';header.classList.remove('nav-splitting');nav.inert=false;requestScrollState();motion.request();}};
  const primaryFlight=flight;primaryFlight.onfinish=()=>{if(flight!==primaryFlight)return;if(primaryFlight.playbackRate<0)stopFlight();else traveller.style.visibility='hidden';};
  // A page restored at a scrolled position can expand smoothly without a previous collapse.
  if(!v.compact)for(const effect of flightEffects){effect.currentTime=640;effect.playbackRate=-1;effect.play();}

 }

 function invalidateLayout(){layoutDirty=true;motion.request();}
 const sizeObserver='ResizeObserver'in window?new ResizeObserver(invalidateLayout):null;sizeObserver?.observe(track);
 function read(s){
  const changed=Math.abs(s.y-lastY)>1;lastY=s.y;if(changed)manual=false;
  // Geometry is stable between resize, font, route and label changes; scroll only compares positions.
  const freshLayout=layoutDirty||!layoutCache||layoutCache.viewportWidth!==s.w;
  if(freshLayout){
   const view=document.querySelector('[data-view]:not([hidden])'),anchor=view?.querySelector('.immersive-hero,.section-intro'),active=nav.querySelector('[aria-current=page]')||links[0],inset=Math.max(12,s.w*.04),available=s.w-inset*2,naturalWidth=track.scrollWidth,fullWidth=Math.min(naturalWidth+12,available),narrow=available<185+fullWidth+24;
   if(anchor!==observedAnchor){if(observedAnchor)sizeObserver?.unobserve(observedAnchor);if(anchor)sizeObserver?.observe(anchor);observedAnchor=anchor;}
   layoutCache={active,activeIndex:links.indexOf(active),activeOffset:active.offsetLeft,inset,available,fullWidth,naturalWidth,narrow,openTop:narrow?76:14,brandTop:narrow?10:14,closedWidth:active.offsetWidth+12,pieceWidth:fullWidth/2,anchorEnd:anchor?anchor.getBoundingClientRect().bottom+s.y:Infinity,viewportWidth:s.w};layoutDirty=false;
  }
  const past=s.y>=layoutCache.anchorEnd;if(!past)manual=false;
  const compact=past&&!manual,nextMode=compact?'compact':past?'peek':'open',changing=mode!==nextMode,innerWidth=layoutCache.fullWidth-12,maxScroll=Math.max(0,layoutCache.naturalWidth-innerWidth);
  let targetScroll=Math.max(0,Math.min(maxScroll,compact&&mode!=='compact'?navViewport.scrollLeft:expandedScroll));
  if(freshLayout||lastActive!==layoutCache.active){const left=layoutCache.activeOffset,right=left+layoutCache.closedWidth-12;if(left<targetScroll+18)targetScroll=Math.max(0,left-18);else if(right>targetScroll+innerWidth-18)targetScroll=Math.min(maxScroll,right-innerWidth+18);}
  return {...layoutCache,compact,past,mode:nextMode,lightX:changing?nav.style.getPropertyValue('--lg-x')||'22%':'22%',lightY:changing?nav.style.getPropertyValue('--lg-y')||'0%':'0%',expandedScroll:targetScroll,navScroll:changing?(compact?navViewport.scrollLeft:targetScroll):0,y:compact?layoutCache.brandTop:layoutCache.openTop,width:compact?layoutCache.closedWidth:layoutCache.fullWidth,shift:compact?-layoutCache.activeOffset:0,paused:s.paused||reduced.matches};
 }

 function write(v){
  const changed=mode!==v.mode||lastActive!==v.active,splitChanged=(mode==='compact')!==v.compact,hadMode=!!mode,nextGeometry=`${v.inset}/${v.fullWidth}/${v.openTop}/${v.closedWidth}/${v.activeIndex}`,layoutChanged=geometry!==nextGeometry,pausedChanged=lastPaused!==v.paused;
  if(!changed&&!layoutChanged&&!pausedChanged)return;
  lastActive=v.active;lastPaused=v.paused;if(flight&&layoutChanged)stopFlight();geometry=nextGeometry;expandedScroll=v.expandedScroll;
  if(changed){mode=v.mode;header.dataset.navMode=mode;header.classList.toggle('nav-compact',v.compact);header.classList.toggle('nav-peek',mode==='peek');const expanderFocused=document.activeElement===toggle;toggle.setAttribute('aria-expanded',String(!v.compact));toggle.setAttribute('aria-label','Expand navigation');toggle.tabIndex=v.compact?0:-1;toggle.setAttribute('aria-hidden',String(!v.compact));if(!v.compact&&expanderFocused){v.active.focus({preventScroll:true});focusAfterExpansion=v.active;}if(v.compact)focusAfterExpansion=null;toggle.inert=!v.compact;
   if(v.compact&&links.includes(document.activeElement)&&document.activeElement!==v.active)toggle.focus({preventScroll:true});
   if(v.compact)navViewport.scrollLeft=0;
   for(const link of links){const hide=v.compact&&link!==v.active;link.inert=hide;link.tabIndex=hide?-1:0;if(hide)link.setAttribute('aria-hidden','true');else link.removeAttribute('aria-hidden');}
  }
  motion.style(header,'--header-inset',`${v.inset}px`);motion.style(nav,'--nav-top',`${v.y}px`);
  motion.style(nav,'--nav-width',`${v.width}px`);motion.style(track,'--nav-track-shift',`${v.shift}px`);
  header.classList.toggle('nav-stacked',v.narrow);header.classList.toggle('nav-motion-off',v.paused);
  if(v.paused&&flight)stopFlight();else if(splitChanged&&hadMode)animateSplit(v);
  if(!v.compact&&!header.classList.contains('nav-splitting'))navViewport.scrollLeft=expandedScroll;requestScrollState();
 }
 function updateScrollState(){
  scrollStateFrame=0;const expanded=mode!=='compact'&&!header.classList.contains('nav-splitting'),max=Math.max(0,navViewport.scrollWidth-navViewport.clientWidth),position=Math.max(0,Math.min(max,navViewport.scrollLeft)),overflow=expanded&&max>1;
  header.classList.toggle('nav-scrollable',overflow);header.classList.toggle('nav-scroll-start',overflow&&position>1);header.classList.toggle('nav-scroll-end',overflow&&position<max-1);
  if(expanded)expandedScroll=position;
  const description=overflow?'Scroll horizontally for more navigation links.':'';if(nav.getAttribute('aria-description')!==description)nav.setAttribute('aria-description',description);
 }
 function requestScrollState(){if(!scrollStateFrame)scrollStateFrame=requestAnimationFrame(updateScrollState);}
 navViewport.addEventListener('scroll',requestScrollState,{passive:true});
 motion.register('compact-navigation',read,write);
 toggle.addEventListener('click',()=>{manual=!manual;lastY=scrollY;header.classList.add('nav-splitting');motion.request();});
 window.addEventListener('keydown',e=>{if(e.key==='Escape'&&manual){manual=false;header.classList.add('nav-splitting');motion.request();}});
 nav.addEventListener('click',e=>{const link=e.target.closest('a');if(link){if(link.getAttribute('href')===location.hash){e.preventDefault();window.scrollTo({top:0,behavior:reduced.matches?'instant':'smooth'});}manual=false;motion.request();}});
 brand.addEventListener('click',e=>{if(location.hash==='#overview'){e.preventDefault();window.scrollTo({top:0,behavior:reduced.matches?'instant':'smooth'});}});
 window.addEventListener('resize',invalidateLayout,{passive:true});window.addEventListener('hashchange',()=>{manual=false;lastY=scrollY;invalidateLayout();});reduced.addEventListener('change',motion.request);document.fonts?.ready.then(invalidateLayout);
 new MutationObserver(invalidateLayout).observe(nav,{subtree:true,attributes:true,attributeFilter:['aria-current']});motion.request();
})();
