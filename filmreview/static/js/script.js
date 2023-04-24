window.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("apiData").addEventListener("click", function() {
        let apiData = this.getAttribute("data-value");
        document.getElementById("film_title").value = apiData;
    });
})