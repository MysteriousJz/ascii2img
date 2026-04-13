import os
import json

HELLO_WORLD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>BetWithMe — Live!</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
    :root{font-family:system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial;}
    body{margin:0;background:#f6f7fb;color:#111;display:flex;min-height:100vh;align-items:flex-start;justify-content:center;padding:40px 16px;}
    .shell{width:100%;max-width:980px;background:#fff;border:1px solid #e3e6ef;border-radius:10px;box-shadow:0 6px 24px rgba(20,24,50,0.06);overflow:visible;}
    header{padding:20px 28px;border-bottom:1px solid #eef0fb}
    h1{margin:0;font-size:18px}
    nav{display:flex;gap:10px;justify-content:center;padding:18px 18px;border-bottom:1px solid #f0f3ff;background:#fbfcff;}
    nav a{padding:10px 14px;border-radius:8px;border:1px solid #d8def8;text-decoration:none;color:#0b3b84;background:transparent}
    nav a.active{background:#0b3b84;color:#fff;border-color:#0b3b84}
    main{padding:24px;}
    .page{display:none}
    .page.active{display:block}
    .placeholder{min-height:220px;border:1px dashed #e6e9fb;border-radius:8px;padding:16px;background:#fbfdff;}
    footer{padding:14px 18px;border-top:1px solid #eef0fb;font-size:13px;color:#556}
    .center{display:flex;justify-content:center;align-items:center}

    /* Carousel styles */
    .carousel{display:flex;flex-direction:column;gap:12px;align-items:center}
    .carousel-viewport{width:100%;max-width:880px;border-radius:6px;overflow:hidden;background:#fff;border:1px solid #eef2ff}
    .carousel-viewport img{display:block;width:100%;height:auto}
    .controls{display:flex;gap:8px;align-items:center}
    .btn{background:#0b3b84;color:#fff;border:0;padding:8px 12px;border-radius:6px;cursor:pointer}
    .meta{font-size:13px;color:#445;margin-top:6px}
    select{margin-bottom:12px;padding:8px;border:1px solid #d8def8;border-radius:6px;background:#fff}

    /* ASCII art image container — scrolls vertically on tall images */
    .ascii-art-container {
        width: 100%;
        max-height: 70vh;
        overflow-y: auto;
        overflow-x: hidden;
        -webkit-overflow-scrolling: touch; /* smooth touch scrolling on iOS */
        margin: 0 auto;
        border: 1px solid #eef0fb;
        background: #fbfdff;
        border-radius: 8px;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.02);
        text-align: center;
    }

    /* The image itself: never upscale, always centered, preserves 1:1 pixel ratio */
    .ascii-img {
        display: block;
        max-width: 100%;
        height: auto;
        /* Images are generated at 2× for Retina; halving via max-width keeps them sharp */
        margin: 0 auto;
        image-rendering: -webkit-optimize-contrast; /* crisp on WebKit */
        image-rendering: crisp-edges;
    }

    /* Fallback text shown only when image fails to load */
    .ascii-fallback {
        display: none;
        color: #778;
        font-style: italic;
        padding: 24px;
        margin: 0;
    }

    /* On small screens the 50%-width rule may make images too small — let them expand */
    @media (max-width: 768px) {
        .ascii-art-container {
            max-height: 60vh;
        }
        .ascii-img {
            width: 100%;
        }
    }
  </style>
</head>
<body>
  <div class="shell" role="application" aria-label="BetWithMe dashboard">
    <header>
      <h1>Bet With Me -- LIVE!! Follow along my journey to doing what cannot be done!</h1>
    </header>

    <div style="text-align: center; margin-bottom: 15px;">
        <img src="/static/und.gif" alt="Under Construction"
       style="max-width: 100%; height: auto;">
    </div>


    <nav id="menu" aria-label="Main menu" class="center">
      <a href="#price" data-page="price" id="link-price">Price Graphs</a>
      <a href="#holdings" data-page="holdings" id="link-holdings">Holdings & Results</a>
      <a href="#math" data-page="math" id="link-math">Taste of math</a>
      <a href="#about" data-page="about" id="link-about">About this project & me</a>
    </nav>

    <main>
      <section id="page-price" class="page active">
        <div class="placeholder">
          <div class="carousel" id="carousel">
            <select id="windowSelect">
              <option value="24">24h Window</option>
              <option value="14.83281573">14.83h Window</option>
              <option value="9.16718427">9.17h Window</option>
              <option value="5.66563146">5.67h Window</option>
              <option value="2.16407865">2.16h Window</option>
            </select>

            <div class="carousel-viewport" id="cvp">
              <img id="carousel-image" src="/static/placeholder.png" alt="price chart">
            </div>

            <div class="controls">
              <button class="btn" id="prevBtn" aria-label="Previous image">&larr; Prev</button>
              <button class="btn" id="nextBtn" aria-label="Next image">Next &rarr;</button>
            </div>

            <div class="meta" id="imgMeta"></div>
          </div>

          <p>Thank you for visiting my website! This is a display of price action with a visualization of what math my algorithm works with in its trading logic.</p>
        </div>
      </section>

      <section id="page-holdings" class="page">
        <div class="placeholder">
          <p>"Nothing outlives its usefulness."</p>
        </div>
      </section>

      <section id="page-math" class="page">
        <div class="ascii-art-container">
          <img src="/static/fibonacci_ladder.png"
               alt="Fibonacci Ladder and Math Concepts — Fibonacci ratios, regression, and averages"
               class="ascii-img"
               width="703" height="3032"
               onerror="this.style.display='none';this.nextElementSibling.style.display='block'">
          <p class="ascii-fallback">[ASCII art unavailable]</p>
        </div>
      </section>

      <section id="page-about" class="page">
      <div class="placeholder">
      <div style="text-align: center;">
        <p>This page is a space to "show my work" for a project that has been privately occuring for 9 years now.</p>
        <p>
         <p>The guiding principal this entire time is that the price always returns to the mean. Always.</p>
         </div>
        <div class="ascii-art-container">
          <img src="/static/trading_pipeline.png"
               alt="The Trading Pipeline — data layers from raw market data to strategy execution"
               class="ascii-img"
               width="712" height="860"
               onerror="this.style.display='none';this.nextElementSibling.style.display='block'">
          <p class="ascii-fallback">[ASCII art unavailable]</p>
        </div>
         <div style="text-align: center;">
         <p>I am leaving talismans of hope in symbols on the website for good luck!</p>
         </div>
      <div style="font-size: 326px; font-family: monospace; text-align: center;">
  ☯
</div>
        <div class="ascii-art-container" style="max-height:none;">
          <img src="/static/way_no_way.png"
               alt="Way No Way — status diagram"
               class="ascii-img"
               width="355" height="176"
               onerror="this.style.display='none';this.nextElementSibling.style.display='block'">
          <p class="ascii-fallback">[ASCII art unavailable]</p>
        </div>
        <div style="font-size:21px; font-family:monospace; text-align:center;">
䷀ ䷁ ䷂ ䷃ ䷄ ䷅ ䷆ ䷇<br>
䷈ ䷉ ䷊ ䷋ ䷌ ䷍ ䷎ ䷏<br>
䷐ ䷑ ䷒ ䷓ ䷔ ䷕ ䷖ ䷗<br>
䷘ ䷙ ䷚ ䷛ ䷜ ䷝ ䷞ ䷟<br>
䷠ ䷡ ䷢ ䷣ ䷤ ䷥ ䷦ ䷧<br>
䷨ ䷩ ䷪ ䷫ ䷬ ䷭ ䷮ ䷯<br>
䷰ ䷱ ䷲ ䷳ ䷴ ䷵ ䷶ ䷷<br>
䷸ ䷹ ䷺ ䷻ ䷼ ䷽ ䷾ ䷿
</div>

      </section>
    </main>

    <footer class="center">
      <small>Congratulations!! You are vistor #{{VISITOR_COUNT}}, that means you win!</small>
    </footer>
  </div>

  <script>
    (function(){
      /* --- image groups by window --- */
      {{IMAGE_GROUPS}}

      var currentWindow = "24";
      var images = imageGroups[currentWindow] || [];
      var idx = 0;
      var imgEl = document.getElementById('carousel-image');
      var metaEl = document.getElementById('imgMeta');
      var selectEl = document.getElementById('windowSelect');

      function update(){
        if(images.length === 0) return;
        var src = images[idx];
        imgEl.src = src;
        metaEl.textContent = "Image " + (idx+1) + " of " + images.length + " — " + src.replace('/static/','');
        // preload neighbors
        var n1 = new Image(); n1.src = images[(idx+1)%images.length];
        var p1 = new Image(); p1.src = images[(idx-1+images.length)%images.length];
      }

      selectEl.addEventListener('change', function(){
        currentWindow = selectEl.value;
        images = imageGroups[currentWindow] || [];
        idx = 0;
        update();
      });

      document.getElementById('nextBtn').addEventListener('click', function(){ if(images.length>0){ idx = (idx+1)%images.length; update(); }});
      document.getElementById('prevBtn').addEventListener('click', function(){ if(images.length>0){ idx = (idx-1+images.length)%images.length; update(); }});
      // keyboard support
      window.addEventListener('keydown', function(e){ if(images.length>0 && e.key === 'ArrowRight') { idx=(idx+1)%images.length; update(); } else if(images.length>0 && e.key==='ArrowLeft'){ idx=(idx-1+images.length)%images.length; update(); }});
      // init
      if(images.length>0) update();

      /* --- page routing --- */
      function show(page){
        document.querySelectorAll('.page').forEach(function(s){s.classList.remove('active')});
        document.querySelectorAll('nav a').forEach(function(a){a.classList.remove('active')});
        var p = document.getElementById('page-'+page);
        var l = document.getElementById('link-'+page);
        if(p) p.classList.add('active');
        if(l) l.classList.add('active');
      }
      function route(){
        var hash = (location.hash||'#about').replace('#','') || 'about';
        show(hash);
      }
      window.addEventListener('hashchange', route, false);
      document.addEventListener('DOMContentLoaded', route, false);
    })();
  </script>
</body>
</html>"""

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')

    # Serve static assets from /static/ (images in root and subdirectories)
    if path.startswith('/static/'):
        file_path = path[1:]  # Remove leading /
        # Prevent directory traversal
        safe_path = os.path.normpath(file_path)
        if not safe_path.startswith('static'):
            start_response("403 Forbidden", [("Content-Type", "text/plain")])
            yield b"Forbidden"
            return
        content_type_map = {
            '.png': 'image/png',
            '.gif': 'image/gif',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.ico': 'image/x-icon',
        }
        ext = os.path.splitext(safe_path)[1].lower()
        if os.path.isfile(safe_path) and ext in content_type_map:
            with open(safe_path, 'rb') as f:
                data = f.read()
            start_response("200 OK", [("Content-Type", content_type_map[ext])])
            yield data
            return
        else:
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            yield b"Not found"
            return

    # Visitor counter: read, increment, write
    counter_file = 'counter.txt'
    try:
        if os.path.exists(counter_file):
            with open(counter_file, 'r') as f:
                count = int(f.read().strip()) + 1
        else:
            count = 1
        with open(counter_file, 'w') as f:
            f.write(str(count))
    except (ValueError, IOError):
        count = 0  # Fallback if file issues

    # Scan static/ for images and group by window
    static_dir = 'static'
    image_groups = {}
    if os.path.exists(static_dir):
        for f in os.listdir(static_dir):
            if f.endswith('.png') and 'h_' in f:
                parts = f.split('h_', 1)
                if len(parts) == 2:
                    window = parts[0]
                    try:
                        timestamp = int(parts[1].replace('.png', ''))
                        if window not in image_groups:
                            image_groups[window] = []
                        image_groups[window].append((timestamp, f"/static/{f}"))
                    except ValueError:
                        continue  # Skip bad filenames

    # Sort each group by timestamp (ascending for logical order)
    for window in image_groups:
        image_groups[window].sort(key=lambda x: x[0])
        image_groups[window] = [path for ts, path in image_groups[window]]

    print("Found image_groups:", image_groups)  # Debug

    # Generate JS object safely
    js_groups = "var imageGroups = " + json.dumps(image_groups) + ";"

    # Inject into HTML
    content = HELLO_WORLD.replace('{{IMAGE_GROUPS}}', js_groups).replace('{{VISITOR_COUNT}}', f'Visitor count: {count}')
    content_bytes = content.encode("utf-8")
    headers = [
      ("Content-Type", "text/html; charset=utf-8"),
      ("Content-Length", str(len(content_bytes))),
      ("Strict-Transport-Security", "max-age=63072000; includeSubDomains; preload"),
      ("X-Content-Type-Options", "nosniff"),
      ("Content-Security-Policy", "default-src 'self'; img-src 'self' https: data:; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"),
    ]
    start_response("200 OK", headers)
    yield content_bytes
