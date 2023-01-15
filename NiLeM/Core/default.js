function PrintLine(line)
{
    var text = document.createElement("p");
    text.appendChild(document.createTextNode(line));
    document.getElementById("q").appendChild(text);
}
function CreateInputbox()
{
    var inputplace = document.createElement("p");
    var inputbox = document.createElement("input");
    inputbox.type = "text";
    inputbox.id = "ans";
    inputbox.name = "ans";
    inputplace.appendChild(inputbox);
    document.getElementById("q").appendChild(inputplace);
}
function CreateInputradio(answers)
{
    var table = document.createElement("table");
    for (let i = 0; i < answers.length; i++)
    {
        var inputplace = document.createElement("tr");
        var inputplaceleft = document.createElement("td");
        var inputradio = document.createElement("input");
        inputradio.type = "radio";
        inputradio.id = "ans";
        inputradio.name = "ans";
        inputplaceleft.appendChild(inputradio);
        inputplace.appendChild(inputplaceleft);
        var inputplaceright = document.createElement("td");
        var radiotext = document.createElement("label");
        radiotext.innerHTML = answers[i];
        inputplaceright.appendChild(radiotext);
        inputplace.appendChild(inputplaceright);
        table.appendChild(inputplace);
    }
    document.getElementById("q").appendChild(table);
}
function CheckEnter(correct_answer)
{
    if (document.getElementById("ans").value == correct_answer)
    {
        document.getElementById("c").innerHTML = correct_string;
    }
    else
    {
        document.getElementById("c").innerHTML = incorrect_string;
    }
}
function CheckRadio(correct_answer)
{
    var ele = document.getElementsByName('ans');
    for (i = 0; i < ele.length; i++)
    {
        if (ele[i].checked)
        {
            if (i == correct_answer)
            {
                document.getElementById("c").innerHTML = correct_string;
            }
            else
            {
                document.getElementById("c").innerHTML = incorrect_string;
            }
        }
    }
}
function ShowCorrect(correct_answer)
{
    document.getElementById("c").innerHTML = correct_answer;
}
function Next()
{
    if (question < document.getElementById("qt").innerHTML)
    {
        question ++;
        if (question < document.getElementById("qt").innerHTML)
            document.getElementById("yq").innerHTML = question + 1;
        ChangeContent();
    }
}
function Previous()
{
    if (question > 0)
    {
        question --;
        ChangeContent();
        document.getElementById("yq").innerHTML = question + 1;
    }
}
