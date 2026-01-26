# Connecting GitHub Copilot to Jira

This guide explains how to integrate GitHub Copilot with Jira for seamless issue tracking and project management.

## Overview

While GitHub Copilot is primarily a code completion tool, you can integrate your GitHub repository with Jira to:
- Link commits and pull requests to Jira issues
- Track development progress in Jira
- Automate workflow transitions based on GitHub events
- View development information directly in Jira issues

## Prerequisites

- A GitHub account with access to this repository
- A Jira account (Cloud or Server/Data Center)
- Admin permissions on your Jira instance (for installation)
- Repository admin access (for GitHub integration)

## Integration Options

### Option 1: GitHub for Jira App (Recommended)

This is the official integration from Atlassian.

#### Installation Steps

1. **Install the GitHub for Jira App**
   - Go to the [Atlassian Marketplace](https://marketplace.atlassian.com/apps/1219592/github-for-jira)
   - Click "Get it now" or "Try it free"
   - Select your Jira site
   - Click "Install app"

2. **Connect Your GitHub Account**
   - In Jira, go to **Apps** → **GitHub** → **Get started**
   - Click "Connect GitHub organization"
   - Authenticate with GitHub
   - Select the organizations you want to connect

3. **Configure Repository Access**
   - Select which repositories to sync with Jira
   - Choose between:
     - All repositories (current and future)
     - Specific repositories (including this calculator repo)

4. **Link Issues Using Smart Commits**
   - In your commit messages, reference Jira issues using the issue key:
     ```bash
     git commit -m "CALC-123 Add new calculator function"
     ```
   - In pull request titles or descriptions:
     ```
     CALC-123: Implement division by zero handling
     ```

#### Features Available

- **Automatic Linking**: Commits, branches, and pull requests are automatically linked to Jira issues
- **Development Panel**: View all development activity in Jira issues
- **Status Transitions**: Configure automatic transitions when PRs are merged
- **Deployment Tracking**: Track deployments from GitHub Actions
- **Code Reviews**: View PR status and reviews in Jira

### Option 2: Jira Software + GitHub Integration (Legacy)

For older integrations or self-hosted Jira instances.

#### Setup Steps

1. **In Jira:**
   - Go to **Settings** → **Applications** → **DVCS accounts**
   - Click "Link GitHub account"
   - Choose "GitHub" or "GitHub Enterprise"

2. **Authorize the Integration:**
   - Follow the OAuth flow to authorize Jira
   - Grant necessary permissions

3. **Configure Repositories:**
   - Add the repositories you want to sync
   - Wait for the initial sync to complete

### Option 3: Using Automation Tools

You can also use third-party automation tools to enhance integration:

1. **Zapier or Make (formerly Integromat):**
   - Create automated workflows between GitHub and Jira
   - Trigger actions in Jira based on GitHub events
   - Requires paid subscription for advanced features

2. **Custom Webhooks:**
   - Set up custom webhooks in GitHub
   - Build custom integration logic
   - Requires technical expertise and infrastructure

## Using the Integration

### Workflow with Copilot and Jira

1. **Create a Jira Issue:**
   - Create an issue in Jira (e.g., `CALC-456: Add scientific calculator functions`)

2. **Create a Branch:**
   - Name your branch with the Jira issue key:
     ```bash
     git checkout -b CALC-456-add-scientific-functions
     ```

3. **Develop with Copilot:**
   - Use GitHub Copilot for code suggestions
   - Copilot will help you write code faster

4. **Commit with Issue References:**
   ```bash
   git commit -m "CALC-456 Implement sin, cos, tan functions"
   ```

5. **Create Pull Request:**
   - Include the Jira issue key in PR title or description
   - The PR will automatically appear in the Jira issue

6. **Track Progress in Jira:**
   - View commits, branches, and PRs in the Development panel
   - Update issue status as you work

### Smart Commit Commands

You can include commands in commit messages to automatically update Jira:

```bash
# Transition an issue
git commit -m "CALC-789 #done Fix calculator bug"

# Log time
git commit -m "CALC-789 #time 2h 30m Add new feature"

# Add comment
git commit -m "CALC-789 #comment Implemented the requested changes"

# Combine commands
git commit -m "CALC-789 #time 1h #comment Fixed the bug #done"
```

## Best Practices

1. **Consistent Naming:**
   - Always use the Jira issue key in branch names and commits
   - Format: `PROJECTKEY-123` (e.g., `CALC-123`)

2. **Meaningful Commits:**
   - Write clear commit messages that explain the change
   - Include the Jira issue key at the beginning

3. **Link Pull Requests:**
   - Reference Jira issues in PR descriptions
   - Use keywords like "Fixes CALC-123" or "Resolves CALC-123"

4. **Enable Automation:**
   - Set up Jira automation rules to transition issues when PRs are merged
   - Configure notifications for team awareness

5. **Use Copilot Effectively:**
   - Let Copilot help with code implementation
   - Focus on issue requirements while coding
   - Use Copilot's suggestions to speed up development

## Troubleshooting

### Issues Not Linking

- Verify the Jira issue key format is correct
- Check that the repository is connected in Jira
- Ensure you have the necessary permissions
- Wait a few minutes for sync to occur

### App Not Syncing

- Check the GitHub for Jira app logs in Jira
- Verify webhook configuration in GitHub
- Re-authenticate the connection
- Contact your Jira administrator

### Missing Development Panel

- Ensure the GitHub for Jira app is installed
- Check that commits include the correct issue key
- Verify repository permissions
- Refresh the Jira issue page

## Additional Resources

- [GitHub for Jira Documentation](https://support.atlassian.com/jira-cloud-administration/docs/integrate-with-github/)
- [Smart Commits Documentation](https://support.atlassian.com/jira-software-cloud/docs/process-issues-with-smart-commits/)
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [Jira Automation Documentation](https://support.atlassian.com/cloud-automation/docs/jira-automation/)

## Example Workflow for This Calculator Project

Here's a complete example workflow for this calculator repository:

1. **Create Jira Issue**: `CALC-101: Add modulo operation`
2. **Create Branch**: 
   ```bash
   git checkout -b CALC-101-add-modulo
   ```
3. **Use Copilot** to implement the feature in `calculator.py`
4. **Commit Changes**:
   ```bash
   git commit -m "CALC-101 Add modulo operation to calculator"
   ```
5. **Push and Create PR**:
   ```bash
   git push origin CALC-101-add-modulo
   ```
6. **PR Title**: "CALC-101: Add modulo operation"
7. **Merge PR**: Issue automatically transitions in Jira

## Notes

- GitHub Copilot itself doesn't directly connect to Jira
- The integration is between GitHub (the platform) and Jira
- Copilot enhances your coding experience while the GitHub-Jira integration handles project tracking
- You can use both tools together in your development workflow

## Support

For issues with this integration:
- GitHub support: https://support.github.com
- Jira support: https://support.atlassian.com
- Repository maintainer: Check repository README for contact information
