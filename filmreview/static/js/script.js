// my api key
const apiKey = '03ba0856ecf076f61e321303a06a27ca';
// base URL for the API
const baseURL = 'https://api.themoviedb.org/3/';
// pathway for image 
const imgUrl = 'https://image.tmdb.org/t/p/';

function getData(type, cb) {
    let xhr = new XMLHttpRequest();
    xhr.open("GET", baseURL + type + "/");
    xhr.send();

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            cb(JSON.parse(this.responseText));
        };
    };
};