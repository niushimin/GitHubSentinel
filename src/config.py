import json
import os

class Config:
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        with open('config.json', 'r') as f:
            config = json.load(f)

            self.email = config.get('email', {})
            self.email['password'] = os.getenv('EMAIL_PASSWORD', self.email.get('password', ''))

            # 加载 GitHub 相关配置
            github_config = config.get('github', {})
            self.github_token = os.getenv('GITHUB_TOKEN', github_config.get('token'))
            self.subscriptions_file = github_config.get('subscriptions_file')
            self.freq_days = github_config.get('progress_frequency_days', 1)
            self.exec_time = github_config.get('progress_execution_time', "08:00")
            
            # 加载报告类型配置
            self.report_types = config.get('report_types', ["github", "hacker_news"])  # 默认报告类型
            
            # 加载 Slack 配置
            slack_config = config.get('slack', {})
            self.slack_webhook_url = slack_config.get('webhook_url')