$(document).ready(function() {
    //Countdown to Summer Sale
    function countdown() {
        let saleStarts = 'June 30, 2020 00:00:00';
        let startDate = new Date();
        let endDate = new Date(saleStarts);

        let startTime = startDate.getTime();
        let endTime = endDate.getTime();

        let timeRemaining = endTime - startTime;

        let seconds = Math.floor(timeRemaining / 1000);
        let minutes = Math.floor(seconds / 60);
        let hours = Math.floor(minutes / 60);
        let days = Math.floor(hours / 24);

        days = Math.floor(days % 30.44);
        hours = hours % 24;
        minutes %= 60;
        seconds %= 60;

        days = (days < 10) ? '0' + days : days;
        hours = (hours < 10) ? '0' + hours : hours;
        minutes = (minutes < 10) ? '0' + minutes : minutes;
        seconds = (seconds < 10) ? '0' + seconds : seconds;

        document.getElementById('days').innerHTML = days;
        document.getElementById('hours').innerHTML = hours;
        document.getElementById('minutes').innerHTML = minutes;
        document.getElementById('seconds').innerHTML = seconds;

        setTimeout(countdown, 1000);
}

countdown();
});