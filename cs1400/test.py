import os
import shutil
root_dir = "/home/josh/Emails-Unpacked"
os.chdir("/home/josh/Emails-Unpacked")

folders = sorted(os.listdir())

weekly_emails = []

for folder in folders:
    os.chdir(os.path.join(root_dir, folder))
    for file in os.listdir():
        with open(file, 'r') as f:
            contents = f.read()
        if 'Dear Friends and Family' in contents:
            if '_Re' in file:
                pass
            elif '_Fwd' in file:
                pass
            else:
                weekly_emails.append(os.path.join(root_dir, folder, file))
                print(os.path.join(root_dir, folder, file))
        elif 'Dear Family and Friends' in contents:
            if '_Re' in file:
                pass
            elif '_Fwd' in file:
                pass
            else:
                weekly_emails.append(os.path.join(root_dir, folder, file))
                print(os.path.join(root_dir, folder, file))
print(f"Total Emails Found: {len(weekly_emails)}")

# for email in weekly_emails:
#     pass
#     shutil.copy2(email, os.path.join(root_dir, 'weeklyEmails'))
