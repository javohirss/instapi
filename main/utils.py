def exchange_token_to_long(token):
    return requests.get(f"https://graph.instagram.com/access_token?grant_type=ig_exchange_token&client_secret={params['client_secret']}&access_token={token}").json()['access_token']

def get_user_data(id, token):
    return requests.get(f"https://graph.instagram.com/{params['api_version']}/{id}?fields=id,account_type,media_count,username&access_token={token}").json()

def get_media_data(id, token):
    return requests.get(f'https://graph.instagram.com/{id}/media?fields=id,caption,media_url,media_type,username,timestamp&access_token={token}').json()
