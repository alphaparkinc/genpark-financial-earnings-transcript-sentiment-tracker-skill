from client import FinancialEarningsTranscriptSentimentTrackerClient

def main():
    client = FinancialEarningsTranscriptSentimentTrackerClient()
    res = client.analyze_earnings_call_tone('AAPL', 'Q3_2026', 'Services revenue reached an all-time record.')
    print('Financial Earnings Sentiment Tracker: ' + res['earnings_sentiment_id'] + ' (' + res['stock_ticker'] + ')')
    print('Sentiment Score: ' + str(res['executive_sentiment_score']) + ' | Guidance: ' + res['guidance_tone_shift'])
    print('Dossier URL: ' + res['transcript_breakdown_dossier_url'])

if __name__ == '__main__':
    main()
