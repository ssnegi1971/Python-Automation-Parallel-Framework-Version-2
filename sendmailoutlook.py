# Source - https://stackoverflow.com/a
# Posted by TheoretiCAL, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-08, License - CC BY-SA 3.0
import sys
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To=sys.argv[1];
#mail.To = 'ssnegi@yahoo.com'
mail.Subject = sys.argv[2];
#mail.Subject = 'Test'
mail.Body = sys.argv[2];
#mail.Body = 'Test'
#mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
#attachment  = "Path to the attachment"
#mail.Attachments.Add(attachment)

mail.Send()