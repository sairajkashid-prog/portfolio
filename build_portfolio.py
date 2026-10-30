import base64, os, json

CARDS = '/home/user/qa/cards'

def b64(name):
    p = os.path.join(CARDS, name + '.jpg')
    if not os.path.exists(p): return ''
    return 'data:image/jpeg;base64,' + base64.b64encode(open(p,'rb').read()).decode()

PROJECTS = [
  dict(id='civiceye-ai', title='CivicEye AI', sub='AI-Powered Smart Civic Issue Management',
       cat=['ai','web'], tags=['React 18','Vite','Node.js','Computer Vision','REST API'],
       blurb='B.Tech capstone. One photo → AI auto-classifies the civic issue, detects duplicates by image + GPS, scores priority 0–100 and routes it to the right municipal department. Three role-based dashboards: citizen, officer, admin analytics.',
       metrics=[('3','role dashboards'),('98%','classification*'),('<3s','inference')],
       live='https://sairajkashid-prog.github.io/civiceye-ai/',
       code='https://github.com/sairajkashid-prog/civiceye-ai', badge='Capstone', featured=True,
       note='Live demo runs in demo mode with a mock API — full backend (Node + Postgres + Redis) runs via docker-compose.'),
  dict(id='ai-learning-roi-studio', title='AI Learning ROI Studio', sub='Enterprise Transformation Calculator',
       cat=['web','data'], tags=['JavaScript','3D CSS','Data Viz','Simulation'],
       blurb='Interactive 3D simulator that turns a workforce skill gap into a defensible business case. Five sliders → live ROI engine → auto-generated, presentation-ready client proposal, grounded in 4,569 courses and 107,018 reviews.',
       metrics=[('327%','sample ROI'),('107k','reviews, grounded'),('5','live sliders')],
       live='https://sairajkashid-prog.github.io/ai-learning-roi-studio/',
       code='https://github.com/sairajkashid-prog/ai-learning-roi-studio', badge='Product', featured=True),
  dict(id='course-market-intelligence', title='Course Market Intelligence', sub='Demand vs. Supply Command Center',
       cat=['data','web'], tags=['JavaScript','Analytics','5 views'],
       blurb='Answers one commercial question: what should a learning company build next? Analyses 4,569 real Coursera + Udemy courses and 92.4M learners into opportunity scores — demand × quality ÷ supply — with a bubble matrix and ranked recommendations.',
       metrics=[('4,569','courses'),('92.4M','learners'),('5','interactive views')],
       live='https://sairajkashid-prog.github.io/course-market-intelligence/',
       code='https://github.com/sairajkashid-prog/course-market-intelligence', badge='Analytics'),
  dict(id='learner-voice-intelligence', title='Learner Voice Intelligence', sub='What makes training succeed or fail',
       cat=['data'], tags=['NLP','Review mining','Playbook'],
       blurb='Mines 107,018 learner reviews into 6 things learners love, 7 things they hate and 5 data-backed content rules. Finding: unhappy learners write 2× longer reviews — the richest feedback hides in the negative tail.',
       metrics=[('107,018','reviews'),('90.9%','positive'),('18','themes')],
       live='https://sairajkashid-prog.github.io/learner-voice-intelligence/',
       code='https://github.com/sairajkashid-prog/learner-voice-intelligence', badge='Analytics'),
  dict(id='cyber-vulnerability-remediation-control-tower', title='Cyber Vulnerability Control Tower', sub='CISA KEV × FIRST EPSS, real data',
       cat=['data','eng'], tags=['Python','Pandas','ETL','CI'],
       blurb='Joins the CISA Known Exploited Vulnerabilities catalog with the complete daily FIRST EPSS file, validates source integrity, enriches every CVE exactly, detects changes and models analyst review capacity — with an explainable review queue.',
       metrics=[('1,661','KEV rows'),('338','enriched'),('CI','+ tests')],
       live='https://sairajkashid-prog.github.io/cyber-vulnerability-remediation-control-tower/',
       code='https://github.com/sairajkashid-prog/cyber-vulnerability-remediation-control-tower', badge='Data Eng'),
  dict(id='openfda-regulatory-dataops-control-tower', title='openFDA DataOps Control Tower', sub='Regulatory pipeline that audits itself',
       cat=['data','eng'], tags=['Python','openFDA','Schema drift','Excel'],
       blurb='Ingests two official FDA datasets, fingerprints schemas, quarantines bad records, detects source drift and links recalls to shortages by exact package NDC — producing an explainable queue, Excel workbook and offline report.',
       metrics=[('2','FDA APIs'),('999','validated'),('24','quarantined')],
       live='https://sairajkashid-prog.github.io/openfda-regulatory-dataops-control-tower/',
       code='https://github.com/sairajkashid-prog/openfda-regulatory-dataops-control-tower', badge='Data Eng'),
  dict(id='pharma-sales-etl-quality-pipeline', title='Pharma Sales ETL & DQ Pipeline', sub='Reproducible Python + SQL',
       cat=['data','eng'], tags=['Python','SQLite','Data Quality','Streamlit'],
       blurb='Row-level quality rules, quarantine of invalid records, a constrained SQLite warehouse and analyst-ready Excel/HTML/Streamlit reports. Every load is idempotent and source-to-target totals reconcile.',
       metrics=[('5,000','transactions'),('92.08%','pass rate'),('0','dup loads')],
       live='https://sairajkashid-prog.github.io/pharma-sales-etl-quality-pipeline/',
       code='https://github.com/sairajkashid-prog/pharma-sales-etl-quality-pipeline', badge='Data Eng'),
  dict(id='ProfessionalWebsite', title='Professional Agency Website', sub='Responsive marketing site',
       cat=['web'], tags=['HTML5','CSS3','Vanilla JS'],
       blurb='Responsive multi-section agency site: hero grid, services, portfolio, testimonials and contact — hand-built CSS with a mobile menu and scroll-based interactions.',
       metrics=[('100%','hand-built'),('0','dependencies')],
       live='https://sairajkashid-prog.github.io/ProfessionalWebsite/',
       code='https://github.com/sairajkashid-prog/ProfessionalWebsite', badge='Web'),
  dict(id='react-form-app', title='React Form with Validation', sub='Controlled components + validation',
       cat=['web'], tags=['React','CRA','Forms'],
       blurb='A production-build React registration form: controlled inputs, per-field validation rules, error states and accessible feedback.',
       metrics=[('React','18'),('CRA','build')],
       live='https://sairajkashid-prog.github.io/react-form-app/',
       code='https://github.com/sairajkashid-prog/react-form-app', badge='Web'),
  dict(id='assignment-3-js-form', title='JS Registration Form', sub='Vanilla validation + UI',
       cat=['web'], tags=['JavaScript','CSS3','DOM'],
       blurb='Form validation written from scratch — regex checks per field, live inline error messages and a polished glass card UI.',
       metrics=[('Vanilla','JS'),('10','field rules')],
       live='https://sairajkashid-prog.github.io/assignment-3-js-form/',
       code='https://github.com/sairajkashid-prog/assignment-3-js-form', badge='Web'),
  dict(id='fsd-lab', title='FSD Lab — Portfolio Page', sub='HTML/CSS fundamentals',
       cat=['web'], tags=['HTML5','CSS3'],
       blurb='Semantic HTML foundations: external, internal and inline CSS, a table and a bottom-anchored form layout.',
       metrics=[('3','CSS methods')],
       live='https://sairajkashid-prog.github.io/fsd-lab/',
       code='https://github.com/sairajkashid-prog/fsd-lab', badge='Web'),
]

VERCEL = {'civiceye-ai': 'https://civiceye-ai-five.vercel.app', 'portfolio': 'https://portfolio-sairaj-kashid.vercel.app', 'course-market-intelligence': 'https://course-market-intelligence-sairaj-kashid.vercel.app', 'ai-learning-roi-studio': 'https://ai-learning-roi-studio-sairaj-kashid.vercel.app', 'learner-voice-intelligence': 'https://learner-voice-intelligence-sairaj-kashid.vercel.app', 'ProfessionalWebsite': 'https://professional-website-sairaj-kashid.vercel.app', 'react-form-app': 'https://react-form-app-sairaj-kashid.vercel.app'}

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

cards_html = []
for p in PROJECTS:
    tags = ''.join(f'<span class="tag">{esc(t)}</span>' for t in p['tags'])
    mets = ''.join(f'<div class="met"><b>{esc(a)}</b><span>{esc(b)}</span></div>' for a,b in p['metrics'])
    note = f'<p class="note">ⓘ {esc(p["note"])}</p>' if p.get('note') else ''
    vurl = VERCEL.get(p['id'])
    vlink = f'<a class="vlink" href="{vurl}" target="_blank" rel="noopener">▲ Also on Vercel</a>' if vurl else ''
    cats = ' '.join(p['cat'])
    feat = ' featured' if p.get('featured') else ''
    img = b64(p['id'])
    cards_html.append(f'''
      <article class="card{feat}" data-cat="{cats}">
        <a class="thumb" href="{p['live']}" target="_blank" rel="noopener">
          <img src="{img}" alt="{esc(p['title'])} screenshot" loading="lazy">
          <span class="badge">{esc(p['badge'])}</span>
          <span class="live">● LIVE</span>
        </a>
        <div class="body">
          <h3>{esc(p['title'])}</h3>
          <p class="sub">{esc(p['sub'])}</p>
          <p class="blurb">{esc(p['blurb'])}</p>
          <div class="mets">{mets}</div>
          <div class="tags">{tags}</div>
          {note}
          <div class="actions">
            <a class="btn primary" href="{p['live']}" target="_blank" rel="noopener">Live Demo ↗</a>
            <a class="btn ghost" href="{p['code']}" target="_blank" rel="noopener">Source Code</a>
          </div>
          {vlink}
        </div>
      </article>''')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E%3Cstop offset='0' stop-color='%235eead4'/%3E%3Cstop offset='.5' stop-color='%23818cf8'/%3E%3Cstop offset='1' stop-color='%2338bdf8'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='64' height='64' rx='14' fill='url(%23g)'/%3E%3Ctext x='32' y='43' font-family='system-ui,sans-serif' font-size='27' font-weight='800' text-anchor='middle' fill='%2304121a'%3ESK%3C/text%3E%3C/svg%3E">
<title>Sairaj Sandip Kashid — Live Project Portfolio</title>
<meta name="description" content="11 deployed full-stack, AI and data-engineering projects by Sairaj Sandip Kashid — every card links to a running live demo.">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#06080f; --bg2:#0a0e1a; --card:#0d1220; --line:rgba(148,163,184,.14);
  --txt:#e8edf7; --muted:#8b9ab3; --accent:#5eead4; --accent2:#818cf8; --accent3:#38bdf8;
  --grad:linear-gradient(120deg,#5eead4 0%,#818cf8 45%,#38bdf8 100%);
}}
html{{scroll-behavior:smooth}}
body{{background:var(--bg);color:var(--txt);font-family:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;line-height:1.6;overflow-x:hidden}}
body::before{{content:"";position:fixed;inset:0;z-index:-2;pointer-events:none;
  background:
   radial-gradient(900px 500px at 12% -8%, rgba(94,234,212,.13), transparent 60%),
   radial-gradient(800px 480px at 88% 4%, rgba(129,140,248,.15), transparent 62%),
   radial-gradient(700px 500px at 50% 108%, rgba(56,189,248,.10), transparent 60%),
   var(--bg)}}
body::after{{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.35;
  background-image:linear-gradient(rgba(148,163,184,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(148,163,184,.055) 1px,transparent 1px);
  background-size:64px 64px;mask-image:radial-gradient(ellipse 80% 60% at 50% 0%,#000 45%,transparent 100%)}}
.wrap{{max-width:1240px;margin:0 auto;padding:0 24px}}

/* ---------- nav ---------- */
nav{{position:sticky;top:0;z-index:60;backdrop-filter:blur(16px);background:rgba(6,8,15,.72);border-bottom:1px solid var(--line)}}
.nav-in{{max-width:1240px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;gap:20px}}
.brand{{display:flex;align-items:center;gap:11px;font-weight:800;letter-spacing:-.02em;font-size:1.02rem}}
.logo{{width:34px;height:34px;border-radius:10px;background:var(--grad);display:grid;place-items:center;color:#04121a;font-weight:900;font-size:.9rem;box-shadow:0 6px 22px rgba(94,234,212,.28)}}
.nav-links{{margin-left:auto;display:flex;gap:26px;align-items:center}}
.nav-links a{{color:var(--muted);text-decoration:none;font-size:.88rem;font-weight:500;transition:color .2s}}
.nav-links a:hover{{color:var(--txt)}}
.nav-cta{{padding:9px 16px;border-radius:9px;background:var(--grad);color:#04121a!important;font-weight:700!important;font-size:.84rem!important}}
@media(max-width:820px){{.nav-links a:not(.nav-cta){{display:none}}}}

/* ---------- hero ---------- */
header.hero{{padding:84px 0 64px;position:relative}}
.pill{{display:inline-flex;align-items:center;gap:9px;padding:7px 15px;border-radius:99px;border:1px solid rgba(94,234,212,.34);
  background:rgba(94,234,212,.07);color:var(--accent);font-size:.78rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase}}
.dot{{width:7px;height:7px;border-radius:50%;background:var(--accent);box-shadow:0 0 0 0 rgba(94,234,212,.6);animation:pulse 2.2s infinite}}
@keyframes pulse{{70%{{box-shadow:0 0 0 9px rgba(94,234,212,0)}}100%{{box-shadow:0 0 0 0 rgba(94,234,212,0)}}}}
h1{{font-size:clamp(2.3rem,5.6vw,4.05rem);line-height:1.04;letter-spacing:-.035em;font-weight:800;margin:22px 0 0;max-width:19ch}}
h1 em{{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}}
.lede{{color:var(--muted);font-size:1.09rem;max-width:63ch;margin-top:20px}}
.lede b{{color:var(--txt);font-weight:600}}
.hero-cta{{display:flex;gap:12px;margin-top:32px;flex-wrap:wrap}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:11px;font-weight:700;font-size:.9rem;
  text-decoration:none;transition:transform .18s,box-shadow .18s,background .18s;border:1px solid transparent}}
.btn.primary{{background:var(--grad);color:#04121a;box-shadow:0 10px 30px rgba(94,234,212,.24)}}
.btn.primary:hover{{transform:translateY(-2px);box-shadow:0 16px 38px rgba(94,234,212,.34)}}
.btn.ghost{{border-color:var(--line);color:var(--txt);background:rgba(148,163,184,.06)}}
.btn.ghost:hover{{background:rgba(148,163,184,.14);transform:translateY(-2px)}}
.stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:56px}}
.stat{{border:1px solid var(--line);border-radius:14px;padding:18px;background:linear-gradient(180deg,rgba(148,163,184,.07),rgba(148,163,184,.02))}}
.stat b{{display:block;font-size:1.72rem;letter-spacing:-.03em;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;font-weight:800}}
.stat span{{color:var(--muted);font-size:.79rem;text-transform:uppercase;letter-spacing:.07em;font-weight:600}}
@media(max-width:700px){{.stats{{grid-template-columns:repeat(2,1fr)}}}}

/* ---------- section ---------- */
section{{padding:56px 0}}
.sec-head{{display:flex;align-items:flex-end;justify-content:space-between;gap:22px;flex-wrap:wrap;margin-bottom:30px}}
.sec-head h2{{font-size:clamp(1.55rem,3vw,2.15rem);letter-spacing:-.03em;font-weight:800}}
.sec-head p{{color:var(--muted);font-size:.94rem;margin-top:7px;max-width:62ch}}
.filters{{display:flex;gap:8px;flex-wrap:wrap}}
.chip{{padding:8px 15px;border-radius:99px;border:1px solid var(--line);background:rgba(148,163,184,.05);color:var(--muted);
  font-size:.82rem;font-weight:600;cursor:pointer;transition:all .18s;font-family:inherit}}
.chip:hover{{color:var(--txt);border-color:rgba(148,163,184,.3)}}
.chip.on{{background:var(--grad);color:#04121a;border-color:transparent;box-shadow:0 6px 20px rgba(94,234,212,.22)}}

/* ---------- grid ---------- */
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(370px,1fr));gap:22px}}
.card{{border:1px solid var(--line);border-radius:17px;overflow:hidden;background:linear-gradient(180deg,rgba(17,23,39,.92),rgba(10,14,26,.92));
  display:flex;flex-direction:column;transition:transform .25s cubic-bezier(.2,.7,.3,1),border-color .25s,box-shadow .25s}}
.card:hover{{transform:translateY(-7px);border-color:rgba(94,234,212,.4);box-shadow:0 24px 60px rgba(0,0,0,.55),0 0 0 1px rgba(94,234,212,.14)}}
.card.featured{{border-color:rgba(94,234,212,.28)}}
.card.hide{{display:none}}
.thumb{{display:block;position:relative;aspect-ratio:16/9.4;overflow:hidden;background:#0a0e1a;border-bottom:1px solid var(--line)}}
.thumb img{{width:100%;height:100%;object-fit:cover;object-position:top center;transition:transform .5s cubic-bezier(.2,.7,.3,1);display:block}}
.card:hover .thumb img{{transform:scale(1.045)}}
.badge{{position:absolute;top:11px;left:11px;padding:5px 11px;border-radius:7px;background:rgba(6,8,15,.82);
  backdrop-filter:blur(8px);border:1px solid var(--line);font-size:.7rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#cbd5e1}}
.live{{position:absolute;top:11px;right:11px;padding:5px 11px;border-radius:7px;background:rgba(16,185,129,.16);
  border:1px solid rgba(16,185,129,.5);color:#34d399;font-size:.68rem;font-weight:800;letter-spacing:.06em;backdrop-filter:blur(8px)}}
.body{{padding:19px 20px 20px;display:flex;flex-direction:column;flex:1}}
.tags{{margin-bottom:2px}}
.body h3{{font-size:1.14rem;letter-spacing:-.02em;font-weight:750}}
.sub{{color:var(--accent);font-size:.79rem;font-weight:600;margin-top:3px;letter-spacing:.01em}}
.blurb{{color:var(--muted);font-size:.866rem;margin-top:11px;line-height:1.62}}
.mets{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:auto;padding-top:15px;border-top:1px dashed rgba(148,163,184,.15)}}
.met{{text-align:center;min-width:0}}
.met b{{display:block;font-size:.98rem;letter-spacing:-.02em;color:var(--txt);font-weight:750;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.met span{{display:block;font-size:.58rem;color:var(--muted);text-transform:uppercase;letter-spacing:.04em;font-weight:600;line-height:1.35;margin-top:2px}}
.tags{{display:flex;gap:6px;flex-wrap:wrap;margin-top:14px}}
.tag{{padding:4px 9px;border-radius:6px;background:rgba(129,140,248,.1);border:1px solid rgba(129,140,248,.22);
  color:#a5b4fc;font-size:.68rem;font-weight:600}}
.note{{margin-top:12px;font-size:.74rem;color:#64748b;line-height:1.5;font-style:italic}}
.actions{{display:flex;gap:9px;margin-top:16px}}
.actions .btn{{flex:1;justify-content:center;padding:10px 12px;font-size:.82rem;border-radius:9px}}
.vlink{{display:block;text-align:center;margin-top:9px;font-size:.72rem;font-weight:600;color:#8b9ab3;text-decoration:none;letter-spacing:.02em}}
.vlink:hover{{color:var(--accent)}}

/* ---------- stack strip ---------- */
.stack{{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:34px 0;background:rgba(148,163,184,.02)}}
.stack-in{{display:flex;flex-wrap:wrap;gap:11px;justify-content:center}}
.spill{{padding:8px 15px;border-radius:9px;border:1px solid var(--line);background:rgba(148,163,184,.05);
  font-size:.82rem;font-weight:600;color:#cbd5e1;transition:.2s}}
.spill:hover{{border-color:rgba(94,234,212,.4);color:var(--accent);transform:translateY(-2px)}}

/* ---------- highlights ---------- */
.hl-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}}
.hl{{border:1px solid var(--line);border-radius:14px;padding:22px;background:linear-gradient(180deg,rgba(148,163,184,.06),transparent)}}
.hl .ico{{font-size:1.4rem}}
.hl h4{{margin:10px 0 7px;font-size:.99rem;font-weight:750}}
.hl p{{color:var(--muted);font-size:.855rem;line-height:1.62}}

/* ---------- contact ---------- */
.contact{{border:1px solid rgba(94,234,212,.24);border-radius:20px;padding:44px 38px;
  background:linear-gradient(135deg,rgba(94,234,212,.09),rgba(129,140,248,.1));text-align:center;position:relative;overflow:hidden}}
.contact h2{{font-size:clamp(1.5rem,3.2vw,2.1rem);letter-spacing:-.03em;font-weight:800}}
.contact p{{color:#a9b8cd;margin-top:11px;max-width:56ch;margin-inline:auto}}
.contact .hero-cta{{justify-content:center}}
footer{{padding:44px 0 56px;color:#5b6b83;font-size:.82rem;text-align:center;border-top:1px solid var(--line);margin-top:44px}}
footer a{{color:var(--muted);text-decoration:none}}
footer a:hover{{color:var(--accent)}}
.reveal{{opacity:0;transform:translateY(22px);transition:opacity .65s ease,transform .65s cubic-bezier(.2,.7,.3,1)}}
.reveal.in{{opacity:1;transform:none}}
@media print{{
  body{{background:#fff!important;color:#111!important}}
  body::before,body::after,nav,.hero-cta,.filters,.thumb .live{{display:none!important}}
  .card{{break-inside:avoid;border:1px solid #ccc!important;background:#fff!important}}
  .card *{{color:#111!important}}
  .blurb,.sub{{color:#444!important}}
  .tag{{border:1px solid #bbb!important;background:#f4f4f4!important}}
  .thumb{{max-height:190px;aspect-ratio:auto}}
  a{{text-decoration:none}}
}}
</style>
</head>
<body>

<nav>
  <div class="nav-in">
    <div class="brand"><div class="logo">SK</div> Sairaj Kashid</div>
    <div class="nav-links">
      <a href="#projects">Projects</a>
      <a href="#stack">Stack</a>
      <a href="#highlights">Highlights</a>
      <a href="#contact">Contact</a>
      <a class="nav-cta" href="https://github.com/sairajkashid-prog" target="_blank" rel="noopener">GitHub ↗</a>
    </div>
  </div>
</nav>

<header class="hero">
  <div class="wrap">
    <span class="pill"><span class="dot"></span> 11 live deployments · open to opportunities</span>
    <h1>I build things that <em>actually run.</em></h1>
    <p class="lede">Final-year Computer Engineering student at <b>MIT World Peace University, Pune</b>.
      This page is a live portfolio — <b>every project below is deployed and clickable</b>, not a screenshot in a slide deck.
      Full-stack apps, AI/ML systems and real-data engineering pipelines, 22 repositories strong.</p>
    <div class="hero-cta">
      <a class="btn primary" href="#projects">See the live projects ↓</a>
      <a class="btn ghost" href="https://github.com/sairajkashid-prog" target="_blank" rel="noopener">GitHub profile ↗</a>
    </div>
    <div class="stats">
      <div class="stat"><b>11</b><span>Live deployments</span></div>
      <div class="stat"><b>22</b><span>GitHub repositories</span></div>
      <div class="stat"><b>7</b><span>Data / AI pipelines</span></div>
      <div class="stat"><b>100%</b><span>Deploy success</span></div>
    </div>
  </div>
</header>

<section id="projects">
  <div class="wrap">
    <div class="sec-head">
      <div>
        <h2>Live projects</h2>
        <p>Click any card — it opens the running application. Full source is on GitHub for every one.</p>
      </div>
      <div class="filters">
        <button class="chip on" data-f="all">All 11</button>
        <button class="chip" data-f="ai">AI &amp; ML</button>
        <button class="chip" data-f="data">Analytics</button>
        <button class="chip" data-f="eng">Data Engineering</button>
        <button class="chip" data-f="web">Web Apps</button>
      </div>
    </div>
    <div class="grid" id="grid">{''.join(cards_html)}
    </div>
  </div>
</section>

<div class="stack" id="stack">
  <div class="wrap">
    <div class="stack-in">
      <span class="spill">JavaScript</span><span class="spill">TypeScript</span><span class="spill">React 18</span>
      <span class="spill">Vite</span><span class="spill">Node.js</span><span class="spill">Express</span>
      <span class="spill">Python</span><span class="spill">Pandas</span><span class="spill">SQL / SQLite</span>
      <span class="spill">Docker</span><span class="spill">GitHub Actions</span><span class="spill">REST APIs</span>
      <span class="spill">HTML5 / CSS3</span><span class="spill">Streamlit</span><span class="spill">Data Visualisation</span>
    </div>
  </div>
</div>

<section id="highlights">
  <div class="wrap">
    <div class="sec-head"><div><h2>How I work</h2>
      <p>Patterns that show up across all of these repositories.</p></div></div>
    <div class="hl-grid">
      <div class="hl"><div class="ico">🧪</div><h4>Tested, not just written</h4>
        <p>CI workflows with property-based and differential tests. The GPU test framework repo ships 133 passing cases and 4 planted bugs that every naive <code>allclose</code> test misses.</p></div>
      <div class="hl"><div class="ico">📊</div><h4>Real data, stated limits</h4>
        <p>CISA KEV, FIRST EPSS and openFDA are live public sources — and each README documents exactly what the analysis cannot claim. Facts separated from inference.</p></div>
      <div class="hl"><div class="ico">🔁</div><h4>Idempotent by default</h4>
        <p>ETL runs are safe to re-run: business keys stay unique, failed rows are quarantined not dropped, and source-to-target totals reconcile on every load.</p></div>
      <div class="hl"><div class="ico">🚀</div><h4>Deployed, not demoed</h4>
        <p>Every project here has a public URL. Static builds, hash routing and relative asset paths so nothing 404s when it leaves localhost.</p></div>
      <div class="hl"><div class="ico">📄</div><h4>Research output</h4>
        <p>Co-author on <em>“Security of LLM-Based AI Agents against Indirect Prompt Injection”</em> — a four-layer defence pipeline for resume screening, with a 60-PDF synthetic benchmark and ablation suite.</p></div>
      <div class="hl"><div class="ico">🧱</div><h4>From-scratch systems</h4>
        <p>GPU particle physics engine (PBD/PBF, C++17 + CUDA behind one C ABI), batched MPPI motion planning for robot fleets, and GPU health drift detection — no frameworks.</p></div>
    </div>
  </div>
</section>

<section id="contact">
  <div class="wrap">
    <div class="contact">
      <h2>Looking for someone who ships?</h2>
      <p>I'm open to full-stack, data engineering and AI engineering roles or internships. Happy to walk through any project's architecture, trade-offs or the parts that broke first.</p>
      <div class="hero-cta">
        <a class="btn primary" href="mailto:sairajkashidsk@gmail.com">✉️ sairajkashidsk@gmail.com</a>
        <a class="btn ghost" href="https://github.com/sairajkashid-prog" target="_blank" rel="noopener">GitHub ↗</a>
        <a class="btn ghost" href="https://linkedin.com/in/sairajkashid-prog" target="_blank" rel="noopener">LinkedIn ↗</a>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    Built &amp; deployed by <a href="https://github.com/sairajkashid-prog" target="_blank" rel="noopener">Sairaj Sandip Kashid</a> · Pune, India ·
    <a href="https://github.com/sairajkashid-prog?tab=repositories" target="_blank" rel="noopener">All 22 repositories ↗</a>
    <div style="margin-top:9px;opacity:.65">* Classification accuracy is simulated on the demo dataset; the production model is fine-tuned on municipal data.</div>
  </div>
</footer>

<script>
// filters
const chips=[...document.querySelectorAll('.chip')];
const cards=[...document.querySelectorAll('.card')];
chips.forEach(c=>c.addEventListener('click',()=>{{
  chips.forEach(x=>x.classList.remove('on')); c.classList.add('on');
  const f=c.dataset.f;
  cards.forEach(card=>{{
    const show = f==='all' || card.dataset.cat.split(' ').includes(f);
    card.classList.toggle('hide',!show);
  }});
}}));
// reveal on scroll
const io=new IntersectionObserver(es=>{{es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.08}});
cards.forEach((c,i)=>{{c.classList.add('reveal');c.style.transitionDelay=(i%3)*70+'ms';io.observe(c)}});
</script>
</body>
</html>'''

open('/home/user/portfolio/index.html','w').write(html)
print('written', len(html)//1024, 'KB')
