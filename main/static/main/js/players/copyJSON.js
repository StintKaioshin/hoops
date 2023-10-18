function clipboard(clicked_id) {
    // Correctly generate the ID for the paragraph element
    let fileID = 'json_' + clicked_id.split("_")[1];
    
    // Get the corresponding paragraph element
    let file = document.getElementById(fileID);

    // Copy the file content to the clipboard
    navigator.clipboard.writeText(file.innerText);

    // Update button text and style
    let btn = document.getElementById(clicked_id);
    btn.innerText = "Copied!";
    btn.classList.remove("btn-primary");
    btn.classList.add("btn-success");
}
