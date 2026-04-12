#!/usr/bin/env python3
"""
Fix book2b_reference.html to match the burgundy/gold theme and format of other units
"""

import re

filepath = 'files seperate/book2b_reference.html'

try:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Remove the unit selector section (the entire div with class unit-selector)
    content = re.sub(
        r'<div class="unit-selector">.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Also remove the standalone unit-selector div if it exists differently
    content = re.sub(
        r'<div class="unit-selector">.*?<!-- Unit Selector -->',
        '<!-- Unit Selector -->',
        content,
        flags=re.DOTALL
    )
    
    # 2. Update body background color
    content = content.replace('background: #f5f5f5;', 'background: #faf8f5;')
    
    # 3. Update purple colors to burgundy/gold
    color_map = {
        '#7c4dff': '#d4af37',  # Accent purple -> Gold
        '#673ab7': '#722f37',  # Purple -> Burgundy
        '#311b92': '#5c1a1a',  # Dark purple -> Dark burgundy
        '#4527a0': '#722f37',  # Another purple shade
    }
    
    for old_color, new_color in color_map.items():
        content = content.replace(old_color, new_color)
    
    # 4. Update unit-header gradient
    content = content.replace(
        'background: linear-gradient(135deg, #5c1a1a 0%, #722f37 100%);',
        'background: linear-gradient(135deg, #722f37 0%, #8b3a3a 100%);'
    )
    
    # 5. Update nav-bar background
    content = content.replace(
        'background: #2c3e50;',
        'background: #722f37;'
    )
    
    # 6. Update nav-links a background
    content = content.replace(
        "background: #34495e;",
        "background: linear-gradient(145deg, #faf8f5 0%, #f0ebe3 100%);"
    )
    content = content.replace(
        "color: white;\n            text-decoration: none;\n            font-weight: 500;\n            transition: all 0.3s;\n            padding: 8px 16px;\n            border-radius: 20px;\n            background: linear-gradient(145deg, #faf8f5 0%, #f0ebe3 100%);",
        "color: #722f37;\n            text-decoration: none;\n            font-weight: 600;\n            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);\n            padding: 10px 20px;\n            border-radius: 25px;\n            background: linear-gradient(145deg, #faf8f5 0%, #f0ebe3 100%);\n            border: 2px solid transparent;\n            box-shadow: 0 2px 4px rgba(114, 47, 55, 0.1), inset 0 1px 0 rgba(255,255,255,0.8);"
    )
    
    # 7. Update nav-links a hover
    content = content.replace(
        'background: #d4af37;',
        'background: linear-gradient(145deg, #722f37 0%, #8b3a3a 100%); color: #fff; border-color: #d4af37; transform: translateY(-2px); box-shadow: 0 6px 12px rgba(114, 47, 55, 0.25), 0 0 0 3px rgba(212, 175, 55, 0.2);'
    )
    
    # 8. Update nav-links a active
    content = content.replace(
        "border-color: white;",
        "border-color: #d4af37; box-shadow: 0 4px 8px rgba(114, 47, 55, 0.3), 0 0 0 3px rgba(212, 175, 55, 0.3), inset 0 2px 4px rgba(0,0,0,0.2);"
    )
    
    # 9. Update toggle-btn
    content = content.replace(
        "background: #34495e;\n            color: white;\n            border: 2px solid transparent;\n            padding: 8px 20px;\n            border-radius: 20px;\n            cursor: pointer;\n            font-weight: bold;\n            transition: all 0.3s;",
        "background: linear-gradient(145deg, #faf8f5 0%, #f0ebe3 100%);\n            color: #722f37;\n            border: 2px solid transparent;\n            padding: 10px 20px;\n            border-radius: 25px;\n            cursor: pointer;\n            font-weight: 600;\n            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);\n            box-shadow: 0 2px 4px rgba(114, 47, 55, 0.1), inset 0 1px 0 rgba(255,255,255,0.8);"
    )
    
    # 10. Update toggle-btn.active
    content = content.replace(
        "background: #722f37;\n            border-color: #d4af37;",
        "background: linear-gradient(145deg, #722f37 0%, #5c1a1a 100%);\n            border-color: #d4af37;\n            color: #d4af37;"
    )
    
    # 11. Update toggle-btn hover
    content = content.replace(
        'background: #44596e;',
        'background: linear-gradient(145deg, #722f37 0%, #8b3a3a 100%); color: #fff; border-color: #d4af37; transform: translateY(-2px);'
    )
    
    # 12. Update section-header
    content = content.replace(
        'background: #5c1a1a;',
        'background: linear-gradient(135deg, #722f37 0%, #8b3a3a 100%);'
    )
    content = content.replace(
        'border-left: 8px solid #d4af37;',
        'border-left: 8px solid #d4af37; border-bottom: 3px solid #d4af37;'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")
    print("Changes made:")
    print("- Removed unit selector section")
    print("- Updated all purple colors to burgundy/gold")
    print("- Updated navigation styling to match other units")
    print("- Updated buttons with 3D effects")
    print("- Updated section headers")
    
except Exception as e:
    print(f"Error: {e}")
