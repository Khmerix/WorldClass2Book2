#!/usr/bin/env python3
"""
Add share buttons to all units in the homework portal
"""

import re

# Template for unit share buttons
unit_template = '''                <div class="homework-links">
                    <div class="homework-type">
                        <h3>📚 Vocabulary</h3>
                        <div class="link-grid">
                            <a href="unit{unit}_vocab.html" class="link-btn link-html">🌐 Online</a>
                            <a href="#" class="link-btn link-google" onclick="showGoogleForm('Unit {unit} Vocabulary')">📋 Google Form</a>
                        </div>
                        <div class="share-buttons">
                            <button class="share-btn share-copy" onclick="copyHomeworkLink('unit{unit}_vocab.html', 'Unit {unit} Vocabulary')">📋 Copy Link</button>
                            <button class="share-btn share-whatsapp" onclick="shareWhatsApp('unit{unit}_vocab.html', 'Unit {unit} Vocabulary')">💬 WhatsApp</button>
                            <button class="share-btn share-email" onclick="shareEmail('unit{unit}_vocab.html', 'Unit {unit} Vocabulary')">📧 Email</button>
                        </div>
                    </div>
                    <div class="homework-type">
                        <h3>📝 Grammar</h3>
                        <div class="link-grid">
                            <a href="unit{unit}_grammar.html" class="link-btn link-html">🌐 Online</a>
                            <a href="#" class="link-btn link-google" onclick="showGoogleForm('Unit {unit} Grammar')">📋 Google Form</a>
                        </div>
                        <div class="share-buttons">
                            <button class="share-btn share-copy" onclick="copyHomeworkLink('unit{unit}_grammar.html', 'Unit {unit} Grammar')">📋 Copy Link</button>
                            <button class="share-btn share-whatsapp" onclick="shareWhatsApp('unit{unit}_grammar.html', 'Unit {unit} Grammar')">💬 WhatsApp</button>
                            <button class="share-btn share-email" onclick="shareEmail('unit{unit}_grammar.html', 'Unit {unit} Grammar')">📧 Email</button>
                        </div>
                    </div>
                    <div class="homework-type">
                        <h3>✍️ Writing</h3>
                        <div class="link-grid">
                            <a href="unit{unit}_writing.html" class="link-btn link-html">🌐 Online</a>
                            <a href="#" class="link-btn link-google" onclick="showGoogleForm('Unit {unit} Writing')">📋 Google Form</a>
                        </div>
                        <div class="share-buttons">
                            <button class="share-btn share-copy" onclick="copyHomeworkLink('unit{unit}_writing.html', 'Unit {unit} Writing')">📋 Copy Link</button>
                            <button class="share-btn share-whatsapp" onclick="shareWhatsApp('unit{unit}_writing.html', 'Unit {unit} Writing')">💬 WhatsApp</button>
                            <button class="share-btn share-email" onclick="shareEmail('unit{unit}_writing.html', 'Unit {unit} Writing')">📧 Email</button>
                        </div>
                    </div>
                </div>
                <div class="qr-section">
                    <button class="qr-btn" onclick="showQR('Unit {unit}', 'unit{unit}')">📱 Show QR Codes</button>
                    <button class="share-all-btn" onclick="shareAllUnit({unit})">📤 Share All Unit {unit} Homework</button>
                </div>'''

def update_portal():
    with open('homework_portal.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update units 8-12
    for unit in range(8, 13):
        # Find the pattern for each unit and replace
        old_pattern = rf'''<div class="homework-links">\s*<div class="homework-type">\s*<h3>📚 Vocabulary</h3>\s*<div class="link-grid">\s*<a href="unit{unit}_vocab\.html" class="link-btn link-html">🌐 Online</a>\s*<a href="#" class="link-btn link-google" onclick="showGoogleForm\('Unit {unit} Vocabulary'\)">📋 Google Form</a>\s*</div>\s*</div>\s*<div class="homework-type">\s*<h3>📝 Grammar</h3>\s*<div class="link-grid">\s*<a href="unit{unit}_grammar\.html" class="link-btn link-html">🌐 Online</a>\s*<a href="#" class="link-btn link-google" onclick="showGoogleForm\('Unit {unit} Grammar'\)">📋 Google Form</a>\s*</div>\s*</div>\s*<div class="homework-type">\s*<h3>✍️ Writing</h3>\s*<div class="link-grid">\s*<a href="unit{unit}_writing\.html" class="link-btn link-html">🌐 Online</a>\s*<a href="#" class="link-btn link-google" onclick="showGoogleForm\('Unit {unit} Writing'\)">📋 Google Form</a>\s*</div>\s*</div>\s*</div>\s*<div class="qr-section">\s*<button class="qr-btn" onclick="showQR\('Unit {unit}', 'unit{unit}'\)">📱 Show QR Codes</button>\s*</div>'''
        
        new_html = unit_template.format(unit=unit)
        content = re.sub(old_pattern, new_html, content, flags=re.DOTALL)
    
    with open('homework_portal.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated all units with share buttons!")

if __name__ == '__main__':
    update_portal()
