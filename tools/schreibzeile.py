import os
ASSETS=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets")
lines=[
 "Autonome Roboter – von der Idee bis zur Platine",
 "Autonomous robots – from idea to PCB",
 "ROS 2 · SLAM · Nav2 · Gazebo",
 "AprilTag-Navigation für eine Drohnenflotte",
 "ESP32 · Arduino · Raspberry Pi · Python · C++",
]
W,H=820,46; fs=20; cw=11.4; per=4.0; T=per*len(lines)
CYAN="#22d3ee"; TXT="#c9d1d9"
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{" / ".join(lines)}">']
css=['.m{font-family:"JetBrains Mono","Fira Code",Consolas,"DejaVu Sans Mono",monospace}']
defs=[]; body=[]
t_type=1.5; t_hold=3.6
for i,l in enumerate(lines):
    n=len(l)+2                      # "> " davor
    w=n*cw; x0=(W-w)/2
    a=t_type/T*100; b=t_hold/T*100; c=per/T*100
    css.append(f'@keyframes k{i}{{0%{{transform:scaleX(0);animation-timing-function:steps({n},end)}}{a:.2f}%{{transform:scaleX(1)}}{b:.2f}%{{transform:scaleX(1);animation-timing-function:steps({n},end)}}{c:.2f}%{{transform:scaleX(0)}}100%{{transform:scaleX(0)}}}}')
    css.append(f'@keyframes c{i}{{0%{{transform:translateX(0);opacity:1;animation-timing-function:steps({n},end)}}{a:.2f}%{{transform:translateX({w:.1f}px)}}{b:.2f}%{{transform:translateX({w:.1f}px);animation-timing-function:steps({n},end)}}{c:.2f}%{{transform:translateX(0);opacity:1}}{c+0.01:.2f}%{{opacity:0}}100%{{opacity:0}}}}')
    css.append(f'.r{i}{{transform-origin:{x0:.1f}px 0;animation:k{i} {T}s infinite;animation-delay:{i*per}s;transform:scaleX(0)}}')
    css.append(f'.q{i}{{animation:c{i} {T}s infinite;animation-delay:{i*per}s;opacity:0}}')
    defs.append(f'<clipPath id="cl{i}"><rect class="r{i}" x="{x0:.1f}" y="0" width="{w:.1f}" height="{H}"/></clipPath>')
    body.append(f'<g clip-path="url(#cl{i})"><text class="m" x="{x0:.1f}" y="30" font-size="{fs}" textLength="{w:.1f}" lengthAdjust="spacingAndGlyphs" fill="{TXT}"><tspan fill="{CYAN}">&gt; </tspan>{l}</text></g>')
    body.append(f'<rect class="q{i}" x="{x0+1:.1f}" y="12" width="10" height="22" fill="{CYAN}"/>')
o.append("<style>"+"\n".join(css)+"</style>")
o.append(f'<rect width="{W}" height="{H}" rx="10" fill="#0b1220"/>')
o.append("<defs>"+"".join(defs)+"</defs>")
o+=body
o.append("</svg>")
open(os.path.join(ASSETS,'typing.svg'),'w').write("\n".join(o))
print("ok")
