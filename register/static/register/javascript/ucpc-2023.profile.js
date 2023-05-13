// Show modal to select THPT or Uni when create team
$(document).ready(function(){
    param = window.location.search;
    if (param == "") $("#staticBackdrop").modal('show');
});

// add param team type to url when select option in create profile page
let uni_option_block = document.getElementById('uni-option-block')
let school_option_block = document.getElementById('school-option-block')

if(uni_option_block) {
    uni_option_block.addEventListener('click', e => window.location.replace(window.location.href + '?type=University'))
}

if(school_option_block) {
    school_option_block.addEventListener('click', e => window.location.replace(window.location.href + '?type=HighSchool'))
}

// add param team type to url in view profile page
let edit_link = document.getElementById('edit-link')
let teammate_info_box = document.getElementsByClassName('teammate-info-box')

if(edit_link) {
    edit_link.setAttribute('href', '/profile/edit/' + (teammate_info_box.length == 4 ? '?type=HighSchool' : '?type=University'))
};

let optionList = document.getElementsByTagName('option')
let urlParams =  new URLSearchParams(window.location.search)
let selectedFlag0 = false, selectedFlag1 = false, selectedFlag2 = false, selectedFlag3 = false
for (let i = 0; i < optionList.length; i++) {
    // hide unrelated options
    if (urlParams.get('type') === 'University' && optionList[i].value.startsWith('THPT')) {
        optionList[i].style.display = 'none'
        optionList[i].setAttribute('disabled', true)
    }
    if (urlParams.get('type') === 'HighSchool' && optionList[i].value.startsWith('DH')) {
        optionList[i].style.display = 'none'
        optionList[i].setAttribute('disabled', true)
    }
    // select default option
    if (window.location.pathname.includes('/profile/create/')) {
        if (!selectedFlag0 && optionList[i].parentElement.id === 'id_teammate_set-0-School') {
            if (urlParams.get('type') === 'University' && optionList[i].value.startsWith('DH')) {
                optionList[i].selected = true
                selectedFlag0 = true
            }
            if (urlParams.get('type') === 'HighSchool' && optionList[i].value.startsWith('THPT')) {
                optionList[i].selected = true
                selectedFlag0 = true
            }
        }
        if (!selectedFlag1 && optionList[i].parentElement.id === 'id_teammate_set-1-School') {
            if (urlParams.get('type') === 'University' && optionList[i].value.startsWith('DH')) {
                optionList[i].selected = true
                selectedFlag1 = true
            }
            if (urlParams.get('type') === 'HighSchool' && optionList[i].value.startsWith('THPT')) {
                optionList[i].selected = true
                selectedFlag1 = true
            }
        }
        if (!selectedFlag2 && optionList[i].parentElement.id === 'id_teammate_set-2-School') {
            if (urlParams.get('type') === 'University' && optionList[i].value.startsWith('DH')) {
                optionList[i].selected = true
                selectedFlag2 = true
            }
            if (urlParams.get('type') === 'HighSchool' && optionList[i].value.startsWith('THPT')) {
                optionList[i].selected = true
                selectedFlag2 = true
            }
        }
        if (!selectedFlag3 && optionList[i].parentElement.id === 'id_teammate_set-3-School') {
            if (urlParams.get('type') === 'University' && optionList[i].value.startsWith('DH')) {
                optionList[i].selected = true
                selectedFlag3 = true
            }
            if (urlParams.get('type') === 'HighSchool' && optionList[i].value.startsWith('THPT')) {
                optionList[i].selected = true
                selectedFlag3 = true
            }
        }
    }
}

// Searchable auto-complete form
$(document).ready(function() {
    $('.school-select').select2();
})