"use strict";
// *** Globaalit muuttujat ***
var gamer_tag; // Pelaajan tunniste
var games;

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

  // Nollataan pelaajan tiedot
  playerData = {
    name: "",
    budget: 1500,
    emissions: 0,
    visitedAirports: 0,
    currentAirport: [50.23, 13.74],
    visitedCoordinates: [],
    currentAirportName: "Praha",
  };

  const name = document.getElementById("nimi").value;
  const difficulty = document.getElementById("vaikeus").value;
  const vastaus1 = await fetch(
    `http://127.0.0.1:3000/newgame/${name}/${difficulty}`
  );
  const vastaus1_json = await vastaus1.json();
  console.log(vastaus1_json);

  const screen = document.getElementById("welcome-screen");
  screen.style.display = "none";
  gamer_tag = games.length - 1;
  loadGame(gamer_tag);
  return gamer_tag;
}

/* Peli valikko */
async function loadList() {
  games = await fetchList();
  console.log(games);

  const target = document.getElementById("myModal");
  target.innerHTML = ""

  for (let i = 0; i < games.length; i++) {
    var gamer_tag = i;
    // Place
    let card = document.createElement("div");
    card.setAttribute("class", "modal-content");
    card.innerHTML = `
        <h2>${games[i].name}</h2>        
        <p>Vaikeus taso: ${games[i].difficulty} | Sijainti: ${
      games[i].location.country
    } | CO2: ${games[i].co2} | Rahat: ${games[i].money}€</p>
        <button onclick="loadGame('${[gamer_tag]}')">Lataa Peli</button>
        `;
    target.appendChild(card);
  }
}

/* Pelin lataus */
async function loadGame(gamer_tag) {
  const screen = document.getElementById("welcome-screen");
  screen.style.display = "none";

  games = await fetchList();
  console.log(games);
  console.log(gamer_tag);

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
      markerColor = "blue";
    } else if (visited == true) {
      markerColor = "grey";  // Kenttä on käyty, niin väri harmaaksi
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

    if (goal == true) {
      markerColor = "purple";
    }

    // Lisää markkerit
    const marker = L.circleMarker(coords, {
      color: markerColor, // Väri
      radius: 6, // Pisteen koko
      weight: 2, // Reunan paksuus
      opacity: 1, // Täytteen läpinäkyvyys
      fillOpacity: 1, // Täytteen läpinäkyvyys
    }).addTo(map).bindPopup(`    
      <b>${games[gamer_tag].airports[i].name}</b><br>
      <button onclick="showFlightDialog('${
        games[gamer_tag].airports[i].name
      }', ${JSON.stringify(coords)}, '${games[gamer_tag].airports[i].icao}')">
        Valitse tämä lentokenttä
      </button>
    `);

    // Jos kenttä on käyty, lisää CSS-luokka
    if (visited) {
      marker.getElement().classList.add("visited");
    }

    if (!lentoBoolean) {
      marker.bindPopup(`<b>${games[gamer_tag].airports[i].name}</b>`);
    }
  }
  update_player_info(gamer_tag);
}


/* Pelaaminen */
async function playGame(flight_type, destination) {
  let query = `http://127.0.0.1:3000/${flight_type}/${destination}`;
  let vastaus2 = await fetch(query);
  let vastaus2_json = await vastaus2.json();
  console.log(vastaus2_json);
  loadGame(gamer_tag);
}

// newGame();
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
    const dialog = document.createElement("div");
    dialog.className = "flight-dialog";
    dialog.innerHTML = `
      <h3>Lentokenttä: ${airportName}</h3>
      <p>${weather}</p>
      <p>Valitse lentoluokka:</p>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
      airportCoords
    )}, 'small', '${airportIcao}')">Vähänpäästöinen</button>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
      airportCoords
    )}, 'normal', '${airportIcao}')">Keskipäästöinen</button>
      <button onclick="confirmFlight('${airportName}', ${JSON.stringify(
      airportCoords
    )}, 'high', '${airportIcao}')">Suurpäästöinen</button>
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

  // Päivitä pelaajan tiedot
  playerData.budget -= cost;
  playerData.emissions += emission / 1000; // Muutetaan kilogrammoiksi
  playerData.visitedAirports++;
  playerData.visitedCoordinates.push(airportCoords); // Lisää nykyinen sijainti käytyihin kenttiin
  playerData.currentAirport = airportCoords;
  playerData.currentAirportName = airportName; // Päivitetään lentokentän nimi

  // Merkitään kenttä käydyksi
  for (let airport of games[gamer_tag].airports) {
    if (airport.name === airportName) {
      airport.visited = true;
    }
  }

  updatePlayerInfo();
  fetchWeather(playerData.currentAirport, updateWeatherInfo); // Päivitä säätiedot kenttämuutoksen jälkeen
  closeDialog();
  checkGameStatus();
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
function checkGameStatus() {
  const goalAirports = games[gamer_tag].airports.filter((airport) => airport.goal);
  const visitedGoals = goalAirports.every((airport) => airport.visited);

  if (visitedGoals) {
    alert("Onneksi olkoon! Olet voittanut pelin!");
    location.reload();
  } else if (playerData.budget <= 0) {
    alert("Rahasi loppuivat. Peli päättyi.");
    location.reload();
  }
}

function update_player_info(gamer_tag) {
  //Päivittää sivupalkin pelaajatiedot
  //Lasketaan käydyt kentät:
  let visited_count = 0;
  for (let airport of games[gamer_tag].airports) {
    if (airport.visited == true) {
      visited_count = visited_count + 1;
    }
  }
  //Laitetaan arvot sivulle:
  document.getElementById("player-name").innerText = games[gamer_tag].name;
  document.getElementById("player-budjetti").innerText = games[gamer_tag].money;
  document.getElementById("player-kohde").innerText = visited_count;
  document.getElementById("player-paastot").innerText = games[gamer_tag].co2;
  document.getElementById("player-location").innerText =
    games[gamer_tag].location.name;
}