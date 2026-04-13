#!/usr/bin/env python3
"""
Add Google Classroom share buttons to all units
"""

with open('homework_portal.html', 'r', encoding='utf-8') as f:
    content = f.read()

# For each unit 8-12, update the share buttons
for unit in range(8, 13):
    for hw_type in ['vocab', 'grammar', 'writing']:
        # Capitalize the homework type for display
        hw_display = hw_type.capitalize()
        if hw_type == 'vocab':
            hw_display = 'Vocabulary'
        
        old = f"""                        <div class="share-buttons">
                            <button class="share-btn share-copy" onclick="copyHomeworkLink('unit{unit}_{hw_type}.html', 'Unit {unit} {hw_display}')">📋 Copy Link</button>
                            <button class="share-btn share-whatsapp" onclick="shareWhatsApp('unit{unit}_{hw_type}.html', 'Unit {unit} {hw_display}')">💬 WhatsApp</button>
                            <button class="share-btn share-email" onclick="shareEmail('unit{unit}_{hw_type}.html', 'Unit {unit} {hw_display}')">📧 Email</button>
                        </div>"""
        
        new = f"""                        <div class="share-buttons">
                            <button class="share-btn share-copy" onclick="copyHomeworkLink('unit{unit}_{hw_type}.html', 'Unit {unit} {hw_display}')">📋 Copy</button>
                            <button class="share-btn share-classroom" onclick="shareClassroom('unit{unit}_{hw_type}.html', 'Unit {unit} {hw_display}')">🏫 Classroom</button>
                            <button class="share-btn share-whatsapp" onclick="shareWhatsApp('unit{unit}_{hw_type}.html', 'Unit {unit} {hw_display}')">💬 WhatsApp</button>
                            <button class="share-btn share-email" onclick="shareEmail('unit{unit}_{hw_type}.html', 'Unit {unit} {hw_display}')">📧 Email</button>
                        </div>"""
        
        content = content.replace(old, new)

with open('homework_portal.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Google Classroom buttons to all units!")
