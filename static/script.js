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

    const response = await fetch("/predict", {
        method: "POST",
        body: formData, 
    });

    const data = await response.json();
    localStorage.setItem("prediction", JSON.stringify(data));
    window.location.href = "/result";
});