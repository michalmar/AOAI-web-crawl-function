# AOAI-web-crawl-function

This repo contains simple web crawler which takes into account a specific page structure and recursivelly crawles throuh websites and stores text from those pages to blob storage.


## Setup
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AZURE_STORAGE_CONNECTION_STRING": "DefaultEndpointsProtocol=https;AccountName=...",
    "AZURE_STORAGE_CONTAINER_NAME": "<YOUR_CONTAINER>",
    "CRAWL_URL": "https://www.example.com/en/subpage/",
    "CRAWL_BASE": "https://www.example.com/en/"
  }
}
```


> Disclaimer: This is a simple web crawler and it is not intended to be used for any malicious purposes. It is intended to be used for educational purposes only. You should always have the permission of the website owner before crawling their website. I do not take any responsibility for the misuse of this code.

