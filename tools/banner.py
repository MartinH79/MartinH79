import os
ASSETS=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets")
bits=[[0,0,0,0,0,0,0,0],[0,1,1,0,1,0,0,0],[0,1,0,1,0,0,1,0],[0,0,0,0,0,1,0,0],[0,1,0,1,0,1,0,0],[0,0,1,1,1,0,1,0],[0,1,1,1,0,1,1,0],[0,0,0,0,0,0,0,0]]
W,H=1200,320
BG="#0b1220"; TRACE="#17233a"; CYAN="#22d3ee"; TXT="#e6edf3"; MUTED="#8b949e"
cell=17; tagN=10; tag=cell*tagN   # 170 px inkl. weißem Rand
tx,ty=930,75                       # Lage des Tags (vor Transformation)
traces=[
 "M0 282 H250 L275 302 H520 L545 282 H700 L730 252 H860",
 "M600 150 H655 L685 120 H770",
 "M640 0 V40 L680 80 H780 L800 100",
 "M1200 310 H1000",
 "M1200 40 H1150 L1120 70 V140",
 "M380 0 V25 L405 50 H610",
 "M0 320 V318",
]
vias=[(860,252),(770,120),(800,100),(1000,310),(1120,140),(610,50),(600,150),(520,302)]
o=[]
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Martin – Robotik, Embedded, Autonome Systeme">')
o.append('''<style>
.t{font-family:"Segoe UI",Ubuntu,"Helvetica Neue",Arial,sans-serif}
.m{font-family:"JetBrains Mono","Fira Code",Consolas,"DejaVu Sans Mono",monospace}
.p{fill:none;stroke:#22d3ee;stroke-width:2;stroke-linecap:round;stroke-dasharray:46 1400;animation:run 6s linear infinite;filter:url(#glow)}
@keyframes run{from{stroke-dashoffset:1446}to{stroke-dashoffset:0}}
.via{animation:blink 3s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:.35}50%{opacity:1}}
.scan{animation:scan 3.2s ease-in-out infinite}
@keyframes scan{0%{transform:translateY(-20px);opacity:0}15%{opacity:.9}85%{opacity:.9}100%{transform:translateY(190px);opacity:0}}
.br{animation:pulse 3.2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:.55}50%{opacity:1}}
.ax{stroke-dasharray:80;stroke-dashoffset:80;animation:draw 3.2s ease-out infinite}
@keyframes draw{0%,10%{stroke-dashoffset:80}35%,90%{stroke-dashoffset:0}100%{stroke-dashoffset:80}}
.cur{animation:cur 1s steps(1) infinite}
@keyframes cur{50%{opacity:0}}
.fade{animation:fade 1.2s ease-out both}
@keyframes fade{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
</style>''')
o.append('''<defs>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="vig" cx="78%" cy="45%" r="60%"><stop offset="0" stop-color="#22d3ee" stop-opacity=".10"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#1b2840"/></pattern>
<linearGradient id="scanG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22d3ee" stop-opacity="0"/><stop offset=".5" stop-color="#22d3ee" stop-opacity=".55"/><stop offset="1" stop-color="#22d3ee" stop-opacity="0"/></linearGradient>
<clipPath id="card"><rect width="1200" height="320" rx="18"/></clipPath>''')
o.append(f'<clipPath id="tagclip"><rect x="{tx}" y="{ty}" width="{tag}" height="{tag}"/></clipPath></defs>')
o.append('<g clip-path="url(#card)">')
o.append(f'<rect width="{W}" height="{H}" fill="{BG}"/><rect width="{W}" height="{H}" fill="url(#dots)"/><rect width="{W}" height="{H}" fill="url(#vig)"/>')
for p in traces: o.append(f'<path d="{p}" fill="none" stroke="{TRACE}" stroke-width="3" stroke-linejoin="round"/>')
for i,p in enumerate(traces): o.append(f'<path class="p" d="{p}" style="animation-delay:-{i*0.9:.1f}s;animation-duration:{5+i%3*1.3:.1f}s"/>')
for i,(x,y) in enumerate(vias): o.append(f'<circle class="via" cx="{x}" cy="{y}" r="5" fill="{BG}" stroke="{CYAN}" stroke-width="2" style="animation-delay:-{i*0.4:.1f}s"/>')
# Text
o.append(f'<g class="fade"><text class="m" x="72" y="96" font-size="18" fill="{CYAN}">~/robotik $ whoami</text>')
o.append(f'<text class="t" x="68" y="168" font-size="76" font-weight="700" fill="{TXT}" textLength="246" lengthAdjust="spacingAndGlyphs">Martin</text>')
o.append(f'<rect class="cur" x="328" y="112" width="14" height="60" fill="{CYAN}"/>')
o.append(f'<text class="t" x="72" y="212" font-size="25" fill="{TXT}">Robotik · Embedded · Autonome Systeme</text>')
o.append(f'<text class="m" x="72" y="244" font-size="16" fill="{MUTED}">Robotics · Embedded · Autonomous Systems</text></g>')
# Tag: leicht gedreht wie aus Kamerasicht
o.append(f'<g transform="rotate(-8 {tx+tag/2} {ty+tag/2}) skewX(-4)">')
o.append(f'<rect x="{tx}" y="{ty}" width="{tag}" height="{tag}" fill="{TXT}"/>')
for r,row in enumerate(bits):
    for c,b in enumerate(row):
        if not b: o.append(f'<rect x="{tx+(c+1)*cell}" y="{ty+(r+1)*cell}" width="{cell+0.5}" height="{cell+0.5}" fill="{BG}"/>')
o.append(f'<g clip-path="url(#tagclip)"><rect class="scan" x="{tx}" y="{ty}" width="{tag}" height="26" fill="url(#scanG)"/></g>')
# Erkennungsrahmen (Ecken) um das schwarze Quadrat
x0,y0,x1,y1=tx+cell-6,ty+cell-6,tx+tag-cell+6,ty+tag-cell+6; L=22
br=f"M{x0} {y0+L}V{y0}H{x0+L} M{x1-L} {y0}H{x1}V{y0+L} M{x1} {y1-L}V{y1}H{x1-L} M{x0+L} {y1}H{x0}V{y1-L}"
o.append(f'<path class="br" d="{br}" fill="none" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>')
cx_,cy_=tx+tag/2,ty+tag/2
o.append(f'<circle cx="{x0+6}" cy="{y1-6}" r="5" fill="#f87171"/>')
o.append(f'<line class="ax" x1="{cx_}" y1="{cy_}" x2="{cx_+62}" y2="{cy_}" stroke="#f87171" stroke-width="4" stroke-linecap="round"/>')
o.append(f'<line class="ax" x1="{cx_}" y1="{cy_}" x2="{cx_}" y2="{cy_+62}" stroke="#4ade80" stroke-width="4" stroke-linecap="round"/>')
o.append(f'<line class="ax" x1="{cx_}" y1="{cy_}" x2="{cx_-30}" y2="{cy_-38}" stroke="#60a5fa" stroke-width="4" stroke-linecap="round"/>')
o.append('</g>')
o.append(f'<text class="m" x="905" y="292" font-size="14" fill="{MUTED}">tag36h11 · id 42 · <tspan fill="{CYAN}">locked</tspan></text>')
o.append('</g></svg>')
open(os.path.join(ASSETS,'banner.svg'),'w').write("\n".join(o))
print("ok", sum(len(x) for x in o), "Zeichen")
