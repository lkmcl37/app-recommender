import math
from dataservice import DataService
import operator
import math

class Helper(object):

    def cosine_similarity(cls, app_list1, app_list2):
        temp = len(app_list1) * len(app_list2)
        match_count = cls.__count_match(app_list1, app_list2)
        return float(match_count) / math.sqrt(temp)

    def __count_match(cls, list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        return len(set1.intersection(set2))

def calculate_user_top_5(user_id, user_download_history, all_download_history):

    app_similarity = {}

    for apps in all_download_history:
        similarity = Helper.cosine_similarity(user_download_history, apps)
        for other_app in apps:
            app_similarity[other_app] = similarity + app_similarity.get(other_app, 0)

    for app in user_download_history:
        app_similarity.pop(app)

    sorted_tups = sorted(app_similarity.items(), key=operator.itemgetter(1), reverse=True)
    top_5_app = [sorted_tups[0][0], sorted_tups[1][0], sorted_tups[2][0], sorted_tups[3][0], sorted_tups[4][0]]
    #print("top_5_app for " + str(user_id) + ":\t" + str(top_5_app))

    DataService.update_user_info({'user_id' : user_id}, {'$set' : {'top_5_app': top_5_app}})
