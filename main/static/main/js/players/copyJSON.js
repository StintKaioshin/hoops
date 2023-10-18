copyButtons = document.getElementsByClassName("copyJSON");

function clipboard(clicked_id) {
    // Derive the corresponding <p> ID based on the button's ID
    let fileID = 'json_' + clicked_id;

    let btn = document.getElementById(clicked_id);
    let file = document.getElementById(fileID);

    // Check if the file element exists (this is a simple debug step, can be removed later)
    if (!file) {
        alert('File element not found for ID: ' + fileID);
        return;
    }

    // Copy the file content to the clipboard
    navigator.clipboard.writeText(file.innerText);

    // Update the button's text and style
    btn.innerText = "Copied!";
    btn.classList.remove("btn-primary");
    btn.classList.add("btn-success");
}
