'use strict';
(() => {
 const status=document.querySelector('.copy-address-status');
 document.querySelectorAll('[data-copy-address]').forEach(button=>button.addEventListener('click',async()=>{
  try {await navigator.clipboard.writeText(button.dataset.copyAddress);status.textContent='Address copied.';}
  catch {status.textContent='Select the address above to copy it.';}
 }));
})();
