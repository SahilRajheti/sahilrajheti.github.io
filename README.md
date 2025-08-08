index.html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Sahil Rajheti — Portfolio</title>

  <!-- Inter font -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="css/style.css">

  <!-- Showdown (markdown -> html) for blog viewer -->
  <script src="https://cdn.jsdelivr.net/npm/showdown@1.9.1/dist/showdown.min.js" defer></script>

  <!-- Main JS -->
  <script defer src="js/script.js"></script>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="index.html">Sahil Rajheti</a>

      <nav class="nav" aria-label="Main navigation">
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="projects.html">Projects</a>
        <a href="blog.html">Blog</a>
        <a href="#contact">Contact</a>
      </nav>

      <button class="nav-toggle" aria-label="Toggle menu">☰</button>
    </div>
  </header>

  <main>
    <!-- HERO -->
    <section class="hero container" id="home">
      <div class="hero-left reveal">
        <img src="images/profile.png" alt="Sahil profile" class="profile-photo">
      </div>

      <div class="hero-right reveal">
        <h1>Hi, I'm <span class="accent">Sahil Rajheti</span></h1>
        <p class="lead">Web developer • Course creator • Learner</p>
        <p>I build responsive portfolio websites, small web apps (including an AI Chatbot integration), and easy-to-follow online courses. I use GitHub Pages to host projects and often test on my iPhone 14 Pro.</p>

        <p class="cta-row">
          <a class="btn" href="projects.html">View Projects</a>
          <a class="btn btn-outline" href="blog.html">Read Blog</a>
        </p>

        <p class="meta">
          Repo: <a href="https://github.com/sahilrajheti/sahilrajheti.github.io" target="_blank" rel="noopener">github.com/sahilrajheti/sahilrajheti.github.io</a>
        </p>
      </div>
    </section>

    <!-- ABOUT -->
    <section id="about" class="container about reveal">
      <h2>About Me</h2>
      <p>My name is <strong>Sahil Rajheti</strong>. I create portfolio websites, short courses (e.g., "How to Earn Money Online"), and tools to learn programming and web development. I enjoy making content that is simple and practical. I also explore projects like car tracking concepts (GPS learning) and small AI tools for chat experiences.</p>

      <p>I prefer a clean, modern UI with animations and smooth scrolling. I test my sites on mobile devices (iPhone 14 Pro) to ensure good performance and responsiveness.</p>

      <p><strong>Contact & Socials:</strong></p>
      <ul class="socials">
        <li><a href="mailto:youremail@example.com">youremail@example.com</a></li>
        <li><a href="https://www.linkedin.com/" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="https://twitter.com/" target="_blank" rel="noopener">Twitter</a></li>
        <li><a href="https://t.me/" target="_blank" rel="noopener">Telegram</a></li>
        <li><a href="https://instagram.com/" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="https://facebook.com/" target="_blank" rel="noopener">Facebook</a></li>
      </ul>
    </section>

    <!-- SKILLS -->
    <section id="skills" class="container skills">
      <h2 class="reveal">Skills</h2>
      <div class="skill-grid">
        <div class="skill-card reveal"><strong>HTML & CSS</strong><div class="small">Responsive layouts</div></div>
        <div class="skill-card reveal"><strong>JavaScript</strong><div class="small">DOM, fetch, UI</div></div>
        <div class="skill-card reveal"><strong>Git & GitHub</strong><div class="small">Pages hosting, repos</div></div>
        <div class="skill-card reveal"><strong>Design</strong><div class="small">UX & animations</div></div>
      </div>
    </section>

    <!-- LATEST PROJECT -->
    <section class="container latest reveal">
      <h2>Featured Project</h2>
      <div class="project-preview">
        <img src="images/project1.png" alt="Project preview">
        <div>
          <h3>Portfolio Template & Blog</h3>
          <p>A clean portfolio with a markdown-powered blog and a Formspree contact form. Replace sample content and publish to GitHub Pages.</p>
          <p><a class="btn" href="projects.html">See Projects</a></p>
        </div>
      </div>
    </section>

    <!-- CONTACT -->
    <section id="contact" class="container contact reveal">
      <h2>Contact Me</h2>
      <p>If you'd like to collaborate, hire me, or ask something — send a message:</p>

      <!-- Formspree form (replace action with your Formspree URL or email) -->
      <form id="contactForm" action="https://formspree.io/f/yourformid" method="POST" class="contact-form">
        <label>
          <span>Name</span>
          <input name="name" type="text" placeholder="Your name" required>
        </label>

        <label>
          <span>Email</span>
          <input name="email" type="email" placeholder="youremail@example.com" required>
        </label>

        <label>
          <span>Message</span>
          <textarea name="message" rows="5" placeholder="Write your message..." required></textarea>
        </label>

        <div class="form-row">
          <button class="btn" type="submit">Send Message</button>
          <button type="button" id="clearForm" class="btn btn-outline">Clear</button>
        </div>

        <p id="formMsg" class="muted" role="status" aria-live="polite"></p>
      </form>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>© 2025 <strong>Sahil Rajheti</strong> · <a href="https://sahilrajheti.github.io" target="_blank" rel="noopener">sahilrajheti.github.io</a></p>
    </div>
  </footer>
</body>
</html>
css./style
./* 
css/style.css 
- Dark modern responsive styles with reveal animations */
:root{
  --bg:#071226;
  --card:#0b1220;
  --muted:#9aa8bd;
  --accent:#60a5fa;
  --text:#e6eef8;
  --glass: rgba(255,255,255,0.02);
  --radius:12px;
  --container:1100px;
  font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Arial;
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
}
*{box-sizing:border-box}
html,body{height:100%;margin:0;background:linear-gradient(180deg,#071024 0%, #07162a 100%);color:var(--text)}
a{color:var(--accent);text-decoration:none}
.container{max-width:var(--container);margin:0 auto;padding:28px}
.site-header{position:sticky;top:0;z-index:40;background:transparent;padding:10px 0}
.header-inner{display:flex;align-items:center;justify-content:space-between}
.brand{font-weight:700;color:var(--text);text-decoration:none}
.nav a{margin-left:18px;color:var(--muted);text-decoration:none;font-weight:600}
.nav-toggle{display:none;background:transparent;border:0;color:var(--text);font-size:22px}

/* Hero */
.hero{display:flex;gap:28px;align-items:center;padding:46px 0}
.profile-photo{width:160px;height:160px;border-radius:18px;object-fit:cover;border:4px solid rgba(255,255,255,0.04)}
.hero-right h1{font-size:32px;margin:0}
.lead{color:var(--muted);margin-top:6px}
.cta-row{margin-top:12px}
.btn{display:inline-block;padding:10px 16px;border-radius:10px;background:var(--accent);color:#04203a;text-decoration:none;font-weight:700;margin-right:8px}
.btn-outline{background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--text)}

/* Sections */
.about, .skills, .latest, .contact{margin-top:28px;padding:20px;background:var(--glass);border-radius:12px}
.skill-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin-top:12px}
.skill-card{padding:18px;border-radius:10px;background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);text-align:center}
.small{color:var(--muted);font-size:13px;margin-top:6px}

/* Project preview */
.project-preview{display:flex;gap:18px;align-items:center}
.project-preview img{width:220px;height:140px;object-fit:cover;border-radius:8px}
.project-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:18px}
.project-card img{width:100%;height:140px;object-fit:cover;border-radius:8px}

/* Contact form */
.contact-form label{display:block;margin-bottom:12px}
.contact-form span{display:block;margin-bottom:6px;color:var(--muted)}
.contact-form input, .contact-form textarea{width:100%;padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:var(--text)}
.form-row{display:flex;gap:12px;align-items:center;margin-top:8px}
.muted{color:var(--muted);margin-top:8px}
.socials{list-style:none;padding:0;margin:8px 0 0 0;display:flex;gap:12px;flex-wrap:wrap}
.socials a{color:var(--muted)}

/* Footer */
.site-footer{padding:18px 0;text-align:center;color:var(--muted);margin-top:36px}

/* Reveal animation */
.reveal{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease}
.reveal.visible{opacity:1;transform:none}

/* Small screens */
@media (max-width:820px){
  .hero{flex-direction:column;text-align:center}
  .nav{display:none}
  .nav-toggle{display:block}
  .profile-photo{width:140px;height:140px}
  .header-inner{gap:12px}
}js/script.js// js/script.js
document.addEventListener('DOMContentLoaded', () => {
  // Nav toggle for mobile
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  if (btn) {
    btn.addEventListener('click', () => {
      if (!nav) return;
      nav.style.display = nav.style.display === 'block' ? '' : 'block';
    });
  }

  // Smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      const id = this.getAttribute('href').slice(1);
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  // Reveal on scroll using IntersectionObserver
  const revealEls = document.querySelectorAll('.reveal');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(e => obs.observe(e));

  // Contact form: simple UX messages (Formspree does submission)
  const form = document.getElementById('contactForm');
  const formMsg = document.getElementById('formMsg');
  const clearBtn = document.getElementById('clearForm');
  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      form.reset();
      formMsg.textContent = '';
    });
  }
  if (form) {
    form.addEventListener('submit', (e) => {
      // Let Formspree handle the POST; show friendly message immediately
      formMsg.textContent = 'Sending…';
      // After short delay, show success hint (Formspree will also respond)
      setTimeout(() => {
        formMsg.textContent = 'If everything is correct, your message is being sent. Check your email inbox for replies.';
        form.reset();
      }, 800);
    });
  } B
});
markdown
b # How I built my first portfolio

**Published:** 2025-08-08

This is a sample blog post in Markdown. Add more posts by creating `.md` files inside `blog/posts/`.  
Use `#` for headings and **bold** for emphasis.

## Tips
- Keep images small (web-optimized)
- Use descriptive filenames like `2025-08-08-post-title.md`
- Push the files to GitHub and they'll be available on your site


