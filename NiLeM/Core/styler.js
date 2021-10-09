function Store(color)
{
    window.localStorage.setItem("color", color);
    location.reload();
}
function Set()
{
    if (window.localStorage.getItem("color"))
    {
        var style = document.createElement("style");
        if (window.localStorage.getItem("color") == "dark")
        {
            style.innerHTML = "body {"
                + "background-color: black;"
                + "color: white;"
                + "}"
                + "button {"
                + "    background-color: #0F0F0F;"
                + "    color: white;"
                + "    border-color: gray;"
                + "}"
                + "input {"
                + "    background-color: #0F0F0F;"
                + "    color: white;"
                + "    border-color: gray;"
                + "}";
        }
        else if (window.localStorage.getItem("color") == "light")
        {
            style.innerHTML = "body {"
                + "background-color: white;"
                + "color: black;"
                + "}"
                + "button {"
                + "    background-color: #F0F0F0;"
                + "    color: black;"
                + "    border-color: gray;"
                + "}"
                + "input {"
                + "    background-color: #F0F0F0;"
                + "    color: black;"
                + "    border-color: gray;"
                + "}";
        }
        document.head.appendChild(style);
    }
}