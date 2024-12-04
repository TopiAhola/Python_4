'use strict';

document.addEventListener('DOMContentLoaded', function() {
  const map = L.map('map1').setView([60.23, 24.74], 5);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  setTimeout(() => {
    map.invalidateSize();
  }, 100);

  window.addEventListener('resize', () => {
    map.invalidateSize();
  });
});

function toggleFullScreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
      } else {
        document.exitFullscreen();
      }
    }

    function toggleSidebar(type) {
      const sidebar = document.getElementById('sidebar-' + type);
      sidebar.classList.add('active');
    }

    function closeSidebar(type) {
      const sidebar = document.getElementById('sidebar-' + type);
      sidebar.classList.remove('active');
    }

    function startGame() {
      const nameInput = document.getElementById('player-name-input').value;
      if (nameInput.trim() === '') {
        alert('Anna pelaajan nimi!');
        return;
      }
      document.getElementById('player-name').textContent = nameInput;
      document.getElementById('name-overlay').style.display = 'none';
    }
    function closeAllSidebars(event) {
    const sidebars = document.querySelectorAll('.sidebar');
    sidebars.forEach(sidebar => {
      if (!sidebar.contains(event.target) && event.target !== sidebar.previousElementSibling) {
        sidebar.classList.remove('active');
      }
    });
  }

  document.addEventListener('click', closeAllSidebars);

  document.querySelectorAll('.sidebar, .menu button').forEach(button => {
    button.addEventListener('click', (event) => {
      event.stopPropagation();
    });
  });

  /*Tähän loppuu html css javascript*/