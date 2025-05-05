const form = document.getElementById('query-form');
const generatedCodeDisplay = document.getElementById('generated-code');
const resultDisplay = document.getElementById('result');
const recentDiv = document.getElementById('recent-queries');
const clearButton = document.getElementById('clear-history');

function renderRecentQueries() {
    const history = JSON.parse(localStorage.getItem('queryHistory')) || [];
    recentDiv.innerHTML = '';

    if (history.length === 0) {
        recentDiv.innerHTML = '<p>No recent queries yet.</p>';
        return;
    }

    history.reverse().forEach(entry => {
        const newEntry = document.createElement('div');
        newEntry.classList.add('mb-3', 'p-2', 'border', 'rounded', 'bg-light');
        newEntry.innerHTML = `
            <strong>Query:</strong> ${entry.query}<br>
            <strong>Code:</strong> <pre>${entry.code}</pre>
            <strong>Result:</strong> <pre>${entry.result}</pre>
        `;
        recentDiv.appendChild(newEntry);
    });
}

function addToHistory(query, code, result) {
    const history = JSON.parse(localStorage.getItem('queryHistory')) || [];
    history.push({ query, code, result });

    // Limit to last 10 entries
    if (history.length > 10) {
        history.shift();
    }

    localStorage.setItem('queryHistory', JSON.stringify(history));
    renderRecentQueries();
}

// Clear history button
clearButton.addEventListener('click', () => {
    localStorage.removeItem('queryHistory');
    renderRecentQueries();
});

// Load history on page load
window.addEventListener('load', renderRecentQueries);

// ---- Form submission ----
form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById('file');
    const queryInput = document.getElementById('query');
    const modeInput = document.querySelector('input[name="mode"]:checked');

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

        // Save to history
        addToHistory(
            queryInput.value,
            queryResult.generated_code || 'No code',
            queryResult.result || 'No result'
        );
    } else {
        generatedCodeDisplay.textContent = '';
        resultDisplay.textContent = 'Query failed.';
    }
});
