#!/usr/bin/env python3
"""
Update unit files to use local video files instead of YouTube
"""

import os
import re

# Video files mapping
video_files = {
    'unit7.html': '../WCL2-U07.mp4',
    'unit8.html': '../WCL2-U08.mp4',
    'unit9.html': '../WCL2-U09.mp4',
    'unit10.html': '../WCL2-U10.mp4',
    'unit11.html': '../WCL2-U11.mp4',
    'unit12.html': '../WCL2-U12.mp4'
}

# CSS for local video player
video_css = '''
        /* Local Video Player Styles */
        .local-video-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin: 20px auto;
            background: #1a1a1a;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            border: 3px solid #d4af37;
        }
        
        .local-video {
            width: 100%;
            height: auto;
            display: block;
        }
        
        .video-fallback {
            padding: 40px;
            text-align: center;
            background: #2d2d2d;
            color: #d4af37;
        }
        
        .video-fallback-icon {
            font-size: 48px;
            margin-bottom: 15px;
        }
        
        .video-offline-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            background: linear-gradient(145deg, #722f37 0%, #5c1a1a 100%);
            color: #d4af37;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            z-index: 10;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        .video-info {
            background: linear-gradient(145deg, #722f37 0%, #5c1a1a 100%);
            color: white;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .video-info-title {
            font-weight: 600;
            font-size: 14px;
        }
        
        .video-info-format {
            background: #d4af37;
            color: #722f37;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 700;
        }
        
        /* Dark mode support */
        body.dark-mode .local-video-container {
            border-color: #d4af37;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
'''

def update_unit_video(filepath, video_path):
    """Update a unit file to use local video"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if already updated
        if 'local-video' in content and video_path in content:
            print(f"Skipping {os.path.basename(filepath)} - already has local video")
            return
        
        # Add CSS before </style>
        if '.local-video-container' not in content:
            content = content.replace('</style>', video_css + '\n        </style>')
        
        # Find and replace YouTube iframe with local video player
        # Pattern matches various YouTube embed formats
        youtube_pattern = r'<iframe[^>]*youtube\.com/embed/[^>]*>[^<]*</iframe>'
        
        local_video_html = f'''<div class="local-video-container">
            <div class="video-offline-badge">📱 OFFLINE VIDEO</div>
            <video class="local-video" controls poster="">
                <source src="{video_path}" type="video/mp4">
                <div class="video-fallback">
                    <div class="video-fallback-icon">🎬</div>
                    <p><strong>Video File:</strong> {os.path.basename(video_path)}</p>
                    <p style="margin-top: 10px; font-size: 13px;">Your browser does not support video playback.</p>
                </div>
            </video>
            <div class="video-info">
                <span class="video-info-title">Unit Video - MP4 Format</span>
                <span class="video-info-format">HD</span>
            </div>
        </div>'''
        
        # Replace YouTube iframe
        content = re.sub(youtube_pattern, local_video_html, content, flags=re.IGNORECASE)
        
        # Also look for video-container or video-wrapper divs that might contain iframes
        # Pattern: <div class="video-container">...<iframe youtube>...</iframe>...</div>
        container_pattern = r'(<div[^>]*class="[^"]*video[^"]*"[^>]*>.*?)(<iframe[^>]*youtube\.com/embed/[^>]*>[^<]*</iframe>)(.*?</div>)'
        
        def replace_container(match):
            before = match.group(1)
            after = match.group(3)
            # Keep the container but replace only the iframe
            return before + local_video_html + after
        
        content = re.sub(container_pattern, replace_container, content, flags=re.IGNORECASE | re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {os.path.basename(filepath)} -> {video_path}")
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# Update all unit files
for unit_file, video_path in video_files.items():
    filepath = os.path.join('files seperate', unit_file)
    if os.path.exists(filepath):
        update_unit_video(filepath, video_path)
    else:
        print(f"File not found: {filepath}")

print("\nDone! All units now use local video files.")
print("\nStudents can now:")
print("- Watch videos without internet connection")
print("- Use native browser video controls (fullscreen, playback speed)")
print("- See 'OFFLINE VIDEO' badge indicating no streaming needed")
