const form = document.querySelector('#registration_form');
const TeamRegex = /\b\S*[AĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴAĂÂÁẮẤÀẰẦẢẲẨÃẴẪẠẶẬĐEÊÉẾÈỀẺỂẼỄẸỆIÍÌỈĨỊOÔƠÓỐỚÒỒỜỎỔỞÕỖỠỌỘỢUƯÚỨÙỪỦỬŨỮỤỰYÝỲỶỸỴA-Z]+\S*\b/;
const NumberRegex = /^([0-9]{10}|[0-9]{11})$/;
const CMNDandCCCD = /^([0-9]{9}|[0-9]{12})$/;
const MSSVRegex = /^[a-zA-Z0-9]+$/;
const NameRegex = /^[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳýỵỷỹ\s\W|_]+$/;
const PasswordRegex = /^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$/;
const EmailRegex = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;


let team = form.elements.namedItem("team");
let valid_team = document.getElementById("valid_team");
let invalid_team = document.getElementById("invalid_team");

let member1 = form.elements.namedItem("member1");
let valid_member1 = document.getElementById("valid_member1");
let invalid_member1 = document.getElementById("invalid_member1");

let mssv1 = form.elements.namedItem("mssv1");
let valid_mssv1 = document.getElementById("valid_mssv1");
let invalid_mssv1 = document.getElementById("invalid_mssv1");

let cmnd1 = form.elements.namedItem("cmnd1");
let valid_cmnd1 = document.getElementById("valid_cmnd1");
let invalid_cmnd1 = document.getElementById("invalid_cmnd1");

let phone1 = form.elements.namedItem("phone1");
let valid_phone1 = document.getElementById("valid_phone1");
let invalid_phone1 = document.getElementById("invalid_phone1");

let member2 = form.elements.namedItem("member2");
let valid_member2 = document.getElementById("valid_member2");
let invalid_member2 = document.getElementById("invalid_member2");

let mssv2 = form.elements.namedItem("mssv2");
let valid_mssv2 = document.getElementById("valid_mssv2");
let invalid_mssv2 = document.getElementById("invalid_mssv2");

let cmnd2 = form.elements.namedItem("cmnd2");
let valid_cmnd2 = document.getElementById("valid_cmnd2");
let invalid_cmnd2 = document.getElementById("invalid_cmnd2");

let phone2 = form.elements.namedItem("phone2");
let valid_phone2 = document.getElementById("valid_phone2");
let invalid_phone2 = document.getElementById("invalid_phone2");

let member3 = form.elements.namedItem("member3");
let valid_member3 = document.getElementById("valid_member3");
let invalid_member3 = document.getElementById("invalid_member3");

let mssv3 = form.elements.namedItem("mssv3");
let valid_mssv3 = document.getElementById("valid_mssv3");
let invalid_mssv3 = document.getElementById("invalid_mssv3");

let cmnd3 = form.elements.namedItem("cmnd3");
let valid_cmnd3 = document.getElementById("valid_cmnd3");
let invalid_cmnd3 = document.getElementById("invalid_cmnd3");

let phone3 = form.elements.namedItem("phone3");
let valid_phone3 = document.getElementById("valid_phone3");
let invalid_phone3 = document.getElementById("invalid_phone3");

let email = form.elements.namedItem("email");
let valid_email = document.getElementById("valid_email");
let invalid_email = document.getElementById("invalid_email");

let password = form.elements.namedItem("password");
let valid_password = document.getElementById("valid_password");
let invalid_password = document.getElementById("invalid_password");

let rpassword = form.elements.namedItem("rpassword");
let valid_rpassword = document.getElementById("valid_rpassword");
let invalid_rpassword = document.getElementById("invalid_rpassword");

team.addEventListener('input', validate);
member1.addEventListener('input', validate);
mssv1.addEventListener('input', validate);
cmnd1.addEventListener('input', validate);
phone1.addEventListener('input', validate);
member2.addEventListener('input', validate);
mssv2.addEventListener('input', validate);
cmnd2.addEventListener('input', validate);
phone2.addEventListener('input', validate);
member3.addEventListener('input', validate);
mssv3.addEventListener('input', validate);
cmnd3.addEventListener('input', validate);
phone3.addEventListener('input', validate);
email.addEventListener('input', validate);
password.addEventListener('input', validate);
rpassword.addEventListener('input', validate);

function validate (e) {
    if (e.target.name == "team") {
        if (TeamRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_team.classList.add('valid_icon');
            invalid_team.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_team.classList.remove('valid_icon');
            invalid_team.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "member1") {
        if (NameRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_member1.classList.add('valid_icon');
            invalid_member1.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_member1.classList.remove('valid_icon');
            invalid_member1.classList.add('invalid_icon');unique
        }
    }

    if (e.target.name == "member2") {
        if (NameRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_member2.classList.add('valid_icon');
            invalid_member2.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_member2.classList.remove('valid_icon');
            invalid_member2.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "member3") {
        if (NameRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_member3.classList.add('valid_icon');
            invalid_member3.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_member3.classList.remove('valid_icon');
            invalid_member3.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "mssv1") {
        if (MSSVRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_mssv1.classList.add('valid_icon');
            invalid_mssv1.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_mssv1.classList.remove('valid_icon');
            invalid_mssv1.classList.add('invalid_icon');unique
        }
    }

    if (e.target.name == "mssv2") {
        if (MSSVRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_mssv2.classList.add('valid_icon');
            invalid_mssv2.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_mssv2.classList.remove('valid_icon');
            invalid_mssv2.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "mssv3") {
        if (MSSVRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_mssv3.classList.add('valid_icon');
            invalid_mssv3.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_mssv3.classList.remove('valid_icon');
            invalid_mssv3.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "cmnd1") {
        if (CMNDandCCCD.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_cmnd1.classList.add('valid_icon');
            invalid_cmnd1.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_cmnd1.classList.remove('valid_icon');
            invalid_cmnd1.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "cmnd2") {
        if (CMNDandCCCD.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_cmnd2.classList.add('valid_icon');
            invalid_cmnd2.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_cmnd2.classList.remove('valid_icon');
            invalid_cmnd2.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "cmnd3") {
        if (CMNDandCCCD.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_cmnd3.classList.add('valid_icon');
            invalid_cmnd3.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_cmnd3.classList.remove('valid_icon');
            invalid_cmnd3.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "phone1") {
        if (NumberRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_phone1.classList.add('valid_icon');
            invalid_phone1.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_phone1.classList.remove('valid_icon');
            invalid_phone1.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "phone2") {
        if (NumberRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_phone2.classList.add('valid_icon');
            invalid_phone2.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_phone2.classList.remove('valid_icon');
            invalid_phone2.classList.add('invalid_icon');
        }
    }

    if (e.target.name == "phone3") {
        if (NumberRegex.test(e.target.value)) {
            e.target.classList.add('valid_input');
            e.target.classList.remove('invalid_input');
            valid_phone3.classList.add('valid_icon');
            invalid_phone3.classList.remove('invalid_icon');
        } else {
            e.target.classList.add('invalid_input');
            e.target.classList.remove('valid_input');
            valid_phone3.classList.remove('valid_icon');
            invalid_phone3.classList.add('invalid_icon');
        }
    }

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

    if (e.target.name == "password") {
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
    }

    if (e.target.name == "rpassword") {
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

function showLoginPassword() {
    var checkBox = document.getElementById("checkbox_login");
    var pwd = document.getElementById("id_password");

    if (checkBox.checked == true) {
        pwd.type = "text";
    } else {
        pwd.type = "password";
    }
}

function showPassword() {
    var checkBox = document.getElementById("checkbox_1");
    var pwd = document.getElementById("pos5");

    if (checkBox.checked == true) {
        pwd.type = "text";
    } else {
        pwd.type = "password";
    }
}

function showRPassword() {
    var checkBox = document.getElementById("checkbox_2");
    var pwd = document.getElementById("pos6");

    if (checkBox.checked == true) {
        pwd.type = "text";
    } else {
        pwd.type = "password";
    }
}

// function showInpuBox(selectElement, other_popUp) {
//     selectElement.addEventListener('change', (event) => {
//         if (event.target.value == 6) {
//             if (other_popUp.style.display == 'none') {
//                 other_popUp.style.display = 'block';
//                 }
//         } else {
//             other_popUp.style.display = 'none';
//         }
//     });
// }

// const school_name1 = document.querySelector('.school_name1');
// const school_name2 = document.querySelector('.school_name2');
// const school_name3 = document.querySelector('.school_name3');
// const popUp1 = document.getElementById("popUp_1");
// const popUp2 = document.getElementById("popUp_2");
// const popUp3 = document.getElementById("popUp_3");

// showInpuBox(school_name1, popUp1)
// showInpuBox(school_name2, popUp2)
// showInpuBox(school_name3, popUp3)

// $("#registration_form").submit(async (event) => {
//     // var data = {};
//     // var informations = {};
//     // var school = {1: 'Trường Đại học Công nghệ Thông tin - UIT',
//     //                 2: 'Trường Đại học Khoa học Xã hội và Nhân văn - HCMUSSH',
//     //                 3: 'Trường Đại học Khoa học Tự nhiên - HCMUS',
//     //                 4: 'Trường Đại học Bách khoa - HCMUT',
//     //                 5: 'Trường Đại học Quốc tế - HCMIU'
//     //             };  

//     let registration_form =  document.getElementById('registration_form');
//     let formData = new FormData(registration_form);
    
//     if (formData.get('school2') == 6) {
//         value = document.getElementById("other_school1").value;
//         formData.set('school1', value);
//     }
//     if (formData.get('school2') == 6) {
//         value = document.getElementById("other_school2").value;
//         formData.set('school2', value);
//     }
//     if (formData.get('school3') == 6) {
//         value = document.getElementById("other_school3").value;
//         formData.set('school3', value);
//     }

//     $.ajax({
//         type: "POST",
//         url: "http://localhost:8000",
//         // contentType: 'multipart/form-data',
//         contentType: false,
//         enctype: 'multipart/form-data',
//         processData: false,
//         cache: false,
//         data: formData,
//         success: (data) => {    
//             console.log(data);
//         }
//     })

//     // formData.forEach((value, key) => {
//     //     if (key.includes('school')) {
//     //         if (value == 6) {
//     //             value = document.getElementById("other_" + key).value;
//     //             informations[key] = value;
//     //         } else {
//     //             informations[key] = school[value];
//     //         }
//     //     } else {
//     //         informations[key] = value;
//     //     }
//     // });

//     // data["informations"] = informations;

//     // fetch('https://us-central1-ucpc-348205.cloudfunctions.net/export_2_sheet', {
//     //     method: 'POST',
//     //     headers: {
//     //         'Content-Type': 'application/json',
//     //     },
//     //     body: JSON.stringify(data),
//     //     })
//     //     .then(response => response.json())
//     //     .then(data => console.log(data.message))
// });