async function analyzeText() {
    const resume = document.getElementById("resumeText").value;

    const res = await fetch("http://127.0.0.1:5000/analyze-text", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ resume })
    });

    const data = await res.json();

    showResult(data);
}

function showResult(data) {

    document.getElementById("score").innerText =
        "Score: " + data.score + "/100";

    const list = document.getElementById("feedback");

    list.innerHTML = "";

    if (data.feedback.length === 0) {
        list.innerHTML = "<li>No suggestions found</li>";
        return;
    }

    data.feedback.forEach(item => {

        const li = document.createElement("li");

        li.innerText = item;

        list.appendChild(li);
    });
}