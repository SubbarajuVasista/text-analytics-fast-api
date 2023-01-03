import requests as req

def call_text_analytics_api(headers, document, endpoint):
    response = req.post("https://text-analytics-fastapi09.cognitiveservices.azure.com//text/analytics/v3.0/" +
                        endpoint, headers=headers, json=document)
    return response.json()