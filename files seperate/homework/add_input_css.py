#!/usr/bin/env python3
"""
Add proper input field CSS to all homework files
"""

import os

INPUT_CSS = '''
        /* Input field styles for student answers */
        .answer-input {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #d4af37;
            border-radius: 8px;
            font-size: 15px;
            font-family: inherit;
            background: white;
            margin-top: 8px;
            transition: all 0.3s;
            box-sizing: border-box;
        }
        
        .answer-input:focus {
            outline: none;
            border-color: #722f37;
            box-shadow: 0 0 0 4px rgba(114, 47, 55, 0.1);
        }
        
        .answer-input::placeholder {
            color: #999;
            font-style: italic;
        }
        
        .answer-textarea {
            width: 100%;
            min-height: 120px;
            padding: 12px 15px;
            border: 2px solid #d4af37;
            border-radius: 8px;
            font-size: 15px;
            font-family: inherit;
            background: white;
            margin-top: 8px;
            resize: vertical;
            transition: all 0.3s;
            box-sizing: border-box;
        }
        
        .answer-textarea:focus {
            outline: none;
            border-color: #722f37;
            box-shadow: 0 0 0 4px rgba(114, 47, 55, 0.1);
        }
        
        .answer-textarea::placeholder {
            color: #999;
            font-style: italic;
        }
        
        .sentence-input {
            border: none;
            border-bottom: 2px solid #722f37;
            background: #f9f5f0;
            font-size: 14px;
            padding: 8px 12px;
            min-width: 200px;
            font-family: inherit;
            border-radius: 4px;
        }
        
        .sentence-input:focus {
            outline: none;
            border-bottom-color: #d4af37;
            background: #fff9e6;
        }
        
        .match-input {
            width: 50px;
            text-align: center;
            border: 2px solid #722f37;
            border-radius: 6px;
            font-size: 18px;
            font-weight: bold;
            padding: 8px;
            text-transform: uppercase;
            background: white;
        }
        
        .match-input:focus {
            outline: none;
            border-color: #d4af37;
            box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.3);
        }
'''

def add_css_to_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if CSS already added
        if '.answer-input {' in content and 'width: 100%' in content:
            print(f"CSS already in {os.path.basename(filepath)}")
            return
        
        # Find the style section and add CSS before </style>
        if '</style>' in content:
            content = content.replace('</style>', INPUT_CSS + '\n        </style>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Added CSS to {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error: {os.path.basename(filepath)}: {e}")

# Process all homework files
homework_dir = '.'
for filename in os.listdir(homework_dir):
    if filename.startswith('unit') and filename.endswith('.html'):
        if 'portal' not in filename and 'template' not in filename:
            add_css_to_file(os.path.join(homework_dir, filename))

print("\nDone! Added input field CSS to all homework files.")
