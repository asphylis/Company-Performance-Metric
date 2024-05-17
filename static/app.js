async function submitQuery() {
    const query = document.getElementById('userQuery').value;
    const response = await fetch('/processQuery', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query })
    });

    if (response.ok) {
        const jsonOutput = await response.json();
        document.getElementById('jsonOutput').innerText = JSON.stringify(jsonOutput, null, 2);
    } else {
        const error = await response.json();
        document.getElementById('jsonOutput').innerText = `Error: ${error.error}`;
    }
}
