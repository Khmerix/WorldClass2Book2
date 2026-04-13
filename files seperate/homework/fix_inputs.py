#!/usr/bin/env python3
"""
Fix homework files - replace answer-line divs with actual input fields
"""

import os
import re

# New CSS to add (ensure inputs are visible)
INPUT_CSS = '''
        /* Input field styles */
        .answer-input {
            width: 100%;
            padding: 12px;
            border: 2px solid #d4af37;
            border-radius: 6px;
            font-size: 14px;
            font-family: inherit;
            background: white;
            margin-top: 8px;
            transition: all 0.3s;
        }
        
        .answer-input:focus {
            outline: none;
            border-color: #722f37;
            box-shadow: 0 0 0 3px rgba(114, 47, 55, 0.1);
        }
        
        .answer-textarea {
            width: 100%;
            min-height: 100px;
            padding: 12px;
            border: 2px solid #d4af37;
            border-radius: 6px;
            font-size: 14px;
            font-family: inherit;
            background: white;
            margin-top: 8px;
            resize: vertical;
            transition: all 0.3s;
        }
        
        .answer-textarea:focus {
            outline: none;
            border-color: #722f37;
            box-shadow: 0 0 0 3px rgba(114, 47, 55, 0.1);
        }
        
        .sentence-input {
            border: none;
            border-bottom: 2px solid #722f37;
            background: transparent;
            font-size: 14px;
            padding: 5px;
            min-width: 150px;
            font-family: inherit;
        }
        
        .sentence-input:focus {
            outline: none;
            border-bottom-color: #d4af37;
        }
        
        .match-input {
            width: 40px;
            text-align: center;
            border: 2px solid #722f37;
            border-radius: 4px;
            font-size: 16px;
            font-weight: bold;
            padding: 5px;
            text-transform: uppercase;
        }
        
        .match-input:focus {
            outline: none;
            border-color: #d4af37;
            box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.3);
        }
'''

def fix_homework_file(filepath):
    """Replace answer divs with actual input fields"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if already has proper inputs
        if 'class="answer-input"' in content and 'convertToInputs' not in content:
            print(f"Skipping {os.path.basename(filepath)} - already has input fields")
            return
        
        # Remove the old convertToInputs function if present
        content = re.sub(
            r'function convertToInputs\(\) \{[^}]+\}',
            '',
            content,
            flags=re.DOTALL
        )
        
        # Remove the call to convertToInputs
        content = re.sub(
            r'convertToInputs\(\);',
            '',
            content
        )
        
        # Replace .answer-line divs with input fields (for short answers)
        # Pattern: <div class="answer-line"></div> or <div class="answer-line" style="..."></div>
        def replace_answer_line(match):
            style = match.group(1) or ''
            return f'<input type="text" class="answer-input" placeholder="Type your answer here..." style="{style}">'
        
        content = re.sub(
            r'<div class="answer-line"([^>]*)></div>',
            replace_answer_line,
            content,
            flags=re.DOTALL
        )
        
        # Replace .answer-space divs with textareas (for long answers)
        def replace_answer_space(match):
            style = match.group(1) or ''
            return f'<textarea class="answer-textarea" placeholder="Type your answer here..." style="{style}"></textarea>'
        
        content = re.sub(
            r'<div class="answer-space"([^>]*)></div>',
            replace_answer_space,
            content,
            flags=re.DOTALL
        )
        
        # Replace inline answer spaces in sentence completion
        # Pattern: ___________________ or similar underscores
        content = re.sub(
            r'_{3,}',
            '<input type="text" class="sentence-input" placeholder="answer">',
            content
        )
        
        # Replace answer blanks in matching exercises
        # Pattern: <span style="...border-bottom...">___</span> or similar
        content = re.sub(
            r'<span[^>]*border-bottom[^>]*>_{1,3}</span>',
            '<input type="text" class="match-input" maxlength="1" placeholder="?">',
            content
        )
        
        # Add the new CSS before </style>
        if '.answer-input' not in content:
            content = content.replace('</style>', INPUT_CSS + '\n        </style>')
        
        # Update saveProgress to use new selectors
        content = re.sub(
            r"document\.querySelectorAll\('input\[type=\"text\"\], \.answer-input-field'\)",
            "document.querySelectorAll('.answer-input, .sentence-input, .match-input')",
            content
        )
        
        content = re.sub(
            r"document\.querySelectorAll\('textarea, \.answer-textarea'\)",
            "document.querySelectorAll('.answer-textarea')",
            content
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")

# Process all homework files
homework_dir = '.'
for filename in os.listdir(homework_dir):
    if filename.startswith('unit') and filename.endswith('.html') and 'portal' not in filename and 'template' not in filename:
        fix_homework_file(os.path.join(homework_dir, filename))

print("\n✅ Done! All homework files now have working input fields.")
print("\nStudents can now:")
print("- Click on answer boxes and type directly")
print("- Answers are saved automatically")
print("- Submit via email, PDF, or print")
