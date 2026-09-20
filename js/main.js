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
        price.textContent = (product.featuredPricePrefix || '') + product.price + ' NIS';
        copy.appendChild(price);
      }
      var details = document.createElement('details');
      details.className = 'hardware-details';
      var summary = document.createElement('summary');
      summary.className = 'hardware-details__summary';
      summary.innerHTML = '<span>عرض المواصفات</span><svg class="hardware-details__icon" aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>';
      var desc = document.createElement('p');
      desc.className = 'hardware-details__text';
      desc.textContent = product.description;
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
})();
