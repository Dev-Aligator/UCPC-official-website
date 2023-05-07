$(document).ready(function(){
    param = window.location.search;
    if (param == "") $("#staticBackdrop").modal('show');
});

document.getElementById('uni-option-block').addEventListener('click', e => {
    window.location.replace(window.location.href + '?type=University');
})

document.getElementById('school-option-block').addEventListener('click', e => {
    window.location.replace(window.location.href + '?type=HighSchool');
})