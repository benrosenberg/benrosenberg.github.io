const main = document.getElementById("main");
const mainfooter = document.getElementById("mainfooter");
const menu = document.getElementById("menu");
const hamburger = document.getElementById("hamburger");

function toggle_menu_active() {
    menu.classList.toggle("inactive");
    main.classList.toggle("menuinactive");
    mainfooter.classList.toggle("menuinactive");
    hamburger.classList.toggle("menuinactive");
}

function set_menu_inactive() {
    menu.classList.add("inactive");
    main.classList.add("menuinactive");
    mainfooter.classList.add("menuinactive");
    hamburger.classList.add("menuinactive");
}

function set_menu_active() {
    menu.classList.remove("inactive");
    main.classList.remove("menuinactive");
    mainfooter.classList.remove("menuinactive");
    hamburger.classList.remove("menuinactive");
}

hamburger.addEventListener("click", () => {
    toggle_menu_active();
});

// Ensure menu visibility is set correctly on page load
window.addEventListener("resize", () => {
    if (window.innerWidth < 769) {
        set_menu_inactive();
    } else {
        set_menu_active();
    }
});

// Initial check on page load
if (window.innerWidth < 769) {
    set_menu_inactive();
} else {
    set_menu_active();
}
