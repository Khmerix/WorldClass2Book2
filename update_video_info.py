#!/usr/bin/env python3
"""
Update video information for all units to match their themes
"""

import os
import re

# Video info for each unit
video_info = {
    'unit7.html': {
        'subtitle': 'Video: Learning and Intelligence',
        'activity_title': '🎥 Unit 7 Video',
        'activity_desc': 'Watch the video about learning, intelligence, and the different ways people acquire knowledge and skills. This video explores various types of intelligence and learning strategies.',
        'box_title': '🎬 World Class 2B - Unit 7 Video',
        'box_subtitle': 'Learning and Education',
        'info_bar': 'Unit 7: Learning and Education'
    },
    'unit8.html': {
        'subtitle': 'Video: Fame and Celebrity Culture',
        'activity_title': '🎥 Unit 8 Video',
        'activity_desc': 'Watch the video about fame, celebrity culture, and the impact of media on public life. This video explores how celebrities influence society and the challenges of living in the public eye.',
        'box_title': '🎬 World Class 2B - Unit 8 Video',
        'box_subtitle': 'The Cult of Celebrity',
        'info_bar': 'Unit 8: Fame and Public Life'
    },
    'unit9.html': {
        'subtitle': 'Video: Health and Well-being',
        'activity_title': '🎥 Unit 9 Video',
        'activity_desc': 'Watch the video about health habits, well-being, and maintaining a balanced lifestyle. This video explores nutrition, exercise, and mental health in modern society.',
        'box_title': '🎬 World Class 2B - Unit 9 Video',
        'box_subtitle': 'To Your Health!',
        'info_bar': 'Unit 9: Health Habits'
    },
    'unit10.html': {
        'subtitle': 'Video: Water and Environment',
        'activity_title': '🎥 Unit 10 Video',
        'activity_desc': 'Watch the video about water resources, environmental conservation, and sustainability. This video explores the importance of protecting our most precious natural resources.',
        'box_title': '🎬 World Class 2B - Unit 10 Video',
        'box_subtitle': 'Our Most Precious Resource',
        'info_bar': 'Unit 10: Water & Environment'
    },
    'unit11.html': {
        'subtitle': 'Video: Art and Creativity',
        'activity_title': '🎥 Unit 11 Video',
        'activity_desc': 'Watch the video about art, creativity, and design. This video explores how artists find inspiration and the role of creativity in shaping our world.',
        'box_title': '🎬 World Class 2B - Unit 11 Video',
        'box_subtitle': 'Inspired Minds',
        'info_bar': 'Unit 11: Art & Creativity'
    },
    'unit12.html': {
        'subtitle': 'Video: Humor and Comedy',
        'activity_title': '🎥 Unit 12 Video',
        'activity_desc': 'Watch the video about humor, comedy, and the role of laughter in society. This video explores different types of comedy and why humor is important in our lives.',
        'box_title': '🎬 World Class 2B - Unit 12 Video',
        'box_subtitle': "What's So Funny?",
        'info_bar': 'Unit 12: Humor & Comedy'
    }
}

def update_video_info(filepath, info):
    """Update video section with correct info"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Update subtitle line
        content = re.sub(
            r'<p style="margin-bottom: 20px; font-size: 18px; color: #666;">.*?</p>',
            f'<p style="margin-bottom: 20px; font-size: 18px; color: #666;">{info["subtitle"]}</p>',
            content,
            count=1
        )
        
        # Update activity box
        content = re.sub(
            r'<div class="activity-box">\s*<h3>.*?</h3>\s*<p>.*?</p>\s*</div>',
            f'''<div class="activity-box">
                    <h3>{info['activity_title']}</h3>
                    <p>{info['activity_desc']}</p>
                </div>''',
            content,
            count=1,
            flags=re.DOTALL
        )
        
        # Update video box title and subtitle
        content = re.sub(
            r'<div class="video-box">\s*<h3 style="font-size: 24px; margin-bottom: 15px;">.*?</h3>\s*<p style="margin-bottom: 20px; opacity: 0.9;">.*?</p>',
            f'''<div class="video-box">
                    <h3 style="font-size: 24px; margin-bottom: 15px;">{info['box_title']}</h3>
                    <p style="margin-bottom: 20px; opacity: 0.9;">{info['box_subtitle']}</p>''',
            content,
            count=1,
            flags=re.DOTALL
        )
        
        # Update info bar
        content = re.sub(
            r'<span class="video-info-title">.*?</span>',
            f'<span class="video-info-title">{info["info_bar"]}</span>',
            content
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {os.path.basename(filepath)}")
        
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# Update all units
for filename, info in video_info.items():
    filepath = os.path.join('files seperate', filename)
    if os.path.exists(filepath):
        update_video_info(filepath, info)
    else:
        print(f"File not found: {filepath}")

print("\nDone! All video info updated to match unit themes.")
