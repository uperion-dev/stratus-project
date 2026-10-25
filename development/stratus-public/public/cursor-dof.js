'use strict';
// Cursor is the focal point. Reuse the shared frame scheduler; no pixel sampling or idle loop.
(()=>{
 const motion=window.StratusMotion;if(!motion||!matchMedia('(hover:hover) and (pointer:fine)').matches)return;
 const layer=document.createElement('div');layer.className='cursor-dof';layer.setAttribute('aria-hidden','true');document.body.append(layer);
 let point=null,dirty=false,active=false;
 const hide=()=>{active=false;dirty=true;motion.request();};
 window.addEventListener('pointermove',event=>{if(event.pointerType!=='mouse'||event.buttons)return;point={x:event.clientX,y:event.clientY};active=true;dirty=true;motion.request();},{passive:true});
 document.documentElement.addEventListener('pointerleave',hide);window.addEventListener('blur',hide);
 document.addEventListener('keydown',hide,{passive:true});document.addEventListener('focusin',event=>{if(event.target.matches('input,textarea,select,[contenteditable=true]'))hide();});
 document.addEventListener('visibilitychange',()=>{if(document.hidden)hide();});
 motion.register('cursor-depth-of-field',state=>{if(!dirty||state.hidden||state.navBusy)return null;dirty=false;return {point,active:active&&!state.paused};},data=>{if(!data)return;if(data.point){motion.style(layer,'--focus-x',`${data.point.x}px`);motion.style(layer,'--focus-y',`${data.point.y}px`);}layer.dataset.active=String(data.active);});
})();
