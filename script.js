// Simple JS: mobile nav toggle, smooth scroll, reveal on scroll
document.addEventListener('DOMContentLoaded', function(){
  // Nav toggle for small screens
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  if(btn){
    btn.addEventListener('click', ()=> {
      if(nav.style.display === 'block') nav.style.display = '';
      else nav.style.display = 'block';
    });
  }

  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function(e){
      e.preventDefault();
      const id = this.getAttribute('href').slice(1);
      const el = document.getElementById(id);
      if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
    });
  });

  // Reveal on scroll
  const revealEls = document.querySelectorAll('.reveal');
  const obs = new IntersectionObserver((entries)=> {
    entries.forEach(entry=>{
      if(entry.isIntersecting) entry.target.classList.add('visible');
    });
  }, {threshold: 0.12});
  revealEls.forEach(e => obs.observe(e));
});
