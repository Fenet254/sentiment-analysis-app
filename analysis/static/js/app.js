
document.addEventListener('DOMContentLoaded', function() {
    loadHistory();
    setupFileUpload();
    setupDragAndDrop();
});

function predict() {
    const text = document.getElementById("text-input").value.trim();
    if (!text) {
        showResult("Please enter some text to analyze.", "error");
        return;
    }

    showLoading(true);

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `text=${encodeURIComponent(text)}`,
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.error) {
            showResult(data.error, "error");
        } else {
            const sentiment = data.prediction;
            const confidence = data.confidence;
            showResult(`Sentiment: ${sentiment.charAt(0).toUpperCase() + sentiment.slice(1)} (${confidence}% confidence)`, sentiment);
            loadHistory();
        }
    })
    .catch((err) => {
        console.error(err);
        showResult("An error occurred. Please try again.", "error");
    })
    .finally(() => {
        showLoading(false);
    });
}

function showResult(message, type = "neutral") {
    const resultDiv = document.getElementById("result");
    resultDiv.className = "result-display";

    if (type === "positive") {
        resultDiv.classList.add("result-positive");
    } else if (type === "negative") {
        resultDiv.classList.add("result-negative");
    }

    let icon = "fa-robot";
    if (type === "positive") icon = "fa-smile";
    else if (type === "negative") icon = "fa-frown";

    resultDiv.innerHTML = `
        <i class="fas ${icon}"></i>
        <p>${message}</p>
    `;

    // Add animation
    resultDiv.style.animation = "none";
    setTimeout(() => {
        resultDiv.style.animation = "pulse 2s infinite";
    }, 10);
}

function clearText() {
    document.getElementById("text-input").value = "";
    showResult("Your sentiment analysis result will appear here", "neutral");
}

function loadHistory() {
    fetch("/history")
    .then((response) => response.json())
    .then((data) => {
        const historyList = document.getElementById("history-list");
        if (data.history && data.history.length > 0) {
            historyList.innerHTML = data.history.map(item => `
                <div class="history-item">
                    <div class="text">"${item.text}"</div>
                    <div class="prediction ${item.prediction}">${item.prediction.charAt(0).toUpperCase() + item.prediction.slice(1)}</div>
                    <div class="confidence">${item.confidence}% confidence</div>
                </div>
            `).join("");
        } else {
            historyList.innerHTML = '<p class="no-history">No analyses yet. Try analyzing some text!</p>';
        }
    })
    .catch((err) => console.error("Error loading history:", err));
}

function clearHistory() {
    if (confirm("Are you sure you want to clear all history?")) {
        fetch("/clear_history", { method: "POST" })
        .then((response) => response.json())
        .then((data) => {
            if (data.message) {
                loadHistory();
                showResult("History cleared successfully!", "neutral");
            }
        })
        .catch((err) => console.error("Error clearing history:", err));
    }
}

function showLoading(show) {
    const overlay = document.getElementById("loading-overlay");
    overlay.style.display = show ? "flex" : "none";
}

// Tab switching functionality
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });

    // Remove active class from all buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    // Show selected tab
    document.getElementById(tabName + '-tab').classList.add('active');
    event.target.classList.add('active');
}

// File upload variables
let csvData = [];
let fileName = '';

// Setup file upload functionality
function setupFileUpload() {
    const fileInput = document.getElementById('file-input');
    const fileInfo = document.getElementById('file-info');

    fileInput.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            handleFileSelect(file);
        }
    });
}

// Setup drag and drop functionality
function setupDragAndDrop() {
    const dropArea = document.getElementById('file-upload-area');

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    function highlight(e) {
        dropArea.classList.add('dragover');
    }

    function unhighlight(e) {
        dropArea.classList.remove('dragover');
    }

    dropArea.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;

        if (files.length > 0) {
            handleFileSelect(files[0]);
        }
    }
}

// Handle file selection
function handleFileSelect(file) {
    // Validate file type
    if (!file.name.toLowerCase().endsWith('.csv')) {
        showBatchResult('Please select a valid CSV file.', 'error');
        return;
    }

    // Validate file size (5MB limit)
    if (file.size > 5 * 1024 * 1024) {
        showBatchResult('File size must be less than 5MB.', 'error');
        return;
    }

    fileName = file.name;
    parseCSV(file);
}

// Parse CSV file
function parseCSV(file) {
    const reader = new FileReader();

    reader.onload = function(e) {
        const csv = e.target.result;
        const lines = csv.split('\n').filter(line => line.trim() !== '');

        if (lines.length < 2) {
            showBatchResult('CSV file must contain at least a header row and one data row.', 'error');
            return;
        }

        const headers = lines[0].split(',').map(h => h.trim().toLowerCase());

        // Check if 'text' column exists
        const textIndex = headers.indexOf('text');
        if (textIndex === -1) {
            showBatchResult('CSV file must contain a "text" column.', 'error');
            return;
        }

        // Parse data rows
        csvData = [];
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',');
            if (values.length > textIndex && values[textIndex].trim()) {
                csvData.push(values[textIndex].trim());
            }
        }

        if (csvData.length === 0) {
            showBatchResult('No valid text data found in CSV file.', 'error');
            return;
        }

        // Update UI
        document.getElementById('file-info').innerHTML = `
            <strong>File:</strong> ${fileName}<br>
            <strong>Records:</strong> ${csvData.length}
        `;

        document.getElementById('batch-predict-btn').disabled = false;
        showBatchResult(`Successfully loaded ${csvData.length} records from ${fileName}. Click "Analyze Batch" to process.`, 'success');
    };

    reader.onerror = function() {
        showBatchResult('Error reading file.', 'error');
    };

    reader.readAsText(file);
}

// Batch prediction function
function batchPredict() {
    if (csvData.length === 0) {
        showBatchResult('No data to analyze. Please upload a CSV file first.', 'error');
        return;
    }

    showLoading(true);
    document.getElementById('batch-predict-btn').disabled = true;

    fetch('/batch_predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texts: csvData }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showBatchResult(data.error, 'error');
        } else {
            displayBatchResults(data.results);
            showBatchResult(`Successfully analyzed ${data.results.length} records!`, 'success');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showBatchResult('An error occurred during batch analysis.', 'error');
    })
    .finally(() => {
        showLoading(false);
        document.getElementById('batch-predict-btn').disabled = false;
    });
}

// Display batch results in table
function displayBatchResults(results) {
    const resultsDiv = document.getElementById('batch-results');

    if (results.length === 0) {
        resultsDiv.innerHTML = '<p class="no-results">No results to display</p>';
        return;
    }

    let tableHTML = `
        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Text</th>
                    <th>Sentiment</th>
                    <th>Confidence</th>
                </tr>
            </thead>
            <tbody>
    `;

    results.forEach((result, index) => {
        const sentimentClass = result.prediction.toLowerCase();
        tableHTML += `
            <tr>
                <td>${index + 1}</td>
                <td class="text-cell">${result.text}</td>
                <td><span class="sentiment ${sentimentClass}">${result.prediction.charAt(0).toUpperCase() + result.prediction.slice(1)}</span></td>
                <td class="confidence">${result.confidence}%</td>
            </tr>
        `;
    });

    tableHTML += '</tbody></table>';
    resultsDiv.innerHTML = tableHTML;
}

// Show batch result message
function showBatchResult(message, type = 'neutral') {
    const resultsDiv = document.getElementById('batch-results');

    let icon = 'fa-info-circle';
    if (type === 'success') icon = 'fa-check-circle';
    else if (type === 'error') icon = 'fa-exclamation-triangle';

    resultsDiv.innerHTML = `
        <div class="batch-message ${type}">
            <i class="fas ${icon}"></i>
            <p>${message}</p>
        </div>
    `;
}

// Clear batch data
function clearBatch() {
    csvData = [];
    fileName = '';
    document.getElementById('file-input').value = '';
    document.getElementById('file-info').innerHTML = '';
    document.getElementById('batch-results').innerHTML = '<p class="no-results">Upload a CSV file and click "Analyze Batch" to see results</p>';
    document.getElementById('batch-predict-btn').disabled = true;
}

// Allow Enter key to trigger prediction
document.getElementById("text-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        predict();
    }
});
