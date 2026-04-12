#!/usr/bin/env python3
"""
Update all files to use Burgundy & Gold color scheme
"""

import os
import re

# Color scheme
BURGUNDY = '#722f37'
GOLD = '#d4af37'
CREAM = '#faf8f5'
DARK_TEXT = '#3d3d3d'

# Files to update
folder = "files seperate"
units = ['unit7.html', 'unit8.html', 'unit9.html', 'unit10.html', 'unit11.html', 'unit12.html']

def update_unit(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace unit header gradient
    content = re.sub(
        r'\.unit-header \{\s*background:\s*linear-gradient\([^)]+\);',
        f'.unit-header {{\n            background: linear-gradient(135deg, {BURGUNDY} 0%, #8b3a3a 100%);',
        content
    )
    
    # Replace unit selector border
    content = re.sub(
        r'border-bottom:\s*2px\s+solid\s+#[a-fA-F0-9]+;',
        f'border-bottom: 2px solid {GOLD};',
        content
    )
    
    # Replace nav bar hover color
    content = re.sub(
        r'\.nav-links a:hover \{\s*color:\s*#[a-fA-F0-9]+;',
        f'.nav-links a:hover {{\n            color: {GOLD};',
        content
    )
    
    # Replace section header border
    content = re.sub(
        r'border-left:\s*8px\s+solid\s+#[a-fA-F0-9]+;',
        f'border-left: 8px solid {BURGUNDY};',
        content
    )
    
    # Replace outcomes box gradient
    content = re.sub(
        r'\.outcomes-box \{\s*background:\s*linear-gradient\([^)]+\);',
        f'.outcomes-box {{\n            background: linear-gradient(135deg, {BURGUNDY} 0%, #8b3a3a 100%);',
        content
    )
    
    # Replace vocab item border
    content = re.sub(
        r'border-left:\s*4px\s+solid\s+#[a-fA-F0-9]+;',
        f'border-left: 4px solid {GOLD};',
        content
    )
    
    # Replace exercise icon background
    content = re.sub(
        r'\.exercise-icon \{\s*background:\s*#[a-fA-F0-9]+;',
        f'.exercise-icon {{\n            background: {BURGUNDY};',
        content
    )
    
    # Replace quick links bar border
    content = re.sub(
        r'border-left:\s*5px\s+solid\s+#[a-fA-F0-9]+;',
        f'border-left: 5px solid {GOLD};',
        content
    )
    
    # Replace link chip colors
    content = re.sub(
        r'border-color:\s*#[a-fA-F0-9]+;\s*color:\s*#[a-fA-F0-9]+;',
        f'border-color: {BURGUNDY};\n            color: {BURGUNDY};',
        content
    )
    
    content = re.sub(
        r'\.link-chip:hover \{\s*background:\s*#[a-fA-F0-9]+;',
        f'.link-chip:hover {{\n            background: {BURGUNDY};',
        content
    )
    
    # Replace reading passage border
    content = re.sub(
        r'border-left:\s*5px\s+solid\s+#[a-fA-F0-9]+;',
        f'border-left: 5px solid {GOLD};',
        content
    )
    
    # Replace audio player border
    content = re.sub(
        r'border-left:\s*4px\s+solid\s+#[a-fA-F0-9]+;',
        f'border-left: 4px solid {GOLD};',
        content
    )
    
    # Replace resources box border
    content = re.sub(
        r'\.resources-box \{\s*background:\s*#fff3e0;\s*border:\s*2px\s+solid\s+#[a-fA-F0-9]+;',
        f'.resources-box {{\n            background: #fff8f0;\n            border: 2px solid {GOLD};',
        content
    )
    
    # Replace resources title color
    content = re.sub(
        r'\.resources-title \{\s*color:\s*#[a-fA-F0-9]+;',
        f'.resources-title {{\n            color: {BURGUNDY};',
        content
    )
    
    # Replace resources link color
    content = re.sub(
        r'\.resources-list a \{\s*color:\s*#[a-fA-F0-9]+;',
        f'.resources-list a {{\n            color: {BURGUNDY};',
        content
    )
    
    # Replace nav button hover
    content = re.sub(
        r'\.nav-btn:hover \{\s*background:\s*#[a-fA-F0-9]+;',
        f'.nav-btn:hover {{\n            background: {BURGUNDY};',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {os.path.basename(filepath)}")

# Update all units
for unit in units:
    filepath = os.path.join(folder, unit)
    try:
        update_unit(filepath)
    except Exception as e:
        print(f"Error updating {unit}: {e}")

print("\nDone!")
