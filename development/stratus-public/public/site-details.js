'use strict';
(() => {
 // Add a consistent typographic accent without changing any copy.
 const headingSelector='.section-intro h1,.home-heading h2,.water-story h2,.public-faq h2,.release-content h2,.spec-section h2,.upcoming-item h2,.shot-name h2,.workspace-card h3';
 function accentHeadings(){document.querySelectorAll(headingSelector).forEach(heading=>{
  if(heading.children.length)return;
  const text=heading.textContent.trim(),split=text.lastIndexOf(' ');
  if(split<0)return;
  heading.textContent=text.slice(0,split)+' ';
  const accent=document.createElement('em');accent.className='type-accent';accent.textContent=text.slice(split+1);heading.append(accent);
 });}
 accentHeadings();
 // The release feed replaces its own cards after initial load.
 const updates=new MutationObserver(()=>{updates.disconnect();accentHeadings();updates.observe(document.querySelector('main'),{childList:true,subtree:true});});
 updates.observe(document.querySelector('main'),{childList:true,subtree:true});
 // Equal square faces share one edge length and meet at half-edge Z offsets.
 const cube=kind=>`<span class="block-model block-${kind}">${['front','right','back','left','top','bottom'].map(face=>`<span class="block-face face-${face}"></span>`).join('')}</span>`;
 const observer=new IntersectionObserver(entries=>entries.forEach(({target,isIntersecting})=>target.classList.toggle('blocks-visible',isIntersecting)),{rootMargin:'60px'});
 // Scale the number of blocks to the visible page height, with irregular spacing.
 document.querySelectorAll('[data-view]').forEach((view,index)=>{
  view.classList.add('scatter-scene');
  const field=document.createElement('div');field.className='block-scatter';field.setAttribute('aria-hidden','true');view.append(field);observer.observe(view);
  let previousCount=-1;
  const update=()=>{
   const height=view.offsetHeight;if(!height)return;
   const count=Math.max(2,Math.min(18,Math.floor(height/230)));
   if(count===previousCount)return;previousCount=count;
   let seed=(314159+index*7919)>>>0;
   const random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;};
   const items=[];
   for(let side=0;side<2;side++){
    const n=Math.floor(count/2)+(side<count%2?1:0);
    for(let i=0;i<n;i++){
     const y=5+90*(i+.18+random()*.64)/n;
     items.push(`<span class="minecraft-block scattered-block scatter-${side}" style="--scatter-y:${y}%;--scatter-x:${random()*5}%;--scatter-size:${48+random()*28}px;--block-angle:${random()*20-10}deg;--drift-delay:${-random()*8}s">${cube(['grass','stone','oak'][Math.floor(random()*3)])}</span>`);
    }
   }
   field.innerHTML=items.join('');
  };
  new ResizeObserver(update).observe(view);update();
 });

})();
