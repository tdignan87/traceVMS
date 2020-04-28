/**
 * Hide questions section of signin page if visiting bakery checkbox is not checked.
 */

window.onload = function() {
    $("#questionaire-set").hide();
    $("#contractor-section").hide();
    $("#visit-only-btn").hide();
}

$('input:radio[name="gridRadios"]').change(
    function() {
        if (this.checked && this.value == 'yesOption') {
            $("#questionaire-set").show();
            $("#contractor-section").show();
            $("#visit-only-btn").hide();
        } else {
            $("#questionaire-set").hide();
            $("#contractor-section").hide();
            $("#visit-only-btn").show();
        }
    });