from pymongo import MongoClient
from helper import calculate_app_top_5, calculate_user_top_5
from dataservice import DataService
import time

def main():
    try:
        client = MongoClient('localhost', 27017)
        DataService.init(client)

        user_download_history = DataService.retrieve_user_download_history()
        app_info = DataService.retrieve_app_info()

        for user_id, download_history in user_download_history.iteritems():
            calculate_user_top_5(user_id, download_history, user_download_history.values())

    except Exception as e:
        print(e)
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    main()
