"use strict";
// *** Globaalit muuttujat ***
var gamer_tag; // Pelaajan tunniste
var games;
let markerGroup;

/// SIVUN HALLINTA ///

/* Aloita peli */
document.getElementById("start-button").addEventListener("click", newGame);

/* Lataa peli modaali */
var modal = document.getElementById("myModal");
var btn = document.getElementById("load-button");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function () {
  modal.style.display = "block";
};
span.onclick = function () {
  modal.style.display = "none";
};
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// *** Sivupalkin hallinta ***
function toggleSidebar(type) {
  document.getElementById(`sidebar-${type}`).classList.add("active");
}

function closeSidebar(type) {
  document.getElementById(`sidebar-${type}`).classList.remove("active");
}

// *** Kokoruututila ***
function toggleFullScreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
}

// Peli kartta
const map = L.map("map1").setView([50.23, 13.74], 4);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

/// DATA KOODEJA ///

/* Listan haku */
async function fetchList() {
  const gameArray = await fetch(`http://127.0.0.1:3000/gamelist`);
  games = await gameArray.json();
  return games;
}

/* Uusi peli */
async function newGame() {
  // Nollataan karttamerkit
  map.eachLayer((layer) => {
    if (layer instanceof L.CircleMarker) {
      map.removeLayer(layer);
    }
  });

  const name = document.getElementById("nimi").value;
  const difficulty = document.getElementById("vaikeus").value;
  const vastaus1 = await fetch(
    `http://127.0.0.1:3000/newgame/${name}/${difficulty}`
  );
  const vastaus1_json = await vastaus1.json();
  console.log(vastaus1_json);

  const screen = document.getElementById("welcome-screen");
  screen.style.display = "none";
  collabTag(name);
}

/* Peli valikko */
async function loadList() {
  games = await fetchList();
  console.log(games);

  const target = document.getElementById("myModal");
  target.innerHTML = ""

  Object.values(games).forEach((game) => {
    let card = document.createElement("div");
    card.setAttribute("class", "modal-content");
    card.innerHTML = `
        <h2>${game.name}</h2>        
        <p>Vaikeus taso: ${game.difficulty} | Sijainti: ${
      game.location.country
    } | CO2: ${game.co2} | Rahat: ${game.money}€</p>
        <button onclick="collabTag('${game.name}')">Lataa Peli</button>
        `;
    target.appendChild(card);
  });
}

async function collabTag(tag){
  const lataa = await fetch(
    `http://127.0.0.1:3000/loadgame/${tag}`
  );
  const lataa_json = await lataa.json();
  console.log(lataa_json);
  gamer_tag = tag;
  loadGame(gamer_tag);
  return gamer_tag;
}

async function loadGame(gamer_tag) {
  const screen = document.getElementById("welcome-screen");
  screen.style.display = "none";

  // Markkeri refresh
  if (markerGroup) {
    markerGroup.clearLayers();
  } else {
    markerGroup = L.layerGroup().addTo(map);
  }

  games = await fetchList();
  console.log(games);
  console.log(gamer_tag);

  if (games[gamer_tag].money < 0) {
    alert("Peli on päättynyt, koska rahasi loppuivat!");
    location.reload();
  }

  for (let i = 0; i < games[gamer_tag].airports.length; i++) {
    // Booleanit ja muut määritelmät
    let location = games[gamer_tag].location.name;
    let visited = games[gamer_tag].airports[i].visited;
    let goal = games[gamer_tag].airports[i].goal;

    let lentoBoolean = false;

    // Kordinaatit ja lentokenttä
    let lentokentta = games[gamer_tag].airports[i].name;
    let lat = games[gamer_tag].airports[i].lat;
    let lon = games[gamer_tag].airports[i].lon;
    let coords = [lat, lon];

    // Markkerin väri määrittely
    let markerColor = "red"; // Oletusväri

    if (location == lentokentta) {
      markerColor = "blue"; // Pelaaja on tässä kentässä
    } else if (visited == true) {
      markerColor = "grey"; // Kenttä on käyty, niin väri harmaaksi
    }

    for (let j = 0; j < games[gamer_tag].flights.length; j++) {
      if (games[gamer_tag].flights[j].name == lentokentta) {
        markerColor = "green";
        lentoBoolean = true;
      }
      if (
        games[gamer_tag].flights[j].name == lentokentta &&
        games[gamer_tag].flights[j].bonus_flight == true
      ) {
        markerColor = "orange";
        lentoBoolean = true;
      }
    }

    // Tavoitekenttä (goal) ja pelaajan saapuminen sinne
    if (goal == true) {
      markerColor = "purple"; // Alustava väri
      if (location == lentokentta) {
        markerColor = "blue"; // Tavoitekenttä muuttuu siniseksi, jos pelaaja on siellä
      }
    }

    // Luo divIcon-tyylinen markkeri (moderni tyyli)
    const marker = L.divIcon({
      className: 'airport-marker',
      html: `<div class="marker" style="background-color: ${markerColor};">
            </div>`,
      iconSize: [14, 14], // Pisteen koko
      iconAnchor: [6, 6], // Keskittää markkerin
    });

    const mapMarker = L.marker(coords, { icon: marker }).bindPopup(`
      <b>${games[gamer_tag].airports[i].name}</b><br>
      <button onclick="showFlightDialog('${
        games[gamer_tag].airports[i].name
      }', ${JSON.stringify(coords)}, '${games[gamer_tag].airports[i].icao}')">
        Valitse tämä lentokenttä
      </button>
    `);

    markerGroup.addLayer(mapMarker); // Add marker to the group

    // Jos kenttä on käyty, lisää CSS-luokka
    if (visited) {
      mapMarker.getElement()?.classList.add("visited");
    }

    // Jos ei ole lentoa, vain tavallinen popup
    if (!lentoBoolean) {
      mapMarker.bindPopup(`<b>${games[gamer_tag].airports[i].name}</b>`);
    }
  }

  update_player_info(gamer_tag);
  return gamer_tag;
}


/* Pelaaminen */
async function playGame(flight_type, destination) {
  let query = `http://127.0.0.1:3000/${flight_type}/${destination}`;
  let vastaus2 = await fetch(query);
  let vastaus2_json = await vastaus2.json();
  console.log(vastaus2_json);
  collabTag(gamer_tag);
}

loadList();

// Globaalit muuttujat ja pelaajan tiedot
const WEATHER_API_KEY = "95cb8ffa6452ef6b75e12f76180ac231"; // OpenWeatherMap API-avain


let playerData = {
  name: "",
  budget: 1500,
  emissions: 0,
  visitedAirports: 0,
  currentAirport: [50.23, 13.74], // Aloituskoordinaatit
  visitedCoordinates: [], // Käydyt lentokentät
  currentAirportName: "Praha", // Aloituskentän nimi
};


// *** Säätiedon haku ***
function fetchWeather(coords, callback) {
  const [lat, lon] = coords;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${WEATHER_API_KEY}&units=metric&lang=fi`;

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Haku epäonnistui.");
      }
      return response.json();
    })
    .then((data) => {
      const weather = `
        Lämpötila: ${data.main.temp}°C<br>
        Tila: ${data.weather[0].description}<br>
        Tuuli: ${data.wind.speed} m/s
      `;
      callback(weather, data.name); // Lähetetään myös kaupungin nimi
    })
    .catch((error) => {
      console.error("Virhe säätietojen haussa:", error);
      callback("Säätiedot eivät ole saatavilla.");
    });
}

// *** Säätiedon näyttäminen ***
function updateWeatherInfo(weather, city) {
  document.getElementById("current-weather").innerHTML = `
    Nykyinen sää ${city}:<br>
    ${weather}
  `;
}


// *** Lentokentän valinta ***
function showFlightDialog(airportName, airportCoords, airportIcao) {
  fetchWeather(airportCoords, (weather, city) => {
    const distance = calculateDistance(playerData.currentAirport, airportCoords); // Laske etäisyys
    const costsPerKm = { small: 0.4, normal: 0.3, high: 0.2 }; // Hinnat per kilometri

    // Lasketaan hinnat eri lentotyypeille
    const smallCost = Math.round(distance * costsPerKm.small).toFixed(2);
    const normalCost = Math.round(distance * costsPerKm.normal).toFixed(2);
    const highCost = Math.round(distance * costsPerKm.high).toFixed(2);

    const dialog = document.createElement("div");
    dialog.className = "flight-dialog";
    dialog.innerHTML = `
      <h3>Lentokenttä: ${airportName}</h3>
      <p>${weather}</p>
      <p>Valitse lentoluokka:</p>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
        airportCoords
      )}, 'small', '${airportIcao}')">Vähänpäästöinen - Hinta: €${smallCost}</button>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
        airportCoords
      )}, 'normal', '${airportIcao}')">Keskipäästöinen - Hinta: €${normalCost}</button>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
        airportCoords
      )}, 'high', '${airportIcao}')">Suurpäästöinen - Hinta: €${highCost}</button>
      <button onclick="closeDialog()">Peruuta</button>
    `;
    document.body.appendChild(dialog);
  });
}

// *** Sulje lentodialogi ***
function closeDialog() {
  const dialog = document.querySelector(".flight-dialog"); // Hakee ensimmäisen löytyvän flight-dialog-elementin
  if (dialog) {
    dialog.remove(); // Poistaa sen DOM:sta
  }
}

// *** Lentovalinnan vahvistus ***
function confirmFlight(airportName, airportCoords, flightType, airportIcao) {
  playGame(flightType, airportIcao);
  const costsPerKm = { low: 0.4, medium: 0.3, high: 0.2 };
  const emissionsPerKm = { low: 75, medium: 150, high: 300 };

  const distance = calculateDistance(playerData.currentAirport, airportCoords);
  const cost = distance * costsPerKm[flightType];
  const emission = distance * emissionsPerKm[flightType];

  if (playerData.budget < cost) {
    alert("Sinulla ei ole tarpeeksi rahaa tähän lentoon!");
    closeDialog();
    return;
  }


  // Merkitään kenttä käydyksi
  for (let airport of games[gamer_tag].airports) {
    if (airport.name === airportName) {
      airport.visited = true;
    }
  }

  updatePlayerInfo();
  fetchWeather(playerData.currentAirport, updateWeatherInfo); // Päivitä säätiedot kenttämuutoksen jälkeen
  closeDialog();
}


// *** Pelaajatietojen päivitys ***
function updatePlayerInfo() {
  // Päivitetään pelaajan tiedot
  document.getElementById(
    "player-budjetti"
  ).textContent = `${playerData.budget.toFixed(2)} €`;
  document.getElementById(
    "player-paastot"
  ).textContent = `${playerData.emissions.toFixed(2)} kg`;
  document.getElementById("player-kohde").textContent =
    playerData.visitedAirports;
  document.getElementById(
    "player-location"
  ).textContent = `Lentokenttä: ${playerData.currentAirportName}`; // Näytetään kenttä nimi
}

// *** Etäisyyden laskenta ***
function calculateDistance(coords1, coords2) {
  if (!coords1 || !coords2) return 0;
  const R = 6371; // Maapallon säde kilometreissä
  const dLat = toRad(coords2[0] - coords1[0]);
  const dLon = toRad(coords2[1] - coords1[1]);
  const lat1 = toRad(coords1[0]);
  const lat2 = toRad(coords2[0]);

  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) ** 2;
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

function toRad(value) {
  return (value * Math.PI) / 180;
}

// *** Pelin tilan tarkastus ***
function update_player_info(gamer_tag) {
  // Lasketaan käydyt kentät
  let visited_count = 0;
  for (let airport of games[gamer_tag].airports) {
    if (airport.visited == true) {
      visited_count++;
    }
  }

  // Tavoitekentät ja käydyt tavoitekentät
  const goalAirports = games[gamer_tag].airports.filter((airport) => airport.goal);
  const visitedGoalsCount = goalAirports.filter((airport) => airport.visited).length;

  // Päivitetään pelaajatiedot
  document.getElementById("player-name").innerText = games[gamer_tag].name;
  document.getElementById("player-budjetti").innerText = games[gamer_tag].money + "€";
  document.getElementById("player-kohde").innerText = visited_count;
  document.getElementById("player-paastot").innerText = games[gamer_tag].co2 + "kg";
  document.getElementById("player-location").innerText =
    games[gamer_tag].location.name;

  // Päivitetään tieto tavoitekentistä
  document.getElementById(
    "player-goals-visited"
  ).textContent = `${visitedGoalsCount}/${goalAirports.length}`;

  // Tarkistetaan, onko pelaaja tavoitekentällä
  const playerMessageElement = document.getElementById("player-message");
  const isPlayerAtGoal = goalAirports.some(
    (airport) => airport.name === games[gamer_tag].location.name
  );

  // Näytä viesti, jos pelaaja on tavoitekentällä
  if (isPlayerAtGoal) {
    playerMessageElement.textContent = "Olet tällä hetkellä tavoitelentokentällä!";
  } else {
    playerMessageElement.textContent = ""; // Tyhjennä viesti, jos pelaaja ei ole enää tavoitekentällä
  }

  // Voittotilanteen tarkistus
  if (goalAirports.every((airport) => airport.visited)) {
    alert("Onneksi olkoon! Olet voittanut pelin!");
    location.reload();
  }
}
