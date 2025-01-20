function render_katex_math() {
    var math = document.getElementsByTagName("equation");
    for (var i = 0; i < math.length; i++) {
        var tmp = math[i].textContent;
        try {
            if (
                math[i].hasAttribute("type") &&
                math[i].getAttribute("type") == "display"
            ) {
                katex.render(math[i].textContent, math[i], {
                    displayMode: true,
                    output: "html",
                });
            } else {
                katex.render(math[i].textContent, math[i], {
                    displayMode: false,
                    output: "html",
                });
            }
        } catch (e) {
            console.log(e);
            console.log(tmp);
        }
    }
}
