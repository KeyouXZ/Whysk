# WhatsApp Bot Using Green API and GROQ AI

This guide walks you through building a WhatsApp bot using [Green API](https://green-api.com/en) for WhatsApp messaging and [GROQ AI](https://groq.com/) for AI-powered responses.

## Prerequisites

1. **Python 3.x**: Make sure you have [Python](https://www.python.org/downloads/) installed.
2. **Green API Account**: Sign up and get your credentials from [Green API](https://green-api.com/en).
3. **Whysk Project**: Clone the [Whysk project](https://github.com/KeyouXZ/Whysk/tree/main).
4. **WhatsApp**: A valid WhatsApp account linked to Green API.

## Step 1: Set Up Green API

1. Create an account on [Green API](https://green-api.com/en).
2. Link your WhatsApp number and get the following credentials:
   - `Instance ID`
   - `API Token`
   
These credentials will be used to authenticate your bot to the Green API service.

## Step 2: Install Python Dependencies

Install the required libraries (virtual env recommend):

```bash
pip install -r requirements.txt
```

## Step 3: Set Up Environment Variables
Create a `.env` file in your project folder and add the following:

```bash
INSTANCE_ID="your-instance-id"
INSTANCE_API_KEY="your-instance-api-key"
GROQ_API_KEY="your-groq-api-key"
```
Replace your-instance-id and your-api-token with the credentials from Green API.
Set your-groq-api-key with the API key from GROQ.

## Step 4: Start the WhatsApp Bot
Run the bot using:

```bash
python main.py
```
The bot will now listen for incoming WhatsApp messages and respond using GROQ AI if using command `!chat`.
