/**
 * Hide questions section of signin page if visiting bakery checkbox is not checked.
 */

window.onload = function() {
    $("#questionaire-set").hide();
    $("#contractor-section").hide();

}

$('input:radio[name="gridRadios"]').change(
    function() {
        if (this.checked && this.value == 'yesOption') {
            console.log("yes selected");
            $("#questionaire-set").show();
            $("#contractor-section").show();
        } else {
            $("#questionaire-set").hide();
            $("#contractor-section").hide();
        }
    });