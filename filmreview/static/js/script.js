// window.addEventListener("DOMContentLoaded", (event) => {
//     document.getElementById("apiData").addEventListener("click", function() {
//         let apiData = this.getAttribute("data-value");
//         document.getElementById("film_title").value = apiData;
//     });
// })

// function to show and hide modals when appropriate
document.addEventListener("DOMContentLoaded", function() {
    let modals = document.querySelectorAll(".modal");
    M.Modal.init(modals);
});