$(document).ready(function() {
    let nutritionButton = document.getElementById('see-nutrition')
    nutritionButton.addEventListener('click', seeNutrition)

    function seeNutrition() {
        let more = document.getElementById('seeMore1');
        if (more.style.display === "none") {
            more.style.display = "block";
        }
        else {
            more.style.display = "none";
        }
    }

    let ingredientButton = document.getElementById('see-ingredients')
    ingredientButton.addEventListener('click', seeIngredients)

    function seeIngredients() {
        let more = document.getElementById('seeMore2');
        if (more.style.display === "none") {
            more.style.display = "block";
        }
        else {
            more.style.display = "none";
        }
    }
});