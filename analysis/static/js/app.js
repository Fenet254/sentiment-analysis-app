document.addEventListener('DOMContentLoaded', function() {
    loadHistory();
    initThemeToggle();
    initConfidenceBar();
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

    // Extract confidence from message if present
    const confidenceMatch = message.match(/(\d+)%/);
    const confidence = confidenceMatch ? parseInt(confidenceMatch[1]) : 0;

    resultDiv.innerHTML = `
        <i class="fas ${icon}"></i>
        <p>${message}</p>
        <div class="confidence-bar">
            <div class="confidence-fill" id="confidence-fill"></div>
            <span class="confidence-text" id="confidence-text">${confidence}%</span>
        </div>
    `;

    // Animate confidence bar
    setTimeout(() => {
        const fill = document.getElementById("confidence-fill");
        if (fill) {
            fill.style.width = `${confidence}%`;
        }
    }, 100);

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

// Theme toggle functionality
function initThemeToggle() {
    const themeBtn = document.getElementById("theme-toggle");
    const body = document.body;

    // Load saved theme
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "dark") {
        body.classList.add("dark-mode");
        updateThemeButton(true);
    }

    themeBtn.addEventListener("click", function() {
        const isDark = body.classList.toggle("dark-mode");
        updateThemeButton(isDark);
        localStorage.setItem("theme", isDark ? "dark" : "light");
    });
}

function updateThemeButton(isDark) {
    const themeBtn = document.getElementById("theme-toggle");
    const icon = themeBtn.querySelector("i");
    const span = themeBtn.querySelector("span");

    if (isDark) {
        icon.className = "fas fa-sun";
        span.textContent = "Light Mode";
        themeBtn.classList.add("active");
    } else {
        icon.className = "fas fa-moon";
        span.textContent = "Dark Mode";
        themeBtn.classList.remove("active");
    }
}

// Initialize confidence bar
function initConfidenceBar() {
    // Reset confidence bar on page load
    const fill = document.getElementById("confidence-fill");
    const text = document.getElementById("confidence-text");
    if (fill) fill.style.width = "0%";
    if (text) text.textContent = "0%";
}

// Allow Enter key to trigger prediction
document.getElementById("text-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        predict();
    }
});
