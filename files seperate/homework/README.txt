================================================================================
WORLD CLASS 2B - INTERACTIVE HOMEWORK SYSTEM
================================================================================

📚 OVERVIEW
-----------
This homework system provides interactive, digital worksheets for students
that can be accessed online, filled out on any device, and submitted in 
multiple ways.

================================================================================

🚀 QUICK START FOR TEACHERS
---------------------------

1. ACCESS THE HOMEWORK PORTAL
   - Open "homework_portal.html" in your browser
   - Or click the "📝 HW" button in the main book navigation

2. SHARE WITH STUDENTS
   METHOD A - Direct Links:
   - Copy the URL of any homework file
   - Share via email, Google Classroom, WhatsApp, etc.
   
   METHOD B - QR Codes:
   - Click "Show QR Codes" on any unit card
   - Display QR code on projector/screen
   - Students scan with phone camera
   
   METHOD C - Google Forms:
   - Create Google Forms versions (see below)
   - Share Google Form links for auto-grading

================================================================================

📖 HOW STUDENTS USE IT
----------------------

1. OPEN THE WORKSHEET
   - Click the link or scan the QR code
   - The worksheet opens in their browser

2. FILL OUT ANSWERS
   - Click on answer boxes and type directly
   - Works on computers, tablets, and phones
   - Progress auto-saves every 30 seconds

3. SUBMIT HOMEWORK
   Click the "📤 Submit" button and choose:
   
   📧 EMAIL: Opens email with homework attached
   📄 PDF: Download as PDF file
   🖨️ PRINT: Print and hand in physically

4. AUTO-SAVE FEATURE
   - Work is automatically saved as they type
   - If they close the browser and come back, work is restored
   - Manual save button also available

================================================================================

⚙️ GOOGLE FORMS INTEGRATION
---------------------------

To create auto-graded Google Forms:

1. Go to forms.google.com
2. Create a new blank form
3. Click "Import questions" (optional, for copying from HTML)
4. Add your questions matching the homework worksheet
5. Set answer key for auto-grading (multiple choice sections)
6. Click "Send" and copy the link
7. Replace the placeholder Google Form links in the portal

TIPS:
- Use "Section" breaks to separate exercises
- Enable "Collect email addresses" to identify students
- Set "Limit to 1 response" if needed
- View responses in Google Sheets

================================================================================

🎨 CUSTOMIZATION
----------------

CHANGING THE TEACHER EMAIL:
1. Open any homework HTML file
2. Find: mailto:teacher@school.edu
3. Replace with your actual email address
4. Save the file

UPDATING GOOGLE FORM LINKS:
1. Open homework_portal.html
2. Find the onclick="showGoogleForm()" function calls
3. Replace with actual Google Form URLs:
   
   Before: onclick="showGoogleForm('Unit 7 Vocabulary')"
   After:  href="https://forms.gle/YOUR_ACTUAL_LINK"

ADDING MORE HOMEWORK:
1. Copy any unitX_*.html file
2. Rename appropriately (e.g., unit7_listening.html)
3. Edit the content
4. Add link to homework_portal.html

================================================================================

💡 FEATURES
-----------

✅ Auto-save every 30 seconds
✅ Work timer tracks time spent
✅ Mobile-friendly responsive design
✅ Works offline (after loading)
✅ Print-optimized layout
✅ Dark mode support
✅ Progress restoration
✅ No login required
✅ Free to use

================================================================================

❓ TROUBLESHOOTING
------------------

Q: Student's work disappeared!
A: Work auto-saves to browser storage. If they cleared browser data 
   or used incognito mode, work may be lost. Always encourage students
   to submit when finished.

Q: Submit button doesn't work!
A: Check that:
   - Pop-ups are not blocked
   - Default email app is set up (for email submission)
   - Browser is up to date

Q: Can't see QR codes!
A: QR codes need to be generated. Use any free QR code generator:
   - qr-code-generator.com
   - qrcode-monkey.com
   - Paste the homework URL to generate the QR code

Q: Google Forms link doesn't work!
A: Make sure to replace the placeholder links with actual Google Form URLs

================================================================================

📁 FILE STRUCTURE
-----------------

homework/
├── homework_portal.html      # Main portal with all links
├── unit7_vocab.html          # Unit 7 vocabulary worksheet
├── unit7_grammar.html        # Unit 7 grammar worksheet
├── unit7_writing.html        # Unit 7 writing worksheet
├── unit8_vocab.html          # Unit 8 vocabulary worksheet
├── unit8_grammar.html        # Unit 8 grammar worksheet
├── unit8_writing.html        # Unit 8 writing worksheet
├── unit9_vocab.html          # Unit 9 vocabulary worksheet
├── unit9_grammar.html        # Unit 9 grammar worksheet
├── unit9_writing.html        # Unit 9 writing worksheet
├── unit10_vocab.html         # Unit 10 vocabulary worksheet
├── unit10_grammar.html       # Unit 10 grammar worksheet
├── unit10_writing.html       # Unit 10 writing worksheet
├── unit11_vocab.html         # Unit 11 vocabulary worksheet
├── unit11_grammar.html       # Unit 11 grammar worksheet
├── unit11_writing.html       # Unit 11 writing worksheet
├── unit12_vocab.html         # Unit 12 vocabulary worksheet
├── unit12_grammar.html       # Unit 12 grammar worksheet
├── unit12_writing.html       # Unit 12 writing worksheet
├── homework_template_interactive.html  # Template for new worksheets
├── make_interactive.py       # Script to add interactivity
└── README.txt                # This file

================================================================================

📝 NOTES FOR DEVELOPERS
-----------------------

- All homework files are standalone HTML (no server required)
- Data is stored in browser localStorage
- No data is sent to any server (privacy-friendly)
- Email submission uses mailto: protocol (opens user's email client)
- PDF export uses browser print to PDF function

To make new homework interactive:
  python make_interactive.py

================================================================================

For questions or support, contact your system administrator.

================================================================================
