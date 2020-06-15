$(document).ready(function () {
    $("#history").show();
    $("#timer").hide();
    // $('.tap-target').tapTarget();


});

function scan_port() {

    $("#history").hide();
    $("#timer").show();
    var minutesLabel = document.getElementById("minutes");
    var secondsLabel = document.getElementById("seconds");
    var totalSeconds = 0;
    setInterval(setTime, 1000);

    function setTime() {
        ++totalSeconds;
        secondsLabel.innerHTML = pad(totalSeconds % 60);
        minutesLabel.innerHTML = pad(parseInt(totalSeconds / 60));
    }

    function pad(val) {
        var valString = val + "";
        if (valString.length < 2) {
            return "0" + valString;
        }
        else {
            return valString;
        }
    }
}
