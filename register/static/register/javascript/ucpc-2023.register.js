const form = document.querySelector('#register-form');

const PasswordRegex = /^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$/;
const EmailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
const PasswordLengthRegex = /^[a-zA-Z0-9]{6,}$/;
const PasswordNumberRegex = /.*[0-9].*/;
const PasswordLetterRegex = /(?=.*[a-z])(?=.*[A-Z]).*/;
let email = form.elements.namedItem("email");
let valid_email = document.getElementById("valid_email");
let invalid_email = document.getElementById("invalid_email");

let password = form.elements.namedItem("password1");
let valid_password = document.getElementById("valid_password");
let invalid_password = document.getElementById("invalid_password");

let rpassword = form.elements.namedItem("password2");
let valid_rpassword = document.getElementById("valid_rpassword");
let invalid_rpassword = document.getElementById("invalid_rpassword");

const passwordValidationList = document.querySelector('.password-validation');
const firstListItem = passwordValidationList.getElementsByTagName('li')[0];
const secondListItem = passwordValidationList.getElementsByTagName('li')[1];
const lastListItem = passwordValidationList.getElementsByTagName('li')[2];

email.addEventListener('input', validate);
password.addEventListener('input', validate);
rpassword.addEventListener('input', validate);


function validate(e) {
    if (e.target.name == "email") {
        if (EmailRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_email.classList.add('valid_icon');
            invalid_email.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_email.classList.remove('valid_icon');
            invalid_email.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "password1") {
        if (PasswordRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_password.classList.add('valid_icon');
            invalid_password.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_password.classList.remove('valid_icon');
            invalid_password.classList.add('invalid_icon');
        }

        if (PasswordLengthRegex.test(e.target.value)){
            firstListItem.style.color = "#4CAF50";
        }
        else{
            firstListItem.style.color = "#D3D3D3";
        }

        if (PasswordNumberRegex.test(e.target.value)){
            secondListItem.style.color = "#4CAF50";
        }
        else{
            secondListItem.style.color = "#D3D3D3";
        }

        if (PasswordLetterRegex.test(e.target.value)){
            lastListItem.style.color = "#4CAF50";
        }

        else{
            lastListItem.style.color = "#D3D3D3";
        }
        
    }

    if (e.target.name == "password2") {
        if (e.target.value == password.value && PasswordRegex.test(e.target.value)) { 
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_rpassword.classList.add('valid_icon');
            invalid_rpassword.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_rpassword.classList.remove('valid_icon');
            invalid_rpassword.classList.add('invalid_icon');
        }
    }
}


const checkbox = document.getElementById('terms-checkbox');
const submitBtn = document.getElementsByClassName('btn');
const errorMessage = document.getElementById('error-message');
checkbox.addEventListener('change', function() {
    // Enable the submit button if the checkbox is checked
    submitBtn.disabled = !checkbox.checked;
  });
  
  form.addEventListener('submit', function(event) {
    // Check if the checkbox is checked
    if (!checkbox.checked) {
      // If it's not checked, prevent the form from being submitted
      event.preventDefault();
      errorMessage.style.display = 'block';
    }
    else{
        errorMessage.style.display = 'none';
    }
  });
  