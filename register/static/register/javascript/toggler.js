var toggler = document.querySelector('.fa-solid.fa-bars')
var navbar = document.querySelector('.Navbar')
var navbarHeight = navbar.clientHeight

toggler.onclick = function () {
    var isClosed = navbar.clientHeight === navbarHeight
    if (isClosed) {
        navbar.style.maxHeight = 'fit-content'
    } else {
        navbar.style.maxHeight = null
    }
}