// // my api key
// const apiKey = '03ba0856ecf076f61e321303a06a27ca';
// base URL for the API
// const baseURL = 'https://api.themoviedb.org/3/';
// // pathway for image 
// const imgUrl = 'https://image.tmdb.org/t/p/';

// const search = document.getElementById('search');

// function getData(type, cb) {
//     let xhr = new XMLHttpRequest();
//     xhr.open("GET", baseURL + type + "/");
//     xhr.send();

//     xhr.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             //cb(JSON.parse(this.responseText));
//             card.push(this.responseText);
//         };
//     };
// };

// function writeToDocument(type) {
//     let card = document.getElementsByClassName('card');
//     card.innerHTML = [];
//     getData(type, function(card) {
//         card = card.results
//         data.forEach(function(item) {
//             let dataRow = [];
//             Object.keys(item).forEach(function(key) {
//                 let rowData = item[key].toString();
//                 dataRow.push(rowData);
//             });
//         });
//         card.innerHTML = rowData;
//     })

// }