/* Namaa premium website interactions: light, accessible and dependency-free. */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var header = document.querySelector('.site-header');
  function updateHeader() {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 10);
  }
  document.addEventListener('scroll', updateHeader, { passive: true });
  updateHeader();

  var hamburger = document.querySelector('.hamburger');
  var mobilePanel = document.getElementById('mobile-panel');
  function closeMenu(restoreFocus) {
    if (!hamburger || !mobilePanel) return;
    hamburger.setAttribute('aria-expanded', 'false');
    hamburger.setAttribute('aria-label', 'فتح القائمة');
    mobilePanel.hidden = true;
    document.body.classList.remove('menu-open');
    if (restoreFocus) hamburger.focus();
  }
  if (hamburger && mobilePanel) {
    hamburger.addEventListener('click', function () {
      var open = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', String(!open));
      hamburger.setAttribute('aria-label', open ? 'فتح القائمة' : 'إغلاق القائمة');
      mobilePanel.hidden = open;
      document.body.classList.toggle('menu-open', !open);
    });
    mobilePanel.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { closeMenu(false); });
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !mobilePanel.hidden) closeMenu(true);
    });
    document.addEventListener('click', function (event) {
      if (!mobilePanel.hidden && header && !header.contains(event.target)) closeMenu(false);
    });
    window.matchMedia('(min-width: 1100px)').addEventListener('change', function (event) {
      if (event.matches) closeMenu(false);
    });
  }

  /* The hero video plays the widescreen desktop product tour across all devices. */
  var heroMedia = document.querySelector('[data-hero-media]');
  var heroVideo = heroMedia ? heroMedia.querySelector('video') : null;
  if (heroVideo) {
    function usePoster() { heroMedia.classList.add('is-fallback'); }
    function syncHeroVideo() {
      if (reduceMotion.matches) {
        heroVideo.pause();
        usePoster();
        return;
      }
      var playAttempt = heroVideo.play();
      if (playAttempt && typeof playAttempt.catch === 'function') playAttempt.catch(function () {});
    }
    heroVideo.addEventListener('error', usePoster);
    heroVideo.querySelectorAll('source').forEach(function (source) { source.addEventListener('error', usePoster); });
    syncHeroVideo();
  }

  /* One simple desktop selector controls one product screenshot. */
  var storySteps = Array.from(document.querySelectorAll('[data-story-index]'));
  var storyImages = Array.from(document.querySelectorAll('[data-story-image]'));
  function setStory(index) {
    storySteps.forEach(function (step, position) {
      step.classList.toggle('is-active', position === index);
      step.setAttribute('aria-pressed', String(position === index));
    });
    storyImages.forEach(function (image, position) { image.classList.toggle('is-active', position === index); });
  }
  if (storySteps.length && storyImages.length === storySteps.length) {
    storySteps.forEach(function (step, index) {
      step.addEventListener('click', function () { setStory(index); });
    });
  }

  /* Hardware: show 4 products initially with expand/collapse toggle. */
  function trustedProductUrl(value) {
    try {
      var url = new URL(value);
      return url.protocol === 'https:' && url.hostname === 'logix-mobile.com' && !url.username && !url.password ? url.href : '';
    } catch (_) { return ''; }
  }
  var rail = document.getElementById('hardware-products');
  var hardware = (window.HARDWARE_PRODUCTS || []).filter(function (product) {
    return product.approved === true;
  });
  var INITIAL_VISIBLE = 4;
  if (rail && hardware.length) {
    /* Build all cards */
    hardware.forEach(function (product, index) {
      var article = document.createElement('article');
      article.className = 'hardware-card';
      if (index >= INITIAL_VISIBLE) {
        article.classList.add('hardware-card--hidden');
        article.setAttribute('aria-hidden', 'true');
      }
      var imageWrap = document.createElement('div');
      imageWrap.className = 'hardware-card__img-wrap';
      var image = document.createElement('img');
      image.src = product.sourceImageUrl || product.image;
      image.width = product.width;
      image.height = product.height;
      image.alt = product.name;
      image.loading = index < INITIAL_VISIBLE ? 'eager' : 'lazy';
      image.decoding = 'async';
      imageWrap.appendChild(image);
      var copy = document.createElement('div');
      copy.className = 'hardware-card__copy';
      var title = document.createElement('h3');
      title.textContent = product.name;
      copy.appendChild(title);
      if (product.approvedPrice === true && typeof product.price === 'number') {
        var price = document.createElement('p');
        price.className = 'hardware-price';
        price.textContent = (product.featuredPricePrefix || '') + product.price + ' شيكل';
        copy.appendChild(price);
      }
      var details = document.createElement('details');
      details.className = 'hardware-details';
      var summary = document.createElement('summary');
      summary.className = 'hardware-details__summary';
      summary.innerHTML = '<span>عرض المواصفات</span><svg class="hardware-details__icon" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>';
      var desc = document.createElement('p');
      desc.className = 'hardware-details__text';
      desc.textContent = product.details || product.description;
      details.append(summary, desc);
      details.addEventListener('toggle', function () {
        var span = summary.querySelector('span');
        if (span) {
          span.textContent = details.open ? 'إخفاء المواصفات' : 'عرض المواصفات';
        }
      });
      copy.appendChild(details);
      article.append(imageWrap, copy);
      rail.appendChild(article);
    });

    /* Inject expand/collapse button only when there are hidden cards */
    if (hardware.length > INITIAL_VISIBLE) {
      var remaining = hardware.length - INITIAL_VISIBLE;
      var expandWrap = document.createElement('div');
      expandWrap.className = 'hardware-expand';
      var expandBtn = document.createElement('button');
      expandBtn.type = 'button';
      expandBtn.className = 'btn btn-secondary hardware-expand__btn';
      expandBtn.setAttribute('aria-expanded', 'false');
      expandBtn.setAttribute('aria-controls', 'hardware-products');
      expandBtn.textContent = 'عرض ' + remaining + ' منتج إضافي';
      var expanded = false;
      expandBtn.addEventListener('click', function () {
        expanded = !expanded;
        rail.querySelectorAll('.hardware-card--hidden').forEach(function (card) {
          card.classList.toggle('hardware-card--visible', expanded);
          card.setAttribute('aria-hidden', String(!expanded));
        });
        expandBtn.setAttribute('aria-expanded', String(expanded));
        expandBtn.textContent = expanded
          ? 'عرض أقل'
          : 'عرض ' + remaining + ' منتج إضافي';
        if (!expanded) {
          rail.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      });
      expandWrap.appendChild(expandBtn);
      rail.after(expandWrap);
    }
  }

  /* Tutorials are injected only after approved real links are supplied. */
  var tutorials = (window.NAMAA_TUTORIALS || []).filter(function (tutorial) {
    try {
      var url = new URL(tutorial.url);
      return tutorial.title && url.protocol === 'https:' && !url.username && !url.password;
    } catch (_) { return false; }
  });
  var template = document.getElementById('tutorials-template');
  var faq = document.getElementById('faq');
  if (tutorials.length && template && faq) {
    var section = template.content.firstElementChild.cloneNode(true);
    tutorials.forEach(function (tutorial) {
      var card = document.createElement('article');
      card.className = 'tutorial-card';
      var title = document.createElement('h3');
      title.textContent = tutorial.title;
      var description = document.createElement('p');
      description.textContent = tutorial.description || '';
      var watch = document.createElement('a');
      watch.href = tutorial.url;
      watch.className = 'btn btn-secondary';
      watch.target = '_blank';
      watch.rel = 'noopener noreferrer';
      watch.textContent = 'شاهد الشرح';
      card.append(title, description, watch);
      section.querySelector('.tutorials-grid').appendChild(card);
    });
    faq.before(section);
  }

  var dialog = document.getElementById('screenshot-dialog');
  var dialogImage = document.getElementById('screenshot-dialog-image');
  var dialogTitle = document.getElementById('screenshot-dialog-title');
  var originalLink = document.getElementById('screenshot-original-link');
  var dialogOpener = null;
  if (dialog && dialogImage && typeof dialog.showModal === 'function') {
    document.querySelectorAll('[data-zoom]').forEach(function (button) {
      button.addEventListener('click', function () {
        var source = button.dataset.zoom;
        var image = button.querySelector('img');
        if (!source) return;
        dialogOpener = button;
        dialogImage.src = source;
        dialogImage.alt = image ? image.alt : button.dataset.title;
        dialogTitle.textContent = button.dataset.title || 'شاشة نماء';
        originalLink.href = source;
        document.body.classList.add('has-dialog');
        dialog.showModal();
      });
    });
    dialog.querySelector('.dialog-close').addEventListener('click', function () { dialog.close(); });
    dialog.addEventListener('click', function (event) {
      if (event.target !== dialog) return;
      var box = dialog.getBoundingClientRect();
      if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
    });
    dialog.addEventListener('close', function () {
      document.body.classList.remove('has-dialog');
      dialogImage.removeAttribute('src');
      if (dialogOpener) dialogOpener.focus({ preventScroll: true });
    });
  }

  var faqButtons = document.querySelectorAll('.faq-item__q');
  faqButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      var open = button.getAttribute('aria-expanded') !== 'true';
      faqButtons.forEach(function (other) {
        var shouldOpen = other === button && open;
        other.setAttribute('aria-expanded', String(shouldOpen));
        var answer = document.getElementById(other.getAttribute('aria-controls'));
        if (answer) answer.hidden = !shouldOpen;
      });
    });
  });

  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      var href = link.getAttribute('href');
      if (!href || href === '#') return;
      var target = document.getElementById(href.slice(1));
      if (!target) return;
      event.preventDefault();
      closeMenu(false);
      var offset = header ? header.getBoundingClientRect().height : 0;
      var top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top: Math.max(0, top), behavior: reduceMotion.matches ? 'auto' : 'smooth' });
      if (window.location.hash !== href) window.history.pushState(null, '', href);
    });
  });

  var year = document.getElementById('current-year');
  if (year) year.textContent = new Date().getFullYear();

  /* Sync spots badge from data-spots-remaining attribute — edit only the HTML attribute. */
  var launchCard = document.querySelector('[data-spots-remaining]');
  if (launchCard) {
    var spotsNum = document.getElementById('spots-num');
    if (spotsNum) spotsNum.textContent = launchCard.dataset.spotsRemaining;
  }

  /* The year-end offer uses one public deadline for everyone. */
  var countdown = document.querySelector('[data-offer-deadline]');
  if (countdown) {
    var deadline = new Date(countdown.dataset.offerDeadline).getTime();
    var timer;
    function updateCountdown() {
      var remaining = deadline - Date.now();
      if (remaining <= 0) {
        countdown.classList.add('is-ended');
        countdown.textContent = 'انتهى عرض آخر السنة';
        if (timer) window.clearInterval(timer);
        return;
      }
      var units = {
        days: Math.floor(remaining / 86400000),
        hours: Math.floor((remaining % 86400000) / 3600000),
        minutes: Math.floor((remaining % 3600000) / 60000),
        seconds: Math.floor((remaining % 60000) / 1000)
      };
      Object.keys(units).forEach(function (unit) {
        var node = countdown.querySelector('[data-' + unit + ']');
        if (node) node.textContent = String(units[unit]).padStart(2, '0');
      });
      countdown.setAttribute('aria-label', 'متبقي ' + units.days + ' يوم و' + units.hours + ' ساعة على نهاية العرض');
    }
    updateCountdown();
    timer = window.setInterval(updateCountdown, 1000);
  }

  /* Interactive Cursor Spotlight Effects (Hardware-accelerated, disabled on touch/reduced-motion) */
  if (!reduceMotion.matches && window.matchMedia('(hover: hover)').matches) {
    /* 1. Hero ambient spotlight following cursor */
    var hero = document.querySelector('.hero');
    if (hero) {
      var heroTicking = false;
      hero.addEventListener('pointermove', function (e) {
        if (!heroTicking) {
          window.requestAnimationFrame(function () {
            var rect = hero.getBoundingClientRect();
            var x = Math.round(e.clientX - rect.left);
            var y = Math.round(e.clientY - rect.top);
            hero.style.setProperty('--hero-mouse-x', x + 'px');
            hero.style.setProperty('--hero-mouse-y', y + 'px');
            heroTicking = false;
          });
          heroTicking = true;
        }
      });
      hero.addEventListener('pointerleave', function () {
        hero.style.setProperty('--hero-mouse-x', '50%');
        hero.style.setProperty('--hero-mouse-y', '35%');
      });
    }

    /* 2. Why Namaa feature cards cursor spotlight */
    var whyCards = document.querySelectorAll('.why-card');
    whyCards.forEach(function (card) {
      card.addEventListener('pointermove', function (e) {
        var rect = card.getBoundingClientRect();
        var x = Math.round(e.clientX - rect.left);
        var y = Math.round(e.clientY - rect.top);
        card.style.setProperty('--mouse-x', x + 'px');
        card.style.setProperty('--mouse-y', y + 'px');
      });
    });
  }

  /* 3. Lightweight Interactive Gold Coins Canvas (<3.5KB, 0 dependencies, auto-paused offscreen) */
  (function () {
    var canvas = document.getElementById('hero-coins-canvas');
    var heroSection = document.querySelector('.hero');
    if (!canvas || !heroSection || reduceMotion.matches) return;

    var ctx = canvas.getContext('2d');
    if (!ctx) return;

    var width = 0;
    var height = 0;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var coins = [];
    var sparks = [];
    var isRunning = false;
    var animId = null;
    var mouse = { x: -9999, y: -9999, active: false };

    function resize() {
      var rect = heroSection.getBoundingClientRect();
      width = rect.width;
      height = rect.height;
      canvas.width = Math.round(width * dpr);
      canvas.height = Math.round(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    var isMobile = window.innerWidth < 768;
    var COIN_COUNT = isMobile ? 8 : 18;

    function getRandomX() {
      if (isMobile) {
        // On mobile, keep the central text column crystal-clear by placing 88% on outer flanks
        if (Math.random() < 0.88) {
          return Math.random() < 0.5 
            ? Math.random() * (width * 0.22) 
            : width * 0.78 + Math.random() * (width * 0.22);
        }
      }
      return Math.random() * (width || 800);
    }

    function createCoin(customY) {
      var depth = 0.45 + Math.random() * 0.55;
      var radius = (isMobile ? 12 + Math.random() * 8 : 17 + Math.random() * 13) * depth;
      var x = getRandomX();
      var isCenterMobile = isMobile && (x > width * 0.25 && x < width * 0.75);
      var baseOpacity = isCenterMobile ? 0.22 : (isMobile ? 0.38 + depth * 0.35 : 0.45 + depth * 0.5);

      return {
        x: x,
        y: customY !== undefined ? customY : (height ? height + Math.random() * 40 : 600),
        radius: radius,
        depth: depth,
        baseVy: -(0.55 + Math.random() * 0.75) * depth,
        vy: -(0.55 + Math.random() * 0.75) * depth,
        vx: (Math.random() - 0.5) * 0.25,
        swayAmp: 0.35 + Math.random() * 0.65,
        swaySpeed: 0.015 + Math.random() * 0.02,
        swayOffset: Math.random() * Math.PI * 2,
        flipAngle: Math.random() * Math.PI * 2,
        flipSpeed: (0.018 + Math.random() * 0.028) * (Math.random() < 0.5 ? 1 : -1),
        tilt: (Math.random() - 0.5) * 0.35,
        tiltSpeed: (Math.random() - 0.5) * 0.003,
        opacity: baseOpacity
      };
    }

    function initCoins() {
      coins = [];
      for (var i = 0; i < COIN_COUNT; i++) {
        coins.push(createCoin(Math.random() * (height || 700)));
      }
    }

    function spawnBurst(originX, originY, count) {
      var burstCount = count || 8;
      for (var i = 0; i < burstCount; i++) {
        var angle = (Math.PI * 2 * i) / burstCount + (Math.random() - 0.5);
        var speed = 1.5 + Math.random() * 3.5;
        sparks.push({
          x: originX,
          y: originY,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 1,
          size: 2 + Math.random() * 3,
          life: 1.0,
          decay: 0.02 + Math.random() * 0.025,
          color: Math.random() < 0.5 ? '#FCD34D' : '#F59E0B'
        });
      }
      if (coins.length < COIN_COUNT + 5) {
        var mini = createCoin(originY);
        mini.x = originX;
        mini.vx = (Math.random() - 0.5) * 4;
        mini.vy = -(2 + Math.random() * 2);
        mini.flipSpeed = 0.07 * (Math.random() < 0.5 ? 1 : -1);
        coins.push(mini);
      }
    }

    function drawCoin(c) {
      ctx.save();
      ctx.translate(c.x, c.y);
      ctx.rotate(c.tilt);

      var flipCos = Math.cos(c.flipAngle);
      var scaleX = flipCos;
      var absScaleX = Math.abs(flipCos);
      var isFront = flipCos >= 0;

      ctx.globalAlpha = c.opacity;

      // 3D Bimetallic Coin Edge thickness when rotating
      var edgeWidth = c.radius * 0.16 * Math.sin(c.flipAngle);
      if (Math.abs(edgeWidth) > 0.6 && absScaleX < 0.96) {
        ctx.save();
        ctx.scale(scaleX, 1);
        ctx.beginPath();
        ctx.ellipse(edgeWidth * 0.85, 0, c.radius, c.radius, 0, 0, Math.PI * 2);
        ctx.fillStyle = '#854D0E'; // Bronze outer rim edge
        ctx.fill();

        // Silver core edge slice
        ctx.beginPath();
        ctx.ellipse(edgeWidth * 0.85, 0, c.radius * 0.64, c.radius * 0.64, 0, 0, Math.PI * 2);
        ctx.fillStyle = '#64748B'; // Cool steel silver edge
        ctx.fill();
        ctx.restore();
      }

      ctx.scale(scaleX, 1);

      // --- 1. OUTER GOLDEN RING (Nickel-Brass) ---
      var goldGrad = ctx.createLinearGradient(-c.radius, -c.radius, c.radius, c.radius);
      goldGrad.addColorStop(0, '#FEF08A');
      goldGrad.addColorStop(0.25, '#F59E0B');
      goldGrad.addColorStop(0.7, '#D97706');
      goldGrad.addColorStop(1, '#854D0E');

      ctx.beginPath();
      ctx.arc(0, 0, c.radius, 0, Math.PI * 2);
      ctx.fillStyle = goldGrad;
      ctx.fill();

      // Outer rim border highlight
      ctx.lineWidth = Math.max(1, c.radius * 0.06);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.45)';
      ctx.stroke();

      // Concentric reeding groove on golden ring
      ctx.lineWidth = Math.max(0.5, c.radius * 0.025);
      ctx.strokeStyle = 'rgba(180, 83, 9, 0.35)';
      ctx.beginPath();
      ctx.arc(0, 0, c.radius * 0.84, 0, Math.PI * 2);
      ctx.stroke();

      // --- 2. INNER SILVER CORE (Cupronickel) ---
      var innerR = c.radius * 0.64;

      // Recessed joint line between gold ring and silver core
      ctx.beginPath();
      ctx.arc(0, 0, innerR + 0.5, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(146, 64, 14, 0.55)';
      ctx.lineWidth = Math.max(0.75, c.radius * 0.035);
      ctx.stroke();

      // Silver core gradient
      var silverGrad = ctx.createLinearGradient(-innerR, -innerR, innerR, innerR);
      silverGrad.addColorStop(0, '#FFFFFF');
      silverGrad.addColorStop(0.22, '#F1F5F9');
      silverGrad.addColorStop(0.55, '#CBD5E1');
      silverGrad.addColorStop(1, '#94A3B8');

      ctx.beginPath();
      ctx.arc(0, 0, innerR, 0, Math.PI * 2);
      ctx.fillStyle = silverGrad;
      ctx.fill();

      // Inner silver rim bevel highlight
      ctx.lineWidth = Math.max(0.5, c.radius * 0.03);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.85)';
      ctx.stroke();

      // --- 3. DUAL-SIDED 3D FACE EMBOSSING ---
      if (absScaleX > 0.25 && c.radius > 8) {
        ctx.save();
        if (isFront) {
          // Front (Obverse): Bold 10 Numeral + شواكل
          ctx.fillStyle = 'rgba(71, 85, 105, 0.85)';
          ctx.font = '900 ' + Math.round(innerR * 0.95) + 'px -apple-system, BlinkMacSystemFont, sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText('10', 0.5, 1);

          ctx.fillStyle = '#334155';
          ctx.fillText('10', 0, 0.2);

          ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
          ctx.fillText('10', -0.5, -0.4);

          if (c.radius > 15 && absScaleX > 0.45) {
            ctx.fillStyle = '#64748B';
            ctx.font = 'bold ' + Math.round(innerR * 0.22) + 'px sans-serif';
            ctx.fillText('شواكل', 0, innerR * 0.55);
          }
        } else {
          // Back (Reverse): Iconic Date Palm Tree Motif
          ctx.strokeStyle = '#475569';
          ctx.fillStyle = '#475569';
          ctx.lineWidth = Math.max(1, c.radius * 0.05);
          ctx.lineCap = 'round';

          // Trunk
          ctx.beginPath();
          ctx.moveTo(0, innerR * 0.55);
          ctx.lineTo(0, -innerR * 0.15);
          ctx.stroke();

          // Palm fronds
          ctx.lineWidth = Math.max(0.8, c.radius * 0.04);
          var frondR = innerR * 0.45;
          for (var a = -0.7; a <= 0.75; a += 0.35) {
            ctx.beginPath();
            ctx.moveTo(0, -innerR * 0.15);
            ctx.quadraticCurveTo(Math.sin(a) * frondR * 0.6, -innerR * 0.15 - Math.cos(a) * frondR * 0.6, Math.sin(a) * frondR, -innerR * 0.15 - Math.cos(a) * frondR * 0.35);
            ctx.stroke();
          }

          // Two date baskets
          ctx.beginPath();
          ctx.arc(-innerR * 0.2, innerR * 0.05, c.radius * 0.06, 0, Math.PI * 2);
          ctx.arc(innerR * 0.2, innerR * 0.05, c.radius * 0.06, 0, Math.PI * 2);
          ctx.fill();

          // Highlight ridge
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
          ctx.lineWidth = Math.max(0.5, c.radius * 0.025);
          ctx.beginPath();
          ctx.moveTo(-0.5, innerR * 0.55);
          ctx.lineTo(-0.5, -innerR * 0.15);
          ctx.stroke();
        }
        ctx.restore();
      }

      // --- 4. SWEEPING METALLIC SHEEN ---
      var sheenX = Math.sin(c.flipAngle * 2) * c.radius;
      var sheenGrad = ctx.createLinearGradient(sheenX - c.radius * 0.45, -c.radius, sheenX + c.radius * 0.45, c.radius);
      sheenGrad.addColorStop(0, 'rgba(255, 255, 255, 0)');
      sheenGrad.addColorStop(0.5, 'rgba(255, 255, 255, 0.35)');
      sheenGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
      ctx.beginPath();
      ctx.arc(0, 0, c.radius, 0, Math.PI * 2);
      ctx.fillStyle = sheenGrad;
      ctx.fill();

      ctx.restore();
    }

    function update() {
      ctx.clearRect(0, 0, width, height);

      // Update and draw sparks
      for (var s = sparks.length - 1; s >= 0; s--) {
        var sp = sparks[s];
        sp.x += sp.vx;
        sp.y += sp.vy;
        sp.vy += 0.08;
        sp.life -= sp.decay;
        if (sp.life <= 0) {
          sparks.splice(s, 1);
          continue;
        }
        ctx.save();
        ctx.globalAlpha = sp.life;
        ctx.fillStyle = sp.color;
        ctx.beginPath();
        ctx.arc(sp.x, sp.y, sp.size * sp.life, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }

      // Update and draw coins
      for (var i = coins.length - 1; i >= 0; i--) {
        var c = coins[i];

        c.swayOffset += c.swaySpeed;
        c.flipAngle += c.flipSpeed;
        c.tilt += c.tiltSpeed;

        c.x += c.vx + Math.sin(c.swayOffset) * c.swayAmp;
        c.y += c.vy;

        // Interaction with mouse/touch
        if (mouse.active) {
          var dx = c.x - mouse.x;
          var dy = c.y - mouse.y;
          var dist = Math.sqrt(dx * dx + dy * dy);
          var repelDist = 135;
          if (dist < repelDist && dist > 0.1) {
            var force = (repelDist - dist) / repelDist;
            c.vx += (dx / dist) * force * 1.5;
            c.vy += (dy / dist) * force * 1.5;
            c.flipSpeed += force * 0.02 * (Math.random() < 0.5 ? 1 : -1);
          }
        }

        c.vx *= 0.94;
        c.vy = c.vy * 0.94 + c.baseVy * 0.06;

        // Reset if passed top
        if (c.y < -c.radius * 2) {
          if (coins.length > COIN_COUNT) {
            coins.splice(i, 1);
            continue;
          }
          c.y = height + c.radius + Math.random() * 25;
          c.x = getRandomX();
          c.vx = (Math.random() - 0.5) * 0.4;
          c.vy = c.baseVy;
        }

        if (c.x < -c.radius * 2) c.x = width + c.radius;
        else if (c.x > width + c.radius * 2) c.x = -c.radius;

        drawCoin(c);
      }

      if (isRunning) {
        animId = window.requestAnimationFrame(update);
      }
    }

    function start() {
      if (!isRunning) {
        isRunning = true;
        animId = window.requestAnimationFrame(update);
      }
    }

    function stop() {
      isRunning = false;
      if (animId) {
        window.cancelAnimationFrame(animId);
        animId = null;
      }
    }

    function onPointerMove(e) {
      var rect = heroSection.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
      mouse.active = true;
    }

    function onPointerLeave() {
      mouse.active = false;
      mouse.x = -9999;
      mouse.y = -9999;
    }

    function onPointerDown(e) {
      var rect = heroSection.getBoundingClientRect();
      var px = e.clientX - rect.left;
      var py = e.clientY - rect.top;
      spawnBurst(px, py, 10);
    }

    heroSection.addEventListener('pointermove', onPointerMove, { passive: true });
    heroSection.addEventListener('pointerleave', onPointerLeave, { passive: true });
    heroSection.addEventListener('pointerdown', onPointerDown, { passive: true });

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            start();
          } else {
            stop();
          }
        });
      }, { threshold: 0.05 });
      observer.observe(heroSection);
    } else {
      start();
    }

    var resizeTimeout;
    window.addEventListener('resize', function () {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(function () {
        resize();
      }, 150);
    }, { passive: true });

    resize();
    initCoins();
  })();
})();
