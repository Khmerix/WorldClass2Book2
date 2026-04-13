#!/usr/bin/env python3
"""
Convert homework HTML files to interactive forms with auto-save and submission
"""

import os
import re

# JavaScript and HTML to add
SUBMIT_BAR_HTML = '''
<!-- Submit Bar -->
<div class="submit-bar">
    <div class="left-group">
        <div class="status-indicator">
            <div class="status-dot"></div>
            <span>Auto-saving...</span>
        </div>
        <div class="timer" id="timer">00:00</div>
    </div>
    <div style="display: flex; gap: 10px;">
        <button class="btn-secondary" onclick="saveProgress()">💾 Save</button>
        <button class="btn-submit" onclick="showSubmitOptions()">📤 Submit</button>
    </div>
</div>

<!-- Auto-save toast -->
<div class="autosave-toast" id="autosaveToast">
    <span>✓</span>
    <span>Progress saved!</span>
</div>

<!-- Submit modal -->
<div class="submit-modal" id="submitModal" onclick="closeSubmitModal(event)">
    <div class="submit-modal-content">
        <h2>📤 Submit Your Homework</h2>
        <div class="submit-options">
            <div class="submit-option" onclick="submitByEmail()">
                <div class="submit-option-icon">📧</div>
                <div class="submit-option-title">Send by Email</div>
                <div class="submit-option-desc">Opens your email with homework attached</div>
            </div>
            <div class="submit-option" onclick="downloadPDF()">
                <div class="submit-option-icon">📄</div>
                <div class="submit-option-title">Download PDF</div>
                <div class="submit-option-desc">Save as PDF to submit later</div>
            </div>
            <div class="submit-option" onclick="printHomework()">
                <div class="submit-option-icon">🖨️</div>
                <div class="submit-option-title">Print</div>
                <div class="submit-option-desc">Print and hand in physically</div>
            </div>
        </div>
        <button class="btn-secondary" onclick="closeSubmitModalDirect()" style="width: 100%; margin-top: 20px;">Cancel</button>
    </div>
</div>
'''

INTERACTIVE_JS = '''
<script>
// ===== AUTO-SAVE FUNCTIONALITY =====
const STORAGE_KEY = 'homework_' + window.location.pathname.replace(/\\/g, '_');
let startTime = Date.now();
let timerInterval;

document.addEventListener('DOMContentLoaded', function() {
    loadProgress();
    startTimer();
    setupAutoSave();
    convertToInputs();
});

function setupAutoSave() {
    setInterval(() => { saveProgress(); }, 30000);
}

function convertToInputs() {
    // Convert answer-line divs to input fields
    document.querySelectorAll('.answer-line').forEach((el, index) => {
        const input = document.createElement('input');
        input.type = 'text';
        input.className = 'answer-input-field';
        input.placeholder = 'Type your answer here...';
        input.dataset.fieldId = 'answer_' + index;
        input.style.cssText = 'width: 100%; padding: 8px; border: none; background: transparent; font-size: 14px;';
        el.innerHTML = '';
        el.appendChild(input);
    });
    
    // Convert long answer spaces to textareas
    document.querySelectorAll('.answer-space').forEach((el, index) => {
        const textarea = document.createElement('textarea');
        textarea.className = 'answer-textarea';
        textarea.placeholder = 'Type your answer here...';
        textarea.dataset.fieldId = 'space_' + index;
        textarea.style.cssText = 'width: 100%; min-height: 60px; padding: 8px; border: none; background: transparent; font-size: 14px; resize: vertical;';
        el.innerHTML = '';
        el.appendChild(textarea);
    });
}

function saveProgress() {
    const data = {};
    
    // Save text inputs
    document.querySelectorAll('input[type="text"], .answer-input-field').forEach((input, index) => {
        data['field_' + index] = input.value;
    });
    
    // Save textareas
    document.querySelectorAll('textarea, .answer-textarea').forEach((textarea, index) => {
        data['textarea_' + index] = textarea.value;
    });
    
    // Save student info
    document.querySelectorAll('.student-info input').forEach((input, index) => {
        data['student_' + index] = input.value;
    });
    
    data.timestamp = new Date().toISOString();
    data.timeSpent = Date.now() - startTime;
    
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    showToast();
}

function loadProgress() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
        const data = JSON.parse(saved);
        
        // Load text inputs
        document.querySelectorAll('input[type="text"], .answer-input-field').forEach((input, index) => {
            if (data['field_' + index]) {
                input.value = data['field_' + index];
            }
        });
        
        // Load textareas
        document.querySelectorAll('textarea, .answer-textarea').forEach((textarea, index) => {
            if (data['textarea_' + index]) {
                textarea.value = data['textarea_' + index];
            }
        });
        
        // Load student info
        document.querySelectorAll('.student-info input').forEach((input, index) => {
            if (data['student_' + index]) {
                input.value = data['student_' + index];
            }
        });
        
        if (data.timeSpent) {
            startTime = Date.now() - data.timeSpent;
        }
    }
}

function showToast() {
    const toast = document.getElementById('autosaveToast');
    toast.style.display = 'flex';
    setTimeout(() => { toast.style.display = 'none'; }, 2000);
}

function startTimer() {
    timerInterval = setInterval(() => {
        const elapsed = Math.floor((Date.now() - startTime) / 1000);
        const minutes = Math.floor(elapsed / 60).toString().padStart(2, '0');
        const seconds = (elapsed % 60).toString().padStart(2, '0');
        document.getElementById('timer').textContent = minutes + ':' + seconds;
    }, 1000);
}

function showSubmitOptions() {
    saveProgress();
    document.getElementById('submitModal').style.display = 'flex';
}

function closeSubmitModal(event) {
    if (event.target === document.getElementById('submitModal')) {
        document.getElementById('submitModal').style.display = 'none';
    }
}

function closeSubmitModalDirect() {
    document.getElementById('submitModal').style.display = 'none';
}

function submitByEmail() {
    saveProgress();
    const subject = 'Homework Submission - ' + document.title;
    const studentName = document.querySelector('.student-info input')?.value || '[Not filled]';
    const body = 'Student Name: ' + studentName + '\\n\\nCompleted homework is ready for submission.\\n\\nTime spent: ' + document.getElementById('timer').textContent + '\\n\\n[Please print to PDF and attach to this email]';
    window.location.href = 'mailto:teacher@school.edu?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    setTimeout(() => { window.print(); }, 500);
}

function downloadPDF() {
    saveProgress();
    window.print();
}

function printHomework() {
    saveProgress();
    window.print();
}

window.addEventListener('beforeunload', function(e) {
    saveProgress();
});
</script>
'''

INTERACTIVE_CSS = '''
        /* Interactive Form Styles */
        input[type="text"], textarea, select {
            width: 100%;
            padding: 8px 12px;
            border: 2px solid #e0d5c8;
            border-radius: 6px;
            font-size: 14px;
            font-family: inherit;
            transition: border-color 0.3s, box-shadow 0.3s;
            background: white;
        }
        
        input[type="text"]:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #722f37;
            box-shadow: 0 0 0 3px rgba(114, 47, 55, 0.1);
        }
        
        textarea {
            resize: vertical;
            min-height: 80px;
        }
        
        .answer-input-field, .answer-textarea {
            width: 100%;
            padding: 10px;
            border: none;
            background: transparent;
            font-size: 14px;
            font-family: inherit;
        }
        
        .answer-textarea {
            resize: vertical;
            min-height: 60px;
        }
        
        /* Submit bar */
        .submit-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 15px 20px;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
            gap: 15px;
        }
        
        .submit-bar .left-group {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        
        .status-indicator {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            color: #666;
        }
        
        .status-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #4CAF50;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        .timer {
            font-family: 'Courier New', monospace;
            font-weight: bold;
            color: #722f37;
            font-size: 14px;
        }
        
        .btn-submit {
            background: linear-gradient(145deg, #722f37 0%, #5c1a1a 100%);
            color: #d4af37;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-weight: 700;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .btn-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(114, 47, 55, 0.3);
        }
        
        .btn-secondary {
            background: #f0f0f0;
            color: #333;
            border: 2px solid #ddd;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: 600;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-secondary:hover {
            background: #e0e0e0;
        }
        
        .autosave-toast {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #4CAF50;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            display: none;
            align-items: center;
            gap: 10px;
            z-index: 200;
            animation: slideIn 0.3s ease;
        }
        
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        .submit-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.6);
            z-index: 300;
            justify-content: center;
            align-items: center;
        }
        
        .submit-modal-content {
            background: white;
            padding: 30px;
            border-radius: 12px;
            max-width: 500px;
            width: 90%;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        
        .submit-modal-content h2 {
            color: #722f37;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .submit-options {
            display: grid;
            gap: 15px;
        }
        
        .submit-option {
            padding: 20px;
            border: 2px solid #e0d5c8;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            text-align: center;
        }
        
        .submit-option:hover {
            border-color: #722f37;
            background: #f9f5f0;
        }
        
        .submit-option-icon {
            font-size: 32px;
            margin-bottom: 10px;
        }
        
        .submit-option-title {
            font-weight: 700;
            color: #722f37;
            margin-bottom: 5px;
        }
        
            font-size: 13px;
            color: #666;
        }
        
        body {
            padding-bottom: 80px;
        }
        
        @media print {
            .submit-bar, .autosave-toast, .submit-modal { display: none !important; }
            body { padding-bottom: 0; }
            .container { box-shadow: none; }
            input, textarea { border: 1px solid #ccc !important; }
        }
        
        @media (max-width: 600px) {
            .submit-bar {
                flex-direction: column;
                padding: 10px;
            }
            .submit-bar .left-group {
                width: 100%;
                justify-content: center;
            }
            .btn-submit {
                width: 100%;
                justify-content: center;
            }
        }
'''

def update_homework_file(filepath):
    """Update a homework file with interactive features"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Skip if already updated
        if 'saveProgress' in content:
            print(f"Skipping {os.path.basename(filepath)} - already interactive")
            return
        
        # Add CSS before </style>
        if '</style>' in content:
            content = content.replace('</style>', INTERACTIVE_CSS + '\n        </style>')
        
        # Add submit bar before </body>
        if '</body>' in content:
            content = content.replace('</body>', SUBMIT_BAR_HTML + INTERACTIVE_JS + '\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# Process all homework files
homework_dir = '.'
for filename in os.listdir(homework_dir):
    if filename.startswith('unit') and filename.endswith('.html') and 'portal' not in filename and 'template' not in filename:
        update_homework_file(os.path.join(homework_dir, filename))

print("\nDone! All homework files are now interactive.")
print("\nFeatures added:")
print("- Auto-save every 30 seconds")
print("- Work timer")
print("- Submit options (Email, PDF, Print)")
print("- Input fields for typing answers")
print("- Progress restoration on page reload")
