#!/usr/bin/env python3
"""
Add Homework navigation to units 8-12
"""

import re

# The new navigation HTML pattern
nav_pattern = '''        <!-- Navigation -->
        <nav class="nav-bar">
            <div class="nav-links">
                <a href="#vocabulary">Vocabulary</a>
                <a href="#grammar">Grammar</a>
                <a href="#listening">Listening</a>
                <a href="#reading">Reading</a>
                <a href="#writing">Writing</a>
                <a href="#speaking">Speaking</a>
                <a href="#video">Video</a>
                <a href="#resources">Resources</a>
                <a href="book2b_reference.html">Reference</a>
            </div>
            <div style="display: flex; gap: 10px; align-items: center;">
                <div class="homework-dropdown" style="position: relative;">
                    <button class="btn-3d btn-sm" onclick="toggleHomeworkMenu('hw-menu-{unit}')" style="background: linear-gradient(145deg, #d4af37 0%, #e5c76b 100%); color: #722f37;">📝 Homework ▼</button>
                    <div id="hw-menu-{unit}" class="homework-menu" style="display: none; position: absolute; top: 100%; right: 0; margin-top: 10px; background: white; border-radius: 8px; box-shadow: 0 8px 20px rgba(0,0,0,0.2); min-width: 150px; z-index: 1000; overflow: hidden;">
                        <a href="homework/unit{unit}_vocab.html" target="_blank" style="display: block; padding: 12px 20px; color: #722f37; text-decoration: none; font-weight: 600; border-bottom: 1px solid #eee; transition: all 0.3s;">📚 Vocabulary</a>
                        <a href="homework/unit{unit}_grammar.html" target="_blank" style="display: block; padding: 12px 20px; color: #722f37; text-decoration: none; font-weight: 600; border-bottom: 1px solid #eee; transition: all 0.3s;">📝 Grammar</a>
                        <a href="homework/unit{unit}_writing.html" target="_blank" style="display: block; padding: 12px 20px; color: #722f37; text-decoration: none; font-weight: 600; transition: all 0.3s;">✍️ Writing</a>
                    </div>
                </div>
                <button class="print-btn" onclick="window.print()">🖨️ Print</button>
            </div>
        </nav>'''

# The CSS to add
css_addition = '''        /* Homework Menu Styles */
        .homework-menu a:hover {
            background: #f9f5f0;
            padding-left: 25px;
        }
        
        body.dark-mode .homework-menu {
            background: #2d2d2d !important;
            border: 1px solid #444;
        }
        
        body.dark-mode .homework-menu a {
            color: #d4af37 !important;
            border-bottom-color: #444 !important;
        }
        
        body.dark-mode .homework-menu a:hover {
            background: #3d3d3d !important;
        }
        '''

# The JS to add
js_addition = '''        // Homework menu toggle
        function toggleHomeworkMenu(menuId) {
            const menu = document.getElementById(menuId);
            if (menu.style.display === 'none') {
                menu.style.display = 'block';
            } else {
                menu.style.display = 'none';
            }
        }
        
        // Close homework menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.homework-dropdown')) {
                document.querySelectorAll('.homework-menu').forEach(menu => {
                    menu.style.display = 'none';
                });
            }
        });
'''

# Old navigation pattern to find and replace
old_nav_pattern = r'''        <!-- Navigation -->
        <nav class="nav-bar">
            <div class="nav-links">
                <a href="#vocabulary">Vocabulary</a>
                <a href="#grammar">Grammar</a>
                <a href="#listening">Listening</a>
                <a href="#reading">Reading</a>
                <a href="#writing">Writing</a>
                <a href="#speaking">Speaking</a>
                <a href="#video">Video</a>
                <a href="#resources">Resources</a>
                <a href="book2b_reference.html">Reference</a>
            </div>
            <div>\s*
                <button class="print-btn" onclick="window.print()">🖨️ Print</button>\s*
            </div>
        </nav>'''

for unit_num in range(8, 13):
    filename = f'files seperate/unit{unit_num}.html'
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if already has homework dropdown
        if 'hw-menu-' in content:
            print(f"Skipping unit{unit_num}.html - already has homework menu")
            continue
        
        # Replace navigation
        new_nav = nav_pattern.format(unit=unit_num)
        content = re.sub(old_nav_pattern, new_nav, content, flags=re.DOTALL)
        
        # Add CSS before body.dark-mode .nav-bar button.active
        if '/* Homework Menu Styles */' not in content:
            content = content.replace(
                'body.dark-mode .nav-bar button.active {',
                css_addition + '        body.dark-mode .nav-bar button.active {'
            )
        
        # Add JS before the magnetic button effect comment
        if '// Homework menu toggle' not in content:
            content = content.replace(
                '// Magnetic button effect',
                js_addition + '        // Magnetic button effect'
            )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated unit{unit_num}.html")
        
    except Exception as e:
        print(f"Error processing unit{unit_num}.html: {e}")

print("\nDone! Homework navigation added to all units.")
