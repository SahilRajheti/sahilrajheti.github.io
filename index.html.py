<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sahil Rajheti | Portfolio</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: #f4f4f4;
      color: #222;
      scroll-behavior: smooth;
    }
    header {
      text-align: center;
      background: #000;
      color: #fff;
      padding: 30px 10px;
    }
    header img {
      width: 150px;
      border-radius: 50%;
      margin: 10px 0;
    }
    section {
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
    }
    h2 {
      border-left: 5px solid #333;
      padding-left: 10px;
      margin-bottom: 15px;
    }
    .skills span {
      background: #eee;
      margin: 5px;
      padding: 6px 12px;
      display: inline-block;
      border-radius: 20px;
    }
    .social a {
      margin: 0 10px;
      text-decoration: none;
      color: #0073e6;
    }
    .project, .blog {
      background: #fff;
      padding: 15px;
      margin: 15px 0;
      border-left: 4px solid #0073e6;
      border-radius: 8px;
    }
    footer {
      text-align: center;
      background: #000;
      color: #fff;
      padding: 20px;
      margin-top: 50px;
    }
    @media (max-width: 600px) {
      header h1 {
        font-size: 22px;
      }
    }

    /* Reveal Animation */
    .reveal {
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.6s ease;
    }
    .reveal.active {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body>

<header>
  <h1>Sahil Rajheti</h1>
  <p>Cloud Developer • GitHub Expert • Web Designer</p>
  <img src="your-image.jpg" alt="Sahil Rajheti" />
</header>

<section class="reveal">
  <h2>About Me</h2>
  <p>Hi! I’m Sahil Rajheti, a passionate web developer and cloud enthusiast. I specialize in creating responsive websites, handling GitHub projects, and automating cloud workflows. Based in Gujarat, India — I build websites that work beautifully on every device.</p>
</section>

<section class="skills reveal">
  <h2>Skills</h2>
  <span>HTML</span>
  <span>CSS</span>
  <span>JavaScript</span>
  <span>GitHub</span>
  <span>Cloud Computing</span>
  <span>Python</span>
</section>

<section class="reveal">
  <h2>Projects</h2>
  <div class="project">
    <h3>Portfolio Website</h3>
    <p>My personal responsive portfolio built with HTML, CSS, and animations.</p>
    <a href="https://sahilrajhetii.github.io" target="_blank">View Project</a>
  </div>
</section>

<section class="reveal">
  <h2>Blog</h2>
  <div class="blog">
    <h3>How I Built My First Website</h3>
    <p>Step-by-step guide I followed to create my first ever portfolio site using GitHub Pages.</p>
  </div>
</section>

<section class="reveal">
  <h2>Contact Me</h2>
  <p>Email: <a href="mailto:sahilkhan701766@gmail.com">sahilkhan701766@gmail.com</a></p>
  <div class="social">
    <a href="https://x.com/Sahil_Rajheti" target="_blank">X (Twitter)</a> |
    <a href="https://in.linkedin.com/in/sahil-rajheti-46853029b" target="_blank">LinkedIn</a> |
    <a href="https://t.me/sahil_rajheti" target="_blank">Telegram</a> |
    <a href="https://www.instagram.com/sahil_rajheti" target="_blank">Instagram</a> |
    <a href="https://www.facebook.com/sahil.rajheti" target="_blank">Facebook</a>
  </div>
</section>

<footer>
  © 2025 Sahil Rajheti Webworks — All rights reserved.
</footer>

<script>
  // Reveal animation
  const reveals = document.querySelectorAll(".reveal");
  window.addEventListener("scroll", () => {
    for (let box of reveals) {
      const boxTop = box.getBoundingClientRect().top;
      if (boxTop < window.innerHeight - 100) {
        box.classList.add("active");
      }
    }
  });
</script>

</body>
</html>