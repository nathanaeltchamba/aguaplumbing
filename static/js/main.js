let prevScrollpos = window.pageYOffset;

window.onscroll = function () {
    let currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.querySelector(".navbar").style.top = "0";
        document.querySelector(".navbar").style.transition = "top 0.5s";
    } else {
        document.querySelector(".navbar").style.top = "-100px";
        document.querySelector(".navbar").style.transition = "top 0.5s";
    }
    prevScrollpos = currentScrollPos;
}

var el = document.getElementById("wrapper");
    var toggleButton = document.getElementById("menu-toggle");

    toggleButton.onclick = function () {
        el.classList.toggle("toggled");
    };