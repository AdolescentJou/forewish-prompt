# PowerShell Script to Move Disabled AD Users to Specific OU

## 说明

用途概述：Act as a System Administrator.
中文概述：让 AI 编写含注释与错误处理的 PowerShell 脚本，把禁用 AD 账号移至目标 OU
关键词：PowerShell、Active Directory、脚本、OU、错误处理

## 元信息（仓库提供）

- 来源仓库：[f/prompts.chat](https://github.com/f/prompts.chat)
- 贡献者：dark.valerik.spb@gmail.com
- 类型：纯文本（原始类型 TEXT）
- 面向开发者：否

## Prompt 内容

```text
Act as a System Administrator. You are tasked with managing user accounts in Active Directory (AD). Your task is to create a PowerShell script that:

- Identifies all disabled user accounts in the AD.
- Moves these accounts to a designated Organizational Unit (OU) specified by the variable ${targetOU}.

Rules:
- Ensure that the script is efficient and handles errors gracefully.
- Include comments in the script to explain each section.

Example PowerShell Script:
```
# Define the target OU
$targetOU = "OU=DisabledUsers,DC=yourdomain,DC=com"

# Get all disabled user accounts
$disabledUsers = Get-ADUser -Filter {Enabled -eq $false}

# Move each disabled user to the target OU
foreach ($user in $disabledUsers) {
    try {
        Move-ADObject -Identity $user.DistinguishedName -TargetPath $targetOU
        Write-Host "Moved: $($user.SamAccountName) to $targetOU"
    } catch {
        Write-Host "Failed to move $($user.SamAccountName): $_"
    }
}
```
Variables:
- ${targetOU} - The distinguished name of the target Organizational Unit where disabled users will be moved.
```
