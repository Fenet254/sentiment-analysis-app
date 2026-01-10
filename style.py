ghsgsuzzzgcgvhgggghcaggggzgggzhhh xccdcfgvhxefdftg
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    min-height: 100vh;
    color: #333;
    overflow-x: hidden;
}

.background {
    background: url('../../static/css/image.png') no-repeat center center fixed;
    background-size: cover;

    min-height: 100vh;
    position: relative;
}

.container {
    max-width: 800px;f
    margin: 0 auto;
    padding: 20px;
    position: relative;
    z-index: 1;
}

/* Header */
header {
    text-align: center;
    margin-top: 50px;
    margin-bottom: 40px;
    color: white;
}

header h1 {
    font-size: 3rem;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    animation: fadeInUp 1s ease-out;
}

header p {
    font-size: 1.2rem;
    opacity: 0.9;
    animation: fadeInUp 1.2s ease-out;
}

/* Main content */
main {
    background: rgba(255, 255, 255, 0.98);
    border-radius: 25px;
    padding: 40px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.15);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    animation: slideInUp 0.8s ease-out;
    position: relative;
    overflow: hidden;
}

main::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    border-radius: 25px 25px 0 0;
}

/* Tab Navigation */
.tab-navigation {
    display: flex;
    margin-bottom: 30px;
    border-bottom: 2px solid #e9ecef;
}

.tab-btn {
    flex: 1;
    padding: 15px 20px;
    border: none;
    background: none;
    color: #6c757d;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    border-bottom: 3px solid transparent;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.tab-btn:hover {
    color: #495057;
    background: rgba(102, 126, 234, 0.05);
}

.tab-btn.active {
    color: #667eea;
    border-bottom-color: #667eea;
    background: rgba(102, 126, 234, 0.1);
}

/* Tab Content */
.tab-content {
    display: none;
}

.tab-content.active {
    display: block;
}

/* Input section */
.input-section {
    margin-bottom: 30px;
}

.input-wrapper {
    position: relative;
}

textarea {
    width: 300px;
    height: 100px;
    width: 100%;
    height: 120px;
    padding: 20px;
    border: 2px solid #e1e5e9;
    border-radius: 15px;
    font-size: 1rem;
    resize: vertical;
    transition: all 0.3s ease;
    font-family: inherit;
    background: rgba(255, 255, 255, 0.8);
}

textarea:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    background: white;
}

.input-actions {
    display: flex;
    gap: 15px;
    margin-top: 15px;
    flex-wrap: wrap;
}

button {
    margin-top: 10px;
    padding: 10px 20px;
    padding: 12px 24px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

#predict-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

#predict-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

#clear-btn {
    background: #f8f9fa;
    color: #6c757d;
    border: 2px solid #e9ecef;
}

#clear-btn:hover {
    background: #e9ecef;
    transform: translateY(-1px);
}

/* Result section */
.result-section {
    margin-bottom: 30px;
}

.result-display {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
    animation: pulse 2s infinite;
}

.result-display i {
    font-size: 2rem;
    margin-bottom: 10px;
    display: block;
}

.result-display p {
    font-size: 1.1rem;
    font-weight: 500;
}

.result-positive {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);
}

.result-negative {
    background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    box-shadow: 0 10px 30px rgba(250, 112, 154, 0.3);
}

#result {
    margin-top: 20px;
}

/* History section */
.history-section h3 {
    color: #333;
    margin-bottom: 15px;
    font-size: 1.3rem;
}

.history-list {
    max-height: 300px;
    overflow-y: auto;
    margin-bottom: 15px;
}

.history-item {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 10px;
    transition: all 0.3s ease;
}

.history-item:hover {
    background: #e9ecef;
    transform: translateX(5px);
}

.history-item .text {
    font-style: italic;
    color: #6c757d;
    margin-bottom: 5px;
}

.history-item .prediction {
    font-weight: bold;
    font-size: 1.1rem;
}

.history-item .confidence {
    font-size: 0.9rem;
    color: #6c757d;
}

.clear-history-btn {
    background: #dc3545;
    color: white;
    width: 100%;
    justify-content: center;
}

.clear-history-btn:hover {
    background: #c82333;
}

/* Batch Processing Styles */
.batch-section {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.file-upload-section {
    margin-bottom: 20px;
}

.file-upload-area {
    border: 2px dashed #667eea;
    border-radius: 15px;
    padding: 40px 20px;
    text-align: center;
    background: rgba(102, 126, 234, 0.05);
    transition: all 0.3s ease;
    cursor: pointer;
}

.file-upload-area:hover {
    background: rgba(102, 126, 234, 0.1);
    border-color: #5a67d8;
}

.file-upload-area.dragover {
    background: rgba(102, 126, 234, 0.15);
    border-color: #5a67d8;
    transform: scale(1.02);
}

.file-upload-area i {
    font-size: 3rem;
    color: #667eea;
    margin-bottom: 15px;
    display: block;
}

.file-upload-area p {
    margin: 5px 0;
    color: #495057;
}

.file-info {
    color: #6c757d;
    font-size: 0.9rem;
}

.upload-btn {
    background: #667eea;
    color: white;
    margin-top: 15px;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.upload-btn:hover {
    background: #5a67d8;
    transform: translateY(-1px);
}

.file-info-display {
    margin-top: 15px;
    padding: 10px;
    background: #f8f9fa;
    border-radius: 10px;
    font-size: 0.9rem;
    color: #495057;
}

.batch-actions {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
}

#batch-predict-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}

#batch-predict-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

#batch-predict-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

#clear-batch-btn {
    background: #f8f9fa;
    color: #6c757d;
    border: 2px solid #e9ecef;
}

#clear-batch-btn:hover {
    background: #e9ecef;
    transform: translateY(-1px);
}

.batch-results-section h3 {
    color: #333;
    margin-bottom: 15px;
    font-size: 1.3rem;
}

.batch-results-table {
    background: white;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.batch-results-table table {
    width: 100%;
    border-collapse: collapse;
}

.batch-results-table th,
.batch-results-table td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #e9ecef;
}

.batch-results-table th {
    background: #f8f9fa;
    font-weight: 600;
    color: #495057;
}

.batch-results-table tr:hover {
    background: #f8f9fa;
}

.batch-results-table .sentiment {
    font-weight: bold;
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 0.9rem;
    text-transform: uppercase;
}

.batch-results-table .positive {
    background: #d4edda;
    color: #155724;
}

.batch-results-table .negative {
    background: #f8d7da;
    color: #721c24;
}

.batch-results-table .confidence {
    font-weight: 500;
    color: #6c757d;
}

.no-results {
    text-align: center;
    color: #6c757d;
    font-style: italic;
    padding: 40px;
}

.batch-message {
    text-align: center;
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
}

.batch-message.success {
    background: rgba(40, 167, 69, 0.1);
    color: #155724;
    border: 1px solid #c3e6cb;
}

.batch-message.error {
    background: rgba(220, 53, 69, 0.1);
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.batch-message i {
    font-size: 1.5rem;
    margin-bottom: 10px;
    display: block;
}

.text-cell {
    max-width: 300px;
    word-wrap: break-word;
    white-space: normal;
}

/* Footer */
footer {
    margin-top: 50px;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 40px 20px;
    color: white;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin-bottom: 30px;
}

.footer-section h4 {
    color: #667eea;
    margin-bottom: 15px;
    font-size: 1.2rem;
    font-weight: 600;
}

.footer-section p {
    color: #ccc;
    line-height: 1.6;
    margin-bottom: 15px;
}

.footer-section ul {
    list-style: none;
    padding: 0;
}

.footer-section li {
    color: #ccc;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.footer-section li i {
    color: #667eea;
    font-size: 0.9rem;
}

.social-links {
    display: flex;
    gap: 15px;
    margin-top: 15px;
}

.social-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    background: rgba(102, 126, 234, 0.1);
    border-radius: 50%;
    color: #667eea;
    text-decoration: none;
    transition: all 0.3s ease;
    border: 1px solid rgba(102, 126, 234, 0.3);
}

.social-link:hover {
    background: #667eea;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 20px;
    text-align: center;
}

.footer-bottom p {
    color: #aaa;
    font-size: 0.9rem;
    margin: 0;
}

/* Loading overlay */
.loading-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: none;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.loading-spinner {
    text-align: center;
    color: white;
}

.loading-spinner i {
    font-size: 3rem;
    margin-bottom: 15px;
    animation: spin 1s linear infinite;
}

.loading-spinner p {
    font-size: 1.2rem;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideInUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.02);
    }
    100% {
        transform: scale(1);
    }
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

/* Responsive design */
@media (max-width: 768px) {
    .container {
        padding: 15px;
    }

    header h1 {
        font-size: 2rem;
    }

    main {
        padding: 20px;
    }

    .input-actions {
        flex-direction: column;
    }

    button {
        width: 100%;
        justify-content: center;
    }

    .footer-content {
        grid-template-columns: 1fr;
        gap: 20px;
    }

    .social-links {
        justify-content: center;
    }
}
