const svg=(body,label)=>`<svg class="scene" viewBox="0 0 780 520" role="img" aria-label="${label}"><defs><linearGradient id="ribbon" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#a80824"/><stop offset=".46" stop-color="#ff4b56"/><stop offset="1" stop-color="#cf0926"/></linearGradient><linearGradient id="ink"><stop stop-color="#3b4ba3"/><stop offset="1" stop-color="#6e79de"/></linearGradient><filter id="shadow"><feDropShadow dx="0" dy="12" stdDeviation="15" flood-opacity=".12"/></filter><pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse"><path d="M34 0H0V34" fill="none" stroke="currentColor" stroke-opacity=".06"/></pattern></defs><rect width="780" height="520" fill="url(#grid)"/>${body}</svg>`;
const text=(x,y,t,cls='label',anchor='middle')=>`<text x="${x}" y="${y}" class="${cls}" text-anchor="${anchor}">${t}</text>`;
const line=(path,cls='wire')=>`<path d="${path}" class="${cls}"/>`;
const dot=(x,y,r=6,cls='accent')=>`<circle cx="${x}" cy="${y}" r="${r}" class="${cls}"/>`;
const doc=(x,y,name,detail,rotate=0)=>`<g transform="translate(${x} ${y}) rotate(${rotate})"><rect width="150" height="190" rx="9" class="paper" filter="url(#shadow)"/><path d="M26 65H124M26 87H109M26 109H124M26 131H93" class="doc-lines"/>${text(75,38,name,'doc-title')}${text(75,165,detail,'small')}</g>`;
const node=(x,y,name,sub='',style='')=>`<g class="${style}"><circle cx="${x}" cy="${y}" r="44" class="node"/>${dot(x,y,8)}${text(x,y+72,name)}${sub?text(x,y+96,sub,'small'):''}</g>`;
const check=(x,y)=>`<g transform="translate(${x} ${y})"><circle r="16" class="green-fill"/><path d="m-7 0 5 5 10-11" fill="none" stroke="white" stroke-width="3"/></g>`;
const photoScenes={
  hero:{file:'hero',alt:'Cinematic 3D crimson ribbon connecting business, logistics and manufacturing around an intelligence core'},
  invoice:{file:'ap',alt:'Three floating glass documents: two validated and one unresolved, connected by a broken crimson link'},
  cost:{file:'inventory',alt:'An empty crystal inventory cube with a residual value sphere linked to a chain of containers'},
  warehouse:{file:'warehouse',alt:'A futuristic warehouse digital twin with a clearly highlighted empty shelf and scanning plane'},
  production:{file:'production',alt:'Robotic manufacturing cell with exploded material layers, a timing wheel and evidence threads'}
};
function cinematic(slide,lang){
  const scene=photoScenes[slide.visual],l=slide.labels[lang];
  const sparks=Array.from({length:9},(_,i)=>`<i class="scene-spark" style="--x:${12+(i*17)%77}%;--y:${15+(i*23)%67}%;--delay:${i*.63}s"></i>`).join('');
  let annotations='',caption='';
  if(slide.visual==='hero'){
    annotations=`<div class="core-orbit"><i></i><i></i></div><div class="hero-data-trail"></div>`;
    caption=`<div class="cinema-caption hero-caption"><span>Dynamics 365</span><i>+</i><span>Copilot</span></div>`;
  }else if(slide.visual==='invoice'){
    annotations=`<div class="verification-sweep"></div><div class="link-pulse"></div><div class="document-labels"><span>${l[0]}</span><span>${l[1]}</span><span>${l[2]}</span></div>`;
    caption=`<div class="cinema-caption"><span class="caption-index">01</span><strong>${l[5]}</strong><span class="caption-end">${l[6]}</span></div>`;
  }else if(slide.visual==='cost'){
    annotations=`<div class="value-orbit"></div><div class="residual-label"><b>0</b><span>${l[0]}</span></div><div class="value-label"><b>฿ ?</b><span>${l[1]}</span></div>`;
    caption=`<div class="cinema-caption"><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span><i class="caption-trace"></i><span>${l[4]}</span></div>`;
  }else if(slide.visual==='warehouse'){
    annotations=`<div class="warehouse-sweep"></div><div class="stock-target"><i></i><i></i><i></i><i></i></div><div class="stock-callout"><span>SHORT PICK</span><b>${lang==='th'?'จุดที่ต้องตรวจสอบ':'Investigate this location'}</b></div>`;
    caption=`<div class="cinema-caption"><span>${l[3]}</span><i class="caption-trace"></i><span>${l[4]}</span><i class="caption-trace"></i><span>${l[5]}</span></div>`;
  }else{
    annotations=`<div class="production-radar"></div><svg class="evidence-threads" viewBox="0 0 780 520" aria-hidden="true"><path d="M180 410Q240 300 385 170Q520 80 645 110M390 420Q385 270 385 170M630 420Q580 280 645 110"/></svg>`;
    caption=`<div class="cinema-caption"><span>${l[2]}</span><i class="caption-trace"></i><span>${l[3]}</span><i class="caption-trace"></i><span>${l[4]}</span></div>`;
  }
  return `<div class="cinema-composition composition-${slide.visual}"><figure class="cinematic cinematic-${slide.visual}"><img class="cinema-image" src="assets/${scene.file}-3d-v2.png" alt="${scene.alt}" ${slide.visual==='hero'?'fetchpriority="high"':'loading="eager"'}><div class="cinema-atmosphere" aria-hidden="true">${sparks}</div><div class="cinema-overlay">${annotations}</div><figcaption class="scene-credit">CONCEPT VISUAL · AI + MOTION DESIGN</figcaption></figure>${caption}</div>`;
}
export function visual(slide,lang){
  const l=slide.labels[lang];
  if(photoScenes[slide.visual])return cinematic(slide,lang);
  switch(slide.visual){
    case 'boundary': return svg(`<path d="M390 52V447" class="divider"/>${text(190,64,l[0],'eyebrow-svg')}${text(583,64,l[1],'eyebrow-svg red-text')}<g class="stagger"><g>${check(62,153)}${text(98,160,l[2],'label','start')}</g><g>${check(62,252)}${text(98,259,l[3],'label','start')}</g><g>${check(62,351)}${text(98,358,l[4],'label','start')}</g></g><g class="stagger">${node(562,145,l[5])}${node(660,273,l[6])}${node(505,366,l[7])}</g>${line('M562 188L644 235M627 299L543 344','flow')}`, 'Existing Microsoft capabilities versus company-specific extension scope');
    case 'architecture': return svg(`${node(115,130,l[0])}${node(115,345,l[1])}${line('M160 130H250Q290 130 290 230H330','flow')}${line('M160 345H250Q290 345 290 249H330','flow')}<circle cx="390" cy="240" r="75" fill="url(#ribbon)" class="breathe"/>${text(390,235,'Copilot','white-hero')}${text(390,267,'Studio','white-text')}${text(390,356,l[5],'small')}${line('M466 240H590','flow')}${node(660,240,l[4])}${text(551,151,l[3],'small')}<path d="M70 453H710" class="wire"/>${text(390,496,l[6],'label')}`, 'Authorized D365 data and approved documents feed Copilot Studio; a business owner reviews cited proposals');
    case 'priorities': return svg(`<path d="M130 130H650M130 230H650M130 330H650M130 430H650" class="lane"/><g class="stagger"><g><circle cx="151" cy="130" r="29" class="accent"/>${text(151,140,'1','white-text')}${text(205,140,l[0],'lane-label','start')}${text(655,140,l[4],'small red-text','end')}</g><g><circle cx="151" cy="230" r="24" class="node"/>${text(151,238,'2')}${text(205,240,l[1],'lane-label','start')}${text(655,240,l[5],'small','end')}</g><g><circle cx="151" cy="330" r="24" class="node"/>${text(151,338,'3')}${text(205,340,l[2],'lane-label','start')}${text(655,340,l[5],'small','end')}</g><g><circle cx="151" cy="430" r="24" class="node"/>${text(151,438,'4')}${text(205,440,l[3],'lane-label','start')}${text(655,440,l[6],'small','end')}</g></g>${text(390,501,l[7],'small')}`, 'Recommended pilot sequence: Accounts Payable first, followed by inventory, warehouse and production');
    case 'pilot': return svg(`<path d="M120 175H660" class="wire"/>${line('M120 175H660','flow')}<g class="stagger">${[0,1,2].map((i)=>`<g><circle cx="${120+i*270}" cy="175" r="47" class="${i===0?'accent':'node'}"/>${text(120+i*270,185,l[i],i===0?'white-hero':'hero-word')}${text(120+i*270,265,l[3+i])}</g>`).join('')}</g><path d="M80 338H700" class="divider"/>${text(136,412,'◷','metric-icon')}${text(390,412,'✓','metric-icon')}${text(640,412,'฿','metric-icon')}${text(136,464,l[6])}${text(390,464,l[7])}${text(640,464,l[8])}`, 'Illustrative six-week pilot: benchmark, build read-only, evaluate time, evidence accuracy and cost');
    case 'closing': return `<div class="closing-art"><div class="closing-halo"></div><img src="assets/closing-original.png" alt="User-supplied 3D red infinity ribbon connecting Dynamics 365 and Copilot" class="closing-image"><div class="closing-orbit"></div></div>`;
    default:return '';
  }
}
