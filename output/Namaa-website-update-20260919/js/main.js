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

  /* Hardware stays secondary: three relevant products maximum. */
  function trustedProductUrl(value) {
    try {
      var url = new URL(value);
      return url.protocol === 'https:' && url.hostname === 'logix-mobile.com' && !url.username && !url.password ? url.href : '';
    } catch (_) { return ''; }
  }
  var rail = document.getElementById('hardware-products');
  var selectedIds = ['wired-scanner', 'wireless-scanner', 'xprinter-n160ii'];
  var hardware = (window.HARDWARE_PRODUCTS || []).filter(function (product) {
    return product.approved === true && selectedIds.indexOf(product.id) !== -1 && trustedProductUrl(product.sourceUrl) && /^assets\/hardware\/[a-z0-9-]+\.webp$/.test(product.image);
  }).sort(function (a, b) { return selectedIds.indexOf(a.id) - selectedIds.indexOf(b.id); });
  if (rail) {
    hardware.slice(0, 3).forEach(function (product) {
      var article = document.createElement('article');
      article.className = 'hardware-card';
      var image = document.createElement('img');
      image.src = product.image;
      image.width = product.width;
      image.height = product.height;
      image.alt = product.name + ' — صورة المنتج من Logix Mobile';
      image.loading = 'eager';
      image.decoding = 'async';
      var copy = document.createElement('div');
      copy.className = 'hardware-card__copy';
      var title = document.createElement('h3');
      title.textContent = product.name;
      var description = document.createElement('p');
      description.textContent = product.description;
      var source = document.createElement('a');
      source.className = 'hardware-product-link';
      source.href = trustedProductUrl(product.sourceUrl);
      source.target = '_blank';
      source.rel = 'noopener noreferrer';
      source.textContent = 'تفاصيل المنتج';
      source.setAttribute('aria-label', 'تفاصيل ' + product.name + ' لدى Logix Mobile — يفتح في نافذة جديدة');
      copy.append(title, description);
      if (product.approvedPrice === true && typeof product.price === 'number') {
        var price = document.createElement('p');
        price.className = 'hardware-price';
        price.textContent = product.price + ' ' + product.currency;
        copy.appendChild(price);
      }
      copy.appendChild(source);
      article.append(image, copy);
      rail.appendChild(article);
    });
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
})();
