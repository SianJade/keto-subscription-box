$(document).ready(function() {
    let seeMoreButton = document.getElementById('see-more-button')
    seeMoreButton.addEventListener('click', seeMore)

    function seeMore() {
        let more = document.getElementById('seeMore1');
        if (more.style.display === "none") {
            more.style.display = "block";
        }
        else {
            more.style.display = "none";
        }
    }
});