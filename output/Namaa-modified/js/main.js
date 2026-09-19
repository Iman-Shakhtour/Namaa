/* Namaa: retained header/menu/FAQ/anchors/year, with accessible screenshot tabs. */
(function () {
  'use strict';
  var motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
  var header = document.querySelector('.site-header');
  function onScrollHeader() {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 12);
  }
  document.addEventListener('scroll', onScrollHeader, { passive: true });
  onScrollHeader();

  /* Existing menu, with native hidden state and keyboard dismissal. */
  var hamburger = document.querySelector('.hamburger');
  var mobilePanel = document.querySelector('.mobile-panel');
  function closeMenu(restoreFocus) {
    if (!hamburger || !mobilePanel) return;
    hamburger.setAttribute('aria-expanded', 'false');
    hamburger.setAttribute('aria-label', 'فتح القائمة');
    mobilePanel.hidden = true;
    if (restoreFocus) hamburger.focus();
  }
  if (hamburger && mobilePanel) {
    hamburger.addEventListener('click', function () {
      var isOpen = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', String(!isOpen));
      hamburger.setAttribute('aria-label', isOpen ? 'فتح القائمة' : 'إغلاق القائمة');
      mobilePanel.hidden = isOpen;
    });
    mobilePanel.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { closeMenu(false); });
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && !mobilePanel.hidden) closeMenu(true);
    });
    document.addEventListener('click', function (event) {
      if (!mobilePanel.hidden && header && !header.contains(event.target)) closeMenu(false);
    });
    header.addEventListener('focusout', function (event) {
      if (!mobilePanel.hidden && event.relatedTarget && !header.contains(event.relatedTarget)) closeMenu(false);
    });
    window.matchMedia('(min-width: 1100px)').addEventListener('change', function (event) {
      if (event.matches) closeMenu(false);
    });
  }

  /* Invalid/empty contact values never become outbound links. */
  var config = window.SITE_CONFIG || {};
  var number = String(config.whatsappNumber || '').trim().replace(/[\s()+-]/g, '');
  var hasWhatsApp = /^[1-9]\d{7,14}$/.test(number);
  var whatsappUrl = hasWhatsApp ? 'https://wa.me/' + number : '';
  document.querySelectorAll('[data-contact-cta]').forEach(function (link) {
    if (!hasWhatsApp) return;
    link.href = whatsappUrl + '?text=' + encodeURIComponent('مرحبًا، أريد أعرف أكثر عن نماء.');
    link.textContent = link.dataset.contactLabel || 'تواصل معنا';
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
  });
  document.querySelectorAll('[data-whatsapp]').forEach(function (link) {
    if (!hasWhatsApp) return;
    link.href = whatsappUrl;
    link.hidden = false;
  });
  function validSocialUrl(value, service) {
    try {
      var url = new URL(value);
      var allowedHosts = service === 'instagram'
        ? ['instagram.com', 'www.instagram.com']
        : ['facebook.com', 'www.facebook.com', 'm.facebook.com', 'fb.com', 'www.fb.com'];
      return url.protocol === 'https:' && !url.username && !url.password && allowedHosts.indexOf(url.hostname) !== -1 ? url.href : '';
    } catch (_) { return ''; }
  }
  document.querySelectorAll('[data-social]').forEach(function (link) {
    var service = link.dataset.social;
    var url = validSocialUrl(config[service + 'Url'] || '', service);
    if (url) { link.href = url; link.hidden = false; }
  });
  var socialContainer = document.querySelector('.footer__social');
  if (socialContainer) socialContainer.hidden = !socialContainer.querySelector('a:not([hidden])');

  /* Hardware text is maintained in a separate data file. */
  (window.HARDWARE_CATEGORIES || []).forEach(function (category) {
    var card = document.querySelector('[data-hardware="' + category.id + '"]');
    if (!card) return;
    card.querySelector('h3').textContent = category.title;
    card.querySelector('p').textContent = category.description;
    card.querySelector('use').setAttribute('href', '#icon-' + category.icon);
  });

  /* Tab keys follow visual RTL order; load one image at a time. */
  var tabList = document.querySelector('.showcase-tabs');
  var tabs = Array.from(document.querySelectorAll('.showcase-tabs [role="tab"]'));
  var panels = Array.from(document.querySelectorAll('.showcase-panel'));
  var deviceControls = document.querySelector('[data-mobile-controls]');
  var deviceButtons = document.querySelectorAll('[data-device]');
  var activeIndex = 0;
  var selectedDevice = 'desktop';
  function updateDevice() {
    var panel = panels[activeIndex];
    if (!panel) return;
    var supportsMobile = panel.dataset.mobile === 'true';
    var device = supportsMobile ? selectedDevice : 'desktop';
    if (deviceControls) deviceControls.hidden = !supportsMobile;
    deviceButtons.forEach(function (button) {
      button.setAttribute('aria-pressed', String(button.dataset.device === device));
    });
    panel.querySelectorAll('[data-device-image]').forEach(function (img) {
      img.hidden = img.dataset.deviceImage !== device;
      if (!img.hidden && !img.getAttribute('src')) img.src = img.dataset.src;
    });
  }
  function selectTab(index, focus) {
    activeIndex = index;
    tabs.forEach(function (tab, i) {
      tab.setAttribute('aria-selected', String(i === index));
      tab.tabIndex = i === index ? 0 : -1;
      panels[i].hidden = i !== index;
    });
    updateDevice();
    if (focus) tabs[index].focus();
  }
  if (tabList && tabs.length && panels.length === tabs.length) {
    tabList.hidden = false;
    tabs.forEach(function (tab, index) {
      tab.addEventListener('click', function () { selectTab(index, false); });
      tab.addEventListener('keydown', function (event) {
        var next = index;
        if (event.key === 'ArrowLeft' || event.key === 'ArrowDown') next = (index + 1) % tabs.length;
        else if (event.key === 'ArrowRight' || event.key === 'ArrowUp') next = (index - 1 + tabs.length) % tabs.length;
        else if (event.key === 'Home') next = 0;
        else if (event.key === 'End') next = tabs.length - 1;
        else return;
        event.preventDefault();
        selectTab(next, true);
      });
    });
    deviceButtons.forEach(function (button) {
      button.addEventListener('click', function () { selectedDevice = button.dataset.device; updateDevice(); });
    });
    selectTab(0, false);
  }

  /* Native responsive image dialog; keep the source aspect ratio. */
  var dialog = document.getElementById('screenshot-dialog');
  var dialogImage = document.getElementById('screenshot-dialog-image');
  var dialogTitle = document.getElementById('screenshot-dialog-title');
  var originalLink = document.getElementById('screenshot-original-link');
  var dialogOpener = null;
  if (dialog && dialogImage && typeof dialog.showModal === 'function') {
    document.querySelectorAll('[data-zoom], [data-panel-zoom]').forEach(function (button) {
      button.addEventListener('click', function () {
        var image = button.querySelector('img:not([hidden])');
        var source = button.dataset.zoom || (image && image.dataset.src);
        if (!source) return;
        dialogOpener = button;
        dialogImage.src = source;
        dialogImage.alt = image ? image.alt : button.dataset.title;
        if (image) { dialogImage.width = image.getAttribute('width'); dialogImage.height = image.getAttribute('height'); }
        dialogTitle.textContent = button.dataset.title || 'شاشة نماء';
        originalLink.href = source;
        document.body.classList.add('has-dialog');
        dialog.showModal();
      });
    });
    dialog.querySelector('.dialog-close').addEventListener('click', function () { dialog.close(); });
    dialog.addEventListener('keydown', function (event) {
      if (event.key !== 'Tab') return;
      var focusable = Array.from(dialog.querySelectorAll('button:not([disabled]), a[href]'));
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault(); last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault(); first.focus();
      }
    });
    dialog.addEventListener('click', function (event) {
      if (event.target === dialog) {
        var bounds = dialog.getBoundingClientRect();
        if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
      }
    });
    dialog.addEventListener('close', function () {
      document.body.classList.remove('has-dialog');
      dialogImage.removeAttribute('src');
      if (dialogOpener) dialogOpener.focus({ preventScroll: true });
    });
  }

  /* Retained FAQ behavior, correct button/answer state. */
  var faqButtons = document.querySelectorAll('.faq-item__q');
  faqButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      var shouldOpen = button.getAttribute('aria-expanded') !== 'true';
      faqButtons.forEach(function (other) {
        var open = other === button && shouldOpen;
        other.setAttribute('aria-expanded', String(open));
        var answer = document.getElementById(other.getAttribute('aria-controls'));
        if (answer) answer.hidden = !open;
      });
    });
  });

  /* Retained smooth anchors: real header height, hash, keyboard destination. */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      var href = link.getAttribute('href');
      if (!href || href === '#') return;
      var target = document.getElementById(href.slice(1));
      if (!target) return;
      event.preventDefault();
      closeMenu(false);
      if (link.closest('#hardware') && href === '#showcase') selectTab(1, false);
      var offset = header ? header.getBoundingClientRect().height : 0;
      var top = target.getBoundingClientRect().top + window.scrollY - offset - 16;
      if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
      window.scrollTo({ top: Math.max(0, top), behavior: motionPreference.matches ? 'auto' : 'smooth' });
      if (window.location.hash !== href) window.history.pushState(null, '', href);
    });
  });

  /* Retained current footer year. */
  var yearEl = document.getElementById('current-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
