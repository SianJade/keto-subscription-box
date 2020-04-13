$(document).ready(function() {
    function seeMore(element) {

    let buttonClicked = event.target;
    let more = document.getElementById(element);
    if (more.style.display === "none") {
        buttonClicked.innerText = "See Less";
        more.style.display = "block";
    }
    else {
        buttonClicked.innerText = "See More";
        more.style.display = "none";
    }
}
seeMore();
});