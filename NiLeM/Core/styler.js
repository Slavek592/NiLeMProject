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
            style.innerHTML = ""
                + "body { "
                + "background-color: black; "
                + "color: white; "
                + "} "
                + "button { "
                + "background-color: #0F0F0F; "
                + "color: white; "
                + "border-color: gray; "
                + "} "
                + "input { "
                + "background-color: #0F0F0F; "
                + "color: white; "
                + "border-color: gray; "
                + "}";
        }
        else if (window.localStorage.getItem("color") == "light")
        {
            style.innerHTML = ""
                + "body { "
                + "background-color: white; "
                + "color: black; "
                + "} "
                + "button { "
                + "background-color: #F0F0F0; "
                + "color: black; "
                + "border-color: gray; "
                + "} "
                + "input { "
                + "background-color: #F0F0F0; "
                + "color: black; "
                + "border-color: gray; "
                + "}";
        }
        else if (window.localStorage.getItem("color") == "fire")
        {
            style.innerHTML = ""
                + "body { "
                + "background-color: red; "
                + "color: black; "
                + "} "
                + "button { "
                + "background-color: #F02F2F; "
                + "color: black; "
                + "border-color: #7F0000; "
                + "} "
                + "input { "
                + "background-color: #F02F2F; "
                + "color: black; "
                + "border-color: #7F0000; "
                + "}";
        }
        else if (window.localStorage.getItem("color") == "water")
        {
            style.innerHTML = ""
                + "body { "
                + "background-color: blue; "
                + "color: black; "
                + "} "
                + "button { "
                + "background-color: #2F2FF0; "
                + "color: black; "
                + "border-color: #00007F; "
                + "} "
                + "input { "
                + "background-color: #2F2FF0; "
                + "color: black; "
                + "border-color: #00007F; "
                + "}";
        }
        else if (window.localStorage.getItem("color") == "grass")
        {
            style.innerHTML = ""
                + "body { "
                + "background-color: green; "
                + "color: black; "
                + "} "
                + "button { "
                + "background-color: #2FF02F; "
                + "color: black; "
                + "border-color: #007F00; "
                + "} "
                + "input { "
                + "background-color: #2FF02F; "
                + "color: black; "
                + "border-color: #007F00; "
                + "}";
        }
        document.head.appendChild(style);
    }
}
Set();

