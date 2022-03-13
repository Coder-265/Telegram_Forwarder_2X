from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5247376403:AAEpmCauVHZenD08dC9pda3i59L9bExFbtg"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001663593277,-1001508463415]# List of chat id's to forward messages from.
    TO_CHATS = [-1001290699524]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
