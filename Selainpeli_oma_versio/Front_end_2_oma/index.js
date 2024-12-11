'use strict';
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

/* Uusi peli */
async function newGame() {
    const name = document.getElementById("nimi").value;
    const difficulty = document.getElementById("vaikeus").value;
    const vastaus1 = await fetch(`http://127.0.0.1:3000/newgame/${name}/${difficulty}`);
    const vastaus1_json = await vastaus1.json();
    console.log(vastaus1_json);

    window.location.href = "peli2v2.html";
};

/* Peli valikko */
async function loadList() {
    const gameArray = await fetch(`http://127.0.0.1:3000/gamelist`);
    const games = await gameArray.json();
    console.log(games);

    const target = document.getElementById("myModal");

    for (let i=0; i<games.length; i++) {
        // Place
        let card = document.createElement("div");
        card.setAttribute("class", "modal-content");
        card.innerHTML =
        `
        <h2>${games[i].name}</h2>        
        <p>Vaikeus taso: ${games[i].difficulty} | Sijainti: ${games[i].location.country} | CO2: ${games[i].co2} | Rahat: ${games[i].money}€</p>
        <button onclick="loadGame('${games[i].name}')">Lataa Peli</button>
        `;
        target.appendChild(card);
}};

newGame();
loadList();