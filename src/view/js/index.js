$(document).ready(function () {
    $("#history").show();
    $("#timer").hide();


});

var data = 0;
function scan_port() {
    if (data == 0) {
        data = 1;
        $("#history").hide();
        $("#timer").show();

        setInterval(setTime, 1000);

        var minutesLabel = document.getElementById("minutes");
        var secondsLabel = document.getElementById("seconds");
        var totalSeconds = 0;
    }

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
