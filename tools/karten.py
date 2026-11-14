import os
ASSETS=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","assets")
import re, textwrap, html
SI=os.environ.get("SIMPLE_ICONS","node_modules/simple-icons/icons/")
BG="#0b1220"; BORDER="#1f2a44"; CYAN="#22d3ee"; TXT="#e6edf3"; SUB="#c9d1d9"; MUTED="#8b949e"; CHIP="#0f2233"
FONT='font-family:"Segoe UI",Ubuntu,"Helvetica Neue",Arial,sans-serif'
MONO='font-family:"JetBrains Mono","Fira Code",Consolas,"DejaVu Sans Mono",monospace'
def icon(slug):
    s=open(SI+slug+".svg").read()
    return re.search(r'<path d="([^"]+)"',s).group(1)
esc=html.escape

# ---------- Technik-Übersicht ----------
reihen=[
 ("Sprachen","Languages",[("Python","python"),("C++","cplusplus"),("Kotlin","kotlin")]),
 ("Embedded","Embedded",[("Arduino","arduino"),("ESP32","espressif"),("Raspberry Pi","raspberrypi")]),
 ("Robotik","Robotics",[("ROS 2","ros"),("ArduPilot",None),("OpenCV","opencv"),("Gazebo",None)]),
 ("Werkzeuge","Tools",[("Linux","linux"),("Git","git"),("Fusion 360","autodesk"),("OpenSCAD","openscad"),("3D-Druck","bambulab"),("MQTT","mqtt")]),
]
W=820; rowh=52; top=22; lx=24; cx0=200
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {top+rowh*len(reihen)+10}" width="{W}" height="{top+rowh*len(reihen)+10}" role="img" aria-label="Technik: '+esc(", ".join(n for _,_,c in reihen for n,_ in c))+'">']
o.append(f'<style>.f{{{FONT}}}.m{{{MONO}}}.c{{opacity:0;animation:in .5s ease-out forwards}}@keyframes in{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}.c:hover rect{{stroke:{CYAN}}}</style>')
o.append(f'<rect width="{W}" height="{top+rowh*len(reihen)+10}" rx="14" fill="{BG}"/>')
k=0
for r,(de,en,chips) in enumerate(reihen):
    y=top+r*rowh
    o.append(f'<text x="{lx}" y="{y+20}" class="f" font-size="14" font-weight="600" fill="{TXT}">{de}</text>')
    o.append(f'<text x="{lx}" y="{y+37}" class="m" font-size="11.5" fill="{MUTED}">{en}</text>')
    x=cx0
    for name,slug in chips:
        w=int(len(name)*7.6)+ (46 if slug else 30)
        o.append(f'<g class="c" style="animation-delay:{k*0.06:.2f}s">')
        o.append(f'<rect x="{x}" y="{y+4}" width="{w}" height="34" rx="8" fill="{CHIP}" stroke="{BORDER}"/>')
        if slug:
            o.append(f'<path transform="translate({x+12} {y+12}) scale(0.75)" d="{icon(slug)}" fill="{CYAN}"/>')
            tx=x+38
        else:
            o.append(f'<circle cx="{x+15}" cy="{y+21}" r="4" fill="{CYAN}"/>'); tx=x+26
        o.append(f'<text x="{tx}" y="{y+26}" class="f" font-size="14" fill="{SUB}" textLength="{len(name)*7.6:.0f}" lengthAdjust="spacingAndGlyphs">{esc(name)}</text></g>')
        x+=w+10; k+=1
o.append('</svg>')
open(os.path.join(ASSETS,'technik.svg'),'w').write("\n".join(o))

# ---------- Projektkarten ----------
projekte=[
 ("drohnen","AprilTag-Frachtdrohnen","in Arbeit",
  "Flotte aus 8 Quadcoptern, die sich in einer Halle über AprilTags orientiert und Container abholt und abliefert.",
  "Quadcopter fleet navigating a hall via AprilTags to pick up and deliver containers.",
  ["ArduPilot","Pi 5","OpenCV","Python"]),
 ("autonomo","AUTONOMO",None,
  "Autonomer Indoor-Lieferroboter mit RPLidar, Omni-Antrieb, IMU und Kamera-Erkennung mit Edge Impulse.",
  "Autonomous indoor delivery robot: RPLidar, omni drive, IMU, Edge Impulse vision.",
  ["Arduino UNO Q","RPLidar","Edge Impulse"]),
 ("omnibot","Omnibot v2.1",None,
  "Holonomer Roboter mit drei Omniwheels. Kompletter ROS 2 Workspace inklusive Gazebo-Simulation.",
  "Holonomic three-omniwheel robot with a full ROS 2 workspace and Gazebo simulation.",
  ["ROS 2","Gazebo","Python"]),
 ("slam","4WD-Roboter mit SLAM",None,
  "Differentialantrieb mit Kartierung und autonomer Navigation: SLAM Toolbox, Nav2, RPLidar A1, BNO055.",
  "Differential-drive robot with mapping and autonomous navigation using SLAM Toolbox and Nav2.",
  ["ROS 2","Nav2","RPLidar A1"]),
 ("growsmart","GrowSmart","Planung",
  "Modulare Indoor-Pflanzstation mit geschlossenem Wasserkreislauf, Sensorik und Grow-Light, 3D-gedruckt.",
  "Modular indoor grow station with closed water loop, sensors and grow light, 3D-printed.",
  ["Arduino UNO Q","Sensorik","3D-Druck"]),
]
CW,CH=400,200
for slug,titel,status,de,en,tech in projekte:
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW}" height="{CH}" role="img" aria-label="{esc(titel)}: {esc(de)}">']
    o.append('<style>.f{'+FONT+'}.m{'+MONO+'}.pl{animation:pl 1.8s ease-in-out infinite}@keyframes pl{0%,100%{opacity:1}50%{opacity:.25}}'
             '.ln{stroke-dasharray:60 400;animation:ln 4s linear infinite}@keyframes ln{from{stroke-dashoffset:460}to{stroke-dashoffset:0}}</style>')
    o.append(f'<rect x="0.5" y="0.5" width="{CW-1}" height="{CH-1}" rx="12" fill="{BG}" stroke="{BORDER}"/>')
    o.append(f'<path class="ln" d="M14 0.5 H{CW-14}" stroke="{CYAN}" stroke-width="2" stroke-linecap="round" opacity=".8"/>')
    o.append(f'<text x="20" y="38" class="f" font-size="18" font-weight="700" fill="{TXT}">{esc(titel)}</text>')
    if status:
        farbe={"in Arbeit":CYAN,"fertig":"#4ade80","Planung":"#fbbf24"}[status]
        sw=len(status)*7+30
        o.append(f'<rect x="{CW-20-sw}" y="20" width="{sw}" height="24" rx="12" fill="none" stroke="{farbe}" stroke-opacity=".6"/>')
        o.append(f'<circle class="{"pl" if status=="in Arbeit" else ""}" cx="{CW-20-sw+13}" cy="32" r="4" fill="{farbe}"/>')
        o.append(f'<text x="{CW-20-sw+23}" y="36.5" class="f" font-size="12" fill="{farbe}">{status}</text>')
    y=64
    for zeile in textwrap.wrap(de,50)[:3]:
        o.append(f'<text x="20" y="{y}" class="f" font-size="13.5" fill="{SUB}">{esc(zeile)}</text>'); y+=19
    y+=4
    for zeile in textwrap.wrap(en,60)[:2]:
        o.append(f'<text x="20" y="{y}" class="f" font-size="12" font-style="italic" fill="{MUTED}">{esc(zeile)}</text>'); y+=17
    x=20
    for t in tech:
        w=len(t)*7+18
        o.append(f'<rect x="{x}" y="{CH-38}" width="{w}" height="22" rx="6" fill="{CHIP}" stroke="{BORDER}"/>')
        o.append(f'<text x="{x+9}" y="{CH-23}" class="m" font-size="11.5" fill="{CYAN}" textLength="{len(t)*7-2}" lengthAdjust="spacingAndGlyphs">{esc(t)}</text>')
        x+=w+8
    o.append('</svg>')
    open(os.path.join(ASSETS,f'projekt-{slug}.svg'),'w').write("\n".join(o))
print("ok")
