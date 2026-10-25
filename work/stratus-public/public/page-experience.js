'use strict';
(()=>{
 const body=document.body,root=document.documentElement,motion=window.StratusMotion,reduced=matchMedia('(prefers-reduced-motion: reduce)');if(!motion)return;
 const veil=document.createElement('div');veil.className='page-transition-veil';veil.setAttribute('aria-hidden','true');body.append(veil);let serial=0,effects=[];
 const disabled=()=>reduced.matches||body.classList.contains('effects-paused');
 function cancel(){for(const effect of effects)effect.cancel();effects=[];body.classList.remove('page-switching');root.dataset.pageTransition='idle';}
 function settled(){cancel();window.dispatchEvent(new CustomEvent('stratus:route-changed',{detail:{phase:'settled'}}));}
 window.StratusPageTransition=async({from,to,apply,direction})=>{
  const run=++serial;cancel();if(!from||from===to||disabled()){apply();settled();return;}
  root.dataset.pageTransition='leaving';
  const wash=veil.animate([{opacity:0,transform:`translateX(${-direction*110}%) skewX(${-direction*12}deg)`},{opacity:.5,offset:.37},{opacity:0,transform:`translateX(${direction*120}%) skewX(${-direction*12}deg)`}],{duration:850,easing:'cubic-bezier(.25,.5,.2,1)',fill:'both'});
  const leaving=from.animate([{opacity:1,transform:'translate3d(0,0,0) scale(1)'},{opacity:0,transform:`translate3d(${-direction*20}px,-8px,0) scale(.992)`}],{duration:190,easing:'cubic-bezier(.4,0,1,1)',fill:'both'});effects=[wash,leaving];
  await leaving.finished.catch(()=>{});if(run!==serial)return;if(disabled()){apply();settled();return;}
  body.classList.add('page-switching');apply();root.dataset.pageTransition='entering';
  const arrival=to.animate([{opacity:0,transform:`translate3d(${direction*38}px,18px,0) scale(.985)`},{opacity:1,transform:`translate3d(${-direction*2}px,-1px,0) scale(1.002)`,offset:.78},{opacity:1,transform:'translate3d(0,0,0) scale(1)'}],{duration:680,easing:'cubic-bezier(.16,.8,.2,1)',fill:'both'});effects.push(arrival);
  await arrival.finished.catch(()=>{});if(run===serial)settled();
 };
 // Switching motion off mid-trip completes the route and removes the transient surfaces.
 new MutationObserver(()=>{if(disabled()&&effects.length)for(const effect of effects)effect.finish();}).observe(body,{attributes:true,attributeFilter:['class']});
 reduced.addEventListener('change',()=>{if(disabled())for(const effect of effects)effect.finish();});
 const header=document.querySelector('.topbar'),nav=header?.querySelector('nav'),feedback=nav?.querySelector('.feedback-nav'),viewport=nav?.querySelector('.nav-viewport');if(!feedback||!viewport)return;
 const orbit=document.createElement('span');orbit.className='feedback-orbit';orbit.setAttribute('aria-hidden','true');orbit.innerHTML=Array.from({length:6},(_,i)=>`<i style="--piece:${i}"></i>`).join('');header.append(orbit);let orbitDirty=true;
 function updateOrbit(){orbitDirty=true;motion.request();}
 motion.register('feedback-fragments',()=>{if(!orbitDirty)return undefined;orbitDirty=false;if(document.hidden||header.classList.contains('nav-splitting')||(header.classList.contains('nav-compact')&&feedback.getAttribute('aria-current')!=='page'))return null;const h=header.getBoundingClientRect(),b=feedback.getBoundingClientRect(),v=viewport.getBoundingClientRect();if(b.left<v.left-1||b.right>v.right+1)return null;return {x:b.left-h.left,y:b.top-h.top,w:b.width,h:b.height};},data=>{if(data===undefined)return;if(!data){orbit.style.opacity='0';return;}motion.style(orbit,'left',`${data.x}px`);motion.style(orbit,'top',`${data.y}px`);motion.style(orbit,'width',`${data.w}px`);motion.style(orbit,'height',`${data.h}px`);orbit.style.opacity='1';});
 new MutationObserver(updateOrbit).observe(header,{attributes:true,attributeFilter:['class','data-nav-page']});viewport.addEventListener('scroll',updateOrbit,{passive:true});nav.addEventListener('transitionend',updateOrbit);window.addEventListener('resize',updateOrbit,{passive:true});window.addEventListener('stratus:route-changed',updateOrbit);document.fonts?.ready.then(updateOrbit);updateOrbit();
})();
