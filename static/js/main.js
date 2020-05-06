let confirmCheck = document.getElementById("noticeCheckbox");
let questions = document.getElementById("exampleFormControlSelect");


$("#questions-asked").change(function() {

    if (questions.selectedIndex == "1") {
        console.log("Rejected Selected");
        $("#confirmation-container").hide();
        $("#visit-only-btn").hide();
        $("option[value='opt01']")
    } else {
        console.log("Pass Selected");
        $("#confirmation-container").show();
    }
})

/**
 * Hide questions section of signin page if visiting bakery checkbox is not checked.
 */

window.onload = function() {
        $("#questionaire-set").hide();
        $("#contractor-section").hide();
        $("#visit-only-btn").hide();
        $("#confirmation-container").hide();
        $("#answer-questions-warning").hide();
        $(".alert-msg").hide();
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
            $("#answer-questions-warning").show();
            $(".alert-msg").show();


            if (this.checked && this.value == 'true') {
                top.location.href = "#questionaire-set"
            }

        } else {
            $("#questionaire-set").hide();
            $("#contractor-section").hide();
            $("#visit-only-btn").show();
            $("#confirmation-container").hide();
            $("#answer-questions-warning").hide();
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