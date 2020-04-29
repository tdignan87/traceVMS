let confirmCheck = document.getElementById("noticeCheckbox");


/**
 * Hide questions section of signin page if visiting bakery checkbox is not checked.
 */

window.onload = function() {
    $("#questionaire-set").hide();
    $("#contractor-section").hide();
    $("#visit-only-btn").hide();
    $("#confirmation-container").hide();

}

/**
 * hide sections of the page and only show depending on whats selected on the radio button
 */

$('input:radio[name="gridRadios"]').change(
    function() {
        if (this.checked && this.value == 'true') {
            $("#questionaire-set").show();
            $("#contractor-section").show();
            $("#visit-only-btn").hide();
            $("#confirmation-container").show();

        } else {
            $("#questionaire-set").hide();
            $("#contractor-section").hide();
            $("#visit-only-btn").show();
            $("#confirmation-container").hide();
        }
    });


/**
 * If checkbox is checked for visiting bakery then show the sign in button.
 */
$("#noticeCheckbox").click(function() {
    if (confirmCheck.checked == true) {
        $("#visit-only-btn").show();
    }
})