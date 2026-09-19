(async function(){
  const mobile=new URLSearchParams(location.search).get('mode')==='mobile';
  const W=mobile?540:1280,H=mobile?720:560,fps=24,slideMs=1350,fadeMs=260;
  const sources=mobile?
    ['/assets/screenshots/namaa-dashboard-mobile.webp','/assets/screenshots/namaa-pos-mobile.webp','/assets/screenshots/namaa-items-mobile.webp','/assets/screenshots/namaa-profit-focus.webp','/assets/screenshots/namaa-rbac-users-public.webp']:
    ['/assets/screenshots/namaa-dashboard-desktop.webp','/assets/screenshots/namaa-pos-desktop.webp','/assets/screenshots/namaa-inventory-desktop.webp','/assets/screenshots/namaa-profit-report.webp','/assets/screenshots/namaa-rbac-users-public.webp'];
  const canvas=document.getElementById('c'),ctx=canvas.getContext('2d',{alpha:false}); canvas.width=W;canvas.height=H;
  const images=await Promise.all(sources.map(src=>new Promise((resolve,reject)=>{const im=new Image();im.onload=()=>resolve(im);im.onerror=reject;im.src=src;})));
  function draw(im,alpha,t,index){
    ctx.save();ctx.globalAlpha=alpha;
    const base=Math.max(W/im.width,H/im.height),scale=base*(1+0.025*t),dw=im.width*scale,dh=im.height*scale;
    const travel=Math.max(0,dw-W),x=-(travel*(index%2?t:1-t));
    const y=Math.min(0,(H-dh)/2);ctx.drawImage(im,x,y,dw,dh);ctx.restore();
  }
  function frame(elapsed){
    ctx.fillStyle='#07182F';ctx.fillRect(0,0,W,H);
    const total=slideMs*images.length,pos=(elapsed%total)/slideMs,index=Math.floor(pos)%images.length,local=pos-index,next=(index+1)%images.length;
    draw(images[index],1,local,index);
    if(local>(slideMs-fadeMs)/slideMs){const a=(local-(slideMs-fadeMs)/slideMs)/(fadeMs/slideMs);draw(images[next],Math.min(1,a),0,next);}
  }
  frame(0);
  const stream=canvas.captureStream(fps),mime=MediaRecorder.isTypeSupported('video/webm;codecs=vp9')?'video/webm;codecs=vp9':'video/webm';
  const recorder=new MediaRecorder(stream,{mimeType:mime,videoBitsPerSecond:mobile?620000:900000}),chunks=[];
  recorder.ondataavailable=e=>{if(e.data.size)chunks.push(e.data)};
  recorder.onstop=()=>{const blob=new Blob(chunks,{type:mime}),reader=new FileReader();reader.onload=()=>{window.videoBase64=reader.result.split(',')[1];window.videoBytes=blob.size;document.getElementById('status').textContent='done '+blob.size};reader.readAsDataURL(blob)};
  const duration=slideMs*images.length,start=performance.now();recorder.start(500);
  function tick(now){const elapsed=now-start;frame(elapsed);if(elapsed<duration)requestAnimationFrame(tick);else recorder.stop()}
  requestAnimationFrame(tick);
})().catch(error=>{window.videoError=String(error);document.getElementById('status').textContent=String(error)});
