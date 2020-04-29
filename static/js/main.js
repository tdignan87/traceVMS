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
 * If any option values equal "Yes" then hide the sign in button and alert the user. If not, and checkbox is checked then system will proceed.Possible future conditions should allow a admin to bypass any yes and permit
 */
$("select.form-control").change(function() {

    if ($(this).children("option:selected").val() == "Yes") {
        alert("Please notify site contact as conditions have failed for entering the site. Only proceed if company has still given you permission to enter site.");
        $("#visit-only-btn").hide();
    } else if (confirmCheck.checked == true) {
        $("#visit-only-btn").show();
    }



});