#!/usr/bin/env python3
"""
Update video player with enhanced controls and captions support
"""

import os
import re

# Enhanced video player HTML with all controls
enhanced_video_html = '''<div class="local-video-container">
            <div class="video-offline-badge">📱 OFFLINE VIDEO</div>
            <video class="local-video" controls controlsList="nodownload" crossorigin="anonymous" style="width: 100%;">
                <source src="{video_path}" type="video/mp4">
                <!-- Subtitle/Caption tracks - add your .vtt files here -->
                <track kind="captions" src="{vtt_path}" srclang="en" label="English" default>
                <track kind="subtitles" src="{vtt_path}" srclang="en" label="English Subtitles">
                <div class="video-fallback">
                    <div class="video-fallback-icon">🎬</div>
                    <p><strong>Video File:</strong> {video_file}</p>
                    <p style="margin-top: 10px; font-size: 13px;">Your browser does not support video playback.</p>
                </div>
            </video>
            <div class="video-controls-hint">
                <span>🎥 Video Controls:</span> Play ▶️ | Pause ⏸️ | Rewind ⏪ | Forward ⏩ | Captions 📝 | Fullscreen 🔲
            </div>
            <div class="video-info">
                <span class="video-info-title">{unit_title}</span>
                <span class="video-info-format">HD</span>
            </div>
        </div>'''

# CSS for enhanced video player
video_controls_css = '''
        /* Enhanced Video Player Controls */
        .local-video {
            width: 100%;
            height: auto;
            display: block;
        }
        
        /* Ensure video controls are visible */
        .local-video::-webkit-media-controls {
            display: flex !important;
        }
        
        .local-video::-webkit-media-controls-enclosure {
            background: rgba(0, 0, 0, 0.7);
            border-radius: 0 0 8px 8px;
        }
        
        /* Custom control hints */
        .video-controls-hint {
            background: linear-gradient(145deg, #3d3d3d 0%, #2d2d2d 100%);
            color: #d4af37;
            padding: 10px 15px;
            font-size: 12px;
            text-align: center;
            border-bottom: 2px solid #d4af37;
        }
        
        .video-controls-hint span {
            font-weight: 700;
            margin-right: 8px;
        }
        
        /* Captions/Subtitles styling */
        .local-video::cue {
            background: rgba(114, 47, 55, 0.9);
            color: #d4af37;
            font-size: 16px;
            font-weight: 600;
            padding: 5px 10px;
            border-radius: 4px;
        }
        
        /* Make controls always visible on hover */
        .local-video-container:hover .local-video::-webkit-media-controls-panel {
            opacity: 1 !important;
        }
        
        /* Audio description for accessibility */
        .video-audio-desc {
            position: absolute;
            left: -10000px;
            width: 1px;
            height: 1px;
            overflow: hidden;
        }
'''

video_mapping = {
    'unit7.html': ('../WCL2-U07.mp4', 'WCL2-U07.mp4', 'Unit 7: Learning and Education', '../captions/unit7.vtt'),
    'unit8.html': ('../WCL2-U08.mp4', 'WCL2-U08.mp4', 'Unit 8: Fame and Public Life', '../captions/unit8.vtt'),
    'unit9.html': ('../WCL2-U09.mp4', 'WCL2-U09.mp4', 'Unit 9: Health Habits', '../captions/unit9.vtt'),
    'unit10.html': ('../WCL2-U10.mp4', 'WCL2-U10.mp4', 'Unit 10: Water & Environment', '../captions/unit10.vtt'),
    'unit11.html': ('../WCL2-U11.mp4', 'WCL2-U11.mp4', 'Unit 11: Art & Creativity', '../captions/unit11.vtt'),
    'unit12.html': ('../WCL2-U12.mp4', 'WCL2-U12.mp4', 'Unit 12: Humor & Comedy', '../captions/unit12.vtt'),
}

def update_video_player(filepath, video_info):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        video_path, video_file, unit_title, vtt_path = video_info
        
        # Add CSS if not present
        if '.video-controls-hint' not in content:
            content = content.replace('</style>', video_controls_css + '\n        </style>')
        
        # Find and replace the video container
        old_pattern = r'<div class="local-video-container">.*?</div>\s*</div>\s*</div>\s*<div class="video-info">'
        
        new_html = f'''<div class="local-video-container">
            <div class="video-offline-badge">📱 OFFLINE VIDEO</div>
            <video class="local-video" controls controlsList="nodownload" crossorigin="anonymous" style="width: 100%;">
                <source src="{video_path}" type="video/mp4">
                <!-- Subtitle/Caption tracks -->
                <track kind="captions" src="{vtt_path}" srclang="en" label="English" default>
                <track kind="subtitles" src="{vtt_path}" srclang="en" label="English Subtitles">
                <div class="video-fallback">
                    <div class="video-fallback-icon">🎬</div>
                    <p><strong>Video File:</strong> {video_file}</p>
                    <p style="margin-top: 10px; font-size: 13px;">Your browser does not support video playback.</p>
                </div>
            </video>
            <div class="video-controls-hint">
                <span>🎥 Video Controls:</span> Play ▶️ | Pause ⏸️ | Rewind ⏪ | Forward ⏩ | Captions CC | Fullscreen 🔲
            </div>
            <div class="video-info">
                <span class="video-info-title">{unit_title}</span>
                <span class="video-info-format">HD</span>
            </div>'''
        
        # Replace the video section
        content = re.sub(
            r'<div class="local-video-container">.*?<div class="video-info">.*?<span class="video-info-format">HD</span>\s*</div>',
            new_html,
            content,
            flags=re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated video player in {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# Update all units
for filename, info in video_mapping.items():
    filepath = os.path.join('files seperate', filename)
    if os.path.exists(filepath):
        update_video_player(filepath, info)
    else:
        print(f"File not found: {filepath}")

print("\n✅ Done! Video players updated with enhanced controls.")
print("\nNote: To enable captions, create .vtt subtitle files and place them in a 'captions' folder.")
