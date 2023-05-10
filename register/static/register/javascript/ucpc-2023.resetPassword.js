const form = document.querySelector('#reset-password-form');

const PasswordRegex = /^(?=.{8,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$/;
const PasswordLengthRegex = /^[a-zA-Z0-9]{8,}$/;
const PasswordNumberRegex = /.*[0-9].*/;
const PasswordLetterRegex = /(?=.*[a-z])(?=.*[A-Z]).*/;


let pass = form.elements.namedItem("new_password1");
let rpass = form.elements.namedItem("new_password2");

const submitButton = document.querySelector('#submit-button');



const passwordValidationList = document.querySelector('.password-validation');
const firstListItem = passwordValidationList.getElementsByTagName('li')[0];
const secondListItem = passwordValidationList.getElementsByTagName('li')[1];
const lastListItem = passwordValidationList.getElementsByTagName('li')[2];

pass.addEventListener('input', validate);
rpass.addEventListener('input', validate);


function validate(e) {
    if (e.target.name == "new_password1") {
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

    if (PasswordRegex.test(pass.value)) {
        submitButton.disabled = false; // enable the submit button
    } else {
        submitButton.disabled = true; // disable the submit button
}
}

