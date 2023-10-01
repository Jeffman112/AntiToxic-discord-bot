import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import datetime
import discord

# Initialize your Discord bot and setup intents
bot_token = ''  # Your bot token here
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Determine the device for PyTorch (CPU or CUDA if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the tokenizer and model for toxicity classification
tokenizer = AutoTokenizer.from_pretrained("FredZhang7/one-for-all-toxicity-v3")
model = AutoModelForSequenceClassification.from_pretrained("FredZhang7/one-for-all-toxicity-v3").to(device)

@client.event
async def on_ready():
    # Event handler when the bot is ready
    print(f'Connected to Discord!')

@client.event
async def on_message(message):
    # Event handler for receiving new messages in Discord
    print("Message received from Discord")
    print(message.content)

    # Tokenize and preprocess the message for model input
    encoding = tokenizer.encode_plus(
        message.content,
        add_special_tokens=True,
        max_length=208,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )
    print('device:', device)
    input_ids = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)

    # Perform inference using the model
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        logits = outputs.logits
        predicted_labels = torch.argmax(logits, dim=1)

    # Extract the predicted label
    value = predicted_labels.item()

    if value == 1:
        # If the message is toxic:
        print("TOXIC")

        # Apply a timeout to the user who sent the message
        member = message.author
        await member.timeout(datetime.timedelta(seconds=0, minutes=5, hours=0, days=0), reason="toxic")

        # Delete the toxic message
        await message.delete()

        # Send a direct message to the user
        dm = await member.create_dm()
        embed = discord.Embed(
            title="Toxic Behavior",
            description="Toxic behavior was detected in the last message you sent. If you think this was a mistake, please contact a moderator.",
            color=discord.Color.blue()
        )
        await dm.send(embed=embed)
    else:
        # If the message is safe:
        print("SAFE")

# Run the Discord bot
client.run(bot_token)
