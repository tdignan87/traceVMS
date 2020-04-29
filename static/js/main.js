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
 * If checkbox is checked for visiting bakery then show the sign in button and move to the top of the page.
 */
$("#noticeCheckbox").click(function() {
    if (confirmCheck.checked == true) {

        $("#visit-only-btn").show();
        top.location.href = "#sign-in-container"
    } else {
        $("#visit-only-btn").hide();
    }
})

/**
 * Sign in btn if visit bakery is yes but checkbox is not checked, alert user they must read rules first.
 */


$("#visit-only-btn").click(function() {

})