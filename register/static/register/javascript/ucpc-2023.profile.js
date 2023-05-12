// Show modal to select THPT or Uni when create team
$(document).ready(function(){
    param = window.location.search;
    if (param == "") $("#staticBackdrop").modal('show');
});
// add param team type to url when select option
document.getElementById('uni-option-block').addEventListener('click', e => {
    window.location.replace(window.location.href + '?type=University');
})

document.getElementById('school-option-block').addEventListener('click', e => {
    window.location.replace(window.location.href + '?type=HighSchool');
})

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
};

// Searchable auto-complete form
$(document).ready(function() {
    $('.school-select').select2();
});