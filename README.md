Dealing with line endings (CRLF vs LF):

Since I expect this project to work with a Python GUI installed on the Windows system - That is why I'm coding through the Command Prompt - I prefer all files end-of-line (eol) to be formatted with CRLF.

Command Prompt uses the Windows git configuration settings. This means that it expects files being formatted with CRLF instead of LF (Linux format).

Now, some files appears as being LF formatted (Pipfile and Pipfile.lock so far).
On the first commit I've received the warning:
warning: LF will be replaced by CRLF in Pipfile.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in Pipfile.lock.
The file will have its original line endings in your working directory

This is because of this configuration:
    core.autocrfl = true
This causes the following:
On commit (i.e. storing files into the index) CRLF >converted to> LF
on checkout (i.e. recreating files stored in the index on the local file system): LF >converted to> CRLF

I only care that the local files have CRLF.

I modified files and did a git reset --hard to the first commit but files (Pipfile.lock) are still marked as LF. So I don't know for the moment what core.autocrfl = true does...
Since git setting file.eol is set to auto possibly VS Code decides self how to format eol in files...
Anyhow, we will see when it's time to use the Python GUI...