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
 const sections=document.querySelectorAll('.immersive-hero,.spatial-journey,.water-story,.public-faq,.public-view>.section-intro');
 const observer=new IntersectionObserver(entries=>entries.forEach(({target,isIntersecting})=>target.classList.toggle('blocks-visible',isIntersecting)),{rootMargin:'60px'});
 sections.forEach((section,index)=>{
  section.classList.add('block-scene');
  const cluster=document.createElement('div');cluster.className='site-block-cluster';cluster.setAttribute('aria-hidden','true');
  cluster.innerHTML=['stone','grass','oak'].map((kind,i)=>`<span class="minecraft-block cluster-block cluster-block-${i}" style="--drift-delay:${-index-i*2}s">${cube(kind)}</span>`).join('');
  section.append(cluster);observer.observe(section);
 });
 // A seeded scatter stays stable across visits and avoids the reading column.
 let seed=314159;
 const random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296;};
 document.querySelectorAll('[data-view],.immersive-hero').forEach(view=>{
  view.classList.add('scatter-scene');
  const field=document.createElement('div');field.className='block-scatter';field.setAttribute('aria-hidden','true');
  const hero=view.matches('.immersive-hero');
  // Uneven gaps and independently placed sides keep the field natural while
  // retaining stable positions and leaving the reading column unobstructed.
  const layout=hero?[[0,13],[1,32],[0,64],[1,85]]:[[0,3],[1,7],[0,14],[1,16],[1,24],[0,30],[1,36],[0,39],[0,46],[1,52],[0,56],[1,65],[0,71],[1,74],[0,82],[1,88],[0,93],[1,97]];
  field.innerHTML=layout.map(([side,y])=>`<span class="minecraft-block scattered-block scatter-${side}" style="--scatter-y:${y+(random()-.5)*1.8}%;--scatter-x:${random()*2.4}%;--scatter-size:${48+random()*28}px;--block-angle:${random()*20-10}deg;--drift-delay:${-random()*8}s">${cube(['grass','stone','oak'][Math.floor(random()*3)])}</span>`).join('');
  view.append(field);observer.observe(view);
 });

})();
