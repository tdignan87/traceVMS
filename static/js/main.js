let confirmCheck = document.getElementById("noticeCheckbox");
let questions = document.querySelector(".select-options");
let editQuestionAdd = document.getElementById("colFormLabelFirst");
let visitorValue = document.getElementById("edit-visitor-dropdown");



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

/**
 * Click event listener for option selected. if wrong value is selected then block messages and display alert message.
 */

$(".select-options").change(function() {
    if (this[this.selectedIndex].value === "1") {
        console.log("1 selected");
        $(".select-options").prop("disabled", true);
        $(".form-check-input").prop("disabled", true);
        $(".alert-msg").show();
    } else {
        console.log("2 selected");
    }
})