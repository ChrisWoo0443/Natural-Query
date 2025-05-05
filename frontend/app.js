document.getElementById('query-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById('file');
    const queryInput = document.getElementById('query');
    const modeInput = document.querySelector('input[name="mode"]:checked');

    const generatedCodeDisplay = document.getElementById('generated-code');
    const resultDisplay = document.getElementById('result');

    generatedCodeDisplay.textContent = "Loading...";
    resultDisplay.textContent = "Loading...";

    // ---- Step 1: Upload file ----
    const fileData = new FormData();
    fileData.append('file', fileInput.files[0]);

    const uploadResponse = await fetch('http://127.0.0.1:8000/upload/', {
        method: 'POST',
        body: fileData
    });

    if (!uploadResponse.ok) {
        generatedCodeDisplay.textContent = '';
        resultDisplay.textContent = 'File upload failed.';
        return;
    }

    const filename = fileInput.files[0].name;

    // ---- Step 2: Send query ----
    const queryData = new FormData();
    queryData.append('query', queryInput.value);
    queryData.append('filename', filename);
    queryData.append('mode', modeInput.value);

    const queryResponse = await fetch('http://127.0.0.1:8000/query/', {
        method: 'POST',
        body: queryData
    });

    const queryResult = await queryResponse.json();

    if (queryResponse.ok) {
        generatedCodeDisplay.textContent = queryResult.generated_code || 'No code generated.';
        resultDisplay.textContent = queryResult.result || 'No result returned.';
    
        // ----- Update recent queries -----
        const recentDiv = document.getElementById('recent-queries');
        const newEntry = document.createElement('div');
        newEntry.classList.add('mb-3', 'p-2', 'border', 'rounded', 'bg-light');
        newEntry.innerHTML = `
            <strong>Query:</strong> ${queryInput.value}<br>
            <strong>Code:</strong> <pre>${queryResult.generated_code}</pre>
            <strong>Result:</strong> <pre>${queryResult.result}</pre>
        `;
    
        // If it's the first query, remove "No recent queries yet."
        if (recentDiv.querySelector('p')) {
            recentDiv.innerHTML = '';
        }
    
        recentDiv.prepend(newEntry);
    } else {
        generatedCodeDisplay.textContent = '';
        resultDisplay.textContent = 'Query failed.';
    }
    
});
