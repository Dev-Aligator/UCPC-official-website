var toggler = document.querySelector('.fa-solid.fa-bars')
var navbar = document.querySelector('.Navbar')
var navbarHeight = navbar.clientHeight
var menuAnimation = document.querySelector('#NavbarSupportedContent')
var img = document.querySelector('.Navbar-brand')

toggler.onclick = function () {
    var isClosed = navbar.clientHeight === navbarHeight
    if (isClosed) {
        navbar.style.maxHeight = 'fit-content'
        menuAnimation.classList.add('animate__animated')
        menuAnimation.classList.add('animate__slideInDown')
        img.style.top = '-' + navbarHeight + 'px'
    } else {
        navbar.style.maxHeight = null
        menuAnimation.classList.remove('animate__animated')
        menuAnimation.classList.remove('animate__slideInDown')
        img.style.top = null
    }
}

var menuItems = document.querySelectorAll('.Nav-item')
Array.from(menuItems).forEach(function (item) {
    item.onclick = function () {
        navbar.style.maxHeight = null
        menuAnimation.classList.remove('animate__animated')
        menuAnimation.classList.remove('animate__slideInDown')
        img.style.top = null
    }
})


