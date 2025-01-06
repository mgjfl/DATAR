import os
import json
import re
from collections import Counter
import numpy as np

def get_github_metadata():
    
    # GitHub metadata
    with open(os.path.join("data", "app_related", "github_metadata.json"), "r") as f:
        github_metadata = json.load(f)
        
    return np.array(github_metadata)

def get_google_play_metadata():

    # Google Play metadata
    with open(os.path.join("data", "app_related", "google_play_metadata.json"), "r") as f:
        google_play_metadata = json.load(f)

    return np.array(google_play_metadata)
    
def github_name_transform(github_name : str):
    return github_name.replace("/", "-_-")
    
def get_reviews_from_github(github_name : str, verbose : bool = True):
    
    json_name = github_name_transform(github_name) + ".json"
    
    try:
        with open(os.path.join("data", "release_related", "all_reviews", json_name), "r") as f:
            output = np.array(json.load(f))
    except Exception as e:
        output = np.array([])
        if verbose: print(e)

    return output

def get_release_metadata_from_github(github_name : str, verbose : bool = True):
    
    json_name = github_name_transform(github_name) + ".json"
    
    
    try:
        with open(os.path.join("data", "release_related", "all_jsons", json_name), "r") as f:
            output = np.array(json.load(f))
    except Exception as e:
        output = np.array([])
        if verbose: print(e)

    return output

def micro_version_comp(micro_version_1 : str, micro_version_2 : str):
    v1_groups = re.search('(\d+)([a-zA-Z])?', micro_version_1)
    v2_groups = re.search('(\d+)([a-zA-Z])?', micro_version_2)
    
    v1_number = v1_groups.group(1)
    v2_number = v2_groups.group(1)

    if v1_number != v2_number:
        return int(v1_number) - int(v2_number)
    
    v1_letter = v1_groups.group(2)
    v2_letter = v2_groups.group(2)

    if v1_letter is None or v2_letter is None: # Having a letter takes precedence
        return 1 if v1_letter is not None else -1
    
    if v1_letter == v2_letter:
        return 0
    
    return 1 if v1_letter > v2_letter else -1

def version_comp(version_1 : str, version_2 : str):
    
    v1 = version_1.split(".")
    v2 = version_2.split(".")
    
    if v1[0] != v2[0]: # Compare major version
        return int(v1[0]) - int(v2[0])
    elif v1[1] != v2[1]: # Compare minor version
        return int(v1[1]) - int(v2[1])
    
    return micro_version_comp(v1[2], v2[2])

def print_statistics(github_metadata, google_play_metadata):
    all_reviews_names = os.listdir(os.path.join("data", "release_related", "all_reviews"))
    all_jsons_names = os.listdir(os.path.join("data", "release_related", "all_jsons"))

    print(f"There are {len(github_metadata)} GitHub repositories with metadata.")
    print(f"There are {len(google_play_metadata)} Google Play repositories with metadata.")
    print(f"There are {len(all_reviews_names)} applications with reviews.")
    print(f"There are {len(all_jsons_names)} applications with release-related metadata.")

def reviews_per_version(all_reviews) -> Counter:
    return Counter(review["reviewCreatedVersion"] for review in all_reviews)

def get_version(release_metadata : dict) -> str:
    
    release_data = release_metadata["release_data"]
    
    keys = release_data.keys()
    
    if "tag_name" in keys:
        return release_data["tag_name"]
    elif "name" in keys:
        return release_data["name"]
    else:
        return None
    
class DATAR:
    
    def __init__(self,
                 github_metadata,
                 google_play_metadata,
                 github_names,
                 all_release_metadata,
                 all_reviews_from_github):
        
        self.github_metadata            = github_metadata
        self.google_play_metadata       = google_play_metadata
        self.github_names               = github_names
        self.all_release_metadata       = all_release_metadata
        self.all_reviews_from_github    = all_reviews_from_github