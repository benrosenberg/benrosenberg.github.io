// adapted from four.lol
function getInitialColorMode() {
    const persistedColorPreference = window.localStorage.getItem("color-mode");
    const hasPersistedPreference = typeof persistedColorPreference === "string"; // If the user has explicitly chosen light or dark,
    // let's use it. Otherwise, this value will be null.
    if (hasPersistedPreference) {
        return persistedColorPreference;
    } // If they haven't been explicit, let's check the media
    // query
    const mql = window.matchMedia("(prefers-color-scheme: dark)");
    const hasMediaQueryPreference = typeof mql.matches === "boolean";
    if (hasMediaQueryPreference) {
        return mql.matches ? "dark" : "light";
    } // If they are using a browser/OS that doesn't support
    // color themes, let's default to 'light'.
    return "light";
}

function setColorsByTheme() {
    const colors = {
        bg: { light: "#ddd", dark: "#282828" },
        bg2: { light: "#ccc", dark: "#343434" },
        bg3: { light: "#bbb", dark: "#404040" },
        text: { light: "black", dark: "#ebdbb2" },
        tagbg: { light: "#ccc", dark: "#555" },
        hoverbg: { light: "#ccc", dark: "#555" },
        easy: { light: "#00932c", dark: "#00ba38" },
        medium: { light: "#cc8400", dark: "#d38900" },
        hard: { light: "#ca1400", dark: "#d71600" },
        buttonborderthickness: { light: "1px", dark: "2px" },
    };
    const colorMode = getInitialColorMode();
    const root = document.documentElement;
    Object.entries(colors).forEach(([name, colorByTheme]) => {
        const cssVarName = `--color-${name}`;
        root.style.setProperty(cssVarName, colorByTheme[colorMode]);
    });
    root.style.setProperty("--initial-color-mode", colorMode);
    const SITEROOT = document.getElementById("SITE_ROOT_TAG").innerText;
    const imageURLS = {
        "cc-svg": {
            light: SITEROOT + "/images/cc.svg",
            dark: SITEROOT + "/images/cc_dark.svg",
        },
        "by-svg": {
            light: SITEROOT + "/images/by.svg",
            dark: SITEROOT + "/images/by_dark.svg",
        },
    };
    Object.entries(imageURLS).forEach(([name, colorByTheme]) => {
        var imageTags = document.getElementsByClassName(name);
        for (let imageTag of imageTags) {
            imageTag.src = colorByTheme[colorMode];
        }
    });
    // set css file depending on color mode as well
    // so that code highlighting is correct
    const stylesheet_titles = {
        light: "hljs-light",
        dark: "hljs-dark",
    };
    var opposite_color_mode = colorMode == "light" ? "dark" : "light";
    enable_stylesheet(stylesheet_titles[colorMode]);
    disable_stylesheet(stylesheet_titles[opposite_color_mode]);
    var hljs_elements = document.getElementsByClassName("hljs");
    for (let element of hljs_elements) {
        if (element.hasAttribute("data-highlighted")) {
            element.setAttribute("data-highlighted", false);
            delete element.dataset.highlighted;
        }
    }
}

function toggleColorMode() {
    const colorMode = getInitialColorMode();
    if (colorMode == "light") {
        window.localStorage.setItem("color-mode", "dark");
    } else if (colorMode == "dark") {
        window.localStorage.setItem("color-mode", "light");
    } else {
        console.log(`Encountered strange color mode: ${colorMode}`);
    }
    setColorsByTheme();
    try {
        // re-render any canvas elements if present
        renderCanvas();
    } catch {
        // fail silently if function does not exist
    }
}

function enable_stylesheet(title) {
    var i, a;
    for (i = 0; (a = document.getElementsByTagName("link")[i]); i++) {
        if (
            a.getAttribute("rel").indexOf("style") != -1 &&
            a.getAttribute("title")
        ) {
            if (a.getAttribute("title") == title) {
                a.disabled = false;
            }
        }
    }
}

function disable_stylesheet(title) {
    var i, a;
    for (i = 0; (a = document.getElementsByTagName("link")[i]); i++) {
        if (
            a.getAttribute("rel").indexOf("style") != -1 &&
            a.getAttribute("title")
        ) {
            if (a.getAttribute("title") == title) a.disabled = true;
        }
    }
}

setColorsByTheme();
