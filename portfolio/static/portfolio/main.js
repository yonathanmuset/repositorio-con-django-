(function () {
  var navbar = document.getElementById('navbar');
  var navLinks = document.getElementById('navLinks');
  var navToggle = document.getElementById('navToggle');

  function updateActiveSection() {
    var sections = document.querySelectorAll('main section[id]');
    var currentSection = '';

    sections.forEach(function (section) {
      if (section.getBoundingClientRect().top <= 140) {
        currentSection = section.id;
      }
    });

    document.querySelectorAll('.nav-links a[href^="#"]').forEach(function (link) {
      if (link.getAttribute('href') === '#' + currentSection) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  window.scrollToSection = function (id) {
    var section = document.getElementById(id);
    if (section) {
      section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else if (navbar) {
      window.location.assign(navbar.getAttribute('data-home-url') + '#' + encodeURIComponent(id));
    }
    window.closeMobileMenu();
  };

  window.scrollToTop = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  window.toggleMobileMenu = function () {
    if (!navLinks || !navToggle) return;
    var isOpen = navLinks.classList.toggle('mobile-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
    navToggle.setAttribute('aria-label', isOpen ? 'Cerrar menú de navegación' : 'Abrir menú de navegación');
  };

  window.closeMobileMenu = function () {
    if (navLinks) navLinks.classList.remove('mobile-open');
    if (navToggle) {
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.setAttribute('aria-label', 'Abrir menú de navegación');
    }
  };

  if (navbar) {
    window.addEventListener('scroll', function () {
      navbar.classList.toggle('scrolled', window.scrollY > 40);
      updateActiveSection();
    }, { passive: true });
    updateActiveSection();
  }

  var reveals = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    reveals.forEach(function (element) {
      element.classList.add('visible');
    });
  } else {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    reveals.forEach(function (element) {
      observer.observe(element);
    });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
