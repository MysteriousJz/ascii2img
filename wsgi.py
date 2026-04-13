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

    /* ASCII art: monospace prevents box-drawing character misalignment */
    pre{font-family:monospace;white-space:pre;}

    /* Scroll container: horizontal scroll for wide ASCII content on mobile */
    .ascii-container{overflow-x:auto;-webkit-overflow-scrolling:touch;}
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
        <div class="ascii-container">
        <pre>


    ███████╗██╗██████╗  ██████╗ ███╗   ██╗ █████╗  ██████╗ ██████╗██╗
    ██╔════╝██║██╔══██╗██╔═══██╗████╗  ██║██╔══██╗██╔════╝██╔════╝██║
    █████╗  ██║██████╔╝██║   ██║██╔██╗ ██║███████║██║     ██║     ██║
    ██╔══╝  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══██║██║     ██║     ██║
    ██║     ██║██████╔╝╚██████╔╝██║ ╚████║██║  ██║╚██████╗╚██████╗██║
    ╚═╝     ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚═╝

╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                    HOW φ COMES FROM FIBONACCI                               ║
║                                                                             ║
║   Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...           ║
║                                                                             ║
║   As you go higher, each pair's ratio approaches φ = 1.6180339...           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║   f(n+1) / f(n)  →  approaches φ from below and above                       ║
║                                                                             ║
║        5 / 3   = 1.666666                                                   ║
║        8 / 5   = 1.6                                                        ║
║       13 / 8   = 1.625                                                      ║
║       21 / 13  = 1.615384                                                   ║
║       34 / 21  = 1.619047                                                   ║
║       55 / 34  = 1.617647                                                   ║
║       89 / 55  = 1.618181                                                   ║
║      144 / 89  = 1.617977                                                   ║
║      233 / 144 = 1.618055                                                   ║
║      377 / 233 = 1.618025                                                   ║
║      610 / 377 = 1.618037                                                   ║
║                                                                             ║
║                         ↓                                                   ║
║                     φ = 1.6180339887...                                     ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║   THE FULL FAMILY:  f(n) / f(n+y)  and  f(n+y) / f(n)                       ║
║                                                                             ║
║   With two Fibonacci numbers, this ratio process lead to                    ║
║   42 magic numbers in the following list.                                   ║
║                                                                             ║
║   Example with y = 1 (adjacent numbers):                                    ║
║                                                                             ║
║        f(n) / f(n+1)  →  0.6180339  (1/φ)                                   ║
║        f(n+1) / f(n)  →  1.6180339  (φ)                                     ║
║                                                                             ║
║   Example with y = 2 (skip one):                                            ║
║                                                                             ║
║        f(n) / f(n+2)  →  0.381966   (1/φ²)                                  ║
║        f(n+2) / f(n)  →  2.6180339  (φ²)                                    ║
║                                                                             ║
║   Example with y = 3 (skip two):                                            ║
║                                                                             ║
║        f(n) / f(n+3)  →  0.236067   (1/φ³)                                  ║
║        f(n+3) / f(n)  →  4.2360679  (φ³)                                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

    ██╗  ██╗██████╗     ███╗   ███╗ █████╗  ██████╗ ██╗ ██████╗     ██╗ ██╗
    ██║  ██║╚════██╗    ████╗ ████║██╔══██╗██╔════╝ ██║██╔════╝    ████████╗
    ███████║ █████╔╝    ██╔████╔██║███████║██║  ███╗██║██║         ╚██╔═██╔╝
    ╚════██║██╔═══╝     ██║╚██╔╝██║██╔══██║██║   ██║██║██║         ████████╗
         ██║███████╗    ██║ ╚═╝ ██║██║  ██║╚██████╔╝██║╚██████╗    ╚██╔═██╔╝
         ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝     ╚═╝ ╚═╝

┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   0.0000014071683973                                                        │
│   0.0000022768462946                                                        │
│   0.0000036840146919                                                        │
│   0.0000059608609865                                                        │
│   0.0000096448756784                                                        │
│   0.0000156057366650                                                        │
│   0.0000252506123434                                                        │
│   0.0000408563490084                                                        │
│   0.0000661069613519                                                        │
│   0.0001069633104                                                           │
│   0.0001730702717                                                           │
│   0.0002800335821                                                           │
│   0.0004531038538                                                           │
│   0.0007331374359                                                           │
│   0.00118624129                                                             │
│   0.0019193787255                                                           │
│   0.003105620015142                                                         │
│   0.005024998740642                                                         │
│   0.008130618755784                                                         │
│   0.013155617496426                                                         │
│   0.021286236252211                                                         │
│   0.034441853748637                                                         │
│   0.055728090000847                                                         │
│   0.090169943749484                                                         │
│   0.145898033750331                                                         │
│   0.236067977499817                                                         │
│   0.381966011250141                                                         │
│   0.618033988749989                                                         │
│   1.6180339889579                                                           │
│   2.6180339889579                                                           │
│   4.2360679779158                                                           │
│   6.85410196687371                                                          │
│   11.0901699447895                                                          │
│   17.9442719116632                                                          │
│   29.0344418564527                                                          │
│   46.9787137681159                                                          │
│   76.0131556174964                                                          │
│   122.991869381244                                                          │
│   199.005024998741                                                          │
│   321.996894379985                                                          │
│   521.001919378725                                                          │
│   842.99881375871                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*******************************************************************************
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


██████╗ ███████╗ ██████╗ ██████╗ ███████╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝ ██╔══██╗██╔════╝██╔════╝██╔════╝██║██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║  ███╗██████╔╝█████╗  ███████╗███████╗██║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║   ██║██╔══██╗██╔══╝  ╚════██║╚════██║██║██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╔╝██║  ██║███████╗███████║███████║██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝


+-----------------------------------------------------------------------------+
|                                                                             |
|                              LINEAR REGRESSION                              |
|                   (Drawing the equidistant line to all data)                |
|                                                                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|   The format to draw a straight line follows this forumla:                  |
|                                                                             |
|   The line:  y  =  mx + b                                                   |
|              ↑     ↑  ↑                                                     |
|              │     │  └─ where line crosses y-axis (intercept)              |
|              │     └──── how steep the line is (slope)                      |
|              └────────── output relevant implication                        |
|                                                                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|   THE SLOPE (m) tells us:                                                   |
|                                                                             |
|     • positive slope  →  line goes up    ↗   (prices increasing)            |
|     • negative slope  →  line goes down  ↘   (prices decreasing)            |
|     • zero slope      →  line is flat    →   (prices flat)                  |
|                                                                             |
|   Bigger slope = steeper line = faster change                               |
|                                                                             |
+-----------------------------------------------------------------------------+
|                                                                             |
|   VISUAL EXAMPLES:                                                          |
|   The data points here form an easily identifiable line through them.       |
|                                                                             |
|      Price  ▲                              x                                |
|           90├                     x       x   x                             |
|             │                x       x  x                                   |
|           80├             x        x                                        |
|             │           x     x  x                                          |
|           70├     x       x    x                                            |
|             │  x      x                                                     |
|           60├x                                                              |
|             │     x                                                         |
|             └────┬────┬────┬────┬────┬────┬────┬► Time                      |
|                  1    2    3    4    5    6    7                            |
|                                                                             |
|   This upward line shows prices increasing over this period of time.        |
|                                                                             |
|      Price  ▲                                                               |
|           90├x    x                                                         |
|             │   x  x   x                                                    |
|           80├  x     x    x  x                                              |
|             │       x   x   x   x   x                                       |
|           70├          x      x    x  x   x                                 |
|             │               x    x   x      x                               |
|           60├                           x     x                             |
|             │                                                               |
|             └────┬────┬────┬────┬────┬────┬────┬► Time                      |
|                  1    2    3    4    5    6    7                            |
|                                                                             |
|   This downward line shows prices decreasing over this period of time.      |
+-----------------------------------------------------------------------------+

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*******************************************************************************
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

     █████╗ ██╗   ██╗███████╗██████╗  █████╗  ██████╗ ███████╗███████╗
    ██╔══██╗██║   ██║██╔════╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝██╔════╝
    ███████║██║   ██║█████╗  ██████╔╝███████║██║  ███╗█████╗  ███████╗
    ██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══██║██║   ██║██╔══╝  ╚════██║
    ██║  ██║ ╚████╔╝ ███████╗██║  ██║██║  ██║╚██████╔╝███████╗███████║
    ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                             THE AVERAGE                                     ┃
┃                                                                             ┃
┃   An average is one number that stands in for many.                         ┃
┃                                                                             ┃
┃   It is the center. The middle. The balance point.                          ┃
┃                                                                             ┃
┃   If all things were equal, they would each be the average.                 ┃
┃                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                             ┃
┃   GIVEN: a, b, c, d, e ...                                                  ┃
┃                                                                             ┃
┃   STEP 1:      a + b + c + d + e + ... = S                                  ┃
┃                                                                             ┃
┃   STEP 2:      S ÷ N = A                                                    ┃
┃                                                                             ┃
┃   WHERE:                                                                    ┃
┃       N is how many things you started with                                 ┃
┃       A is the average                                                      ┃
┃                                                                             ┃
┃   THE AVERAGE SATISFIES:                                                    ┃
┃                                                                             ┃
┃       (a - A) + (b - A) + (c - A) + ... = 0                                 ┃
┃                                                                             ┃
┃   The deviations above cancel the deviations below.                         ┃
┃   It is the point where the seesaw balances.                                ┃
┃                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                             ┃
┃   EXAMPLE WITH NUMBERS:                                                     ┃
┃                                                                             ┃
┃   SET:        2, 4, 4, 4, 5, 5, 7, 9                                        ┃
┃                                                                             ┃
┃   STEP 1:     2 + 4 + 4 + 4 + 5 + 5 + 7 + 9 = 40                            ┃
┃                                                                             ┃
┃   STEP 2:     40 ÷ 8 = 5                                                    ┃
┃                                                                             ┃
┃   AVERAGE = 5                                                               ┃
┃                                                                             ┃
┃   CHECK:                                                                    ┃
┃       (2-5) + (4-5) + (4-5) + (4-5) + (5-5) + (5-5) + (7-5) + (9-5)         ┃
┃       = -3 + -1 + -1 + -1 + 0 + 0 + 2 + 4                                   ┃
┃       = 0                                                                   ┃
┃                                                                             ┃
┃   The negatives and positives cancel perfectly.                             ┃
┃   That is what an average does.                                             ┃
┃                                                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

        </pre>
        </div>
      </section>

      <section id="page-about" class="page">
      <div style="text-align: center;">
        <p>This page is a space to "show my work" for a project that has been privately occuring for 9 years now.</p>
        <p>
         <p>The guiding prinicipal this entire time is that the price always returns to the mean. Always.</p>
         </div>
                 <div class="ascii-container">
<pre>
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                         THE TRADING PIPELINE                                 ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║                           LAYER 0: RAW DATA                                  ║
║  ─────────────────────────────────────────────────────────────────────────── ║
║                                                                              ║
║    Live trades from exchange via websocket with RATE, QTY, TIME              ║
║    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓              ║
║    Dances with and is normalized by friends in the last 6 seconds.           ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║                      LAYER 1: MATHEMATICAL INDICATORS                        ║
║  ─────────────────────────────────────────────────────────────────────────── ║
║                                                                              ║
║    • Novel Regression-based support/resistance                               ║
║    • Fibonacci ladder divergence measure                                     ║
║    • RSI — Really Sustained Intention                                        ║
║    • Bollinger Bands — volatility envelopes                                  ║
║    • Cascading recent trend angles                                           ║
║                                                                              ║
║    21 indicators in total, calculated every 2 seconds                        ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║                         LAYER 2: BINARY MASK                                 ║
║  ─────────────────────────────────────────────────────────────────────────── ║
║                                                                              ║
║    Indicators are utlizied in making TRUE/FALSE queries:                     ║
║                                                                              ║
║    • Has price been by here recently?                                        ║
║    • Is what price has done going to catch up to them?                       ║
║    • Has price entered a dangerous part of town?                             ║
║    • Does price look like a reversed and or upsidedown letter J?             ║
║                                                                              ║
║    74 binary signals per 2 seconds — the language of the system              ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║                     LAYER 3: STRATEGY & EXECUTION                            ║
║  ─────────────────────────────────────────────────────────────────────────── ║
║                   THIS MAY BE AN OVERSIMPLIFICATION                          ║
║                           (BTC/USD PAIR)                                     ║
║                                                                              ║
║        ┌─ IN USD ──────────┐                                                 ║
║        │  AFTER BTC DIP    │ ────┐                                           ║
║        └───────────────────┘     │                                           ║
║                                  │                                           ║
║        ┌─ IN USD ──────────┐     │                                           ║
║        │  START OF RALLY   │ ────▶▶▶BUY                                   ║
║        └───────────────────┘                                                 ║
║                                                                              ║
║        ┌─ IN BTC ──────────┐                                                 ║
║        │  AFTER BTC RALLY  │ ────┐                                           ║
║        └───────────────────┘     │                                           ║
║                                  │                                           ║
║        ┌─ IN BTC ──────────┐     │                                           ║
║        │  START OF DIP     │ ────▶▶▶SELL                                  ║
║        └───────────────────┘                                                 ║
║                                                                              ║
║                                                                              ║
║    There is only the need to be in the right position while price works.     ║
║                                                                              ║
║    While the platform allows for extreme detail, the first goal: 1%/weekly   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝



         </div>
         <div style="text-align: center;">
         <p>The wish to take this from not yet done, to already complete, is what I am here to show.</p>
         <p>I am leaving talismans of hope in symbols on the website for good luck!</p>
         </div>
      <div style="font-size: 96px; font-family: monospace; text-align: center;">
  ☯
</div>
        <div class="ascii-container">
        <pre>

┌─[ WAY NO WAY ]─────────────────────┐
│                                    │
│         STATUS: NON ACTION         │
│                                    │
│   ———                        — —   │
│   — —       ══════════▶     ———   │
│   ———                        — —   │
│   — —                        ———   │
│   ———       ══════════▶     — —   │
│   — —                        ———   │
└────────────────────────────────────┘
</pre>
        </div>
      </section>
    </main>

    <footer class="center">
      <small>It's time to start investing in your future, one baby step at a time!! {{VISITOR_COUNT}}</small>
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

    # Serve images from /static/
    if path.startswith('/static/'):
        file_path = path[1:]  # Remove leading /
        if os.path.exists(file_path) and file_path.endswith('.png'):
            with open(file_path, 'rb') as f:
                content = f.read()
            start_response("200 OK", [("Content-Type", "image/png")])
            return [content]
        else:
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"Image not found"]

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
