document.getElementById("fileInput").addEventListener("change", (event) => {
    const file = event.target.files[0];
    const imagePreview = document.getElementById("imagePreview");
    imagePreview.innerHTML = "";
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            const img = document.createElement("img");
            img.src = e.target.result;
            img.style.maxWidth = "100%";
            img.style.height = "auto";
            imagePreview.appendChild(img);
        };
        reader.readAsDataURL(file);
    } else {
        imagePreview.innerHTML = "<span>Preview will appear here</span>";
    }
});

document.getElementById("removeImage").addEventListener("click", () => {
    document.getElementById("fileInput").value = "";
    document.getElementById("imagePreview").innerHTML = "<span>Preview will appear here</span>";
});

document.getElementById("detectImage").addEventListener("click", async () => {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
        alert("Please upload an image first!");
        return;
    }

    const formData = new FormData();
    formData.append("my_image", fileInput.files[0]);

    try {
        const response = await fetch("/detect", {
            method: "POST",
            body: formData,
        });
        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("resultImage").src = data.image_url;
        document.getElementById("resultText").textContent = `Prediction: ${data.result} (${data.confidence})`;
        document.getElementById("resultModal").style.display = "flex";
    } catch (err) {
        alert("Error during prediction. Please try again.");
    }
});

function closeModal() {
    document.getElementById("resultModal").style.display = "none";
}
