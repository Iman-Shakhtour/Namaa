/* ==========================================================================
   نماء — Landing Page Scripts
   Vanilla JS. No external dependencies. Respects prefers-reduced-motion.
   ========================================================================== */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------- Header scroll state ---------------- */
  var header = document.querySelector('.site-header');
  function onScrollHeader() {
    if (!header) return;
    if (window.scrollY > 12) header.classList.add('is-scrolled');
    else header.classList.remove('is-scrolled');
  }
  document.addEventListener('scroll', onScrollHeader, { passive: true });
  onScrollHeader();

  /* ---------------- Mobile menu ---------------- */
  var hamburger = document.querySelector('.hamburger');
  var mobilePanel = document.querySelector('.mobile-panel');
  if (hamburger && mobilePanel) {
    hamburger.addEventListener('click', function () {
      var isOpen = hamburger.getAttribute('aria-expanded') === 'true';
      if (!isOpen && header) {
        mobilePanel.style.top = header.getBoundingClientRect().height + 'px';
      }
      hamburger.setAttribute('aria-expanded', String(!isOpen));
      mobilePanel.classList.toggle('is-open', !isOpen);
      document.body.style.overflow = !isOpen ? 'hidden' : '';
    });
    mobilePanel.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        hamburger.setAttribute('aria-expanded', 'false');
        mobilePanel.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---------------- Generic scroll reveal (IntersectionObserver) ---------------- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-fade, .reveal-scale');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.14, rootMargin: '0px 0px -8% 0px' }
    );
    revealEls.forEach(function (el, i) {
      var group = el.closest('.stagger');
      if (group) {
        var idx = Array.prototype.indexOf.call(group.children, el);
        el.style.setProperty('--reveal-delay', Math.min(idx, 6) * 0.09 + 's');
      }
      io.observe(el);
    });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---------------- Big statement word-by-word reveal ---------------- */
  var bigStatement = document.querySelector('.big-statement__title');
  if (bigStatement && !bigStatement.dataset.split) {
    var text = bigStatement.textContent.trim();
    var words = text.split(/\s+/);
    bigStatement.dataset.split = '1';
    bigStatement.innerHTML = words
      .map(function (w, i) {
        return '<span class="word" style="--i:' + i + '">' + w + '</span>';
      })
      .join(' ');
    if ('IntersectionObserver' in window) {
      var ioWords = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.querySelectorAll('.word').forEach(function (w) {
                w.classList.add('is-visible');
              });
              ioWords.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.4 }
      );
      ioWords.observe(bigStatement);
    } else {
      bigStatement.querySelectorAll('.word').forEach(function (w) { w.classList.add('is-visible'); });
    }
  }

  /* ---------------- Barcode sweep animation (once, on view) ---------------- */
  var barcodeVisual = document.querySelector('.barcode__visual');
  if (barcodeVisual && !reduceMotion && 'IntersectionObserver' in window) {
    var ioBarcode = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            barcodeVisual.classList.add('sweep-play');
            ioBarcode.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    ioBarcode.observe(barcodeVisual);
  }

  /* ---------------- Inventory sticky scroll story ---------------- */
  var invSteps = document.querySelectorAll('.inv-step');
  var invDots = document.querySelectorAll('.inv-story__progress i');
  var invStickyImg = document.querySelector('.inv-story__sticky img');
  if (invSteps.length && 'IntersectionObserver' in window) {
    var ioInv = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var idx = Array.prototype.indexOf.call(invSteps, entry.target);
          if (entry.isIntersecting) {
            invSteps.forEach(function (s) { s.classList.remove('is-active'); });
            entry.target.classList.add('is-active');
            invDots.forEach(function (d, di) { d.classList.toggle('is-active', di === idx); });
            if (invStickyImg && !reduceMotion) {
              invStickyImg.style.transform = 'scale(1.015)';
              setTimeout(function () { invStickyImg.style.transform = 'scale(1)'; }, 260);
            }
          }
        });
      },
      { threshold: 0, rootMargin: '-45% 0px -45% 0px' }
    );
    invSteps.forEach(function (s) { ioInv.observe(s); });
  }

  /* ---------------- FAQ accordion ---------------- */
  var faqButtons = document.querySelectorAll('.faq-item__q');
  faqButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.closest('.faq-item');
      var isOpen = item.getAttribute('aria-expanded') === 'true';
      document.querySelectorAll('.faq-item').forEach(function (el) {
        el.setAttribute('aria-expanded', 'false');
        var q = el.querySelector('.faq-item__q');
        if (q) q.setAttribute('aria-expanded', 'false');
      });
      if (!isOpen) {
        item.setAttribute('aria-expanded', 'true');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---------------- Smooth anchor scrolling with header offset ---------------- */
  var headerHeight = 84;
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var id = a.getAttribute('href');
      if (!id || id === '#') return;
      var target = document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
      window.scrollTo({ top: top, behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  });

  /* ---------------- Lead form -> WhatsApp handoff ---------------- */
  var leadForm = document.getElementById('lead-form');
  if (leadForm) {
    leadForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = leadForm.querySelector('#lf-name').value.trim();
      var phone = leadForm.querySelector('#lf-phone').value.trim();
      var typeSel = leadForm.querySelector('#lf-type');
      var type = typeSel.options[typeSel.selectedIndex] ? typeSel.options[typeSel.selectedIndex].text : '';
      var branches = leadForm.querySelector('#lf-branches').value.trim();

      var lines = [
        'مرحبًا، أريد أعرف أكثر عن نماء.',
        'الاسم: ' + (name || '-'),
        'رقم الهاتف: ' + (phone || '-'),
        'نوع النشاط: ' + (type || '-')
      ];
      if (branches) lines.push('عدد الفروع/المخازن: ' + branches);

      var msg = encodeURIComponent(lines.join('\n'));
      var waNumber = 'WHATSAPP_NUMBER';
      window.open('https://wa.me/' + waNumber + '?text=' + msg, '_blank', 'noopener');
    });
  }

  /* ---------------- Current year in footer ---------------- */
  var yearEl = document.getElementById('current-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------------- Card pointer spotlight (desktop, fine pointer only) ---------------- */
  var finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
  if (finePointer.matches && !reduceMotion) {
    document.querySelectorAll('.card').forEach(function (el) {
      el.addEventListener('pointermove', function (e) {
        var rect = el.getBoundingClientRect();
        el.style.setProperty('--spot-x', ((e.clientX - rect.left) / Math.max(1, rect.width) * 100).toFixed(1) + '%');
        el.style.setProperty('--spot-y', ((e.clientY - rect.top) / Math.max(1, rect.height) * 100).toFixed(1) + '%');
        el.classList.add('has-pointer');
      }, { passive: true });
      el.addEventListener('pointerleave', function () {
        el.classList.remove('has-pointer');
      }, { passive: true });
    });

    /* ---------------- Hero pointer parallax (desktop, fine pointer only) ---------------- */
    var heroVisual = document.querySelector('.hero__visual');
    if (heroVisual) {
      var heroFrame = null, tx = 0, ty = 0;
      var renderParallax = function () {
        heroVisual.style.setProperty('--hx', (tx * 8).toFixed(2) + 'px');
        heroVisual.style.setProperty('--hy', (ty * 6).toFixed(2) + 'px');
        heroFrame = null;
      };
      heroVisual.addEventListener('pointermove', function (e) {
        var rect = heroVisual.getBoundingClientRect();
        tx = ((e.clientX - rect.left) / Math.max(1, rect.width) - 0.5) * 2;
        ty = ((e.clientY - rect.top) / Math.max(1, rect.height) - 0.5) * 2;
        if (!heroFrame) heroFrame = requestAnimationFrame(renderParallax);
      }, { passive: true });
      heroVisual.addEventListener('pointerleave', function () {
        tx = 0; ty = 0;
        if (!heroFrame) heroFrame = requestAnimationFrame(renderParallax);
      }, { passive: true });
    }
  }
})();
