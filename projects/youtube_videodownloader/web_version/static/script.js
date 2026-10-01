async function startDownload() {
    const url = document.getElementById('url').value.trim();
    const folder = document.getElementById('folder').value.trim();
    const btn = document.getElementById('downloadBtn');

    if (!url) {
        showStatus("Please enter a valid YouTube URL.", "error");
        return;
    }

    btn.disabled = true;
    btn.innerText = "Downloading... (Check Terminal)";
    showStatus("Fetching video info and downloading...", "info");

    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url, output_path: folder })
        });

        const data = await response.json();

        if (response.ok) {
            showStatus(data.message, "success");
            document.getElementById('url').value = '';
        } else {
            showStatus("Error: " + data.message, "error");
        }
    } catch (err) {
        showStatus("An unexpected network error occurred.", "error");
    } finally {
        btn.disabled = false;
        btn.innerText = "Download Video";
    }
}

function showStatus(message, type) {
    const statusDiv = document.getElementById('status');
    statusDiv.classList.remove('hidden', 'bg-red-900', 'bg-green-950', 'bg-blue-950', 'text-red-300', 'text-green-300', 'text-blue-300', 'border-red-700', 'border-green-800', 'border-blue-800');
    
    if (type === "success") {
        statusDiv.classList.add('bg-green-950', 'text-green-300', 'border', 'border-green-800');
    } else if (type === "error") {
        statusDiv.classList.add('bg-red-900', 'text-red-300', 'border', 'border-red-700');
    } else {
        statusDiv.classList.add('bg-blue-950', 'text-blue-300', 'border', 'border-blue-800');
    }
    statusDiv.innerText = message;
}