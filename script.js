$(document).ready(function() {

  $('#form').submit(function(e) {
    e.preventDefault();
    var name = $('#textOnly').val();

    var email = $('#email').val();
    var password = $('#password').val();
    myInput.onkeyup = function() {
  // Validate lowercase letters
     var lowerCaseLetters = /[a-z]/g;
    if(myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
}
    $(".error").remove();

    if (name.length < 1) {
      $('#textOnly').after('<span class="error">This field is required</span>');
    }


    if (email.length < 1) {
      $('#email').after('<span class="error">This field is required</span>');
    } else {
      var regEx = /^[A-Z0-9][A-Z0-9._%+-]{0,63}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/;
      var validEmail = regEx.test(email);
      if (!validEmail) {
        $('#email').after('<span class="error">Enter a valid email</span>');
      }
    }
    if (password.length < 8) {
      $('#password').after('<span class="error">Password must be at least 8 characters long</span>');
    }
  });

});