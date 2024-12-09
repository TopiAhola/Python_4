'use strict';

//Tässä on toiminnallisuus testilomakkeelle

//Lomake 1 uuden pelin aloittamiseksi:
let lomake1 = document.getElementById("lomake1");
lomake1.addEventListener("submit", new_game);

//Lomake 2 pelin pelaamiseksi
let lomake2 = document.getElementById("lomake2");
lomake2.addEventListener("submit", play_game);

//Lomake 3 pelin lataamiseksi
let lomake3 = document.getElementById("lomake3");
lomake3.addEventListener("submit", load_game);

//Lomake 4 tallennusten hakemiseksi
let lomake4 = document.getElementById("lomake4");
lomake4.addEventListener("click", game_list);

async function new_game() {
    console.log("new_game funktio")
    event.preventDefault()
    let name = document.getElementById("nimi").value;
    let difficulty = document.getElementById("vaikeus").value;
    let query =`http://127.0.0.1:3000/newgame/${name}/${difficulty}`
    console.log(query)
    try {
        let vastaus1 = await fetch(query);
        let vastaus1_json = await vastaus1.json();
        console.log(vastaus1_json)
        document.getElementById("tuloste").innerHTML = vastaus1_json;
          }
    catch (error) {
    console.log(error.message);
  }
}

async function play_game() {
  console.log("play_game funktio")
  event.preventDefault()
  let flight_type = document.getElementById("flight_type").value;
  let destination = document.getElementById("destination").value;
  let query =`http://127.0.0.1:3000/${flight_type}/${destination}`
  console.log(query)
  try {
    let vastaus2 = await fetch(query);
    let vastaus2_json = await vastaus2.json();
    console.log(vastaus2_json)
    document.getElementById("tuloste").innerText = vastaus2_json;
  }
  catch (error) {
    console.log(error.message);
  }
}

async function load_game() {
    console.log("load_game funktio")
    event.preventDefault()
    let name2 = document.getElementById("nimi2").value;
    let query =`http://127.0.0.1:3000/loadgame/${name2}`
    console.log(query)
    try {
        let vastaus3 = await fetch(query);
        let vastaus3_json = await vastaus3.json();
        console.log(vastaus3_json)
        document.getElementById("tuloste").innerHTML = vastaus3_json;
          }
    catch (error) {
    console.log(error.message);
  }
}

async function game_list() {
  console.log("game_list funktio")
  event.preventDefault()
  //let name2 = document.getElementById("nimi2").value;
    let query =`http://127.0.0.1:3000/gamelist`
    console.log(query)
    try {
        let vastaus4 = await fetch(query);
        let vastaus4_json = await vastaus4.json();
        console.log(vastaus4_json)
        document.getElementById("tuloste").innerHTML = vastaus4_json;
          }
    catch (error) {
      console.log(error.message);
    }
}