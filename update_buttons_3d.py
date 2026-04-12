#!/usr/bin/env python3
"""
3D Button Theme Updater - Applies dynamic 3D button styles to all HTML files
"""

import os
import re

# Comprehensive 3D Button CSS to inject
BUTTON_CSS = """
        /* ===== 3D DYNAMIC BUTTONS ===== */
        
        /* Base 3D Button Style */
        .btn-3d {
            display: inline-block;
            padding: 12px 28px;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #fff;
            background: linear-gradient(145deg, #8b3a3a 0%, #722f37 50%, #5c1a1a 100%);
            border: none;
            border-radius: 50px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 4px 6px rgba(114, 47, 55, 0.3),
                0 10px 20px rgba(114, 47, 55, 0.2),
                inset 0 1px 0 rgba(255,255,255,0.2),
                inset 0 -2px 0 rgba(0,0,0,0.2);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            transform: translateY(0);
        }
        
        .btn-3d::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.3), transparent);
            transition: left 0.5s ease;
        }
        
        .btn-3d:hover::before {
            left: 100%;
        }
        
        .btn-3d:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 
                0 8px 15px rgba(114, 47, 55, 0.4),
                0 15px 30px rgba(114, 47, 55, 0.25),
                inset 0 1px 0 rgba(255,255,255,0.3),
                inset 0 -2px 0 rgba(0,0,0,0.2);
            background: linear-gradient(145deg, #722f37 0%, #8b3a3a 50%, #722f37 100%);
        }
        
        .btn-3d:active {
            transform: translateY(-1px) scale(0.98);
            box-shadow: 
                0 2px 4px rgba(114, 47, 55, 0.3),
                0 5px 10px rgba(114, 47, 55, 0.2),
                inset 0 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Gold Accent Button */
        .btn-gold {
            background: linear-gradient(145deg, #e5c76b 0%, #d4af37 50%, #b8960c 100%);
            color: #722f37;
            box-shadow: 
                0 4px 6px rgba(212, 175, 55, 0.4),
                0 10px 20px rgba(212, 175, 55, 0.25),
                inset 0 1px 0 rgba(255,255,255,0.4),
                inset 0 -2px 0 rgba(0,0,0,0.1);
            font-weight: 800;
        }
        
        .btn-gold:hover {
            background: linear-gradient(145deg, #d4af37 0%, #e5c76b 50%, #d4af37 100%);
            color: #5c1a1a;
            box-shadow: 
                0 8px 15px rgba(212, 175, 55, 0.5),
                0 15px 30px rgba(212, 175, 55, 0.3),
                inset 0 1px 0 rgba(255,255,255,0.5),
                inset 0 -2px 0 rgba(0,0,0,0.1);
        }
        
        .btn-gold:active {
            box-shadow: 
                0 2px 4px rgba(212, 175, 55, 0.4),
                0 5px 10px rgba(212, 175, 55, 0.2),
                inset 0 2px 4px rgba(0,0,0,0.15);
        }
        
        /* Outline 3D Button */
        .btn-outline {
            background: transparent;
            color: #722f37;
            border: 2px solid #722f37;
            box-shadow: 
                0 4px 6px rgba(114, 47, 55, 0.1),
                0 0 0 4px rgba(114, 47, 55, 0.05);
        }
        
        .btn-outline:hover {
            background: #722f37;
            color: #fff;
            box-shadow: 
                0 8px 15px rgba(114, 47, 55, 0.3),
                0 0 0 6px rgba(114, 47, 55, 0.1);
        }
        
        /* Small Button Variant */
        .btn-sm {
            padding: 8px 18px;
            font-size: 12px;
        }
        
        /* Large Button Variant */
        .btn-lg {
            padding: 16px 36px;
            font-size: 16px;
        }
        
        /* Icon Button */
        .btn-icon {
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .btn-icon svg,
        .btn-icon i,
        .btn-icon span.icon {
            font-size: 1.2em;
            transition: transform 0.3s ease;
        }
        
        .btn-icon:hover svg,
        .btn-icon:hover i,
        .btn-icon:hover span.icon {
            transform: translateX(3px);
        }
        
        /* Rounded Square Buttons (for nav) */
        .btn-square {
            border-radius: 12px;
            padding: 10px 20px;
        }
        
        /* Pill Button */
        .btn-pill {
            border-radius: 50px;
        }
        
        /* Floating Action Button Style */
        .btn-float {
            box-shadow: 
                0 6px 12px rgba(114, 47, 55, 0.25),
                0 0 0 1px rgba(114, 47, 55, 0.1),
                inset 0 1px 0 rgba(255,255,255,0.2);
        }
        
        .btn-float:hover {
            transform: translateY(-4px);
            box-shadow: 
                0 12px 24px rgba(114, 47, 55, 0.35),
                0 0 0 1px rgba(114, 47, 55, 0.15),
                inset 0 1px 0 rgba(255,255,255,0.25);
        }
        
        /* Gradient Shine Effect */
        .btn-shine {
            position: relative;
            overflow: hidden;
        }
        
        .btn-shine::after {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                to right,
                transparent 0%,
                rgba(255,255,255,0.1) 50%,
                transparent 100%
            );
            transform: rotate(30deg) translateX(-100%);
            transition: transform 0.6s ease;
        }
        
        .btn-shine:hover::after {
            transform: rotate(30deg) translateX(100%);
        }
        
        /* Ripple Effect on Click */
        .btn-ripple {
            position: relative;
            overflow: hidden;
        }
        
        .btn-ripple span.ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(212, 175, 55, 0.4);
            transform: scale(0);
            animation: ripple-animation 0.6s linear;
            pointer-events: none;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
        
        /* Glow Effect */
        .btn-glow {
            animation: glow-pulse 2s ease-in-out infinite;
        }
        
        @keyframes glow-pulse {
            0%, 100% {
                box-shadow: 
                    0 4px 6px rgba(114, 47, 55, 0.3),
                    0 0 20px rgba(212, 175, 55, 0.2);
            }
            50% {
                box-shadow: 
                    0 4px 6px rgba(114, 47, 55, 0.3),
                    0 0 30px rgba(212, 175, 55, 0.4);
            }
        }
        
        /* Button Group */
        .btn-group {
            display: inline-flex;
            gap: 0;
        }
        
        .btn-group .btn-3d {
            border-radius: 0;
        }
        
        .btn-group .btn-3d:first-child {
            border-radius: 50px 0 0 50px;
        }
        
        .btn-group .btn-3d:last-child {
            border-radius: 0 50px 50px 0;
        }
        
        /* Dark Mode Button Styles */
        body.dark-mode .btn-3d {
            background: linear-gradient(145deg, #8b3a3a 0%, #5c1a1a 50%, #3d1515 100%);
            box-shadow: 
                0 4px 6px rgba(0, 0, 0, 0.4),
                0 10px 20px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255,255,255,0.1),
                inset 0 -2px 0 rgba(0,0,0,0.3);
        }
        
        body.dark-mode .btn-3d:hover {
            background: linear-gradient(145deg, #722f37 0%, #8b3a3a 50%, #722f37 100%);
            box-shadow: 
                0 8px 15px rgba(0, 0, 0, 0.5),
                0 15px 30px rgba(0, 0, 0, 0.35),
                0 0 20px rgba(212, 175, 55, 0.2),
                inset 0 1px 0 rgba(255,255,255,0.15),
                inset 0 -2px 0 rgba(0,0,0,0.3);
        }
        
        body.dark-mode .btn-gold {
            background: linear-gradient(145deg, #e5c76b 0%, #d4af37 50%, #b8960c 100%);
            color: #3d1515;
            box-shadow: 
                0 4px 6px rgba(212, 175, 55, 0.3),
                0 10px 20px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255,255,255,0.3);
        }
        
        body.dark-mode .btn-outline {
            border-color: #d4af37;
            color: #d4af37;
            box-shadow: 
                0 4px 6px rgba(0, 0, 0, 0.2),
                0 0 0 4px rgba(212, 175, 55, 0.05);
        }
        
        body.dark-mode .btn-outline:hover {
            background: #d4af37;
            color: #3d1515;
            box-shadow: 
                0 8px 15px rgba(212, 175, 55, 0.3),
                0 0 0 6px rgba(212, 175, 55, 0.1);
        }
        
        /* Section Navigation Buttons Enhancement */
        .nav-bar button {
            background: linear-gradient(145deg, #faf8f5 0%, #f0ebe3 100%);
            color: #722f37;
            border: 2px solid transparent;
            padding: 10px 20px;
            border-radius: 25px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 
                0 2px 4px rgba(114, 47, 55, 0.1),
                inset 0 1px 0 rgba(255,255,255,0.8);
            position: relative;
            overflow: hidden;
        }
        
        .nav-bar button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: rgba(212, 175, 55, 0.2);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            transition: width 0.4s ease, height 0.4s ease;
        }
        
        .nav-bar button:hover::before {
            width: 200%;
            height: 200%;
        }
        
        .nav-bar button:hover {
            background: linear-gradient(145deg, #722f37 0%, #8b3a3a 100%);
            color: #fff;
            border-color: #d4af37;
            transform: translateY(-2px);
            box-shadow: 
                0 6px 12px rgba(114, 47, 55, 0.25),
                0 0 0 3px rgba(212, 175, 55, 0.2),
                inset 0 1px 0 rgba(255,255,255,0.1);
        }
        
        .nav-bar button.active {
            background: linear-gradient(145deg, #722f37 0%, #5c1a1a 100%);
            color: #d4af37;
            border-color: #d4af37;
            box-shadow: 
                0 4px 8px rgba(114, 47, 55, 0.3),
                0 0 0 3px rgba(212, 175, 55, 0.3),
                inset 0 2px 4px rgba(0,0,0,0.2);
        }
        
        body.dark-mode .nav-bar button {
            background: linear-gradient(145deg, #3d3d3d 0%, #2d2d2d 100%);
            color: #e0e0e0;
            box-shadow: 
                0 2px 4px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255,255,255,0.05);
        }
        
        body.dark-mode .nav-bar button:hover {
            background: linear-gradient(145deg, #722f37 0%, #5c1a1a 100%);
            color: #fff;
            border-color: #d4af37;
        }
        
        body.dark-mode .nav-bar button.active {
            background: linear-gradient(145deg, #5c1a1a 0%, #722f37 100%);
            color: #d4af37;
            border-color: #d4af37;
            box-shadow: 
                0 4px 8px rgba(0, 0, 0, 0.4),
                0 0 0 3px rgba(212, 175, 55, 0.2),
                inset 0 2px 4px rgba(0,0,0,0.3);
        }
        
        /* Audio/Play Buttons */
        .audio-btn, .play-btn {
            background: linear-gradient(145deg, #722f37 0%, #5c1a1a 100%);
            color: #d4af37;
            border: 2px solid #d4af37;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 20px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 
                0 4px 8px rgba(114, 47, 55, 0.3),
                inset 0 1px 0 rgba(255,255,255,0.1);
        }
        
        .audio-btn:hover, .play-btn:hover {
            transform: scale(1.1) translateY(-2px);
            box-shadow: 
                0 8px 16px rgba(114, 47, 55, 0.4),
                0 0 20px rgba(212, 175, 55, 0.3),
                inset 0 1px 0 rgba(255,255,255,0.2);
        }
        
        .audio-btn:active, .play-btn:active {
            transform: scale(0.95);
            box-shadow: 
                0 2px 4px rgba(114, 47, 55, 0.3),
                inset 0 2px 4px rgba(0,0,0,0.2);
        }
        
        body.dark-mode .audio-btn,
        body.dark-mode .play-btn {
            background: linear-gradient(145deg, #5c1a1a 0%, #3d1515 100%);
            box-shadow: 
                0 4px 8px rgba(0, 0, 0, 0.4),
                inset 0 1px 0 rgba(255,255,255,0.05);
        }
"""

def find_files(root_dir):
    """Find all HTML files recursively"""
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                html_files.append(os.path.join(dirpath, filename))
    return html_files

def inject_button_css(filepath):
    """Inject 3D button CSS before the closing </style> tag"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if already has 3D button styles
        if 'btn-3d' in content:
            print(f"Skipping {os.path.basename(filepath)} - already has 3D buttons")
            return
        
        # Find the closing </style> tag and insert before it
        if '</style>' in content:
            content = content.replace('</style>', BUTTON_CSS + '\n        </style>')
        else:
            # If no style tag, add one in head
            if '</head>' in content:
                content = content.replace('</head>', f'<style>\n{BUTTON_CSS}\n        </style>\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# Main execution
root_dir = '.'
html_files = find_files(root_dir)

print(f"Found {len(html_files)} HTML files")
print("Injecting 3D button styles...\n")

for filepath in html_files:
    inject_button_css(filepath)

print("\nDone! 3D button styles applied to all files.")
