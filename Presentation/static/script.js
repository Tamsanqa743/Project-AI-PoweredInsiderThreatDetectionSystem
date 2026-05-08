document.getElementById("upload-form").addEventListener("submit", async function(e) {
    // Prevent normal form submission (page refresh)
    e.preventDefault();

    const fileInput = document.getElementById("upload-form");
    alert("JS function called");
    if (!fileInput.files.length) {
        console.log("File arr length:", fileInput.files.length)
        alert("Select a file first");
        return;
    }

    alert("JS function called 2nd");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("result").innerText =
            data.message || data.error;

    } catch (err) {
        console.error(err);
        document.getElementById("result").innerText =
            "Upload failed";
    }
});