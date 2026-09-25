document
    .getElementById("predictionForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const data = {
            idc1: parseFloat(document.getElementById("idc1").value),
            idc2: parseFloat(document.getElementById("idc2").value),
            vdc1: parseFloat(document.getElementById("vdc1").value),
            vdc2: parseFloat(document.getElementById("vdc2").value),
            irr: parseFloat(document.getElementById("irr").value),
            pvt: parseFloat(document.getElementById("pvt").value)
        };

        try {

            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.error) {
                alert("Error: " + result.error);
                return;
            }

            document.getElementById("condition").textContent =
                result.condition;

            document.getElementById("maintenance").textContent =
                result.maintenance;

        } catch (error) {

            alert("Unable to connect to the Flask server.");

            console.error(error);
        }
    });