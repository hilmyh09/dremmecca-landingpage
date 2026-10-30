#!/usr/bin/env python3
"""Generator 3 landing page promo Jadiumrah (hard selling, gaya Scalev Dreammecca, palet Jadiumrah).

Pakai:  python3 build.py <folder_gambar> <folder_output_embedded>
- Versi relatif (gambar via assets/images/...) ditulis ke folder skrip ini, untuk repo.
- Versi embedded (gambar base64 JPEG/PNG saja, siap impor Scalev) ditulis ke folder output.
Semua angka program berasal dari script iklan yang diberikan pemilik (30 Okt 2026).
"""
import base64, html, os, sys, urllib.parse

WA_NUMBER = "6281110066986"
COMPANY = "PT. Globalindo Sukses Maksima"
PPIU = "02200064127450010"

def wa(msg):
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, urllib.parse.quote(msg))

ICON_WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.5 3.5A11 11 0 0 0 3.2 16.8L2 22l5.3-1.4A11 11 0 1 0 20.5 3.5Zm-8.5 17a9 9 0 0 1-4.6-1.3l-.3-.2-3.1.8.8-3-.2-.3A9 9 0 1 1 12 20.5Zm5-6.7c-.3-.1-1.6-.8-1.9-.9-.3-.1-.4-.1-.6.1l-.9 1.1c-.2.2-.3.2-.6.1a7.3 7.3 0 0 1-3.6-3.2c-.3-.5.3-.4.8-1.5.1-.2 0-.4 0-.5l-.9-2c-.2-.5-.4-.5-.6-.5h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3c.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.2Z"/></svg>'
IC = {
 "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "plane": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M2 16l20-8-4 10-6-3-5 4 1-6-6-2 4 1Z"/></svg>',
 "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0M16 4.5a3.5 3.5 0 0 1 0 7M22 20a6 6 0 0 0-4-5.6"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8.5-8 9-4.5-.5-8-4-8-9V6l8-3Z"/><path d="m9 12 2 2 4-4"/></svg>',
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M8 10h8M8 14h5M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9l-5 4V6Z"/></svg>',
 "tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 12V4h8l10 10-8 8L3 12Z"/><circle cx="7.5" cy="8.5" r="1.5"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
}

CSS = r"""
    :root{--green:#173E35;--green-900:#0F2C26;--green-800:#1C4A3F;--cream:#F4F0E6;--sage:#54695E;--mint:#9BD9B8;--ink:#1C2622;--muted:#5F6F68;--paper:#fff;--soft:#F6F7F4;--wa:#25D366;--wa-dark:#1DB954;--line:rgba(23,62,53,.12);--line-dark:rgba(244,240,230,.14);--sans:"Poppins",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;--r:16px;--r-lg:24px;--max:1240px;--pad:clamp(1.25rem,4vw,2.5rem)}
    *,*::before,*::after{box-sizing:border-box}
    html{scroll-padding-top:90px}@media(prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
    body{margin:0;font-family:var(--sans);font-size:1rem;line-height:1.6;color:var(--ink);background:var(--paper);overflow-x:hidden;-webkit-font-smoothing:antialiased;padding-bottom:84px}
    @media(min-width:861px){body{padding-bottom:0}}
    img{display:block;max-width:100%;height:auto}
    h1,h2,h3{margin:0;font-weight:800;letter-spacing:-.02em;line-height:1.12}
    p,ul,ol{margin:0}ul,ol{padding:0;list-style:none}
    button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer}
    :focus-visible{outline:3px solid var(--mint);outline-offset:3px}
    .visually-hidden{position:absolute!important;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
    .wrap{width:min(var(--max),100% - 2*var(--pad));margin-inline:auto}
    .section{padding:clamp(3.5rem,7vw,6rem) 0}.section--soft{background:var(--soft)}
    .eyebrow{font-size:.78rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--sage);margin-bottom:1rem}
    .h2{font-size:clamp(1.9rem,4vw,2.9rem);color:var(--green);max-width:22ch}
    .sub{margin-top:1rem;font-size:1.05rem;color:var(--muted);max-width:62ch}
    .btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;min-height:3.4rem;padding:.9rem 1.75rem;border-radius:999px;font-weight:700;text-decoration:none;border:2px solid transparent;text-align:center}
    .btn svg{width:1.25em;height:1.25em;flex:none}
    .btn--wa{background:var(--wa);color:#fff;box-shadow:0 10px 30px rgba(37,211,102,.35)}.btn--wa:hover{background:var(--wa-dark)}
    .btn--outline{background:transparent;color:#fff;border-color:rgba(255,255,255,.7)}.btn--outline:hover{background:rgba(255,255,255,.08)}
    .btn--green{background:var(--green);color:#fff}.btn--green:hover{background:var(--green-900)}
    .btn--sm{min-height:2.8rem;padding:.6rem 1.25rem;font-size:.95rem}
    @media(prefers-reduced-motion:no-preference){.btn{transition:background-color .18s,transform .18s}.btn:active{transform:scale(.98)}}
    .hdr{position:sticky;top:0;z-index:30;background:rgba(15,44,38,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line-dark);color:var(--cream)}
    .hdr .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem;min-height:76px}
    .brand{display:flex;align-items:center;gap:.75rem;text-decoration:none;color:var(--cream)}
    .brand__logo{height:44px;width:auto}.brand--lg .brand__logo{height:56px}
    .brand__tag{font-size:.8rem;line-height:1.25;color:rgba(244,240,230,.75);padding-left:.75rem;border-left:1px solid rgba(244,240,230,.25)}
    .hdr .btn--sm{white-space:nowrap}
    @media(max-width:560px){.brand__tag{display:none}.hdr .btn--sm{padding:.55rem 1rem;font-size:.88rem}}
    .hero{background:radial-gradient(120% 90% at 85% 10%,var(--green-800) 0%,var(--green) 45%,var(--green-900) 100%);color:var(--cream);padding:clamp(3rem,7vw,5.5rem) 0 clamp(6rem,10vw,8.5rem)}
    .hero__grid{display:grid;gap:3rem;align-items:center}.hero__grid>*{min-width:0}
    @media(min-width:960px){.hero__grid{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:4rem}}
    .pill{display:inline-flex;align-items:center;padding:.5rem 1.1rem;border-radius:999px;border:1px solid rgba(244,240,230,.35);background:rgba(255,255,255,.07);color:var(--cream);font-size:.9rem;font-weight:600}
    .hero h1{margin-top:1.5rem;font-size:clamp(2.2rem,6.5vw,4.6rem);line-height:1.04;color:#fff}
    .hero h1 .hl{color:var(--mint)}
    .hero__desc{margin-top:1.1rem;font-size:1.1rem;color:rgba(244,240,230,.88);max-width:56ch}
    .chips{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1.4rem}
    .chip{display:inline-flex;align-items:center;gap:.5rem;padding:.55rem 1rem;border-radius:999px;border:1px solid rgba(244,240,230,.28);font-size:.92rem;font-weight:600}
    .chip svg{width:1.05em;height:1.05em;color:var(--mint)}
    .price{margin-top:1.5rem;display:grid;grid-template-columns:auto 1fr;gap:1.25rem;align-items:center;padding:1.25rem 1.5rem;border-radius:var(--r);background:rgba(255,255,255,.06);border:1px solid rgba(244,240,230,.14)}
    .price__k small{display:block;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(244,240,230,.7)}
    .price__k strong{display:block;font-size:clamp(1.7rem,3vw,2.3rem);font-weight:800;color:#fff;line-height:1.1;margin-top:.2rem;white-space:nowrap}
    .price__k em{font-style:normal;font-size:.8em;color:var(--mint)}
    .price p{color:rgba(244,240,230,.85);font-size:.95rem}.price p strong{color:#fff}
    @media(max-width:480px){.price{grid-template-columns:1fr}}
    .hero__actions{display:flex;flex-wrap:wrap;gap:.85rem;margin-top:1.75rem}
    .ticks{display:flex;flex-wrap:wrap;gap:.5rem 1.5rem;margin-top:1.5rem;font-size:.9rem;color:rgba(244,240,230,.85)}
    .ticks li::before{content:"✓";color:var(--mint);font-weight:800;margin-right:.5rem}
    .hero__visual img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:var(--r-lg);box-shadow:0 30px 60px rgba(0,0,0,.35);background:var(--green-800)}
    .hero__visual figcaption{margin-top:.6rem;font-size:.8rem;color:rgba(244,240,230,.6)}
    @media(max-width:480px){.hero__actions .btn{width:100%}.hero__visual img{aspect-ratio:4/3}}
    .overlap{margin-top:clamp(-4rem,-7vw,-5.5rem);position:relative;z-index:2}
    .cards4{display:grid;gap:1rem}@media(min-width:640px){.cards4{grid-template-columns:1fr 1fr}}@media(min-width:1024px){.cards4{grid-template-columns:repeat(4,1fr)}}
    .card{background:var(--paper);border-radius:var(--r);padding:1.4rem;box-shadow:0 12px 40px rgba(15,44,38,.10);border:1px solid var(--line)}
    .card__ic{width:2.6rem;height:2.6rem;border-radius:12px;background:var(--soft);color:var(--green);display:grid;place-items:center;margin-bottom:.9rem}.card__ic svg{width:1.3rem;height:1.3rem}
    .card h3{font-size:1.05rem;color:var(--green)}.card p{margin-top:.35rem;font-size:.93rem;color:var(--muted)}
    .variants{display:grid;gap:1.25rem;margin-top:2rem}@media(min-width:900px){.variants{grid-template-columns:repeat(var(--n,1),1fr)}}
    .variant{border:1px solid var(--line);border-radius:var(--r-lg);background:var(--paper);padding:1.6rem;display:flex;flex-direction:column;gap:1rem}
    .variant--dark{background:var(--green);color:var(--cream);border-color:transparent}
    .variant__head{display:flex;justify-content:space-between;gap:1rem;align-items:flex-start;flex-wrap:wrap}
    .variant h3{font-size:1.35rem;color:var(--green)}.variant--dark h3{color:#fff}
    .variant__price{font-size:1.9rem;font-weight:800;color:var(--green);line-height:1}.variant--dark .variant__price{color:#fff}
    .variant__price small{display:block;font-size:.72rem;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:.3rem}.variant--dark .variant__price small{color:rgba(244,240,230,.7)}
    .variant__meta{display:flex;flex-wrap:wrap;gap:.5rem}
    .variant__meta span{display:inline-flex;align-items:center;gap:.4rem;padding:.4rem .8rem;border-radius:999px;background:var(--soft);font-size:.85rem;font-weight:600;color:var(--green)}
    .variant--dark .variant__meta span{background:rgba(255,255,255,.1);color:var(--cream)}
    .variant__meta svg{width:1em;height:1em}
    .dates{display:grid;gap:.6rem;grid-template-columns:repeat(auto-fit,minmax(150px,1fr))}
    .date{display:flex;flex-direction:column;align-items:center;gap:.25rem;padding:.9rem .75rem;border-radius:14px;border:2px solid var(--line);text-decoration:none;color:var(--green);background:var(--paper);font-weight:700;text-align:center}
    .date:hover{border-color:var(--wa)}
    .date small{font-size:.75rem;font-weight:500;color:var(--muted)}
    .date b{font-size:1.15rem;line-height:1.1}
    .date .go{margin-top:.35rem;display:inline-flex;align-items:center;gap:.35rem;font-size:.8rem;color:var(--wa-dark)}.date .go svg{width:1em;height:1em}
    .variant--dark .date{background:rgba(255,255,255,.06);border-color:rgba(244,240,230,.2);color:#fff}.variant--dark .date small{color:rgba(244,240,230,.7)}.variant--dark .date .go{color:var(--mint)}
    .variant .note{font-size:.82rem;color:var(--muted)}.variant--dark .note{color:rgba(244,240,230,.7)}
    .numcards{display:grid;gap:1rem;margin-top:2rem}@media(min-width:800px){.numcards{grid-template-columns:1fr 1fr}}
    .numcard{background:var(--paper);border:1px solid var(--line);border-radius:var(--r);padding:1.6rem}
    .numcard--dark{background:var(--green);color:var(--cream);border-color:transparent}
    .numcard__n{font-size:.8rem;font-weight:800;letter-spacing:.14em;color:var(--sage)}.numcard--dark .numcard__n{color:var(--mint)}
    .numcard h3{margin-top:.5rem;font-size:1.25rem;color:var(--green)}.numcard--dark h3{color:#fff}
    .numcard p{margin-top:.5rem;font-size:.95rem;color:var(--muted)}.numcard--dark p{color:rgba(244,240,230,.82)}
    .steps{display:grid;gap:1rem;margin-top:2rem}@media(min-width:800px){.steps{grid-template-columns:repeat(3,1fr)}}
    .step{background:var(--paper);border:1px solid var(--line);border-radius:var(--r);padding:1.6rem}
    .step__n{width:2.6rem;height:2.6rem;border-radius:50%;display:grid;place-items:center;background:var(--soft);color:var(--green);font-weight:800;margin-bottom:1rem}
    .step h3{font-size:1.2rem;color:var(--green)}.step p{margin-top:.5rem;font-size:.95rem;color:var(--muted)}
    .bar{margin-top:1.5rem;display:grid;grid-template-columns:auto 1fr auto;gap:1rem;align-items:center;padding:1.25rem 1.5rem;border-radius:var(--r);background:var(--green);color:var(--cream)}
    .bar__ic{width:3rem;height:3rem;border-radius:12px;background:rgba(255,255,255,.08);display:grid;place-items:center;color:var(--mint)}.bar__ic svg{width:1.4rem;height:1.4rem}
    .bar strong{display:block;color:#fff}.bar span{font-size:.93rem;color:rgba(244,240,230,.8)}
    @media(max-width:700px){.bar{grid-template-columns:auto 1fr}.bar .btn{grid-column:1/-1;width:100%}}
    .faq{max-width:820px;margin-top:2rem;display:grid;gap:.75rem}
    .faq__item{background:var(--paper);border:1px solid var(--line);border-radius:14px}.faq__item h3{font-size:1rem}
    .faq__t{width:100%;display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:1.1rem 1.25rem;text-align:left;font-weight:700;color:var(--green);border-radius:14px}
    .faq__t::after{content:"+";flex:none;width:1.8rem;height:1.8rem;border-radius:50%;display:grid;place-items:center;background:var(--soft);color:var(--green);font-size:1.2rem;font-weight:700}
    .faq__t[aria-expanded="true"]::after{content:"–"}
    .faq__p{padding:0 1.25rem 1.2rem;color:var(--muted);font-size:.95rem}.faq__p[hidden]{display:none}
    .panel{background:radial-gradient(100% 120% at 50% 0%,var(--green-800) 0%,var(--green) 50%,var(--green-900) 100%);color:var(--cream);border-radius:var(--r-lg);padding:clamp(2.5rem,6vw,4.5rem) var(--pad);text-align:center}
    .panel h2{font-size:clamp(1.9rem,4vw,2.8rem);color:#fff;max-width:24ch;margin-inline:auto}
    .panel p{margin-top:1rem;max-width:58ch;margin-inline:auto;color:rgba(244,240,230,.85)}
    .panel .btn{margin-top:1.75rem;min-width:min(100%,380px)}
    .panel small{display:block;margin-top:1rem;font-size:.85rem;color:rgba(244,240,230,.65)}
    .cross{display:grid;gap:1rem;margin-top:2rem}@media(min-width:800px){.cross{grid-template-columns:1fr 1fr}}
    .cross a{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:1.25rem 1.5rem;border-radius:var(--r);border:1px solid var(--line);background:var(--paper);text-decoration:none;color:var(--green)}
    .cross a:hover{border-color:var(--wa)}
    .cross strong{display:block;font-size:1.05rem}.cross span{font-size:.9rem;color:var(--muted)}
    .cross .go{flex:none;font-weight:700;color:var(--wa-dark);font-size:.9rem}
    .ftr{background:var(--green-900);color:rgba(244,240,230,.85);padding:3.5rem 0 2rem}
    .ftr__grid{display:grid;gap:2rem}@media(min-width:800px){.ftr__grid{grid-template-columns:1.4fr 1fr 1fr}}
    .ftr h4{margin:0 0 .75rem;font-size:1rem;color:#fff}.ftr li{padding:.2rem 0;font-size:.95rem}
    .ftr a{color:rgba(244,240,230,.9);text-decoration:none}.ftr a:hover{color:#fff}
    .ftr__tag{margin-top:.9rem;font-weight:600;color:#fff}
    .ftr__bottom{margin-top:2.5rem;padding-top:1.25rem;border-top:1px solid var(--line-dark);font-size:.85rem;color:rgba(244,240,230,.6);display:grid;gap:.4rem}
    .sticky{position:fixed;left:0;right:0;bottom:0;z-index:40;padding:.6rem var(--pad) calc(.6rem + env(safe-area-inset-bottom));background:rgba(15,44,38,.96);border-top:1px solid var(--line-dark);backdrop-filter:blur(8px)}
    .sticky .btn{width:100%;min-height:3rem}
    @media(min-width:861px){.sticky{display:none}}
"""

JS = r"""
    (function(){
      document.querySelectorAll('[data-year]').forEach(function(e){e.textContent=new Date().getFullYear()});
      document.querySelectorAll('.faq__t').forEach(function(b){
        var p=document.getElementById(b.getAttribute('aria-controls'));
        b.addEventListener('click',function(){var o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',o?'false':'true');p.hidden=o;});
      });
    })();
"""

def esc(s): return html.escape(s, quote=True)

def render(cfg, img):
    """img(name) -> src string (relative path atau data URI)."""
    msg_general = cfg.get("wa_general") or "Assalamualaikum, saya tertarik program %s Jadiumrah. Mohon info itinerary, fasilitas, harga, dan ketersediaan seat." % cfg["program"]
    cfg.setdefault("wa_date", WA_DATE)
    n_var = len(cfg["variants"])
    variants_html = []
    for i, v in enumerate(cfg["variants"]):
        dates = "".join(
            '<a class="date" href="%s" target="_blank" rel="noopener"><small>%s</small><b>%s</b><span class="go">%sTanya seat</span></a>'
            % (wa(cfg["wa_date"].format(program=v["program_name"], tanggal=d["full"])), esc(d["sub"]), esc(d["label"]), ICON_WA)
            for d in v["dates"])
        meta = "".join('<span>%s%s</span>' % (IC[k], esc(t)) for k, t in v["meta"])
        variants_html.append(f'''
        <article class="variant{' variant--dark' if v.get('dark') else ''}">
          <div class="variant__head">
            <div><h3>{esc(v["title"])}</h3><p class="note">{esc(v["subtitle"])}</p></div>
            <div class="variant__price"><small>Mulai dari</small>{esc(v["price"])}</div>
          </div>
          <div class="variant__meta">{meta}</div>
          <div class="dates">{dates}</div>
          <p class="note">{esc(v["note"])}</p>
        </article>''')
    cards = "".join(f'<div class="card"><div class="card__ic">{IC[c[0]]}</div><h3>{esc(c[1])}</h3><p>{esc(c[2])}</p></div>' for c in cfg["cards"])
    why = "".join(f'<div class="numcard{" numcard--dark" if i==0 else ""}"><p class="numcard__n">0{i+1}</p><h3>{esc(w[0])}</h3><p>{esc(w[1])}</p></div>' for i, w in enumerate(cfg["why"]))
    steps = "".join(f'<li class="step"><div class="step__n">{i+1}</div><h3>{esc(s[0])}</h3><p>{esc(s[1])}</p></li>' for i, s in enumerate(cfg["steps"]))
    faq = "".join(f'<div class="faq__item"><h3><button class="faq__t" type="button" id="q{i+1}" aria-expanded="false" aria-controls="a{i+1}">{esc(q)}</button></h3><div class="faq__p" id="a{i+1}" role="region" aria-labelledby="q{i+1}" hidden>{esc(a)}</div></div>' for i, (q, a) in enumerate(cfg["faq"]))
    cross = "".join(f'<a href="{wa(c["wa"])}" target="_blank" rel="noopener"><div><strong>{esc(c["title"])}</strong><span>{esc(c["sub"])}</span></div><span class="go">Tanya via WA →</span></a>' for c in cfg["cross"])
    chips = "".join(f'<li class="chip">{IC[k]}{esc(t)}</li>' for k, t in cfg["chips"])
    ticks = "".join(f'<li>{esc(t)}</li>' for t in [f"Izin PPIU {PPIU}", COMPANY] + cfg["ticks"])
    h1 = cfg["h1"].replace("[", '<span class="hl">').replace("]", "</span>")
    wa_gen = wa(msg_general)
    return f'''<!doctype html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(cfg["title"])}</title>
  <meta name="description" content="{esc(cfg["description"])}">
  <meta name="theme-color" content="#173E35">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="id_ID">
  <meta property="og:title" content="{esc(cfg["title"])}">
  <meta property="og:description" content="{esc(cfg["description"])}">
  <!-- og:image: isi URL HTTPS publik gambar 1200x630 bila sudah ada hosting -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>{CSS}  </style>
</head>
<body>

<header class="hdr">
  <div class="wrap">
    <a class="brand" href="#top" aria-label="Jadiumrah"><img class="brand__logo" src="{img('logo-cream.png')}" alt="Jadiumrah" width="788" height="245"><span class="brand__tag">Umrah Tenang<br>Menyenangkan</span></a>
    <a class="btn btn--wa btn--sm" href="{wa_gen}" target="_blank" rel="noopener">{ICON_WA}Chat Admin</a>
  </div>
</header>

<main id="top">
  <section class="hero" aria-labelledby="h1">
    <div class="wrap hero__grid">
      <div>
        <span class="pill">{esc(cfg["pill"])}</span>
        <h1 id="h1">{h1}</h1>
        <p class="hero__desc">{esc(cfg["desc"])}</p>
        <ul class="chips" aria-label="Ringkasan program">{chips}</ul>
        <div class="price">
          <div class="price__k"><small>Harga mulai dari</small><strong>{esc(cfg["price"])} <em>/ jamaah</em></strong></div>
          <p><strong>{esc(cfg["price_lead"])}</strong> {esc(cfg["price_note"])}</p>
        </div>
        <div class="hero__actions">
          <a class="btn btn--wa" href="{wa_gen}" target="_blank" rel="noopener">{ICON_WA}{esc(cfg["cta_main"])}</a>
          <a class="btn btn--outline" href="#jadwal">Lihat Pilihan Tanggal</a>
        </div>
        <ul class="ticks">{ticks}</ul>
      </div>
      <figure class="hero__visual">
        <img src="{img(cfg["hero_img"])}" width="{cfg["hero_w"]}" height="{cfg["hero_h"]}" alt="{esc(cfg["hero_alt"])}" fetchpriority="high">
        <figcaption>Dokumentasi perjalanan bersama Jadiumrah.</figcaption>
      </figure>
    </div>
  </section>

  <section class="overlap" aria-label="Keunggulan program">
    <div class="wrap"><div class="cards4">{cards}</div></div>
  </section>

  <section class="section" id="jadwal" aria-labelledby="h-jadwal">
    <div class="wrap">
      <p class="eyebrow">Pilih tanggal keberangkatan</p>
      <h2 class="h2" id="h-jadwal">{esc(cfg["jadwal_h2"])}</h2>
      <p class="sub">{esc(cfg["jadwal_sub"])}</p>
      <div class="variants" style="--n:{n_var}">{''.join(variants_html)}</div>
      <div class="bar">
        <div class="bar__ic">{IC["users"]}</div>
        <div><strong>Kuota tiap rombongan dijaga.</strong><span>Supaya pendampingan tetap personal, seat per tanggal tidak kami buka tanpa batas. Tanya ketersediaan sebelum penuh.</span></div>
        <a class="btn btn--wa btn--sm" href="{wa_gen}" target="_blank" rel="noopener">{ICON_WA}Cek Seat</a>
      </div>
    </div>
  </section>

  <section class="section section--soft" id="kenapa" aria-labelledby="h-kenapa">
    <div class="wrap">
      <p class="eyebrow">Kenapa Jadiumrah</p>
      <h2 class="h2" id="h-kenapa">{esc(cfg["why_h2"])}</h2>
      <div class="numcards">{why}</div>
    </div>
  </section>

  <section class="section" id="cara" aria-labelledby="h-cara">
    <div class="wrap">
      <p class="eyebrow">Cara daftar</p>
      <h2 class="h2" id="h-cara">Tiga langkah, tanggalmu terkunci.</h2>
      <ol class="steps">{steps}</ol>
      <p class="sub" style="font-size:.9rem">Tidak ada pembayaran di halaman ini. Rincian harga, fasilitas, itinerary, dan ketentuan dikonfirmasi tertulis oleh admin sebelum Anda memutuskan.</p>
    </div>
  </section>

  <section class="section section--soft" id="faq" aria-labelledby="h-faq">
    <div class="wrap">
      <p class="eyebrow">FAQ</p>
      <h2 class="h2" id="h-faq">Yang sering ditanyakan sebelum chat admin.</h2>
      <div class="faq">{faq}</div>
    </div>
  </section>

  <section class="section" id="konsultasi" aria-labelledby="h-cta">
    <div class="wrap">
      <div class="panel">
        <h2 id="h-cta">{esc(cfg["closing_h2"])}</h2>
        <p>{esc(cfg["closing_p"])}</p>
        <a class="btn btn--wa" href="{wa_gen}" target="_blank" rel="noopener">{ICON_WA}{esc(cfg["cta_close"])}</a>
        <small>Balasan dari admin Jadiumrah. Tidak ada pembayaran di halaman ini.</small>
      </div>
    </div>
  </section>

  <section class="section section--soft" id="program-lain" aria-labelledby="h-lain">
    <div class="wrap">
      <p class="eyebrow">Program lain Jadiumrah 2027</p>
      <h2 class="h2" id="h-lain">Tanggalnya belum pas? Lihat pilihan lainnya.</h2>
      <div class="cross">{cross}</div>
    </div>
  </section>
</main>

<footer class="ftr">
  <div class="wrap">
    <div class="ftr__grid">
      <div>
        <a class="brand brand--lg" href="#top"><img class="brand__logo" src="{img('logo-cream.png')}" alt="Jadiumrah" width="788" height="245"></a>
        <p class="ftr__tag">Umrah Tenang Menyenangkan</p>
      </div>
      <div><h4>Hubungi kami</h4><ul><li><a href="{wa_gen}" target="_blank" rel="noopener">WhatsApp Admin</a></li></ul></div>
      <div><h4>Legalitas</h4><ul><li>{esc(COMPANY)}</li><li>Izin PPIU {PPIU}</li></ul></div>
    </div>
    <div class="ftr__bottom">
      <p>{esc(cfg["footnote"])}</p>
      <p>&copy; <span data-year></span> Jadiumrah. Umrah Tenang Menyenangkan.</p>
    </div>
  </div>
</footer>

<div class="sticky"><a class="btn btn--wa" href="{wa_gen}" target="_blank" rel="noopener">{ICON_WA}{esc(cfg["cta_sticky"])}</a></div>

<script>{JS}</script>
</body>
</html>
'''

# ---------------------------------------------------------------- KONTEN 3 PROGRAM
WA_DATE = "Assalamualaikum, saya tertarik program {program} Jadiumrah keberangkatan {tanggal}. Mohon info itinerary, fasilitas, harga, dan ketersediaan seat."
CROSS_HEMAT = {"title": "Umroh Hemat Januari 2027", "sub": "9 hari · 12, 19, 26 Januari · transit · mulai Rp32,9 jt", "wa": "Assalamualaikum, saya ingin info program Umroh Hemat Januari 2027 Jadiumrah."}
CROSS_RAMADAN = {"title": "Umroh Awal Ramadan 2027", "sub": "9 hari · 2 & 9 Februari · Saudia direct · mulai Rp35,9 jt", "wa": "Assalamualaikum, saya ingin info program Umroh Awal Ramadan 2027 Jadiumrah."}
CROSS_SYAWAL = {"title": "Umroh Syawal 2027", "sub": "9 hari · 12, 15, 18, 20 Maret · direct/transit · mulai Rp30,9 jt", "wa": "Assalamualaikum, saya ingin info program Umroh Syawal 2027 Jadiumrah."}

COMMON_STEPS = [
    ("Chat admin, sebut tanggal pilihanmu", "Klik tombol WhatsApp, pesan sudah terisi. Tambahkan jumlah jamaah dan kebutuhan khusus bila ada."),
    ("Terima rincian tertulis", "Admin kirim itinerary, fasilitas yang termasuk, harga sesuai pilihan kamar, dan ketentuan pendaftaran."),
    ("Amankan seat, lalu persiapan", "Setelah cocok, seat dikunci sesuai ketentuan. Tim bantu dokumen dan pembekalan sampai hari keberangkatan."),
]
COMMON_TICKS = ["Rombongan terjaga, pendampingan personal", "Konsultasi gratis, tanpa komitmen"]

PAGES = [
 {
  "slug": "umroh-hemat-januari-2027", "program": "Umroh Hemat Januari 2027",
  "title": "Umroh Hemat Januari 2027 Mulai Rp32,9 Juta | Jadiumrah",
  "description": "Umroh 9 hari Januari 2027 bersama Jadiumrah. Pilih 12, 19, atau 26 Januari. Penerbangan transit Qatar Airways, Etihad, atau Oman Air. Mulai Rp32,9 juta. Chat admin sekarang.",
  "pill": "Umroh Hemat · 9 Hari · Januari 2027",
  "h1": "Berhenti Bilang “Nanti”. [Januari 2027], Kamu Berangkat Umroh.",
  "desc": "Sudah lama ingin umroh tapi tiap ditanya kapan, jawabannya selalu nanti? Program Umroh Hemat Jadiumrah memberi kamu tiga tanggal pasti di Januari 2027 dengan harga yang masuk akal. Tinggal pilih, lalu chat admin.",
  "chips": [("cal", "12 · 19 · 26 Januari 2027"), ("clock", "9 hari"), ("plane", "Qatar Airways / Etihad / Oman Air")],
  "price": "Rp32,9 jt",
  "price_lead": "Program hemat, pendampingan tetap personal.",
  "price_note": "Harga mengikuti ketersediaan program dan pilihan kamar. Rincian pasti dikirim admin via WhatsApp.",
  "cta_main": "Tanya Admin via WhatsApp",
  "ticks": COMMON_TICKS,
  "hero_img": "rombongan-uhud.jpg", "hero_w": 1000, "hero_h": 1333,
  "hero_alt": "Rombongan jamaah Jadiumrah berfoto bersama di kawasan Jabal Uhud, Madinah.",
  "cards": [
    ("tag", "Mulai Rp32,9 juta", "Pilihan paling hemat di awal 2027, tanpa mengorbankan pendampingan."),
    ("cal", "Tiga tanggal pasti", "12, 19, atau 26 Januari. Sesuaikan dengan cuti dan agenda keluarga."),
    ("plane", "Maskapai transit ternama", "Qatar Airways, Etihad, atau Oman Air sesuai ketersediaan program."),
    ("users", "Rombongan terjaga", "Kuota dijaga agar pendamping sempat mengenal setiap jamaah."),
  ],
  "jadwal_h2": "Tiga tanggal di Januari 2027. Mana yang paling memungkinkan untukmu?",
  "jadwal_sub": "Klik tanggal, pesan WhatsApp langsung terisi. Admin akan menjawab dengan rincian itinerary, fasilitas, dan ketersediaan seat untuk tanggal itu.",
  "variants": [{
    "program_name": "Umroh Hemat Januari 2027", "title": "Umroh Hemat 9 Hari", "subtitle": "Penerbangan transit, pilihan maskapai sesuai ketersediaan program.",
    "price": "Rp32,9 jt", "dark": True,
    "meta": [("clock", "9 hari"), ("plane", "Qatar Airways / Etihad / Oman Air"), ("pin", "Makkah & Madinah")],
    "dates": [{"sub": "Selasa", "label": "12 Jan 2027", "full": "12 Januari 2027"}, {"sub": "Selasa", "label": "19 Jan 2027", "full": "19 Januari 2027"}, {"sub": "Selasa", "label": "26 Jan 2027", "full": "26 Januari 2027"}],
    "note": "Harga mulai dari, per jamaah. Konfirmasi fasilitas dan ketentuan ke admin sebelum memutuskan.",
  }],
  "why_h2": "Hemat bukan berarti dilepas sendirian.",
  "why": [
    ("Pendampingan yang dekat", "Jumlah jamaah per rombongan dijaga, sehingga tim punya ruang mengenali kebutuhanmu dan menjawab pertanyaan tanpa antre panjang."),
    ("Izin resmi dan terdaftar", f"{COMPANY}, pemegang Izin PPIU {PPIU}. Berangkat dengan travel yang jelas legalitasnya."),
    ("Tanggal pasti, rencana jelas", "Tiga tanggal keberangkatan sudah ditetapkan. Kamu tinggal menyesuaikan cuti, bukan menunggu kepastian."),
    ("Dibimbing dari persiapan sampai pulang", "Pembekalan sebelum berangkat, arahan di setiap tahapan ibadah, dan pendamping yang kamu kenal sejak awal."),
  ],
  "steps": COMMON_STEPS,
  "faq": [
    ("Rp32,9 juta itu sudah termasuk apa saja?", "Rincian fasilitas yang termasuk, pilihan kamar, dan ketentuan harga dikirim tertulis oleh admin. Klik tombol WhatsApp dan sebut tanggal yang kamu minati."),
    ("Maskapainya pasti yang mana?", "Qatar Airways, Etihad, atau Oman Air, mengikuti ketersediaan program pada tanggal yang kamu pilih. Admin akan mengonfirmasi maskapai untuk tanggal tersebut."),
    ("Saya belum pernah umroh, apakah cocok?", "Cocok. Ada pembekalan sebelum berangkat, arahan di setiap tahapan, dan pendamping yang dikenalkan sejak awal. Pertanyaan apa pun boleh disampaikan sejak chat pertama."),
    ("Bisa berangkat bersama orang tua?", "Bisa. Sampaikan kondisi dan kebutuhan mereka saat chat, agar admin menjelaskan bentuk bantuan yang tersedia pada tanggal pilihanmu."),
    ("Kalau belum yakin, boleh tanya-tanya dulu?", "Boleh, konsultasi gratis dan tanpa komitmen. Tidak ada pembayaran di halaman ini."),
  ],
  "closing_h2": "Januari 2027 masih sempat kamu siapkan. Mulai dari satu chat.",
  "closing_p": "Sebut tanggal yang kamu minati, admin Jadiumrah kirim itinerary, fasilitas, dan ketersediaan seat. Setelah itu, keputusan tetap di tanganmu.",
  "cta_close": "Chat Admin, Tanya Seat Januari",
  "cta_sticky": "Tanya Seat Januari via WhatsApp",
  "cross": [CROSS_RAMADAN, CROSS_SYAWAL],
  "footnote": "Harga mulai dari Rp32,9 juta per jamaah, mengikuti ketersediaan program dan pilihan kamar. Maskapai Qatar Airways, Etihad, atau Oman Air sesuai ketersediaan. Rincian dan ketentuan dikonfirmasi tertulis oleh admin.",
 },
 {
  "slug": "umroh-awal-ramadan-2027", "program": "Umroh Awal Ramadan 2027",
  "title": "Umroh Awal Ramadan 2027, Saudia Direct, Mulai Rp35,9 Juta | Jadiumrah",
  "description": "Rasakan awal Ramadan di Tanah Suci. Umroh 9 hari bersama Jadiumrah, berangkat 2 atau 9 Februari 2027, Saudia Airlines penerbangan direct, mulai Rp35,9 juta. Chat admin sekarang.",
  "pill": "Umroh Awal Ramadan · 9 Hari · Saudia Direct",
  "h1": "Ramadan Tahun Depan, [Kamu di Makkah].",
  "desc": "Bayangkan membuka Ramadan dengan tarawih di Masjidil Haram. Program Umroh Awal Ramadan 2027 Jadiumrah: 9 hari, penerbangan langsung Saudia Airlines, dua pilihan tanggal di Februari. Seat program Ramadan selalu paling cepat terisi, jadi mulai tanya dari sekarang.",
  "chips": [("cal", "2 · 9 Februari 2027"), ("clock", "9 hari"), ("plane", "Saudia Airlines · direct")],
  "price": "Rp35,9 jt",
  "price_lead": "Penerbangan langsung, tanpa transit.",
  "price_note": "Harga mengikuti ketersediaan program dan pilihan kamar. Rincian pasti dikirim admin via WhatsApp.",
  "cta_main": "Tanya Seat Ramadan via WhatsApp",
  "ticks": COMMON_TICKS,
  "hero_img": "masjidil-haram.jpg", "hero_w": 1200, "hero_h": 675,
  "hero_alt": "Rombongan jamaah Jadiumrah berpakaian ihram di pelataran Masjidil Haram pada malam hari, Ka'bah di latar belakang.",
  "cards": [
    ("plane", "Saudia Airlines direct", "Terbang langsung, lebih hemat tenaga. Tiba lebih segar untuk mulai ibadah."),
    ("cal", "2 atau 9 Februari 2027", "Dua tanggal di awal Ramadan. Pilih yang paling pas dengan cuti dan keluarga."),
    ("tag", "Mulai Rp35,9 juta", "Harga program 9 hari, rincian fasilitas dikirim tertulis oleh admin."),
    ("users", "Rombongan terjaga", "Kuota dijaga agar pendampingan tetap personal di tengah padatnya Ramadan."),
  ],
  "jadwal_h2": "Dua tanggal di awal Ramadan 2027. Pilih yang paling memungkinkan.",
  "jadwal_sub": "Klik tanggal, pesan WhatsApp langsung terisi. Admin menjawab dengan itinerary, fasilitas, dan ketersediaan seat untuk tanggal itu.",
  "variants": [{
    "program_name": "Umroh Awal Ramadan 2027", "title": "Umroh Awal Ramadan 9 Hari", "subtitle": "Penerbangan langsung Saudia Airlines.",
    "price": "Rp35,9 jt", "dark": True,
    "meta": [("clock", "9 hari"), ("plane", "Saudia Airlines · direct"), ("pin", "Makkah & Madinah")],
    "dates": [{"sub": "Selasa", "label": "2 Feb 2027", "full": "2 Februari 2027"}, {"sub": "Selasa", "label": "9 Feb 2027", "full": "9 Februari 2027"}],
    "note": "Harga mulai dari, per jamaah. Konfirmasi fasilitas dan ketentuan ke admin sebelum memutuskan.",
  }],
  "why_h2": "Ramadan di Tanah Suci butuh persiapan matang. Kami dampingi dari awal.",
  "why": [
    ("Pendampingan personal saat Makkah ramai", "Ramadan adalah musim paling padat. Rombongan yang terjaga membuat pendamping tetap bisa memantau dan mengarahkan setiap jamaah."),
    ("Izin resmi dan terdaftar", f"{COMPANY}, pemegang Izin PPIU {PPIU}. Berangkat dengan travel yang jelas legalitasnya."),
    ("Penerbangan langsung", "Saudia Airlines direct, tanpa transit. Lebih ringan untuk jamaah senior dan keluarga dengan anak."),
    ("Dibimbing dari persiapan sampai pulang", "Pembekalan sebelum berangkat, arahan di setiap tahapan ibadah, dan pendamping yang kamu kenal sejak awal."),
  ],
  "steps": COMMON_STEPS,
  "faq": [
    ("Rp35,9 juta itu sudah termasuk apa saja?", "Rincian fasilitas, pilihan kamar, dan ketentuan harga dikirim tertulis oleh admin. Klik tombol WhatsApp dan sebut tanggal yang kamu minati."),
    ("Kenapa harus tanya dari sekarang?", "Program Ramadan biasanya paling cepat terisi, dan kuota per rombongan kami jaga. Tanya lebih awal memberi kamu waktu menyiapkan dokumen dan memilih tanggal dengan tenang."),
    ("Apakah penerbangannya benar-benar direct?", "Ya, program ini menggunakan Saudia Airlines dengan penerbangan langsung. Jadwal pasti dikonfirmasi admin untuk tanggal pilihanmu."),
    ("Saya baru pertama kali umroh, apakah cocok?", "Cocok. Ada pembekalan sebelum berangkat, arahan di setiap tahapan, dan pendamping yang dikenalkan sejak awal."),
    ("Bisa berangkat bersama orang tua?", "Bisa. Sampaikan kondisi dan kebutuhan mereka saat chat, agar admin menjelaskan bentuk bantuan yang tersedia."),
  ],
  "closing_h2": "Ramadan 2027 tinggal beberapa bulan. Amankan rencanamu sekarang.",
  "closing_p": "Sebut tanggal 2 atau 9 Februari, admin Jadiumrah kirim itinerary, fasilitas, dan ketersediaan seat. Keputusan tetap di tanganmu, tapi seat tidak menunggu.",
  "cta_close": "Chat Admin, Tanya Seat Ramadan",
  "cta_sticky": "Tanya Seat Ramadan via WhatsApp",
  "cross": [CROSS_HEMAT, CROSS_SYAWAL],
  "footnote": "Harga mulai dari Rp35,9 juta per jamaah, mengikuti ketersediaan program dan pilihan kamar. Saudia Airlines penerbangan langsung. Rincian dan ketentuan dikonfirmasi tertulis oleh admin.",
 },
 {
  "slug": "umroh-syawal-2027", "program": "Umroh Syawal 2027",
  "title": "Umroh Syawal 2027 Mulai Rp30,9 Juta, Direct atau Transit | Jadiumrah",
  "description": "Umroh Syawal 9 hari Maret 2027 bersama Jadiumrah. Transit mulai Rp30,9 juta (15 & 20 Maret) atau direct mulai Rp35,9 juta (12 & 18 Maret). Pilih tanggalmu, chat admin sekarang.",
  "pill": "Umroh Syawal · 9 Hari · Maret 2027",
  "h1": "Umroh Setelah Ramadan, [Mulai Rp30,9 Juta]. Pilih Direct atau Transit.",
  "desc": "Belum bisa ambil jadwal saat Ramadan? Umroh Syawal 2027 Jadiumrah punya empat tanggal di Maret dan dua pilihan penerbangan. Budget Rp30 sampai 35 jutaan? Dua-duanya masuk. Tinggal pilih yang paling cocok, lalu chat admin.",
  "chips": [("cal", "12 · 15 · 18 · 20 Maret 2027"), ("clock", "9 hari"), ("plane", "Direct atau transit")],
  "price": "Rp30,9 jt",
  "price_lead": "Transit mulai Rp30,9 jt, direct mulai Rp35,9 jt.",
  "price_note": "Harga mengikuti ketersediaan program dan pilihan kamar. Rincian pasti dikirim admin via WhatsApp.",
  "cta_main": "Tanya Admin via WhatsApp",
  "ticks": COMMON_TICKS,
  "hero_img": "keluarga-kabah.jpg", "hero_w": 1000, "hero_h": 1333,
  "hero_alt": "Keluarga jamaah Jadiumrah, orang tua bersama tiga anak, berfoto di depan Ka'bah.",
  "cards": [
    ("tag", "Dua pilihan harga", "Transit mulai Rp30,9 juta atau direct mulai Rp35,9 juta. Sesuaikan dengan budget."),
    ("cal", "Empat tanggal di Maret", "12, 15, 18, atau 20 Maret 2027. Mudah disesuaikan dengan cuti setelah Lebaran."),
    ("plane", "Direct atau transit", "Saudia / Garuda Indonesia untuk direct, Qatar Airways / Emirates untuk transit."),
    ("users", "Rombongan terjaga", "Kuota dijaga agar pendamping sempat mengenal setiap jamaah."),
  ],
  "jadwal_h2": "Dua program, empat tanggal. Bandingkan, lalu klik yang paling pas.",
  "jadwal_sub": "Klik tanggal, pesan WhatsApp langsung terisi dengan program dan tanggalnya. Admin menjawab dengan itinerary, fasilitas, dan ketersediaan seat.",
  "variants": [
    {
      "program_name": "Umroh Syawal 2027 (transit)", "title": "Syawal Transit", "subtitle": "Paling hemat. Qatar Airways atau Emirates sesuai ketersediaan program.",
      "price": "Rp30,9 jt", "dark": True,
      "meta": [("clock", "9 hari"), ("plane", "Qatar Airways / Emirates"), ("pin", "Makkah & Madinah")],
      "dates": [{"sub": "Senin", "label": "15 Mar 2027", "full": "15 Maret 2027"}, {"sub": "Sabtu", "label": "20 Mar 2027", "full": "20 Maret 2027"}],
      "note": "Harga mulai dari, per jamaah. Konfirmasi fasilitas dan ketentuan ke admin.",
    },
    {
      "program_name": "Umroh Syawal 2027 (direct)", "title": "Syawal Direct", "subtitle": "Terbang langsung. Saudia Airlines atau Garuda Indonesia sesuai ketersediaan program.",
      "price": "Rp35,9 jt", "dark": False,
      "meta": [("clock", "9 hari"), ("plane", "Saudia / Garuda Indonesia · direct"), ("pin", "Makkah & Madinah")],
      "dates": [{"sub": "Jumat", "label": "12 Mar 2027", "full": "12 Maret 2027"}, {"sub": "Kamis", "label": "18 Mar 2027", "full": "18 Maret 2027"}],
      "note": "Harga mulai dari, per jamaah. Konfirmasi fasilitas dan ketentuan ke admin.",
    },
  ],
  "why_h2": "Sebelum memilih paket, jangan cuma lihat tanggal dan harga.",
  "why": [
    ("Maskapai dan jenis penerbangan jelas", "Kamu tahu sejak awal mana yang direct dan mana yang transit, berikut pilihan maskapainya. Tidak ada kejutan di bandara."),
    ("Izin resmi dan terdaftar", f"{COMPANY}, pemegang Izin PPIU {PPIU}. Berangkat dengan travel yang jelas legalitasnya."),
    ("Fasilitas dijelaskan tertulis", "Minta rincian fasilitas yang termasuk sebelum memutuskan, supaya kamu bisa membandingkan kedua program secara objektif."),
    ("Rombongan terjaga, pendampingan personal", "Kuota per rombongan dijaga. Pembekalan sebelum berangkat, arahan di setiap tahapan, pendamping yang kamu kenal."),
  ],
  "steps": COMMON_STEPS,
  "faq": [
    ("Apa beda program transit dan direct selain harga?", "Perbedaan utamanya pada penerbangan: transit dengan Qatar Airways atau Emirates (15 & 20 Maret, mulai Rp30,9 juta), direct dengan Saudia atau Garuda Indonesia (12 & 18 Maret, mulai Rp35,9 juta). Perbedaan fasilitas dan itinerary dijelaskan admin secara tertulis."),
    ("Harga itu sudah termasuk apa saja?", "Rincian fasilitas, pilihan kamar, dan ketentuan harga dikirim admin via WhatsApp. Sebut program dan tanggal yang kamu minati."),
    ("Maskapainya pasti yang mana?", "Mengikuti ketersediaan program pada tanggal pilihanmu. Admin akan mengonfirmasi maskapai untuk tanggal tersebut."),
    ("Saya baru pertama kali umroh, apakah cocok?", "Cocok. Ada pembekalan sebelum berangkat, arahan di setiap tahapan, dan pendamping yang dikenalkan sejak awal."),
    ("Bisa berangkat bersama orang tua atau anak?", "Bisa. Sampaikan kondisi dan kebutuhan keluarga saat chat, agar admin menjelaskan bentuk bantuan yang tersedia dan menyarankan program yang paling sesuai."),
  ],
  "closing_h2": "Jangan sampai rencana umroh tertunda lagi hanya karena belum ketemu tanggal.",
  "closing_p": "Empat tanggal, dua pilihan penerbangan. Sebut yang kamu minati, admin Jadiumrah kirim perbedaan fasilitas, itinerary, dan ketersediaan seat.",
  "cta_close": "Chat Admin, Bandingkan Program Syawal",
  "cta_sticky": "Tanya Seat Syawal via WhatsApp",
  "cross": [CROSS_HEMAT, CROSS_RAMADAN],
  "footnote": "Harga mulai dari Rp30,9 juta (transit) dan Rp35,9 juta (direct) per jamaah, mengikuti ketersediaan program dan pilihan kamar. Maskapai sesuai ketersediaan. Rincian dan ketentuan dikonfirmasi tertulis oleh admin.",
 },
]

def main():
    img_dir, out_dir = sys.argv[1], sys.argv[2]
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    def embedded(name):
        mime = "image/png" if name.endswith(".png") else "image/jpeg"
        with open(os.path.join(img_dir, name), "rb") as f:
            return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())
    def relative(name):
        return "../assets/images/" + name if name == "logo-cream.png" else "assets/images/" + name
    for cfg in PAGES:
        rel = render(cfg, relative)
        emb = render(cfg, embedded)
        with open(os.path.join(here, cfg["slug"] + ".html"), "w") as f: f.write(rel)
        with open(os.path.join(out_dir, cfg["slug"] + ".html"), "w") as f: f.write(emb)
        print(cfg["slug"], "relative KB", len(rel.encode())//1024, "| embedded KB", len(emb.encode())//1024)

if __name__ == "__main__":
    main()
