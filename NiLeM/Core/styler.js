function Store(item, name = "color")
{
    window.localStorage.setItem(name, item);
    location.reload();
}
function Set()
{
    var style = document.createElement("style");
    if (window.localStorage.getItem("color"))
    {
        if (window.localStorage.getItem("color") == "light")
        {
            style.innerHTML = ""
                + "body { "
                + "background-color: #E0E0E0; "
                + "color: black; "
                + "} "
                + "button { "
                + "background-color: #C0C0C0; "
                + "color: black; "
                + "border-color: gray; "
                + "} "
                + "input { "
                + "background-color: #C0C0C0; "
                + "color: black; "
                + "border-color: gray; "
                + "}";
        }
        else if (window.localStorage.getItem("color") == "fire")
        {
            style.innerHTML = ""
                + "body { "
                + "background-color: #DC0F0F; "
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
                + "background-color: #0000C0; "
                + "color: white; "
                + "} "
                + "button { "
                + "background-color: #0050F0; "
                + "color: white; "
                + "border-color: #00007F; "
                + "} "
                + "input { "
                + "background-color: #0050F0; "
                + "color: white; "
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
        else
        {
            style.innerHTML = ""
                + "body { "
                + "background-color: #00001F; "
                + "color: white; "
                + "} "
                + "button { "
                + "background-color: #0F0F2F; "
                + "color: white; "
                + "border-color: gray; "
                + "} "
                + "input { "
                + "background-color: #0F0F2F; "
                + "color: white; "
                + "border-color: gray; "
                + "}";
        }
    }
    else
    {
        Store("dark")
        style.innerHTML = ""
            + "body { "
            + "background-color: #00001F; "
            + "color: white; "
            + "} "
            + "button { "
            + "background-color: #0F0F2F; "
            + "color: white; "
            + "border-color: gray; "
            + "} "
            + "input { "
            + "background-color: #0F0F2F; "
            + "color: white; "
            + "border-color: gray; "
            + "}";
    }
    if (DetectMobile())
    {
        style.innerHTML += " "
            + ".image_big { "
            + "width: 150px; "
            + "} "
            + ".image_small { "
            + "width: 100px; "
            + "}"
        style.innerHTML += " "
            + "body { "
            + "margin: 25px;"
            + "} "
            + "h1 { "
            + "font-size: 80px; "
            + "} "
            + "h2 { "
            + "font-size: 60px; "
            + "} "
            + "h3 { "
            + "font-size: 30px; "
            + "} "
            + "h4 { "
            + "font-size: 20px; "
            + "} "
            + "p { "
            + "font-size: 30px; "
            + "} "
            + "button { "
            + "font-size: 50px; "
            + "margin: 5px; "
            + "} "
            + "input { "
            + "font-size: 30px; "
            + "} "
            + "input[type=radio] { "
            + "height: 1em; "
            + "}"
    }
    else
    {
        style.innerHTML += " "
            + ".image_big { "
            + "width: 280px; "
            + "} "
            + ".image_small { "
            + "width: 140px; "
            + "}"
        style.innerHTML += " "
            + "body { "
            + "margin: 10px;"
            + "} "
            + "h1 { "
            + "font-size: 60px; "
            + "} "
            + "h2 { "
            + "font-size: 50px; "
            + "} "
            + "h3 { "
            + "font-size: 32px; "
            + "} "
            + "h4 { "
            + "font-size: 28px; "
            + "} "
            + "p { "
            + "font-size: 25px; "
            + "} "
            + "button { "
            + "font-size: 25px; "
            + "margin: 5px; "
            + "} "
            + "input { "
            + "font-size: 25px; "
            + "} "
            + "input[type=radio] { "
            + "height: 1em; "
            + "}"
    }
    style.innerHTML += " "
        + "h1, h2, h3, h4, h5, h6, p, div { "
        + "text-align: center; "
        + "font-family: Arial, Helvetica, sans-serif; "
        + "} "
        + "table {"
        + "margin-left: auto; "
        + "margin-right: auto; "
        + "}"
    document.head.appendChild(style);
}
function DetectMobile()
{
    const toMatch = [
        /Android/i,
        /webOS/i,
        /iPhone/i,
        /iPad/i,
        /iPod/i,
        /BlackBerry/i,
        /Windows Phone/i
    ];
    return toMatch.some((toMatchItem) => {
        return navigator.userAgent.match(toMatchItem);
    });
}
Set();

