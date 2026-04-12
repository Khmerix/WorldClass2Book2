#!/usr/bin/env python3
"""
Add audio pronunciation buttons to vocabulary words
Since we don't have audio files, we'll add a TTS (Text-to-Speech) feature
or placeholders for future audio files
"""

import os
import re

# CSS for audio buttons
audio_css = '''
        /* Vocabulary Audio Pronunciation */
        .vocab-item {
            position: relative;
        }
        
        .vocab-audio-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: linear-gradient(145deg, #d4af37 0%, #e5c76b 100%);
            color: #722f37;
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            z-index: 5;
        }
        
        .vocab-audio-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        
        .vocab-audio-btn:active {
            transform: scale(0.95);
        }
        
        .vocab-audio-btn.playing {
            animation: pulse-audio 1s infinite;
        }
        
        @keyframes pulse-audio {
            0%, 100% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.7); }
            50% { box-shadow: 0 0 0 10px rgba(212, 175, 55, 0); }
        }
        
        /* Alternative: Google TTS link */
        .vocab-tts-link {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            margin-top: 8px;
            padding: 5px 10px;
            background: #f0f0f0;
            border-radius: 15px;
            font-size: 12px;
            color: #722f37;
            text-decoration: none;
            transition: all 0.3s;
        }
        
        .vocab-tts-link:hover {
            background: #d4af37;
            color: white;
        }
        
        .vocab-pronunciation {
            font-size: 13px;
            color: #666;
            font-style: italic;
            margin-top: 5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .vocab-pronunciation .ipa {
            font-family: 'Segoe UI', Tahoma, sans-serif;
            background: #f9f5f0;
            padding: 2px 8px;
            border-radius: 4px;
            border: 1px solid #d4af37;
        }
        
        body.dark-mode .vocab-audio-btn {
            background: linear-gradient(145deg, #e5c76b 0%, #d4af37 100%);
            color: #3d1515;
        }
        
        body.dark-mode .vocab-pronunciation {
            color: #aaa;
        }
        
        body.dark-mode .vocab-pronunciation .ipa {
            background: #3d3d3d;
            border-color: #d4af37;
            color: #d4af37;
        }
'''

# JavaScript for text-to-speech
audio_js = '''
    <!-- Vocabulary Audio Pronunciation -->
    <script>
        // Text-to-Speech for vocabulary pronunciation
        function speakWord(word) {
            if ('speechSynthesis' in window) {
                // Cancel any ongoing speech
                window.speechSynthesis.cancel();
                
                const utterance = new SpeechSynthesisUtterance(word);
                utterance.lang = 'en-US';
                utterance.rate = 0.8;
                utterance.pitch = 1;
                
                // Find the button and add playing animation
                const buttons = document.querySelectorAll('.vocab-audio-btn');
                buttons.forEach(btn => {
                    if (btn.getAttribute('data-word') === word) {
                        btn.classList.add('playing');
                        btn.innerHTML = '🔊';
                    }
                });
                
                utterance.onend = function() {
                    buttons.forEach(btn => {
                        if (btn.getAttribute('data-word') === word) {
                            btn.classList.remove('playing');
                            btn.innerHTML = '🔈';
                        }
                    });
                };
                
                window.speechSynthesis.speak(utterance);
            } else {
                alert('Text-to-speech is not supported in your browser.');
            }
        }
        
        // Add audio buttons to vocabulary items
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('.vocab-item').forEach(item => {
                const wordEl = item.querySelector('.vocab-word');
                if (wordEl) {
                    const word = wordEl.textContent.trim();
                    const audioBtn = document.createElement('button');
                    audioBtn.className = 'vocab-audio-btn';
                    audioBtn.setAttribute('data-word', word);
                    audioBtn.innerHTML = '🔈';
                    audioBtn.title = 'Click to hear pronunciation';
                    audioBtn.onclick = function(e) {
                        e.stopPropagation();
                        speakWord(word);
                    };
                    item.appendChild(audioBtn);
                }
            });
        });
    </script>
'''

def add_audio_to_unit(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Skip if already has audio
        if 'speakWord' in content or 'vocab-audio-btn' in content:
            print(f"Skipping {os.path.basename(filepath)} - audio already added")
            return
        
        # Add CSS
        if '.vocab-audio-btn' not in content:
            content = content.replace('</style>', audio_css + '\n        </style>')
        
        # Add JavaScript before </body>
        if 'speakWord' not in content:
            content = content.replace('</body>', audio_js + '\n</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Added audio to {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error adding audio to {filepath}: {e}")

# Process all unit files
for unit_num in range(7, 13):
    filename = f'files seperate/unit{unit_num}.html'
    if os.path.exists(filename):
        add_audio_to_unit(filename)
    else:
        print(f"File not found: {filename}")

print("\nDone! Added pronunciation audio to all units.")
print("\nFeatures:")
print("- 🔈 Speaker icon on each vocabulary word")
print("- Click to hear text-to-speech pronunciation")
print("- Uses browser's built-in TTS (no audio files needed)")
print("- Works offline once page is loaded")
