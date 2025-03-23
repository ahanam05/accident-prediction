document.addEventListener("DOMContentLoaded", function () {
    const cursor = document.createElement("div");
    cursor.classList.add("cursor");
    document.body.appendChild(cursor);

    document.addEventListener("mousemove", function (e) {
        cursor.style.left = `${e.clientX}px`;
        cursor.style.top = `${e.clientY}px`;
    });
});


document.getElementById("prediction-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    let formData = new FormData(this);
    let data = {
        age: parseInt(formData.get("age")),
        gender: formData.get("gender"),
        speed_of_impact: parseFloat(formData.get("speed")),
        helmet_used: formData.get("helmet"),
        seatbelt_used: formData.get("seatbelt"),
    };

    let response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    let result = await response.json();
    localStorage.setItem("prediction", JSON.stringify(result));

    window.location.href = "/result";
});