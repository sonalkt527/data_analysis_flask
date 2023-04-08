from googleapiclient.discovery import build
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

api_key='AIzaSyBdwOjnzEn_IE1krwVVf64HH3z8TPZHyfk'
youtube=build('youtube','v3',developerKey=api_key)


class find_res:

    def get_id(self,s):
        request = youtube.channels().list(
            part='snippet, contentDetails, statistics', forUsername=s)
        response = request.execute()

        return response

    def get_channel_stats(self, youtube, channel_id1):
        request = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id1)
        response = request.execute()

        all_data = []

        data = dict(channel_name=response['items'][0]['snippet']['title'],
                    subscriber=response['items'][0]['statistics']['subscriberCount'],
                    views=response['items'][0]['statistics']['viewCount'],
                    total_video=response['items'][0]['statistics']['videoCount'])
        all_data.append(data)

        return all_data

    def return_res(self):
        channel_id = self.get_id()
        channel_id1 = channel_id['items'][0]['id']
        channel_stat = (self.get_channel_stats(youtube, channel_id1))


