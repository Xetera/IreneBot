from Utility import resources as ex
from module.keys import twitter_account_id, twitter_username


class Twitter:
    async def update_status(self, context):
        ex.api.update_status(status=context)
        tweet = ex.api.user_timeline(user_id=f'{twitter_account_id}', count=1)[0]
        return f"https://twitter.com/{twitter_username}/status/{tweet.id}"

    async def delete_status(self, context):
        ex.api.destroy_status(context)

    async def recent_tweets(self, context):
        tweets = ex.api.user_timeline(user_id=f'{twitter_account_id}', count=context)
        final_tweet = ""
        for tweet in tweets:
            final_tweet += f"> **Tweet ID:** {tweet.id} | **Tweet:** {tweet.text}\n"
        return final_tweet

