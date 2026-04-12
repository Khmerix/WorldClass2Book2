#!/usr/bin/env python3
"""
Add Button Interaction JavaScript to HTML files
"""

import os
import re

# JavaScript for ripple effect and button interactions
BUTTON_JS = """
    <!-- 3D Button Interactions -->
    <script>
        // Ripple effect for buttons
        document.addEventListener('click', function(e) {
            const btn = e.target.closest('.btn-ripple, .btn-3d, .nav-bar button');
            if (!btn) return;
            
            const ripple = document.createElement('span');
            ripple.className = 'ripple';
            
            const rect = btn.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            
            btn.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
        
        // Magnetic button effect
        document.querySelectorAll('.btn-3d, .audio-btn, .play-btn').forEach(btn => {
            btn.addEventListener('mousemove', function(e) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                this.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px)`;
            });
            
            btn.addEventListener('mouseleave', function() {
                this.style.transform = '';
            });
        });
    </script>
"""

def find_files(root_dir):
    """Find all HTML files recursively"""
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                html_files.append(os.path.join(dirpath, filename))
    return html_files

def inject_button_js(filepath):
    """Inject button JS before the closing </body> tag"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if already has button JS
        if 'btn-ripple' in content and 'ripple.remove()' in content:
            print(f"Skipping {os.path.basename(filepath)} - already has button JS")
            return
        
        # Insert before closing body tag
        if '</body>' in content:
            content = content.replace('</body>', BUTTON_JS + '\n</body>')
        elif '</html>' in content:
            content = content.replace('</html>', BUTTON_JS + '\n</html>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# Main execution
root_dir = '.'
html_files = find_files(root_dir)

print(f"Found {len(html_files)} HTML files")
print("Adding button interaction JavaScript...\n")

for filepath in html_files:
    inject_button_js(filepath)

print("\nDone! Button interactions added to all files.")
