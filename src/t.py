

import slackweb

url = "https://hooks.slack.com/services/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"
slack = slackweb.Slack(url)

txt = input("a")
slack.notify(text = txt)
