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
    var inputplace = document.createElement("p");
    inputplace.id = "inp";

    for (let i = 0; i < answers.length; i++)
    {
        var inputradio = document.createElement("input");
        inputradio.type = "radio";
        inputradio.id = "ans";
        inputradio.name = "ans";
        inputplace.appendChild(inputradio);
        inputplace.appendChild(document.createTextNode(answers[i]));
    }

    document.getElementById("q").appendChild(inputplace);
}
function CheckEnter(correct_string, incorrect_string, correct_answer)
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
function CheckRadio(correct_string, incorrect_string, correct_answer)
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
