$(document).ready(function () {
    $("#history").show();
    $("#timer").hide();
});

var data, minutesLabel, secondsLabel, totalSeconds, valString;
data = 0;

function scanPort() {

    if (data == 0) {
        data = 1;
        $("#history").hide();
        $("#timer").show();
        setInterval(setTime, 1000);
        minutesLabel = document.getElementById("minutes");
        secondsLabel = document.getElementById("seconds");
        totalSeconds = 0;
    }  
}

function setTime() {
    ++totalSeconds;
    secondsLabel.innerHTML = pad(totalSeconds % 60);
    minutesLabel.innerHTML = pad(parseInt(totalSeconds / 60));
}

function pad(val) {
    valString = val + "";
    if (valString.length < 2) {
        return "0" + valString;
    }
    else {
        return valString;
    }
}